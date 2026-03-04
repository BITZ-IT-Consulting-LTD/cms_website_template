<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Help Services"
      description="Manage the protection services and detailed help content displayed on the homepage."
      action-label="Add Help Service" :action-icon="PlusIcon" @action="openCreateModal" />

    <!-- Stats -->
    <StatsGrid>
      <StatCard label="Total Categories" :value="stats.total" :icon="ShieldCheckIcon" color="blue" />
      <StatCard label="Active Items" :value="stats.active" :icon="CheckCircleIcon" color="green" />
      <StatCard label="Homepage Order" :value="stats.ordered" :icon="ListBulletIcon" color="purple" />
    </StatsGrid>

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading help services..." />

    <!-- Empty State -->
    <EmptyState v-else-if="services.length === 0" title="No Help Services Found"
      message="Set up the protection areas (e.g., Child Protection, GBV) that users can interact with."
      action-label="Add First Service" :action-icon="PlusIcon" :icon="ShieldCheckIcon" @action="openCreateModal" />

    <!-- Help Services Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-6">
      <div v-for="service in services" :key="service.id"
        class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden group hover:shadow-xl transition-all duration-300">
        <div class="p-8">
          <div class="flex justify-between items-start mb-6">
            <div class="flex items-center gap-4">
              <div
                class="p-4 rounded-2xl bg-blue-50 text-blue-600 group-hover:bg-blue-600 group-hover:text-white transition-all duration-300 shadow-sm">
                <component :is="getIcon(service.icon_name)" class="h-8 w-8" />
              </div>
              <div>
                <h3 class="text-xl font-black text-gray-900">{{ service.title }}</h3>
                <span class="text-xs font-bold text-gray-400 uppercase tracking-widest">Key: {{ service.key }}</span>
              </div>
            </div>
            <div class="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
              <button @click="editService(service)"
                class="p-2.5 bg-gray-50 hover:bg-blue-50 rounded-xl text-gray-400 hover:text-blue-600 transition-all shadow-sm">
                <PencilSquareIcon class="h-5 w-5" />
              </button>
              <button @click="confirmDelete(service)"
                class="p-2.5 bg-gray-50 hover:bg-red-50 rounded-xl text-gray-400 hover:text-red-600 transition-all shadow-sm">
                <TrashIcon class="h-5 w-5" />
              </button>
            </div>
          </div>

          <!-- Content Preview -->
          <div class="space-y-4 mb-6">
            <div>
              <span class="text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] block mb-1">Homepage
                Summary</span>
              <p class="text-gray-600 text-sm leading-relaxed line-clamp-2 italic">"{{ service.summary }}"</p>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <span class="text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] block mb-1">Scope
                  Items</span>
                <span class="text-sm font-bold text-gray-900">{{ service.scope_items?.length || 0 }} Items</span>
              </div>
              <div>
                <span class="text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] block mb-1">Action
                  Steps</span>
                <span class="text-sm font-bold text-gray-900">{{ service.steps?.length || 0 }} Steps</span>
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between pt-6 border-t border-gray-50 mt-auto">
            <div class="flex items-center gap-4">
              <div class="flex flex-col">
                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">Homepage Order</span>
                <span class="text-sm font-black text-gray-900">#{{ service.homepage_display_order }}</span>
              </div>
            </div>
            <span class="flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-full"
              :class="service.is_active ? 'bg-green-50 text-green-700 border border-green-100' : 'bg-gray-100 text-gray-500 border border-gray-200'">
              <span class="w-2 h-2 rounded-full"
                :class="service.is_active ? 'bg-green-500 animate-pulse' : 'bg-gray-400'"></span>
              {{ service.is_active ? 'Active' : 'Inactive' }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Enhanced Edit/Create Modal -->
    <Transition name="modal">
      <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
        <div class="absolute inset-0 bg-gray-900/60 backdrop-blur-md" @click="closeModal"></div>
        <div
          class="bg-white rounded-[2.5rem] shadow-2xl w-full max-w-4xl relative overflow-hidden transition-all transform flex flex-col max-h-[90vh]">
          <!-- Modal Header -->
          <div class="p-8 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
            <div class="flex items-center gap-4">
              <div
                class="w-12 h-12 bg-blue-600 rounded-2xl flex items-center justify-center text-white shadow-lg shadow-blue-200">
                <CubeIcon class="h-6 w-6" />
              </div>
              <div>
                <h3 class="text-2xl font-black text-gray-900">{{ modalTitle }}</h3>
                <p class="text-sm text-gray-500 font-medium">Configure deep-linking and interactive steps</p>
              </div>
            </div>
            <button @click="closeModal"
              class="p-3 hover:bg-white rounded-2xl transition-all shadow-sm text-gray-400 hover:text-gray-900 border border-transparent hover:border-gray-100">
              <XMarkIcon class="h-6 w-6" />
            </button>
          </div>

          <!-- Modal Body (Scrollable) -->
          <div class="flex-1 overflow-y-auto p-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
              <!-- Left Column: Basic Info -->
              <div class="space-y-6">
                <div>
                  <h4 class="text-xs font-black text-gray-400 uppercase tracking-[0.2em] mb-4">Core Identification</h4>
                  <div class="space-y-4">
                    <div>
                      <label class="block text-sm font-bold text-gray-700 mb-2">Service Title</label>
                      <input v-model="form.title" type="text" required placeholder="e.g., Child Protection"
                        class="form-input" />
                    </div>
                    <div>
                      <label class="block text-sm font-bold text-gray-700 mb-2">Unique URL Key (Slug)</label>
                      <select v-model="form.key" required class="form-input">
                        <option value="child-protection">child-protection</option>
                        <option value="gbv">gbv</option>
                        <option value="migrants">migrants</option>
                        <option value="psea">psea</option>
                      </select>
                      <p class="text-[10px] text-gray-400 mt-2 font-bold uppercase tracking-wider">Crucial for deep
                        links (e.g., sauti116.go.ug/#child-protection)</p>
                    </div>
                  </div>
                </div>

                <div>
                  <h4 class="text-xs font-black text-gray-400 uppercase tracking-[0.2em] mb-4">Visuals & Display</h4>
                  <div class="grid grid-cols-2 gap-4">
                    <div>
                      <label class="block text-sm font-bold text-gray-700 mb-2">Heroicon Name</label>
                      <input v-model="form.icon_name" type="text" placeholder="ShieldCheckIcon" class="form-input" />
                    </div>
                    <div>
                      <label class="block text-sm font-bold text-gray-700 mb-2">Home Order</label>
                      <input v-model="form.homepage_display_order" type="number" class="form-input" />
                    </div>
                  </div>
                </div>

                <div>
                  <label class="block text-sm font-bold text-gray-700 mb-2">Homepage Summary Card Text</label>
                  <textarea v-model="form.summary" rows="3" required
                    placeholder="A short 1-2 sentence hook for the homepage grid..."
                    class="form-input resize-none italic"></textarea>
                </div>

                <div class="flex items-center gap-3 p-4 bg-gray-50 rounded-2xl border border-gray-100">
                  <input type="checkbox" id="is_active" v-model="form.is_active"
                    class="w-6 h-6 rounded-lg text-blue-600 focus:ring-blue-600 border-gray-300" />
                  <label for="is_active" class="text-sm font-bold text-gray-700 cursor-pointer select-none">
                    This service is active and visible to public
                  </label>
                </div>
              </div>

              <!-- Right Column: Rich Content -->
              <div class="space-y-6">
                <div>
                  <h4 class="text-xs font-black text-gray-400 uppercase tracking-[0.2em] mb-4">Expanded Bio Content</h4>
                  <div class="space-y-4">
                    <div>
                      <label class="block text-sm font-bold text-gray-700 mb-2">Introduction Text (Expanded
                        View)</label>
                      <textarea v-model="form.intro_text" rows="4" required
                        placeholder="Detailed explanation shown when the user expands the service card..."
                        class="form-input resize-none"></textarea>
                    </div>
                    <div>
                      <label class="block text-sm font-bold text-gray-700 mb-2">Scope Items (One per line)</label>
                      <textarea v-model="scopeItemsText" rows="4"
                        placeholder="Abuse/Neglect&#10;Labor Exploitation&#10;Missing Children"
                        class="form-input resize-none font-medium"></textarea>
                    </div>
                  </div>
                </div>

                <!-- Steps Manager -->
                <div>
                  <div class="flex justify-between items-center mb-4">
                    <h4 class="text-xs font-black text-gray-400 uppercase tracking-[0.2em]">What to expect (Steps)</h4>
                    <button type="button" @click="addStep"
                      class="text-blue-600 font-bold text-xs hover:underline flex items-center gap-1">
                      <PlusIcon class="w-4 h-4" /> Add Step
                    </button>
                  </div>
                  <div class="space-y-3">
                    <div v-for="(step, index) in localSteps" :key="index"
                      class="p-4 bg-white border border-gray-100 rounded-2xl shadow-sm space-y-3 relative group/step">
                      <button @click="removeStep(index)"
                        class="absolute top-2 right-2 p-1 text-gray-300 hover:text-red-500 opacity-0 group-hover/step:opacity-100 transition-opacity">
                        <TrashIcon class="w-4 h-4" />
                      </button>
                      <div class="flex items-center gap-2">
                        <span
                          class="w-6 h-6 rounded-full bg-blue-100 text-blue-600 text-[10px] font-black flex items-center justify-center">{{
                            index + 1 }}</span>
                        <input v-model="step.title" type="text" placeholder="Step title"
                          class="flex-1 text-sm font-bold border-none p-0 focus:ring-0" />
                      </div>
                      <textarea v-model="step.description" rows="2" placeholder="Step instructions..."
                        class="w-full text-xs text-gray-600 border-none p-0 focus:ring-0 resize-none"></textarea>
                    </div>
                    <div v-if="localSteps.length === 0"
                      class="text-center py-6 border-2 border-dashed border-gray-100 rounded-2xl text-gray-400 text-xs font-medium italic">
                      No steps defined. Add steps to guide the user.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Modal Footer -->
          <div class="p-8 border-t border-gray-100 flex gap-4 bg-gray-50/50">
            <button type="button" @click="closeModal"
              class="flex-1 px-8 py-4 rounded-2xl border border-gray-200 font-black text-gray-600 hover:bg-white hover:shadow-sm transition-all focus:ring-4 focus:ring-gray-100">
              Cancel
            </button>
            <button @click="saveFullService" :disabled="saving"
              class="flex-[2] px-8 py-4 rounded-2xl bg-blue-600 text-white font-black hover:bg-blue-700 shadow-xl shadow-blue-200 transition-all flex items-center justify-center focus:ring-4 focus:ring-blue-100 group">
              <div v-if="saving" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-3"></div>
              <component :is="submitIcon" v-else class="w-5 h-5 mr-3 group-hover:scale-110 transition-transform" />
              {{ submitLabel }}
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted, watch } from 'vue';
  import { api } from '@/utils/api';
  import { useToast } from 'vue-toastification';
  import { PageHeader, StatsGrid, StatCard, LoadingState, EmptyState } from '@/components/admin';
  import {
    PlusIcon,
    ShieldCheckIcon,
    PencilSquareIcon,
    TrashIcon,
    XMarkIcon,
    CheckCircleIcon,
    EyeSlashIcon,
    ListBulletIcon,
    CubeIcon,
    UserGroupIcon,
    PhoneIcon,
    ChatBubbleLeftRightIcon,
    FingerPrintIcon,
    LifebuoyIcon
  } from '@heroicons/vue/24/outline';

  const toast = useToast();
  const services = ref([]);
  const loading = ref(true);
  const showModal = ref(false);
  const editingService = ref(null);
  const saving = ref(false);

  const form = ref({
    key: 'child-protection',
    title: '',
    summary: '',
    icon_name: 'ShieldCheckIcon',
    intro_text: '',
    scope_items: [],
    is_active: true,
    order: 0,
    homepage_display_order: 0
  });

  const scopeItemsText = ref('');
  const localSteps = ref([]);

  const modalTitle = computed(() => {
    return editingService.value ? 'Edit Help Service' : 'Create New Service';
  });

  const submitLabel = computed(() => {
    return editingService.value ? 'Update All Content' : 'Publish Service';
  });

  const submitIcon = computed(() => {
    return editingService.value ? CheckCircleIcon : PlusIcon;
  });

  const stats = computed(() => {
    const items = services.value || [];
    return {
      total: items.length,
      active: items.filter(s => s.is_active).length,
      ordered: items.filter(s => s.homepage_display_order > 0).length
    };
  });

  const getIcon = (name) => {
    const map = {
      ShieldCheckIcon,
      UserGroupIcon,
      PhoneIcon,
      ChatBubbleLeftRightIcon,
      FingerPrintIcon,
      LifebuoyIcon
    };
    return map[name] || ShieldCheckIcon;
  };

  const fetchServices = async () => {
    loading.value = true;
    try {
      const response = await api.helpServices.list();
      services.value = response.data.results || response.data;
    } catch (error) {
      console.error('Error fetching help services:', error);
      toast.error('Failed to load help services');
    } finally {
      loading.value = false;
    }
  };

  const openCreateModal = () => {
    editingService.value = null;
    form.value = {
      key: 'child-protection',
      title: '',
      summary: '',
      icon_name: 'ShieldCheckIcon',
      intro_text: '',
      scope_items: [],
      is_active: true,
      order: services.value.length + 1,
      homepage_display_order: services.value.length + 1
    };
    scopeItemsText.value = '';
    localSteps.value = [];
    showModal.value = true;
  };

  const closeModal = () => {
    showModal.value = false;
    editingService.value = null;
  };

  const addStep = () => {
    localSteps.value.push({
      title: '',
      description: '',
      step_order: localSteps.value.length + 1
    });
  };

  const removeStep = (index) => {
    localSteps.value.splice(index, 1);
    // Reorder
    localSteps.value.forEach((s, i) => s.step_order = i + 1);
  };

  const saveFullService = async () => {
    saving.value = true;
    try {
      // 1. Process scope items
      const payload = {
        ...form.value,
        scope_items: scopeItemsText.value
          .split('\n')
          .map(item => item.trim())
          .filter(item => item !== ''),
        steps: localSteps.value.map(s => ({
          title: s.title,
          description: s.description,
          step_order: s.step_order
        }))
      };

      if (editingService.value) {
        await api.helpServices.update(editingService.value.id, payload);
      } else {
        await api.helpServices.create(payload);
      }

      toast.success('Help service content updated successfully');
      await fetchServices();
      closeModal();
    } catch (error) {
      console.error('Error saving help service:', error);
      toast.error('Failed to save help service');
    } finally {
      saving.value = false;
    }
  };

  const editService = (service) => {
    editingService.value = service;
    form.value = { ...service };
    scopeItemsText.value = (service.scope_items || []).join('\n');
    localSteps.value = JSON.parse(JSON.stringify(service.steps || []));
    showModal.value = true;
  };

  const confirmDelete = async (service) => {
    if (confirm(`Are you sure you want to delete "${service.title}"? This will remove all associated content and steps.`)) {
      try {
        await api.helpServices.delete(service.id);
        toast.success('Help service removed');
        await fetchServices();
      } catch (error) {
        console.error('Error deleting service:', error);
        toast.error('Failed to delete service');
      }
    }
  };

  onMounted(fetchServices);
</script>

<style scoped>
  .form-input {
    width: 100%;
    padding: 0.875rem 1.25rem;
    border-radius: 1rem;
    border: 1px solid #e5e7eb;
    outline: none;
    transition: all 0.2s;
    font-weight: 500;
    color: #374151;
    background-color: white;
  }

  .form-input:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 4px #dbeafe;
  }

  .modal-enter-active,
  .modal-leave-active {
    transition: opacity 0.3s ease;
  }

  .modal-enter-from,
  .modal-leave-to {
    opacity: 0;
  }

  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>
