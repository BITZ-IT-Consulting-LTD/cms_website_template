<template>
    <div class="p-6">
        <!-- Page Header -->
        <PageHeader title="General Feedback"
            description="View and manage messages submitted via the website contact form." />

        <!-- Stats -->
        <StatsGrid>
            <StatCard label="Total Messages" :value="stats.total" :icon="ChatBubbleLeftRightIcon" color="blue" />
            <StatCard label="Pending Review" :value="stats.pending" :icon="ClockIcon" color="amber" />
            <StatCard label="Resolved" :value="stats.processed" :icon="CheckCircleIcon" color="green" />
        </StatsGrid>

        <!-- Loading State -->
        <LoadingState v-if="loading" message="Loading messages..." />

        <!-- Empty State -->
        <EmptyState v-else-if="messages.length === 0" title="No Messages Found"
            message="When users submit feedback on the contact page, they will appear here."
            :icon="ChatBubbleLeftRightIcon" />

        <!-- Messages List -->
        <div v-else class="space-y-4">
            <div v-for="msg in messages" :key="msg.id"
                class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden group hover:shadow-lg transition-all duration-300">
                <div class="p-6 flex flex-col md:flex-row gap-6">
                    <div class="flex-1">
                        <div class="flex items-center gap-3 mb-2">
                            <h3 class="text-lg font-bold text-gray-900">{{ msg.name || 'Anonymous User' }}</h3>
                            <span v-if="msg.email" class="text-sm text-blue-600 font-medium">{{ msg.email }}</span>
                            <span class="text-xs text-gray-400 font-bold ml-auto">{{ formatDate(msg.submitted_at)
                            }}</span>
                        </div>
                        <p
                            class="text-gray-700 leading-relaxed bg-gray-50/50 p-4 rounded-2xl border border-gray-100 italic">
                            "{{ msg.message }}"
                        </p>
                    </div>
                    <div class="flex md:flex-col justify-between items-end shrink-0 gap-4">
                        <span class="flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-full"
                            :class="msg.is_processed ? 'bg-green-50 text-green-700 border border-green-100' : 'bg-amber-50 text-amber-700 border border-amber-100'">
                            <span class="w-2 h-2 rounded-full"
                                :class="msg.is_processed ? 'bg-green-500' : 'bg-amber-500 animate-pulse'"></span>
                            {{ msg.is_processed ? 'Reviewed' : 'Pending' }}
                        </span>
                        <div class="flex gap-2">
                            <button v-if="!msg.is_processed" @click="markAsProcessed(msg.id)"
                                class="px-4 py-2 bg-blue-600 text-white text-xs font-black rounded-xl hover:bg-blue-700 transition-all shadow-md shadow-blue-100">
                                Mark Reviewed
                            </button>
                            <button @click="deleteMessage(msg.id)"
                                class="p-2 bg-gray-50 hover:bg-red-50 rounded-xl text-gray-400 hover:text-red-600 transition-all border border-transparent hover:border-red-100">
                                <TrashIcon class="h-5 w-5" />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, computed, onMounted } from 'vue';
    import { api } from '@/utils/api';
    import { useToast } from 'vue-toastification';
    import { PageHeader, StatsGrid, StatCard, LoadingState, EmptyState } from '@/components/admin';
    import {
        ChatBubbleLeftRightIcon,
        ClockIcon,
        CheckCircleIcon,
        TrashIcon,
        EnvelopeIcon
    } from '@heroicons/vue/24/outline';

    const toast = useToast();
    const messages = ref([]);
    const loading = ref(true);

    const stats = computed(() => {
        return {
            total: messages.value.length,
            pending: messages.value.filter(m => !m.is_processed).length,
            processed: messages.value.filter(m => m.is_processed).length,
        };
    });

    const fetchMessages = async () => {
        loading.value = true;
        try {
            const response = await api.feedback.list();
            messages.value = response.data.results || response.data;
        } catch (error) {
            console.error('Error fetching feedback:', error);
            toast.error('Failed to load feedback messages');
        } finally {
            loading.value = false;
        }
    };

    const markAsProcessed = async (id) => {
        try {
            await api.feedback.update(id, { is_processed: true });
            toast.success('Message marked as reviewed');
            await fetchMessages();
        } catch (error) {
            console.error('Error updating message:', error);
            toast.error('Failed to update message');
        }
    };

    const deleteMessage = async (id) => {
        if (confirm('Are you sure you want to delete this feedback?')) {
            try {
                await api.feedback.delete(id);
                toast.success('Message deleted');
                await fetchMessages();
            } catch (error) {
                console.error('Error deleting message:', error);
                toast.error('Failed to delete message');
            }
        }
    };

    const formatDate = (dateStr) => {
        if (!dateStr) return '';
        const date = new Date(dateStr);
        return date.toLocaleString('en-US', {
            month: 'short',
            day: 'numeric',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    };

    onMounted(fetchMessages);
</script>
