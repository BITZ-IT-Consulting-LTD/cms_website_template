<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Team Members</h1>
        <p class="text-gray-600 mt-1">Manage users and their roles</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="btn-primary flex items-center"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New User
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Users</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <UsersIcon class="h-8 w-8 text-blue-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Admins</p>
            <p class="text-3xl font-bold text-red-600 mt-2">{{ stats.admins }}</p>
          </div>
          <div class="p-3 bg-red-100 rounded-lg">
            <ShieldCheckIcon class="h-8 w-8 text-red-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Editors</p>
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ stats.editors }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-lg">
            <PencilIcon class="h-8 w-8 text-purple-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Active</p>
            <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.active }}</p>
          </div>
          <div class="p-3 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-8 w-8 text-green-600" />
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-4">
      <div class="flex flex-col sm:flex-row gap-4 items-center justify-between">
        <div class="relative flex-1 w-full sm:w-auto">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search users..."
            class="w-full sm:w-80 pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]"
          />
        </div>
        <select v-model="filterRole" class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]">
          <option value="">All Roles</option>
          <option value="ADMIN">Admin</option>
          <option value="EDITOR">Editor</option>
          <option value="AUTHOR">Author</option>
          <option value="VIEWER">Viewer</option>
        </select>
        <select v-model="filterStatus" class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]">
          <option value="">All Status</option>
          <option value="active">Active</option>
          <option value="inactive">Inactive</option>
        </select>
      </div>
    </div>

    <!-- Users Table -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
      <div v-if="loading" class="p-8 text-center">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-[#8B4000]"></div>
        <p class="mt-2 text-gray-600">Loading users...</p>
      </div>
      <div v-else-if="filteredUsers.length === 0" class="p-8 text-center">
        <UsersIcon class="h-12 w-12 text-gray-400 mx-auto mb-4" />
        <h3 class="text-lg font-medium text-gray-900 mb-2">No users found</h3>
        <p class="text-gray-600 mb-4">
          {{ searchQuery || filterRole || filterStatus ? 'Try adjusting your search criteria.' : 'Get started by adding your first team member.' }}
        </p>
        <p v-if="!searchQuery && !filterRole && !filterStatus" class="text-sm text-gray-500 mb-4">
          You can create users via Django admin panel: <code class="bg-gray-100 px-2 py-1 rounded">python manage.py createsuperuser</code>
        </p>
        <button v-if="!searchQuery && !filterRole && !filterStatus" @click="showCreateModal = true" class="btn-primary">
          <PlusIcon class="h-4 w-4 inline mr-2" />
          Add New User
        </button>
      </div>
      <div v-else>
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Last Login</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="user in filteredUsers" :key="user.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="h-10 w-10 rounded-full bg-[#8B4000] flex items-center justify-center text-white font-semibold">
                    {{ user.first_name?.[0] || user.username?.[0] || 'U' }}
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900">{{ user.first_name || user.username }}</div>
                    <div class="text-sm text-gray-500">@{{ user.username }}</div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span :class="getRoleClass(user.role)" class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full">
                  {{ user.role }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ user.email }}</td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span :class="user.is_active ? 'text-green-600' : 'text-gray-400'" class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-50">
                  {{ user.is_active ? 'Active' : 'Inactive' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatDate(user.last_login) }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button @click="editUser(user)" class="text-[#8B4000] hover:text-[#6B3000] mr-4">Edit</button>
                <button @click="deleteUser(user)" class="text-red-600 hover:text-red-900">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Create/Edit Modal -->
    <Teleport to="body">
      <div v-if="showCreateModal || editingUser" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg shadow-xl w-full max-w-md p-6">
          <h2 class="text-2xl font-bold text-gray-900 mb-4">{{ editingUser ? 'Edit User' : 'Add New User' }}</h2>
          <form @submit.prevent="editingUser ? updateUser() : createUser()">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Username</label>
                <input v-model="userForm.username" type="text" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]" />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">First Name</label>
                <input v-model="userForm.first_name" type="text" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]" />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Last Name</label>
                <input v-model="userForm.last_name" type="text" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]" />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                <input v-model="userForm.email" type="email" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]" />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Role</label>
                <select v-model="userForm.role" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]">
                  <option value="">Select role</option>
                  <option value="ADMIN">Admin</option>
                  <option value="EDITOR">Editor</option>
                  <option value="AUTHOR">Author</option>
                  <option value="VIEWER">Viewer</option>
                </select>
              </div>
              <div v-if="!editingUser">
                <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                <input v-model="userForm.password" type="password" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]" />
              </div>
              <div class="flex items-center">
                <input v-model="userForm.is_active" type="checkbox" id="is_active" class="rounded border-gray-300 text-[#8B4000] focus:ring-[#8B4000]" />
                <label for="is_active" class="ml-2 text-sm text-gray-700">Active</label>
              </div>
            </div>
            <div class="flex justify-end gap-3 mt-6">
              <button type="button" @click="closeModal" class="px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50">Cancel</button>
              <button type="submit" class="btn-primary">{{ editingUser ? 'Update' : 'Create' }}</button>
            </div>
          </form>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import {
  PlusIcon,
  UsersIcon,
  ShieldCheckIcon,
  PencilIcon,
  CheckCircleIcon,
  MagnifyingGlassIcon
} from '@heroicons/vue/24/outline'
import { api } from '@/utils/api'

const toast = useToast()

// Refs
const users = ref([])
const loading = ref(false)
const showCreateModal = ref(false)
const editingUser = ref(null)
const searchQuery = ref('')
const filterRole = ref('')
const filterStatus = ref('')

const userForm = ref({
  username: '',
  first_name: '',
  last_name: '',
  email: '',
  role: '',
  password: '',
  is_active: true
})

const stats = computed(() => {
  const usersList = Array.isArray(users.value) ? users.value : []
  const total = usersList.length
  const admins = usersList.filter(u => u.role === 'ADMIN').length
  const editors = usersList.filter(u => u.role === 'EDITOR').length
  const active = usersList.filter(u => u.is_active).length
  
  return { total, admins, editors, active }
})

const filteredUsers = computed(() => {
  // Ensure users is always an array
  let filtered = Array.isArray(users.value) ? users.value : []
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(u =>
      u.username?.toLowerCase().includes(query) ||
      u.email?.toLowerCase().includes(query) ||
      u.first_name?.toLowerCase().includes(query)
    )
  }
  
  if (filterRole.value) {
    filtered = filtered.filter(u => u.role === filterRole.value)
  }
  
  if (filterStatus.value) {
    filtered = filtered.filter(u =>
      filterStatus.value === 'active' ? u.is_active : !u.is_active
    )
  }
  
  return filtered
})

const fetchUsers = async () => {
  loading.value = true
  try {
    const response = await api.users.list()
    const data = response.data
    // Ensure users is always an array
    users.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
    
    console.log('Loaded users:', users.value.length)
  } catch (err) {
    console.error('Failed to fetch users:', err)
    const errorMsg = err.response?.data?.detail || err.message || 'Failed to load users'
    toast.error(errorMsg)
    // Always ensure users is an array even on error
    users.value = []
  } finally {
    loading.value = false
  }
}

const editUser = (user) => {
  editingUser.value = user
  userForm.value = {
    username: user.username,
    first_name: user.first_name,
    last_name: user.last_name,
    email: user.email,
    role: user.role,
    password: '',
    is_active: user.is_active
  }
  showCreateModal.value = true
}

const deleteUser = async (user) => {
  if (!confirm(`Are you sure you want to delete ${user.username}?`)) return
  
  try {
    await api.users.delete(user.id)
    toast.success('User deleted successfully')
    await fetchUsers()
  } catch (err) {
    console.error('Failed to delete user:', err)
    toast.error('Failed to delete user')
  }
}

const createUser = async () => {
  try {
    await api.users.create(userForm.value)
    toast.success('User created successfully')
    closeModal()
    await fetchUsers()
  } catch (err) {
    console.error('Failed to create user:', err)
    toast.error(err.response?.data?.detail || 'Failed to create user')
  }
}

const updateUser = async () => {
  try {
    await api.users.update(editingUser.value.id, userForm.value)
    toast.success('User updated successfully')
    closeModal()
    await fetchUsers()
  } catch (err) {
    console.error('Failed to update user:', err)
    toast.error(err.response?.data?.detail || 'Failed to update user')
  }
}

const closeModal = () => {
  showCreateModal.value = false
  editingUser.value = null
  userForm.value = {
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    role: '',
    password: '',
    is_active: true
  }
}

const formatDate = (date) => {
  if (!date) return 'Never'
  return new Date(date).toLocaleDateString()
}

const getRoleClass = (role) => {
  const classes = {
    'ADMIN': 'bg-red-100 text-red-800',
    'EDITOR': 'bg-purple-100 text-purple-800',
    'AUTHOR': 'bg-blue-100 text-blue-800',
    'VIEWER': 'bg-gray-100 text-gray-800'
  }
  return classes[role] || 'bg-gray-100 text-gray-800'
}

onMounted(() => {
  fetchUsers()
})
</script>

<style scoped>
.stats-card {
  @apply bg-white rounded-lg shadow-sm border border-gray-200 p-6;
  font-family: 'Roboto', sans-serif;
}

.btn-primary {
  @apply px-4 py-2 bg-[#8B4000] text-white rounded-lg hover:bg-[#6B3000] transition-colors;
  font-family: 'Roboto', sans-serif;
}
</style>
