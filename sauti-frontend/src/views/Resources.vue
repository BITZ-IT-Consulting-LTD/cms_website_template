<template>
  <div class="section-padding">
    <div class="container-custom">
      <h1 class="text-center mb-12">Resources</h1>
      
      <Loader v-if="loading" message="Loading resources..." />
      
      <div v-else-if="resources.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="resource in resources" :key="resource.id" class="card card-body">
          <div class="flex items-start space-x-4">
            <div class="bg-teal-100 p-3 rounded-lg">
              <svg class="w-6 h-6 text-teal-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd"/>
              </svg>
            </div>
            <div class="flex-1">
              <h3 class="font-bold text-gray-900 mb-2">{{ resource.title }}</h3>
              <p class="text-sm text-gray-600 mb-4">{{ resource.description }}</p>
              <a :href="resource.file" target="_blank" class="btn-primary text-sm">Download</a>
            </div>
          </div>
        </div>
      </div>

      <p v-else class="text-center text-gray-600">No resources available yet.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useResourcesStore } from '@/store/resources'
import Loader from '@/components/common/Loader.vue'

const resourcesStore = useResourcesStore()
const resources = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    await resourcesStore.fetchResources()
    resources.value = resourcesStore.resources
  } finally {
    loading.value = false
  }
})
</script>
