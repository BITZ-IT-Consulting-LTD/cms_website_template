<template>
  <div class="mt-8 bg-white border border-gray-200 rounded-xl overflow-hidden shadow-sm">
    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between bg-gray-50/50">
      <div class="flex items-center space-x-2">
        <ClockIcon class="h-5 w-5 text-gray-400" />
        <h3 class="text-lg font-bold text-gray-900">Audit History</h3>
      </div>
      <span class="text-xs font-medium text-gray-500 uppercase tracking-wider">Immutable Change Log</span>
    </div>

    <div v-if="loading" class="p-8 text-center">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary mx-auto"></div>
      <p class="mt-2 text-sm text-gray-500">Loading history...</p>
    </div>

    <div v-else-if="!history || history.length === 0" class="p-8 text-center text-gray-500">
      <p>No historical changes recorded for this item.</p>
    </div>

    <div v-else class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50/30">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Action</th>
            <th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">User</th>
            <th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Date & Time</th>
            <th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Changes</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-100">
          <tr v-for="record in history" :key="record.history_id" class="hover:bg-gray-50/50 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap">
              <span 
                class="px-2.5 py-1 rounded-full text-xs font-bold uppercase tracking-wider"
                :class="getActionBadgeClass(record.history_type)"
              >
                {{ getActionLabel(record.history_type) }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="flex items-center">
                <div class="h-7 w-7 rounded-lg bg-gray-100 flex items-center justify-center mr-3">
                  <UserIcon class="h-4 w-4 text-gray-500" />
                </div>
                <div>
                  <div class="text-sm font-bold text-gray-900">{{ record.history_user_fullname }}</div>
                  <div class="text-xs text-gray-500">{{ record.history_user_username }}</div>
                </div>
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ formatDate(record.history_date) }}</div>
              <div class="text-xs text-gray-500">{{ formatTime(record.history_date) }}</div>
            </td>
            <td class="px-6 py-4">
              <div v-if="record.changes && record.changes.length > 0" class="space-y-2">
                <div v-for="change in record.changes" :key="change.field" class="text-xs">
                  <span class="font-bold text-gray-700">{{ change.field }}:</span>
                  <div class="flex items-center space-x-2 mt-0.5">
                    <span class="px-1.5 py-0.5 bg-red-50 text-red-600 rounded line-through break-all">{{ change.old }}</span>
                    <ArrowRightIcon class="h-3 w-3 text-gray-400" />
                    <span class="px-1.5 py-0.5 bg-green-50 text-green-700 rounded break-all">{{ change.new }}</span>
                  </div>
                </div>
              </div>
              <div v-else-if="record.history_type === '+'" class="text-xs text-gray-400 italic">
                Initial creation
              </div>
              <div v-else class="text-xs text-gray-400 italic">
                No data changes (meta-update)
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { 
  ClockIcon, 
  UserIcon, 
  ArrowRightIcon 
} from '@heroicons/vue/24/outline'

defineProps({
  history: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const getActionLabel = (type) => {
  switch (type) {
    case '+': return 'Created'
    case '~': return 'Updated'
    case '-': return 'Deleted'
    default: return type
  }
}

const getActionBadgeClass = (type) => {
  switch (type) {
    case '+': return 'bg-green-100 text-green-700'
    case '~': return 'bg-blue-100 text-blue-700'
    case '-': return 'bg-red-100 text-red-700'
    default: return 'bg-gray-100 text-gray-700'
  }
}

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString('en-GB', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  })
}

const formatTime = (dateStr) => {
  return new Date(dateStr).toLocaleTimeString('en-GB', {
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>
