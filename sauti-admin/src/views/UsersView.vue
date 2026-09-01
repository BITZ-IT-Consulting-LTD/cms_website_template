<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Team Members</h1>
        <p class="text-gray-600 mt-1">Manage users and their roles</p>
      </div>
      <button
        @click="openCreateUser"
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

    <!-- Tabs -->
    <div class="border-b border-gray-200">
      <nav class="flex gap-6">
        <button
          @click="activeTab = 'users'"
          :class="['py-3 px-1 border-b-2 text-sm font-medium', activeTab === 'users' ? 'border-[#8B4000] text-[#8B4000]' : 'border-transparent text-gray-500 hover:text-gray-700']"
        >Users</button>
        <button
          @click="activeTab = 'roles'"
          :class="['py-3 px-1 border-b-2 text-sm font-medium', activeTab === 'roles' ? 'border-[#8B4000] text-[#8B4000]' : 'border-transparent text-gray-500 hover:text-gray-700']"
        >Roles & Permissions</button>
      </nav>
    </div>

    <div v-if="activeTab === 'users'" class="space-y-6">
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
          <option v-for="role in roles" :key="role.id" :value="role.id">{{ role.name }}</option>
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
        <table class="min-w-full">
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
          <tbody class="bg-white">
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
                <div class="flex items-center gap-1.5">
                  <span :class="getRoleClass(user.role_detail?.slug)" class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full">
                    {{ user.role_detail?.name || 'No role' }}
                  </span>
                  <span v-if="user.is_superuser" class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-amber-100 text-amber-800" title="Super administrator (protected)">
                    Super Admin
                  </span>
                </div>
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
            <!-- Display general errors -->
            <div v-if="validationErrors.non_field_errors || validationErrors.detail" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
              <p class="text-sm text-red-600">
                {{ Array.isArray(validationErrors.non_field_errors) ? validationErrors.non_field_errors[0] : (validationErrors.detail || validationErrors.non_field_errors) }}
              </p>
            </div>

            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Username</label>
                <input
                  v-model="userForm.username"
                  type="text"
                  required
                  :class="['w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]', validationErrors.username ? 'border-red-500' : 'border-gray-300']"
                />
                <p v-if="validationErrors.username" class="mt-1 text-sm text-red-600">
                  {{ Array.isArray(validationErrors.username) ? validationErrors.username[0] : validationErrors.username }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">First Name</label>
                <input
                  v-model="userForm.first_name"
                  type="text"
                  required
                  :class="['w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]', validationErrors.first_name ? 'border-red-500' : 'border-gray-300']"
                />
                <p v-if="validationErrors.first_name" class="mt-1 text-sm text-red-600">
                  {{ Array.isArray(validationErrors.first_name) ? validationErrors.first_name[0] : validationErrors.first_name }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Last Name</label>
                <input
                  v-model="userForm.last_name"
                  type="text"
                  required
                  :class="['w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]', validationErrors.last_name ? 'border-red-500' : 'border-gray-300']"
                />
                <p v-if="validationErrors.last_name" class="mt-1 text-sm text-red-600">
                  {{ Array.isArray(validationErrors.last_name) ? validationErrors.last_name[0] : validationErrors.last_name }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                <input
                  v-model="userForm.email"
                  type="email"
                  required
                  :class="['w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]', validationErrors.email ? 'border-red-500' : 'border-gray-300']"
                />
                <p v-if="validationErrors.email" class="mt-1 text-sm text-red-600">
                  {{ Array.isArray(validationErrors.email) ? validationErrors.email[0] : validationErrors.email }}
                </p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Role</label>
                <select
                  v-model="userForm.role"
                  required
                  :class="['w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]', validationErrors.role ? 'border-red-500' : 'border-gray-300']"
                >
                  <option value="">Select role</option>
                  <option v-for="role in roles" :key="role.id" :value="role.id">{{ role.name }}</option>
                </select>
                <p v-if="validationErrors.role" class="mt-1 text-sm text-red-600">
                  {{ Array.isArray(validationErrors.role) ? validationErrors.role[0] : validationErrors.role }}
                </p>
              </div>
              <div v-if="!editingUser">
                <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                <input
                  v-model="userForm.password"
                  type="password"
                  required
                  :class="['w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]', validationErrors.password ? 'border-red-500' : 'border-gray-300']"
                />
                <p v-if="validationErrors.password" class="mt-1 text-sm text-red-600">
                  {{ Array.isArray(validationErrors.password) ? validationErrors.password[0] : validationErrors.password }}
                </p>
              </div>
              <div v-if="!editingUser">
                <label class="block text-sm font-medium text-gray-700 mb-2">Confirm Password</label>
                <input
                  v-model="userForm.password2"
                  type="password"
                  required
                  :class="['w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]', validationErrors.password2 ? 'border-red-500' : 'border-gray-300']"
                />
                <p v-if="validationErrors.password2" class="mt-1 text-sm text-red-600">
                  {{ Array.isArray(validationErrors.password2) ? validationErrors.password2[0] : validationErrors.password2 }}
                </p>
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

    <!-- Roles & Permissions tab -->
    <div v-if="activeTab === 'roles'" class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 lg:col-span-1">
        <div class="p-4 border-b border-gray-200 flex items-center justify-between">
          <h2 class="font-semibold text-gray-900">Roles</h2>
          <button @click="startNewRole" class="text-sm text-[#8B4000] hover:text-[#6B3000] font-medium">+ New Role</button>
        </div>
        <ul>
          <li
            v-for="role in roles"
            :key="role.id"
            @click="selectRole(role)"
            :class="['px-4 py-3 border-b border-gray-100 cursor-pointer hover:bg-gray-50 flex items-center justify-between', selectedRole?.id === role.id ? 'bg-orange-50' : '']"
          >
            <div>
              <p class="text-sm font-medium text-gray-900">{{ role.name }}</p>
              <p class="text-xs text-gray-500">{{ role.user_count }} user{{ role.user_count === 1 ? '' : 's' }}<span v-if="role.is_default"> · default</span></p>
            </div>
          </li>
        </ul>
      </div>

      <div class="bg-white rounded-lg shadow-sm border border-gray-200 lg:col-span-2 p-6" v-if="selectedRole">
        <div class="flex items-center justify-between mb-4">
          <input
            v-model="roleForm.name"
            :disabled="selectedRole.is_default"
            placeholder="Role name"
            :class="[
              'text-lg font-semibold text-gray-900 px-2 py-1 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#8B4000]',
              selectedRole.is_default ? 'border border-transparent bg-transparent' : 'border border-gray-300 disabled:bg-gray-100'
            ]"
          />
          <button
            v-if="!selectedRole.is_default && selectedRole.id"
            @click="deleteRole(selectedRole)"
            class="text-sm text-red-600 hover:text-red-800"
          >Delete Role</button>
        </div>

        <div v-for="group in permissionsByCategory" :key="group.category" class="mb-5">
          <h3 class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">{{ group.category }}</h3>
          <label v-for="perm in group.items" :key="perm.id" class="flex items-center gap-2 py-1">
            <input type="checkbox" :value="perm.id" v-model="roleForm.permissions" class="rounded border-gray-300 text-[#8B4000] focus:ring-[#8B4000]" />
            <span class="text-sm text-gray-700">{{ perm.label }}</span>
          </label>
        </div>

        <div class="flex justify-end gap-3 mt-6 pt-4 border-t border-gray-100">
          <button @click="saveRole" class="btn-primary">{{ selectedRole.id ? 'Save Changes' : 'Create Role' }}</button>
        </div>
      </div>
      <div v-else class="bg-white rounded-lg shadow-sm border border-gray-200 lg:col-span-2 p-6 text-center text-gray-500">
        Select a role to edit its permissions, or create a new one.
      </div>
    </div>
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
const roles = ref([])
const permissions = ref([])
const loading = ref(false)
const showCreateModal = ref(false)
const editingUser = ref(null)
const searchQuery = ref('')
const filterRole = ref('')
const filterStatus = ref('')
const activeTab = ref('users')
const selectedRole = ref(null)
const roleForm = ref({ name: '', permissions: [] })

const userForm = ref({
  username: '',
  first_name: '',
  last_name: '',
  email: '',
  role: '',
  password: '',
  password2: '',
  is_active: true
})

const validationErrors = ref({})

const stats = computed(() => {
  const usersList = Array.isArray(users.value) ? users.value : []
  const total = usersList.length
  const admins = usersList.filter(u => u.role_detail?.slug === 'admin' || u.is_superuser).length
  const editors = usersList.filter(u => u.role_detail?.slug === 'editor').length
  const active = usersList.filter(u => u.is_active).length

  return { total, admins, editors, active }
})

const permissionsByCategory = computed(() => {
  const groups = {}
  for (const perm of permissions.value) {
    if (!groups[perm.category]) groups[perm.category] = []
    groups[perm.category].push(perm)
  }
  return Object.keys(groups).sort().map(category => ({ category, items: groups[category] }))
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
    // <select> v-model always yields a string; user.role is a numeric FK id.
    filtered = filtered.filter(u => String(u.role) === String(filterRole.value))
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

const fetchRoles = async () => {
  try {
    const response = await api.roles.list()
    roles.value = Array.isArray(response.data) ? response.data : (response.data.results || [])
  } catch (err) {
    console.error('Failed to fetch roles:', err)
  }
}

const fetchPermissions = async () => {
  try {
    const response = await api.permissions.list()
    permissions.value = Array.isArray(response.data) ? response.data : (response.data.results || [])
  } catch (err) {
    console.error('Failed to fetch permissions:', err)
  }
}

const selectRole = (role) => {
  selectedRole.value = role
  roleForm.value = { name: role.name, permissions: role.permissions.slice() }
}

const startNewRole = () => {
  selectedRole.value = { id: null, is_default: false }
  roleForm.value = { name: '', permissions: [] }
}

const saveRole = async () => {
  try {
    if (selectedRole.value.id) {
      await api.roles.update(selectedRole.value.id, roleForm.value)
      toast.success('Role updated')
    } else {
      await api.roles.create(roleForm.value)
      toast.success('Role created')
    }
    await fetchRoles()
    selectedRole.value = null
  } catch (err) {
    toast.error(err.response?.data?.name?.[0] || err.response?.data?.detail || 'Failed to save role')
  }
}

const deleteRole = async (role) => {
  if (!confirm(`Delete role "${role.name}"?`)) return
  try {
    await api.roles.delete(role.id)
    toast.success('Role deleted')
    selectedRole.value = null
    await fetchRoles()
  } catch (err) {
    toast.error(err.response?.data?.detail || 'Failed to delete role')
  }
}

const openCreateUser = () => {
  // The create/edit modal is teleported from within the Users-tab-only
  // section, so it never renders while viewing Roles & Permissions -- switch
  // tabs first so "Add New User" always actually opens the form.
  activeTab.value = 'users'
  showCreateModal.value = true
}

const editUser = (user) => {
  editingUser.value = user
  validationErrors.value = {}
  userForm.value = {
    username: user.username,
    first_name: user.first_name,
    last_name: user.last_name,
    email: user.email,
    role: user.role,
    password: '',
    password2: '',
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
  // Clear previous validation errors
  validationErrors.value = {}

  try {
    await api.users.create(userForm.value)
    toast.success('User created successfully')
    closeModal()
    await fetchUsers()
  } catch (err) {
    console.error('Failed to create user:', err)

    // Handle validation errors from Django
    if (err.response?.data) {
      const errors = err.response.data

      // Store all validation errors
      validationErrors.value = errors

      // Show a toast with the first error message
      if (errors.password2) {
        const errorMsg = Array.isArray(errors.password2) ? errors.password2[0] : errors.password2
        toast.error(errorMsg)
      } else if (errors.password) {
        const errorMsg = Array.isArray(errors.password) ? errors.password[0] : errors.password
        toast.error(errorMsg)
      } else if (errors.detail) {
        toast.error(errors.detail)
      } else if (errors.username) {
        const errorMsg = Array.isArray(errors.username) ? errors.username[0] : errors.username
        toast.error(errorMsg)
      } else {
        toast.error('Failed to create user. Please check the form.')
      }
    } else {
      toast.error(err.message || 'Failed to create user')
    }
  }
}

const updateUser = async () => {
  // Clear previous validation errors
  validationErrors.value = {}

  try {
    await api.users.update(editingUser.value.id, userForm.value)
    toast.success('User updated successfully')
    closeModal()
    await fetchUsers()
  } catch (err) {
    console.error('Failed to update user:', err)

    // Handle validation errors from Django
    if (err.response?.data) {
      const errors = err.response.data
      validationErrors.value = errors

      // Show appropriate error message
      if (errors.detail) {
        toast.error(errors.detail)
      } else {
        toast.error('Failed to update user. Please check the form.')
      }
    } else {
      toast.error(err.message || 'Failed to update user')
    }
  }
}

const closeModal = () => {
  showCreateModal.value = false
  editingUser.value = null
  validationErrors.value = {}
  userForm.value = {
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    role: '',
    password: '',
    password2: '',
    is_active: true
  }
}

const formatDate = (date) => {
  if (!date) return 'Never'
  return new Date(date).toLocaleDateString()
}

const getRoleClass = (slug) => {
  const classes = {
    'admin': 'bg-red-100 text-red-800',
    'editor': 'bg-purple-100 text-purple-800',
    'author': 'bg-blue-100 text-blue-800',
    'viewer': 'bg-gray-100 text-gray-800'
  }
  return classes[slug] || 'bg-indigo-100 text-indigo-800'
}

onMounted(() => {
  fetchUsers()
  fetchRoles()
  fetchPermissions()
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
