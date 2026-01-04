<template>
  <div class="voice-capture">
    <div class="status-indicator" :class="{ 'recording': isRecording }">
      <div class="icon">
        <i v-if="isRecording" class="fas fa-microphone-alt pulse"></i>
        <i v-else class="fas fa-microphone-alt"></i>
      </div>
      <div class="status-text">{{ statusMessage }}</div>
      <div v-if="isRecording" class="time-limit-indicator">
        <div class="progress-bar">
          <div class="progress" :style="{ width: recordingProgressPercent + '%' }"></div>
        </div>
        <div class="time-remaining">{{ timeRemainingMessage }}</div>
      </div>
    </div>

    <div class="controls">
      <button @click="toggleRecording" class="btn" :class="isRecording ? 'btn-danger' : 'btn-primary'"
        ref="recordButton">
        <i :class="isRecording ? 'fas fa-stop-circle' : 'fas fa-microphone'"></i>
        {{ isRecording ? 'Stop Recording' : 'Start Recording' }}
      </button>
    </div>

    <div v-if="audioBlobUrl" class="playback">
      <div class="audio-player">
        <audio :src="audioBlobUrl" controls class="custom-audio-player"></audio>
      </div>
    </div>

    <div v-if="capturedText && capturedText !== 'Listening...'" class="actions">
      <button type="button" @click="confirmRecording" class="btn btn-success">
        <i class="fas fa-check"></i> Use This Recording
      </button>
      <button @click="resetRecording" class="btn btn-outline">
        <i class="fas fa-redo"></i> Try Again
      </button>
    </div>
  </div>
</template>

<script>
  import { ref, computed, onMounted } from "vue";

  export default {
    name: "EnhancedVoiceCapture",
    emits: ["capturedText", "recordingComplete"],

    setup(props, { emit }) {
      const capturedText = ref("");
      const isRecording = ref(false);
      const audioBlobUrl = ref(null);
      const recordingStartTime = ref(null);
      const recordingDuration = ref(0);
      const MIN_RECORDING_TIME = 0; // 4 minutes in seconds
      const MAX_RECORDING_TIME = 5 * 60; // 5 minutes in seconds
      const recordButton = ref(null);
      const isReadyToStop = ref(false);

      let recognition = null;
      let mediaRecorder = null;
      let audioChunks = [];
      let durationTimer = null;
      let autoStopTimer = null;

      // Computed status message
      const statusMessage = computed(() => {
        if (isRecording.value) {
          return `Recording${recordingDuration.value ? ` (${formatDuration(recordingDuration.value)})` : '...'}`;
        } else if (capturedText.value && capturedText.value !== 'Listening...') {
          return 'Recording complete!';
        } else {
          return 'Ready to record';
        }
      });

      // Time remaining message
      const timeRemainingMessage = computed(() => {
        const timeRemaining = MAX_RECORDING_TIME - recordingDuration.value;
        if (timeRemaining <= 0) return "Recording complete";

        return `${formatDuration(timeRemaining)} remaining`;
      });

      // Recording progress percentage
      const recordingProgressPercent = computed(() => {
        return Math.min((recordingDuration.value / MAX_RECORDING_TIME) * 100, 100);
      });

      // Format duration to MM:SS
      const formatDuration = (seconds) => {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
      };

      // Speech recognition setup
      const initSpeechRecognition = () => {
        const SpeechRecognition =
          window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {
          alert(
            "Your browser does not support speech recognition. Please use Chrome or Edge."
          );
          return;
        }

        recognition = new SpeechRecognition();
        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.continuous = true;

        recognition.addEventListener("result", (event) => {
          const transcript = Array.from(event.results)
            .map((result) => result[0].transcript)
            .join(" ");
          capturedText.value = transcript;
        });

        recognition.addEventListener("error", (event) => {
          console.error("Speech Recognition Error:", event.error);
          if (event.error !== 'no-speech') {
            capturedText.value = `Error: ${event.error}. Please try again.`;
          }
        });
      };

      const startRecording = async () => {
        try {
          isRecording.value = true;
          capturedText.value = "Listening...";
          recordingStartTime.value = Date.now();
          recordingDuration.value = 0;
          isReadyToStop.value = false;

          // Start the duration timer
          durationTimer = setInterval(() => {
            recordingDuration.value = Math.floor((Date.now() - recordingStartTime.value) / 1000);

            // Check minimum recording time
            if (recordingDuration.value >= MIN_RECORDING_TIME) {
              isReadyToStop.value = true;
            }
          }, 1000);

          // Set auto-stop timer for maximum recording time
          autoStopTimer = setTimeout(() => {
            if (isRecording.value) {
              stopRecording();
            }
          }, MAX_RECORDING_TIME * 1000);

          // Start speech recognition
          recognition.start();

          // Start audio recording
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          mediaRecorder = new MediaRecorder(stream);
          audioChunks = [];

          mediaRecorder.addEventListener("dataavailable", (event) => {
            audioChunks.push(event.data);
          });

          mediaRecorder.start();
        } catch (error) {
          console.error("Error starting recording:", error);
          capturedText.value = `Error: Could not access microphone. Please check your permissions.`;
          isRecording.value = false;
          clearInterval(durationTimer);
          clearTimeout(autoStopTimer);
        }
      };

      const stopRecording = () => {
        // Check if minimum time has elapsed
        if (recordingDuration.value < MIN_RECORDING_TIME) {
          const timeNeeded = MIN_RECORDING_TIME - recordingDuration.value;
          const secondsText = timeNeeded === 1 ? 'second' : 'seconds';
          alert(`Please record for at least ${MIN_RECORDING_TIME / 60} minutes. You need ${timeNeeded} more ${secondsText}.`);
          return;
        }

        isRecording.value = false;
        clearInterval(durationTimer);
        clearTimeout(autoStopTimer);

        // Stop speech recognition
        if (recognition) {
          recognition.stop();
        }

        // Stop audio recording
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
          mediaRecorder.stop();
          mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
            audioBlobUrl.value = URL.createObjectURL(audioBlob);

            // If no text was captured, provide feedback
            if (capturedText.value === "Listening...") {
              capturedText.value = "No speech detected, but audio was recorded. You can review the recording.";
            }

            // Emit recording complete event with duration info
            emit("recordingComplete", {
              duration: recordingDuration.value,
              audioBlob: audioBlob
            });
          });
        }

        // Release microphone
        if (mediaRecorder && mediaRecorder.stream) {
          mediaRecorder.stream.getTracks().forEach(track => track.stop());
        }
      };

      // Toggle recording state
      const toggleRecording = () => {
        if (isRecording.value) {
          stopRecording();
        } else {
          startRecording();
        }
      };

      // Reset the recording
      const resetRecording = () => {
        capturedText.value = "";
        isRecording.value = false;
        if (audioBlobUrl.value) {
          URL.revokeObjectURL(audioBlobUrl.value);
          audioBlobUrl.value = null;
        }
        recordingDuration.value = 0;
        audioChunks = [];
      };

      // Confirm and emit captured text
      const confirmRecording = () => {
        if ((capturedText.value && capturedText.value !== 'Listening...') || audioBlobUrl.value) {
          emit("capturedText", capturedText.value);
        }
      };

      // Initialize on setup
      onMounted(() => {
        initSpeechRecognition();
      });

      return {
        capturedText,
        isRecording,
        audioBlobUrl,
        statusMessage,
        timeRemainingMessage,
        recordingProgressPercent,
        toggleRecording,
        confirmRecording,
        resetRecording,
        recordButton,
        isReadyToStop
      };
    },
  };
</script>

<style scoped>
  .voice-capture {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    background-color: #f8f9fa;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    margin: 1rem 0;
    font-family: inherit;
  }

  .status-indicator {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1rem;
    padding: 1rem;
    border-radius: 8px;
    background-color: #f8f9fa;
    transition: all 0.3s ease;
  }

  .status-indicator.recording {
    background-color: rgba(220, 53, 69, 0.1);
  }

  .icon {
    font-size: 2rem;
    color: #6c757d;
    margin-bottom: 0.5rem;
  }

  .status-indicator.recording .icon {
    color: #dc3545;
  }

  .status-text {
    font-size: 1rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
  }

  .time-limit-indicator {
    width: 100%;
    margin-top: 0.5rem;
  }

  .progress-bar {
    width: 100%;
    height: 8px;
    background-color: #e9ecef;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 0.5rem;
  }

  .progress {
    height: 100%;
    background-color: #dc3545;
    transition: width 1s linear;
  }

  .time-remaining {
    font-size: 0.8rem;
    text-align: center;
    color: #6c757d;
  }

  .pulse {
    animation: pulse 1.5s infinite;
  }

  @keyframes pulse {
    0% {
      transform: scale(1);
      opacity: 1;
    }

    50% {
      transform: scale(1.05);
      opacity: 0.8;
    }

    100% {
      transform: scale(1);
      opacity: 1;
    }
  }

  .controls {
    display: flex;
    justify-content: center;
    margin-bottom: 1rem;
  }

  .btn {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 6px;
    font-weight: 500;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }

  .btn i {
    font-size: 1.1rem;
  }

  .btn-primary {
    background-color: #0d6efd;
    color: white;
  }

  .btn-primary:hover {
    background-color: #0b5ed7;
  }

  .btn-danger {
    background-color: #dc3545;
    color: white;
  }

  .btn-danger:hover {
    background-color: #bb2d3b;
  }

  .btn-success {
    background-color: #198754;
    color: white;
  }

  .btn-success:hover {
    background-color: #157347;
  }

  .btn-outline {
    background-color: transparent;
    color: #6c757d;
    border: 1px solid #dee2e6;
  }

  .btn-outline:hover {
    background-color: #f8f9fa;
    border-color: #adb5bd;
  }

  .playback {
    margin-bottom: 1rem;
    width: 100%;
  }

  .audio-player {
    width: 100%;
    padding: 0.5rem;
    background-color: #f8f9fa;
    border-radius: 6px;
    border: 1px solid #dee2e6;
  }

  .custom-audio-player {
    width: 100%;
  }

  .actions {
    display: flex;
    justify-content: space-between;
    gap: 10px;
  }

  @media (max-width: 768px) {
    .actions {
      flex-direction: column;
    }

    .btn {
      width: 100%;
    }
  }
</style>
