<template>
  <div class="py-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold">Manage Site Content</h1>
      <button @click="openCreateModal" class="btn-primary">
        <PlusIcon class="h-5 w-5 mr-2" />
        Add Content
      </button>
    </div>

    <!-- Main Tabs (Pages) -->
    <div class="mb-8 border-b border-gray-200 overflow-x-auto">
      <nav class="flex space-x-8" aria-label="Main Tabs">
        <button v-for="page in pages" :key="page.value" @click="activePage = page.value" :class="[
          'px-3 py-2 font-medium text-sm rounded-md whitespace-nowrap',
          activePage === page.value ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:text-gray-700'
        ]">
          {{ page.label }}
        </button>
      </nav>
    </div>

    <!-- ==================== ABOUT PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'about'" class="space-y-6">

      <!-- Section 1: Hero Grid Images -->
      <CollapsibleSection
        title="Hero Grid Images"
        subtitle="Manage the 9 images displayed in the hero section grid on the About page"
        :icon="PhotoIcon"
        :badge="{ text: `${heroImagesStats.filled}/9`, color: heroImagesStats.filled === 9 ? 'green' : 'amber' }"
        defaultOpen
      >
        <div class="bg-gray-50 rounded-2xl p-4 mb-4">
          <p class="text-sm text-gray-600 mb-4">Click on any position to add or edit the image for that slot.</p>

          <!-- Grid Preview -->
          <div class="grid grid-cols-[1fr_2fr_1fr] gap-2 max-w-2xl mx-auto">
            <!-- Left Column -->
            <div class="flex flex-col gap-2">
              <ImageSlotMini v-for="pos in [1, 2, 3]" :key="pos" :position="pos"
                :image="getHeroImageByPosition(pos)" :label="heroPositionLabels[pos]?.name"
                @click="openHeroImageModal(pos)" />
            </div>
            <!-- Center Grid (2x2) -->
            <div class="grid grid-cols-2 grid-rows-2 gap-2">
              <ImageSlotMini v-for="pos in [4, 5, 6, 7]" :key="pos" :position="pos"
                :image="getHeroImageByPosition(pos)" :label="heroPositionLabels[pos]?.name"
                @click="openHeroImageModal(pos)" />
            </div>
            <!-- Right Column -->
            <div class="flex flex-col gap-2">
              <ImageSlotMini v-for="pos in [8, 9]" :key="pos" :position="pos"
                :image="getHeroImageByPosition(pos)" :label="heroPositionLabels[pos]?.name"
                @click="openHeroImageModal(pos)" />
              <div class="aspect-[4/3] bg-blue-50 rounded-lg flex items-center justify-center border border-blue-200">
                <p class="text-blue-600 text-[10px] font-bold text-center px-1">"Every Child Matters"</p>
              </div>
            </div>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Impact Statistics -->
      <CollapsibleSection
        title="Impact Statistics"
        subtitle="Update the stat cards in the 'Reach Across the Nation' section"
        :icon="ChartBarIcon"
        :badge="{ text: `${impactStats.length} cards`, color: 'blue' }"
      >
        <div class="space-y-3">
          <div v-for="(stat, index) in impactStats" :key="stat.valueKey"
            class="grid grid-cols-1 md:grid-cols-12 gap-3 items-start border border-gray-100 rounded-lg p-3 bg-gray-50">
            <div class="md:col-span-3">
              <label class="block text-xs font-semibold text-gray-600 mb-1">Value</label>
              <input v-model="stat.value" type="text"
                class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm" placeholder="e.g. 2.7M+" />
            </div>
            <div class="md:col-span-7">
              <label class="block text-xs font-semibold text-gray-600 mb-1">Label</label>
              <input v-model="stat.label" type="text"
                class="w-full px-3 py-2 border border-gray-300 rounded-md text-sm" placeholder="e.g. Calls Received" />
            </div>
            <div class="md:col-span-2 flex items-center justify-between gap-2 pt-5">
              <span class="text-xs font-semibold text-gray-400">Card {{ index + 1 }}</span>
              <button @click="removeImpactStat(stat)" class="text-xs font-semibold text-red-500 hover:text-red-700">
                Remove
              </button>
            </div>
          </div>
          <div class="flex gap-2 pt-2">
            <button @click="addImpactStat"
              class="px-4 py-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-700 hover:bg-gray-50">
              + Add Card
            </button>
            <button @click="saveImpactStats" :disabled="impactStatsSaving"
              class="px-4 py-2 text-sm font-medium rounded-lg bg-emerald-600 text-white hover:bg-emerald-700">
              {{ impactStatsSaving ? 'Saving...' : 'Save Impact Stats' }}
            </button>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 3: Team Members -->
      <CollapsibleSection
        title="Team Members"
        subtitle="Manage organization team profiles displayed on the About page"
        :icon="UserGroupIcon"
        :badge="{ text: `${teamMembers.length} members`, color: 'purple' }"
      >
        <div v-if="teamLoading" class="py-8 text-center text-gray-500">Loading team...</div>
        <div v-else>
          <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3 mb-4">
            <div v-for="member in teamMembers" :key="member.id"
              class="bg-white rounded-xl border border-gray-200 overflow-hidden cursor-pointer hover:shadow-md transition-shadow"
              @click="openTeamModal(member)">
              <div class="aspect-square bg-gray-100 relative">
                <img v-if="member.image_url || member.image" :src="member.image_url || member.image" :alt="member.name"
                  class="w-full h-full object-cover" />
                <div v-else class="w-full h-full flex items-center justify-center">
                  <UserIcon class="w-10 h-10 text-gray-300" />
                </div>
                <div class="absolute top-1 right-1">
                  <span class="w-2 h-2 rounded-full block" :class="member.is_active ? 'bg-green-500' : 'bg-gray-300'"></span>
                </div>
              </div>
              <div class="p-2">
                <p class="text-xs font-bold text-gray-900 truncate">{{ member.name }}</p>
                <p class="text-[10px] text-gray-500 truncate">{{ member.role }}</p>
              </div>
            </div>
            <!-- Add New Card -->
            <div class="bg-gray-50 rounded-xl border-2 border-dashed border-gray-200 flex items-center justify-center cursor-pointer hover:border-emerald-400 hover:bg-emerald-50 transition-colors min-h-[140px]"
              @click="openTeamModal(null)">
              <div class="text-center p-2">
                <PlusIcon class="h-8 w-8 mx-auto text-gray-400" />
                <p class="text-xs font-bold text-gray-400 mt-1">Add Member</p>
              </div>
            </div>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 4: Timeline Events -->
      <CollapsibleSection
        title="Timeline Events"
        subtitle="Manage the 'Our Journey' timeline milestones"
        :icon="ClockIcon"
        :badge="{ text: `${timelineEvents.length} events`, color: 'indigo' }"
      >
        <div v-if="timelineLoading" class="py-8 text-center text-gray-500">Loading timeline...</div>
        <div v-else>
          <div class="space-y-2 mb-4">
            <div v-for="event in timelineEvents" :key="event.id"
              class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg border border-gray-100 cursor-pointer hover:bg-gray-100"
              @click="openTimelineModal(event)">
              <div class="w-16 h-16 bg-indigo-100 rounded-lg flex items-center justify-center flex-shrink-0">
                <span class="text-indigo-600 font-bold text-sm">{{ event.year }}</span>
              </div>
              <div class="flex-1 min-w-0">
                <p class="font-bold text-gray-900 text-sm">{{ event.title }}</p>
                <p class="text-xs text-gray-500 truncate">{{ event.description }}</p>
              </div>
              <div class="flex gap-1">
                <button @click.stop="openTimelineModal(event)" class="p-1.5 hover:bg-white rounded-lg">
                  <PencilIcon class="h-4 w-4 text-gray-400" />
                </button>
                <button @click.stop="deleteTimeline(event)" class="p-1.5 hover:bg-white rounded-lg">
                  <TrashIcon class="h-4 w-4 text-red-400" />
                </button>
              </div>
            </div>
          </div>
          <button @click="openTimelineModal(null)"
            class="w-full py-3 border-2 border-dashed border-gray-200 rounded-lg text-sm font-medium text-gray-500 hover:border-indigo-400 hover:text-indigo-600">
            + Add Timeline Event
          </button>
        </div>
      </CollapsibleSection>

      <!-- Section 5: Core Values -->
      <CollapsibleSection
        title="Core Values"
        subtitle="Manage the core values displayed on the About page"
        :icon="HeartIcon"
        :badge="{ text: `${coreValues.length} values`, color: 'rose' }"
      >
        <div v-if="valuesLoading" class="py-8 text-center text-gray-500">Loading values...</div>
        <div v-else>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4">
            <div v-for="value in coreValues" :key="value.id"
              class="flex items-start gap-3 p-4 bg-gradient-to-br from-gray-50 to-white rounded-xl border border-gray-100 cursor-pointer hover:shadow-md"
              @click="openValueModal(value)">
              <div :class="['w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0', valueColorClasses(value).bg]">
                <component :is="sharedIconComponent(value.icon)" :class="['h-5 w-5', valueColorClasses(value).text]" />
              </div>
              <div class="flex-1 min-w-0">
                <p class="font-bold text-gray-900 text-sm">{{ value.title }}</p>
                <p class="text-xs text-gray-500 line-clamp-2">{{ value.description }}</p>
              </div>
            </div>
          </div>
          <button @click="openValueModal(null)"
            class="w-full py-3 border-2 border-dashed border-rose-200 rounded-lg text-sm font-medium text-rose-400 hover:border-rose-400 hover:text-rose-600">
            + Add Core Value
          </button>
        </div>
      </CollapsibleSection>

      <!-- Section 6: Protection Approach -->
      <CollapsibleSection
        title="Protection Approach"
        subtitle="Manage the case resolution path steps"
        :icon="ShieldCheckIcon"
        :badge="{ text: `${protectionApproaches.length} steps`, color: 'teal' }"
      >
        <div v-if="approachLoading" class="py-8 text-center text-gray-500">Loading...</div>
        <div v-else>
          <div class="space-y-2 mb-4">
            <div v-for="(approach, idx) in protectionApproaches" :key="approach.id"
              class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg border border-gray-100 cursor-pointer hover:shadow-sm"
              @click="openApproachModal(approach)">
              <div :class="['w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0', approachColorClasses(approach).bg]">
                <component :is="sharedIconComponent(approach.icon)" :class="['h-4 w-4', approachColorClasses(approach).text]" />
              </div>
              <div class="flex-1 min-w-0">
                <p class="font-bold text-gray-900 text-sm">{{ idx + 1 }}. {{ approach.title }}</p>
                <p class="text-xs text-gray-500 truncate">{{ approach.description }}</p>
              </div>
              <button @click.stop="deleteApproach(approach)" class="p-1.5 hover:bg-white rounded-lg">
                <TrashIcon class="h-4 w-4 text-red-400" />
              </button>
            </div>
          </div>
          <button @click="openApproachModal(null)"
            class="w-full py-3 border-2 border-dashed border-teal-200 rounded-lg text-sm font-medium text-teal-500 hover:border-teal-400 hover:text-teal-600">
            + Add Step
          </button>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== OPERATIONS PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'operations'" class="space-y-6">

      <!-- Section 1: Journey Steps Images -->
      <CollapsibleSection
        title="Journey Steps Images"
        subtitle="Manage the 4 images for 'The Journey of a Voice' section"
        :icon="MapIcon"
        :badge="{ text: `${opsJourneyImagesStats.filled}/${opsJourneyImagesStats.total}`, color: opsJourneyImagesStats.filled === 4 ? 'green' : 'amber' }"
        defaultOpen
      >
        <div class="bg-gray-50 rounded-2xl p-4 mb-4">
          <p class="text-sm text-gray-600 mb-4">Click on any step to add or edit the image for that position.</p>

          <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div v-for="pos in opsJourneyPositions" :key="pos.value"
              class="bg-white rounded-xl border-2 border-dashed border-gray-200 hover:border-emerald-400 cursor-pointer overflow-hidden transition-all"
              @click="openOpsImageModal(pos.value, pos)">
              <div class="aspect-[4/5] bg-gray-100 relative">
                <img v-if="getOpsImageByPosition(pos.value)?.image_url"
                  :src="getOpsImageByPosition(pos.value).image_url"
                  :alt="pos.name"
                  class="w-full h-full object-cover" />
                <div v-else class="w-full h-full flex items-center justify-center">
                  <PhotoIcon class="w-10 h-10 text-gray-300" />
                </div>
                <div v-if="getOpsImageByPosition(pos.value)" class="absolute top-2 right-2">
                  <span class="w-3 h-3 rounded-full block bg-green-500"></span>
                </div>
              </div>
              <div class="p-3 text-center">
                <p class="text-sm font-bold text-gray-900">{{ pos.name }}</p>
                <p class="text-xs text-gray-500">{{ pos.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Infrastructure Image -->
      <CollapsibleSection
        title="Infrastructure Image"
        subtitle="Manage the main image for the infrastructure section"
        :icon="CogIcon"
        :badge="{ text: opsInfraImageExists ? '1/1' : '0/1', color: opsInfraImageExists ? 'green' : 'amber' }"
      >
        <div class="bg-gray-50 rounded-2xl p-4">
          <p class="text-sm text-gray-600 mb-4">This image appears in the 'Our Foundation' infrastructure section.</p>

          <div class="max-w-md mx-auto">
            <div class="bg-white rounded-xl border-2 border-dashed border-gray-200 hover:border-emerald-400 cursor-pointer overflow-hidden transition-all"
              @click="openOpsImageModal(opsInfraPosition.value, opsInfraPosition)">
              <div class="aspect-square bg-gray-100 relative">
                <img v-if="getOpsImageByPosition('infrastructure')?.image_url"
                  :src="getOpsImageByPosition('infrastructure').image_url"
                  alt="Infrastructure"
                  class="w-full h-full object-cover" />
                <div v-else class="w-full h-full flex items-center justify-center flex-col">
                  <CogIcon class="w-12 h-12 text-gray-300 mb-2" />
                  <p class="text-sm text-gray-400">Click to upload</p>
                </div>
                <div v-if="getOpsImageByPosition('infrastructure')" class="absolute top-2 right-2">
                  <span class="w-3 h-3 rounded-full block bg-green-500"></span>
                </div>
              </div>
              <div class="p-3 text-center">
                <p class="text-sm font-bold text-gray-900">{{ opsInfraPosition.name }}</p>
                <p class="text-xs text-gray-500">{{ opsInfraPosition.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 3: Services Images -->
      <CollapsibleSection
        title="Services Images"
        subtitle="Manage the 6 images for 'Services We Offer' section"
        :icon="BriefcaseIcon"
        :badge="{ text: `${opsServiceImagesStats.filled}/${opsServiceImagesStats.total}`, color: opsServiceImagesStats.filled === 6 ? 'green' : 'amber' }"
      >
        <div class="bg-gray-50 rounded-2xl p-4 mb-4">
          <p class="text-sm text-gray-600 mb-4">Click on any service to add or edit its image.</p>

          <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div v-for="pos in opsServicePositions" :key="pos.value"
              class="bg-white rounded-xl border-2 border-dashed border-gray-200 hover:border-emerald-400 cursor-pointer overflow-hidden transition-all"
              @click="openOpsImageModal(pos.value, pos)">
              <div class="aspect-video bg-gray-100 relative">
                <img v-if="getOpsImageByPosition(pos.value)?.image_url"
                  :src="getOpsImageByPosition(pos.value).image_url"
                  :alt="pos.name"
                  class="w-full h-full object-cover" />
                <div v-else class="w-full h-full flex items-center justify-center">
                  <PhotoIcon class="w-8 h-8 text-gray-300" />
                </div>
                <div v-if="getOpsImageByPosition(pos.value)" class="absolute top-2 right-2">
                  <span class="w-3 h-3 rounded-full block bg-green-500"></span>
                </div>
              </div>
              <div class="p-3">
                <p class="text-sm font-bold text-gray-900">{{ pos.name }}</p>
                <p class="text-xs text-gray-500 line-clamp-1">{{ pos.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- Operations Page Text Content (shown below sections) -->
    <div v-if="activePage === 'operations'" class="mt-8">
      <h3 class="text-lg font-bold text-gray-800 mb-4">Text Content</h3>
      <p class="text-sm text-gray-500 mb-4">Edit text labels, titles, and descriptions for the Operations page.</p>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="item in filteredContent" :key="item.key"
          class="bg-white rounded-lg shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
          @click="openEditModal(item)">
          <div class="flex justify-between items-start mb-2">
            <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || item.key }}</h4>
            <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
              {{ item.type }}
            </span>
          </div>
          <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
        </div>
      </div>
    </div>

    <!-- ==================== HOME PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'home'" class="space-y-6">

      <!-- Section 1: Hero Section -->
      <CollapsibleSection
        title="Hero Section"
        subtitle="Main banner content - headline, subheadline, and call-to-action buttons"
        :icon="SparklesIcon"
        :badge="{ text: `${getContentCountByPrefix('home_hero_')} items`, color: 'blue' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('home_hero_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: News Section -->
      <CollapsibleSection
        title="News Section"
        subtitle="News/Updates section titles and featured news placeholders"
        :icon="NewspaperIcon"
        :badge="{ text: `${getContentCountByPrefix('home_news_')} items`, color: 'purple' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('home_news_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 3: Partners Section -->
      <CollapsibleSection
        title="Partners Section"
        subtitle="Partners/Supporters section titles and descriptions"
        :icon="UsersIcon"
        :badge="{ text: `${getContentCountByPrefix('home_partners_')} items`, color: 'green' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('home_partners_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 4: Social Links -->
      <CollapsibleSection
        title="Social Media Links"
        subtitle="Social media URLs and labels"
        :icon="GlobeAltIcon"
        :badge="{ text: `${getContentCountByPrefix('home_social_')} items`, color: 'cyan' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('home_social_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 5: Logos & Alt Text -->
      <CollapsibleSection
        title="Logos & Alt Text"
        subtitle="Logo image alt text and accessibility labels"
        :icon="PhotoIcon"
        :badge="{ text: `${getContentCountByPrefix('home_logo_')} items`, color: 'gray' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('home_logo_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== VIDEOS PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'videos'" class="space-y-6">

      <!-- Section 1: Page Header -->
      <CollapsibleSection
        title="Page Header"
        subtitle="Video gallery page title and description"
        :icon="FilmIcon"
        :badge="{ text: `${getContentCountByPrefix('videos_page_')} items`, color: 'red' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('videos_page_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Search Section -->
      <CollapsibleSection
        title="Search & UI"
        subtitle="Search box placeholder and button labels"
        :icon="MagnifyingGlassIcon"
        :badge="{ text: `${getContentCountByPrefix('videos_search_')} items`, color: 'blue' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('videos_search_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== BLOG PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'blog'" class="space-y-6">

      <!-- Section 1: Page Header -->
      <CollapsibleSection
        title="Page Header"
        subtitle="Blog page title and description"
        :icon="DocumentTextIcon"
        :badge="{ text: `${getContentCountByPrefix('blog_page_')} items`, color: 'orange' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('blog_page_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Search & Filters -->
      <CollapsibleSection
        title="Search & Filters"
        subtitle="Search placeholder, category dropdown, and filter buttons"
        :icon="FunnelIcon"
        :badge="{ text: `${getBlogFilterContentCount()} items`, color: 'blue' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getBlogFilterContent()" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== NEWS PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'news'" class="space-y-6">

      <!-- Section 1: Page Header -->
      <CollapsibleSection
        title="Page Header"
        subtitle="News/Updates page title"
        :icon="NewspaperIcon"
        :badge="{ text: `${getContentCountByPrefix('news_page_')} items`, color: 'violet' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('news_page_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== RESOURCES PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'resources'" class="space-y-6">

      <!-- Section 1: Page Header -->
      <CollapsibleSection
        title="Page Header"
        subtitle="Resources page title and description"
        :icon="FolderIcon"
        :badge="{ text: `${getContentCountByPrefix('resources_page_')} items`, color: 'emerald' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('resources_page_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Search & Filters -->
      <CollapsibleSection
        title="Search & Filters"
        subtitle="Search placeholder and category filter labels"
        :icon="MagnifyingGlassIcon"
        :badge="{ text: `${getResourcesFilterContentCount()} items`, color: 'blue' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getResourcesFilterContent()" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== FAQS PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'faqs'" class="space-y-6">

      <!-- Section 1: Page Header -->
      <CollapsibleSection
        title="Page Header"
        subtitle="FAQs page title and description"
        :icon="QuestionMarkCircleIcon"
        :badge="{ text: `${getContentCountByPrefix('faqs_page_')} items`, color: 'amber' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('faqs_page_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Search -->
      <CollapsibleSection
        title="Search"
        subtitle="FAQ search placeholder text"
        :icon="MagnifyingGlassIcon"
        :badge="{ text: `${getContentCountByPrefix('faqs_search_')} items`, color: 'blue' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('faqs_search_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== CONTACT PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'contact'" class="space-y-6">

      <!-- Section 1: Page Header -->
      <CollapsibleSection
        title="Page Header"
        subtitle="Contact page title, subtitle, and description"
        :icon="EnvelopeIcon"
        :badge="{ text: `${getContentCountByPrefix('contact_page_')} items`, color: 'sky' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('contact_page_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== PARTNERS PAGE SECTIONS ==================== -->
    <div v-if="activePage === 'partners'" class="space-y-6">

      <!-- Section 1: CTA Section -->
      <CollapsibleSection
        title="Call to Action"
        subtitle="Partners CTA section - title, text, and buttons"
        :icon="HandRaisedIcon"
        :badge="{ text: `${getContentCountByPrefix('partners_cta_')} items`, color: 'lime' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('partners_cta_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== FOOTER SECTIONS ==================== -->
    <div v-if="activePage === 'footer'" class="space-y-6">

      <!-- Section 1: Brand -->
      <CollapsibleSection
        title="Brand & Description"
        subtitle="Footer brand description and tagline"
        :icon="BuildingOfficeIcon"
        :badge="{ text: `${getContentCountByPrefix('footer_brand_')} items`, color: 'slate' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('footer_brand_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Contact Info -->
      <CollapsibleSection
        title="Contact Information"
        subtitle="Hotline number, email address, and labels"
        :icon="PhoneIcon"
        :badge="{ text: `${getFooterContactCount()} items`, color: 'green' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getFooterContactContent()" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 3: Section Headings -->
      <CollapsibleSection
        title="Section Headings"
        subtitle="Menu, Support, and Contact column headings"
        :icon="Bars3Icon"
        :badge="{ text: `${getFooterHeadingsCount()} items`, color: 'purple' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getFooterHeadingsContent()" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 4: Legal -->
      <CollapsibleSection
        title="Legal & Copyright"
        subtitle="Copyright text and country label"
        :icon="ScaleIcon"
        :badge="{ text: `${getFooterLegalCount()} items`, color: 'gray' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getFooterLegalContent()" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== HEADER SECTIONS ==================== -->
    <div v-if="activePage === 'header'" class="space-y-6">

      <!-- Section 1: Header Content -->
      <CollapsibleSection
        title="Header Content"
        subtitle="Logo alt text and hotline label"
        :icon="Bars3Icon"
        :badge="{ text: `${getContentCountByPrefix('header_')} items`, color: 'indigo' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getContentByPrefix('header_')" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== GLOBAL SETTINGS SECTIONS ==================== -->
    <div v-if="activePage === 'global'" class="space-y-6">

      <!-- Section 1: Site Information -->
      <CollapsibleSection
        title="Site Information"
        subtitle="Site name and description"
        :icon="GlobeAltIcon"
        :badge="{ text: `${getGlobalSiteInfoCount()} items`, color: 'blue' }"
        defaultOpen
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getGlobalSiteInfoContent()" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>

      <!-- Section 2: Hotline Settings -->
      <CollapsibleSection
        title="Hotline Settings"
        subtitle="Hotline number and operating hours"
        :icon="PhoneIcon"
        :badge="{ text: `${getGlobalHotlineCount()} items`, color: 'green' }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="item in getGlobalHotlineContent()" :key="item.key"
            class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
            @click="openEditModal(item)">
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || formatKeyLabel(item.key) }}</h4>
              <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
                {{ item.type }}
              </span>
            </div>
            <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
          </div>
        </div>
      </CollapsibleSection>
    </div>

    <!-- ==================== FALLBACK: OTHER PAGES (services, reports, donate, reports_insights) ==================== -->
    <div v-if="['services', 'reports', 'donate', 'reports_insights'].includes(activePage)">
      <!-- Standard grid for pages without specific sections -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-if="filteredContent.length === 0"
          class="col-span-full text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
          <p class="text-gray-500">No content found for this page.</p>
          <button @click="openCreateModal" class="mt-4 text-blue-600 hover:text-blue-800 font-medium">
            Create new content item
          </button>
        </div>

        <div v-for="item in filteredContent" :key="item.key"
          class="bg-white rounded-lg shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
          @click="openEditModal(item)">
          <div class="flex justify-between items-start mb-2">
            <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || item.key }}</h4>
            <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
              {{ item.type }}
            </span>
          </div>
          <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
        </div>
      </div>
    </div>

    <!-- About Page Text Content (shown below sections) -->
    <div v-if="activePage === 'about'" class="mt-8">
      <h3 class="text-lg font-bold text-gray-800 mb-4">Text Content</h3>
      <p class="text-sm text-gray-500 mb-4">Edit text labels, titles, and descriptions for the About page.</p>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="item in aboutTextContent" :key="item.key"
          class="bg-white rounded-lg shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer"
          @click="openEditModal(item)">
          <div class="flex justify-between items-start mb-2">
            <h4 class="font-semibold text-gray-900 text-sm">{{ item.label || item.key }}</h4>
            <span :class="getTypeBadgeClass(item.type)" class="px-2 py-0.5 text-[10px] font-semibold rounded-full capitalize">
              {{ item.type }}
            </span>
          </div>
          <p class="text-xs text-gray-500 line-clamp-2">{{ item.value || '(Empty)' }}</p>
        </div>
      </div>
    </div>

    <!-- ==================== MODALS ==================== -->

    <!-- Site Content Edit Modal -->
    <div v-if="showModal" class="fixed z-50 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75" @click="closeModal"></div>
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-xl relative">
          <form @submit.prevent="saveContent" class="p-6">
            <h3 class="text-xl font-bold mb-4">{{ isEditing ? 'Edit Content' : 'Create Content' }}</h3>

            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Key</label>
                <input v-if="!isEditing" v-model="form.key" type="text" required
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg" placeholder="e.g. about_hero_title" />
                <input v-else :value="form.key" disabled class="w-full px-3 py-2 border border-gray-200 rounded-lg bg-gray-100" />
              </div>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Label</label>
                  <input v-model="form.label" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Type</label>
                  <select v-model="form.type" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                    <option value="text">Text</option>
                    <option value="heading">Heading</option>
                    <option value="button">Button</option>
                    <option value="photo">Photo URL</option>
                  </select>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Content Value</label>
                <textarea v-model="form.value" rows="4" class="w-full px-3 py-2 border border-gray-300 rounded-lg"></textarea>
              </div>
            </div>

            <div class="flex gap-3 mt-6">
              <button type="button" @click="closeModal" class="flex-1 px-4 py-2 border border-gray-300 rounded-lg font-medium">
                Cancel
              </button>
              <button type="submit" class="flex-1 px-4 py-2 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700">
                Save
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Hero Image Modal -->
    <div v-if="showHeroImageModal" class="fixed z-50 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeHeroImageModal"></div>
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg relative">
          <div class="p-6 border-b border-gray-100">
            <h3 class="text-xl font-bold">{{ editingHeroImage ? 'Edit Image' : 'Add Image' }}</h3>
            <p class="text-sm text-gray-500">Position {{ selectedHeroPosition }}: {{ heroPositionLabels[selectedHeroPosition]?.name }}</p>
          </div>
          <form @submit.prevent="saveHeroImage" class="p-6 space-y-4">
            <div class="bg-blue-50 rounded-xl p-3 text-sm text-blue-800">
              {{ heroPositionLabels[selectedHeroPosition]?.description }}
            </div>

            <div @click="heroFileInput?.click()"
              class="aspect-video rounded-xl border-2 border-dashed border-gray-200 hover:border-emerald-400 cursor-pointer overflow-hidden flex items-center justify-center bg-gray-50">
              <img v-if="heroImagePreview" :src="heroImagePreview" class="w-full h-full object-cover" />
              <div v-else class="text-center p-4">
                <CloudArrowUpIcon class="h-10 w-10 mx-auto text-gray-400 mb-2" />
                <p class="text-sm font-medium text-gray-400">Click to upload</p>
              </div>
              <input type="file" ref="heroFileInput" class="hidden" accept="image/*" @change="handleHeroImageChange" />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
              <input v-model="heroForm.title" type="text" required class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Alt Text</label>
              <input v-model="heroForm.alt_text" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
            </div>
            <div class="flex items-center gap-2">
              <input type="checkbox" v-model="heroForm.is_active" id="hero_active" class="rounded" />
              <label for="hero_active" class="text-sm">Show on website</label>
            </div>

            <div class="flex gap-3 pt-4">
              <button type="button" @click="closeHeroImageModal" class="flex-1 px-4 py-2 border border-gray-300 rounded-lg font-medium">
                Cancel
              </button>
              <button type="submit" :disabled="heroSaving" class="flex-1 px-4 py-2 bg-emerald-600 text-white rounded-lg font-medium hover:bg-emerald-700">
                {{ heroSaving ? 'Saving...' : 'Save' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Team Member Modal -->
    <div v-if="showTeamModal" class="fixed z-50 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeTeamModal"></div>
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg relative">
          <div class="p-6 border-b border-gray-100">
            <h3 class="text-xl font-bold">{{ editingTeamMember ? 'Edit Team Member' : 'Add Team Member' }}</h3>
          </div>
          <form @submit.prevent="saveTeamMember" class="p-6 space-y-4">
            <div class="flex justify-center">
              <div @click="teamFileInput?.click()"
                class="w-32 h-32 rounded-2xl border-2 border-dashed border-gray-200 hover:border-emerald-400 cursor-pointer overflow-hidden flex items-center justify-center bg-gray-50">
                <img v-if="teamImagePreview" :src="teamImagePreview" class="w-full h-full object-cover" />
                <div v-else class="text-center">
                  <CloudArrowUpIcon class="h-8 w-8 mx-auto text-gray-400" />
                  <p class="text-xs text-gray-400 mt-1">Photo</p>
                </div>
                <input type="file" ref="teamFileInput" class="hidden" accept="image/*" @change="handleTeamImageChange" />
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
                <input v-model="teamForm.name" type="text" required class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Role</label>
                <input v-model="teamForm.role" type="text" required class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Bio</label>
              <textarea v-model="teamForm.bio" rows="2" class="w-full px-3 py-2 border border-gray-300 rounded-lg"></textarea>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Display Order</label>
                <input v-model="teamForm.order" type="number" class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
              </div>
              <div class="flex items-center pt-6">
                <input type="checkbox" v-model="teamForm.is_active" id="team_active" class="rounded mr-2" />
                <label for="team_active" class="text-sm">Show on website</label>
              </div>
            </div>
            <div class="flex gap-3 pt-4">
              <button type="button" @click="closeTeamModal" class="flex-1 px-4 py-2 border border-gray-300 rounded-lg font-medium">Cancel</button>
              <button v-if="editingTeamMember" type="button" @click="deleteTeamMember" class="px-4 py-2 bg-red-100 text-red-600 rounded-lg font-medium">Delete</button>
              <button type="submit" :disabled="teamSaving" class="flex-1 px-4 py-2 bg-emerald-600 text-white rounded-lg font-medium">
                {{ teamSaving ? 'Saving...' : 'Save' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Timeline Event Modal -->
    <div v-if="showTimelineModal" class="fixed z-50 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeTimelineModal"></div>
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg relative">
          <div class="p-6 border-b border-gray-100">
            <h3 class="text-xl font-bold">{{ editingTimeline ? 'Edit Timeline Event' : 'Add Timeline Event' }}</h3>
          </div>
          <form @submit.prevent="saveTimeline" class="p-6 space-y-4">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Year</label>
                <input v-model="timelineForm.year" type="text" required placeholder="e.g. 2013, Aug 2013" class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Order</label>
                <input v-model="timelineForm.order" type="number" class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
              <input v-model="timelineForm.title" type="text" required class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
              <textarea v-model="timelineForm.description" rows="3" required class="w-full px-3 py-2 border border-gray-300 rounded-lg"></textarea>
            </div>
            <div class="flex items-center gap-2">
              <input type="checkbox" v-model="timelineForm.is_visible" id="timeline_active" class="rounded" />
              <label for="timeline_active" class="text-sm">Show on website</label>
            </div>
            <div class="flex gap-3 pt-4">
              <button type="button" @click="closeTimelineModal" class="flex-1 px-4 py-2 border border-gray-300 rounded-lg font-medium">Cancel</button>
              <button type="submit" :disabled="timelineSaving" class="flex-1 px-4 py-2 bg-indigo-600 text-white rounded-lg font-medium">
                {{ timelineSaving ? 'Saving...' : 'Save' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Core Value Modal -->
    <div v-if="showValueModal" class="fixed z-50 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeValueModal"></div>
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg relative">
          <div class="p-6 border-b border-gray-100">
            <h3 class="text-xl font-bold">{{ editingValue ? 'Edit Core Value' : 'Add Core Value' }}</h3>
          </div>
          <form @submit.prevent="saveValue" class="p-6 space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
              <input v-model="valueForm.title" type="text" required class="w-full px-3 py-2 border border-gray-300 rounded-lg" placeholder="e.g. Integrity" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
              <textarea v-model="valueForm.description" rows="3" required class="w-full px-3 py-2 border border-gray-300 rounded-lg"></textarea>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Icon</label>
                <select v-model="valueForm.icon" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                  <option v-for="opt in sharedIconOptions" :key="opt" :value="opt">{{ opt }}</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Color Theme</label>
                <select :value="valueColorTheme" @change="setValueColorTheme($event.target.value)" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                  <option v-for="opt in Object.keys(valueColorThemes)" :key="opt" :value="opt">{{ opt }}</option>
                </select>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Order</label>
                <input v-model="valueForm.order" type="number" class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
              </div>
              <div class="flex items-center pt-6">
                <input type="checkbox" v-model="valueForm.is_active" id="value_active" class="rounded mr-2" />
                <label for="value_active" class="text-sm">Show on website</label>
              </div>
            </div>
            <div class="flex items-center gap-2 text-sm text-gray-500">
              <span class="text-xs uppercase tracking-wide">Preview</span>
              <div :class="['w-8 h-8 rounded-lg flex items-center justify-center', valueColorClasses(valueForm).bg]">
                <component :is="sharedIconComponent(valueForm.icon)" :class="['h-4 w-4', valueColorClasses(valueForm).text]" />
              </div>
            </div>
            <div class="flex gap-3 pt-4">
              <button type="button" @click="closeValueModal" class="flex-1 px-4 py-2 border border-gray-300 rounded-lg font-medium">Cancel</button>
              <button v-if="editingValue" type="button" @click="deleteValue" class="px-4 py-2 bg-red-100 text-red-600 rounded-lg font-medium">Delete</button>
              <button type="submit" :disabled="valueSaving" class="flex-1 px-4 py-2 bg-rose-600 text-white rounded-lg font-medium">
                {{ valueSaving ? 'Saving...' : 'Save' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Protection Approach Modal -->
    <div v-if="showApproachModal" class="fixed z-50 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeApproachModal"></div>
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg relative">
          <div class="p-6 border-b border-gray-100">
            <h3 class="text-xl font-bold">{{ editingApproach ? 'Edit Step' : 'Add Step' }}</h3>
          </div>
          <form @submit.prevent="saveApproach" class="p-6 space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
              <input v-model="approachForm.title" type="text" required class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
              <textarea v-model="approachForm.description" rows="3" required class="w-full px-3 py-2 border border-gray-300 rounded-lg"></textarea>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Icon</label>
                <select v-model="approachForm.icon" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                  <option v-for="opt in sharedIconOptions" :key="opt" :value="opt">{{ opt }}</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Color</label>
                <select v-model="approachForm.color" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                  <option v-for="opt in approachColorOptions" :key="opt" :value="opt">{{ opt }}</option>
                </select>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Order</label>
                <input v-model="approachForm.order" type="number" class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
              </div>
              <div class="flex items-center pt-6">
                <input type="checkbox" v-model="approachForm.is_active" id="approach_active" class="rounded mr-2" />
                <label for="approach_active" class="text-sm">Show on website</label>
              </div>
            </div>
            <div class="flex items-center gap-2 text-sm text-gray-500">
              <span class="text-xs uppercase tracking-wide">Preview</span>
              <div :class="['w-8 h-8 rounded-full flex items-center justify-center', approachColorClasses(approachForm).bg]">
                <component :is="sharedIconComponent(approachForm.icon)" :class="['h-4 w-4', approachColorClasses(approachForm).text]" />
              </div>
            </div>
            <div class="flex gap-3 pt-4">
              <button type="button" @click="closeApproachModal" class="flex-1 px-4 py-2 border border-gray-300 rounded-lg font-medium">Cancel</button>
              <button type="submit" :disabled="approachSaving" class="flex-1 px-4 py-2 bg-teal-600 text-white rounded-lg font-medium">
                {{ approachSaving ? 'Saving...' : 'Save' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Operations Image Modal -->
    <div v-if="showOpsImageModal" class="fixed z-50 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeOpsImageModal"></div>
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg relative">
          <div class="p-6 border-b border-gray-100">
            <h3 class="text-xl font-bold">{{ editingOpsImage ? 'Edit Image' : 'Add Image' }}</h3>
            <p class="text-sm text-gray-500">{{ getOpsPositionInfo(selectedOpsImagePosition)?.name }}</p>
          </div>
          <form @submit.prevent="saveOpsImage" class="p-6 space-y-4">
            <div class="bg-emerald-50 rounded-xl p-3 text-sm text-emerald-800">
              {{ getOpsPositionInfo(selectedOpsImagePosition)?.description }}
            </div>

            <div @click="opsFileInput?.click()"
              class="aspect-video rounded-xl border-2 border-dashed border-gray-200 hover:border-emerald-400 cursor-pointer overflow-hidden flex items-center justify-center bg-gray-50">
              <img v-if="opsImagePreview" :src="opsImagePreview" class="w-full h-full object-cover" />
              <div v-else class="text-center p-4">
                <CloudArrowUpIcon class="h-10 w-10 mx-auto text-gray-400 mb-2" />
                <p class="text-sm font-medium text-gray-400">Click to upload</p>
              </div>
              <input type="file" ref="opsFileInput" class="hidden" accept="image/*" @change="handleOpsImageChange" />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
              <input v-model="opsForm.title" type="text" required class="w-full px-3 py-2 border border-gray-300 rounded-lg" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Alt Text</label>
              <input v-model="opsForm.alt_text" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-lg" placeholder="Describe the image for accessibility" />
            </div>
            <div class="flex items-center gap-2">
              <input type="checkbox" v-model="opsForm.is_active" id="ops_active" class="rounded" />
              <label for="ops_active" class="text-sm">Show on website</label>
            </div>

            <div class="flex gap-3 pt-4">
              <button type="button" @click="closeOpsImageModal" class="flex-1 px-4 py-2 border border-gray-300 rounded-lg font-medium">
                Cancel
              </button>
              <button v-if="editingOpsImage" type="button" @click="deleteOpsImage" class="px-4 py-2 bg-red-100 text-red-600 rounded-lg font-medium hover:bg-red-200">
                Delete
              </button>
              <button type="submit" :disabled="opsSaving" class="flex-1 px-4 py-2 bg-emerald-600 text-white rounded-lg font-medium hover:bg-emerald-700">
                {{ opsSaving ? 'Saving...' : 'Save' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, reactive, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useContentStore } from '@/store/content'
import { api } from '@/utils/api'
import { useToast } from 'vue-toastification'
import {
  PlusIcon, PhotoIcon, ChartBarIcon, UserGroupIcon, ClockIcon, HeartIcon,
  ShieldCheckIcon, PencilIcon, TrashIcon, CloudArrowUpIcon, UserIcon,
  CogIcon, PhoneIcon, MapIcon, BriefcaseIcon,
  // New icons for organized page sections
  SparklesIcon, NewspaperIcon, GlobeAltIcon, FilmIcon, MagnifyingGlassIcon,
  DocumentTextIcon, FunnelIcon, FolderIcon, QuestionMarkCircleIcon,
  EnvelopeIcon, HandRaisedIcon, BuildingOfficeIcon, Bars3Icon, ScaleIcon,
  UsersIcon, CheckIcon, BoltIcon, ShieldExclamationIcon
} from '@heroicons/vue/24/outline'

// Import collapsible components as SFCs
import CollapsibleSection from '@/components/CollapsibleSection.vue'
import ImageSlotMini from '@/components/ImageSlotMini.vue'

const toast = useToast()
const contentStore = useContentStore()
const route = useRoute()

// ==================== STATE ====================
const allContent = ref([])
const activePage = ref('home')
const showModal = ref(false)
const isEditing = ref(false)
const searchQuery = ref('')
const filterType = ref('')
const filterStatus = ref('')

// Form for site content
const form = reactive({ key: '', label: '', value: '', type: 'text', page: 'home', description: '' })

// Hero Images
const heroImages = ref([])
const heroImagesLoading = ref(false)
const showHeroImageModal = ref(false)
const selectedHeroPosition = ref(1)
const editingHeroImage = ref(null)
const heroSaving = ref(false)
const heroImageFile = ref(null)
const heroImagePreview = ref(null)
const heroFileInput = ref(null)
const heroForm = ref({ title: '', alt_text: '', is_active: true })

const heroPositionLabels = {
  1: { name: 'Left Top', description: 'Community engagement image' },
  2: { name: 'Left Middle', description: 'Call center operations' },
  3: { name: 'Left Bottom', description: 'Family support image' },
  4: { name: 'Center Top-Left', description: 'Main team photo' },
  5: { name: 'Center Top-Right', description: 'Positive outcomes' },
  6: { name: 'Center Bottom-Left', description: 'Active work shot' },
  7: { name: 'Center Bottom-Right', description: 'Child protection' },
  8: { name: 'Right Top', description: 'Operations overview' },
  9: { name: 'Right Middle', description: 'Inclusive community' }
}

// Impact Stats
const impactStats = ref([])
const impactStatsLoading = ref(false)
const impactStatsSaving = ref(false)

// Team Members
const teamMembers = ref([])
const teamLoading = ref(false)
const showTeamModal = ref(false)
const editingTeamMember = ref(null)
const teamSaving = ref(false)
const teamImageFile = ref(null)
const teamImagePreview = ref(null)
const teamFileInput = ref(null)
const teamForm = ref({ name: '', role: '', bio: '', order: 0, is_active: true })

// Timeline Events
const timelineEvents = ref([])
const timelineLoading = ref(false)
const showTimelineModal = ref(false)
const editingTimeline = ref(null)
const timelineSaving = ref(false)
const timelineForm = ref({ title: '', description: '', year: '', order: 0, is_visible: true })

// Core Values
const coreValues = ref([])
const valuesLoading = ref(false)
const showValueModal = ref(false)
const editingValue = ref(null)
const valueSaving = ref(false)
const sharedIconOptions = ['ShieldCheck', 'Heart', 'Users', 'Check', 'Shield', 'Globe', 'Zap', 'Phone', 'Clock']
const valueColorThemes = {
  blue: { color_from: 'blue-500', color_to: 'blue-600', border_color: 'blue-100' },
  green: { color_from: 'green-500', color_to: 'green-600', border_color: 'green-100' },
  orange: { color_from: 'orange-500', color_to: 'orange-600', border_color: 'orange-100' },
  purple: { color_from: 'purple-500', color_to: 'purple-600', border_color: 'purple-100' },
  red: { color_from: 'red-500', color_to: 'red-600', border_color: 'red-100' },
  gray: { color_from: 'gray-500', color_to: 'gray-600', border_color: 'gray-100' }
}
const defaultValueForm = () => ({ title: '', description: '', order: coreValues.value.length, is_active: true, icon: 'ShieldCheck', ...valueColorThemes.blue })
const valueForm = ref(defaultValueForm())
const valueColorTheme = computed(() => (valueForm.value.color_from || 'blue-500').split('-')[0])
function setValueColorTheme(theme) {
  Object.assign(valueForm.value, valueColorThemes[theme] || valueColorThemes.blue)
}
const sharedIconComponentMap = {
  ShieldCheck: ShieldCheckIcon,
  Heart: HeartIcon,
  Users: UsersIcon,
  Check: CheckIcon,
  Shield: ShieldExclamationIcon,
  Globe: GlobeAltIcon,
  Zap: BoltIcon,
  Phone: PhoneIcon,
  Clock: ClockIcon
}
function sharedIconComponent(iconName) {
  return sharedIconComponentMap[iconName] || ShieldCheckIcon
}
const valueColorClassMap = {
  blue: { bg: 'bg-blue-100', text: 'text-blue-600' },
  green: { bg: 'bg-green-100', text: 'text-green-600' },
  orange: { bg: 'bg-orange-100', text: 'text-orange-600' },
  purple: { bg: 'bg-purple-100', text: 'text-purple-600' },
  red: { bg: 'bg-red-100', text: 'text-red-600' },
  gray: { bg: 'bg-gray-100', text: 'text-gray-600' }
}
function valueColorClasses(value) {
  const key = (value?.color_from || 'blue-500').split('-')[0]
  return valueColorClassMap[key] || valueColorClassMap.blue
}

// Protection Approaches
const protectionApproaches = ref([])
const approachLoading = ref(false)
const showApproachModal = ref(false)
const editingApproach = ref(null)
const approachSaving = ref(false)
const approachColorOptions = ['blue', 'green', 'orange', 'purple', 'red', 'gray', 'teal']
const defaultApproachForm = () => ({ title: '', description: '', order: protectionApproaches.value.length, is_active: true, icon: 'ShieldCheck', color: 'blue' })
const approachForm = ref(defaultApproachForm())
const approachColorClassMap = {
  blue: { bg: 'bg-blue-100', text: 'text-blue-600' },
  green: { bg: 'bg-green-100', text: 'text-green-600' },
  orange: { bg: 'bg-orange-100', text: 'text-orange-600' },
  purple: { bg: 'bg-purple-100', text: 'text-purple-600' },
  red: { bg: 'bg-red-100', text: 'text-red-600' },
  gray: { bg: 'bg-gray-100', text: 'text-gray-600' },
  teal: { bg: 'bg-teal-100', text: 'text-teal-600' }
}
function approachColorClasses(value) {
  return approachColorClassMap[value?.color] || approachColorClassMap.blue
}

// Operations Images
const operationsImages = ref([])
const operationsImagesLoading = ref(false)
const showOpsImageModal = ref(false)
const selectedOpsImagePosition = ref('')
const editingOpsImage = ref(null)
const opsSaving = ref(false)
const opsImageFile = ref(null)
const opsImagePreview = ref(null)
const opsFileInput = ref(null)
const opsForm = ref({ title: '', alt_text: '', is_active: true })

const opsJourneyPositions = [
  { value: 'journey_step_1', name: 'Step 1 - Access', description: 'Image for the Access/Call 116 step' },
  { value: 'journey_step_2', name: 'Step 2 - Response', description: 'Image for the Response/Counselors step' },
  { value: 'journey_step_3', name: 'Step 3 - Management', description: 'Image for the Case Management step' },
  { value: 'journey_step_4', name: 'Step 4 - Protection', description: 'Image for the Protection/Resolution step' },
]

const opsServicePositions = [
  { value: 'service_counseling', name: 'Telephone Counseling', description: 'Professional counseling services image' },
  { value: 'service_walkin', name: 'Walk-In Support', description: 'Face-to-face consultation image' },
  { value: 'service_media', name: 'Media Response', description: 'Media and U-report response image' },
  { value: 'service_guidance', name: 'Information & Guidance', description: 'Information provision image' },
  { value: 'service_referral', name: 'Essential Referrals', description: 'Service referral image' },
  { value: 'service_community', name: 'Community Sensitization', description: 'Community awareness image' },
]

const opsInfraPosition = { value: 'infrastructure', name: 'Infrastructure', description: 'Main infrastructure section image' }

// Pages list
const pages = [
  { value: 'home', label: 'Home' },
  { value: 'about', label: 'About' },
  { value: 'operations', label: 'Operations' },
  { value: 'videos', label: 'Videos' },
  { value: 'blog', label: 'Blog' },
  { value: 'news', label: 'News' },
  { value: 'resources', label: 'Resources' },
  { value: 'faqs', label: 'FAQs' },
  { value: 'contact', label: 'Contact' },
  { value: 'partners', label: 'Partners' },
  { value: 'footer', label: 'Footer' },
  { value: 'header', label: 'Header' },
  { value: 'global', label: 'Global' },
  { value: 'services', label: 'Services' },
  { value: 'reports', label: 'Reports' },
  { value: 'donate', label: 'Donate' },
]

// Handle tab query parameter - must be after pages definition
watch(() => route.query.tab, (tab) => {
  if (tab && pages.some(p => p.value === tab)) {
    activePage.value = tab
  }
}, { immediate: true })

// ==================== COMPUTED ====================
const heroImagesStats = computed(() => ({
  filled: heroImages.value.length,
  empty: 9 - heroImages.value.length
}))

const opsJourneyImagesStats = computed(() => ({
  filled: operationsImages.value.filter(img => img.position.startsWith('journey_')).length,
  total: 4
}))

const opsServiceImagesStats = computed(() => ({
  filled: operationsImages.value.filter(img => img.position.startsWith('service_')).length,
  total: 6
}))

const opsInfraImageExists = computed(() => operationsImages.value.some(img => img.position === 'infrastructure'))

const filteredContent = computed(() => {
  let result = allContent.value.filter(item => item.page === activePage.value)
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    result = result.filter(item =>
      item.key?.toLowerCase().includes(q) ||
      item.label?.toLowerCase().includes(q) ||
      item.value?.toLowerCase().includes(q)
    )
  }
  if (filterType.value) result = result.filter(item => item.type === filterType.value)
  if (filterStatus.value === 'published') result = result.filter(item => item.is_published)
  if (filterStatus.value === 'unpublished') result = result.filter(item => !item.is_published)
  return result
})

const aboutTextContent = computed(() => {
  return allContent.value.filter(item => item.page === 'about' && !item.key.includes('stats_stat'))
})

// ==================== METHODS ====================
function getTypeBadgeClass(type) {
  const map = {
    text: 'bg-gray-100 text-gray-800',
    heading: 'bg-purple-100 text-purple-800',
    photo: 'bg-green-100 text-green-800',
    button: 'bg-blue-100 text-blue-800',
  }
  return map[type] || 'bg-gray-100 text-gray-800'
}

function clearFilters() {
  searchQuery.value = ''
  filterType.value = ''
  filterStatus.value = ''
}

// Helper: Format a content key as a readable label
function formatKeyLabel(key) {
  return key
    .replace(/^(home_|videos_|blog_|news_|resources_|faqs_|contact_|partners_|footer_|header_|global_)/, '')
    .replace(/_/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase())
}

// Helper: Get content items by prefix (for organized sections)
function getContentByPrefix(prefix) {
  return allContent.value
    .filter(item => item.key?.startsWith(prefix))
    .sort((a, b) => a.key.localeCompare(b.key))
}

function getContentCountByPrefix(prefix) {
  return allContent.value.filter(item => item.key?.startsWith(prefix)).length
}

// Blog filter content (search, categories, buttons, loading)
function getBlogFilterContent() {
  return allContent.value.filter(item =>
    item.page === 'blog' && (
      item.key?.includes('_search_') ||
      item.key?.includes('_categories_') ||
      item.key?.includes('_all_button') ||
      item.key?.includes('_articles_button') ||
      item.key?.includes('_loading')
    )
  ).sort((a, b) => a.key.localeCompare(b.key))
}

function getBlogFilterContentCount() {
  return getBlogFilterContent().length
}

// Resources filter content
function getResourcesFilterContent() {
  return allContent.value.filter(item =>
    item.page === 'resources' && (
      item.key?.includes('_search_') ||
      item.key?.includes('_filter_')
    )
  ).sort((a, b) => a.key.localeCompare(b.key))
}

function getResourcesFilterContentCount() {
  return getResourcesFilterContent().length
}

// Footer section helpers
function getFooterContactContent() {
  return allContent.value.filter(item =>
    item.page === 'footer' && (
      item.key?.includes('_contact_') ||
      item.key?.includes('_hotline_') ||
      item.key?.includes('_email_')
    )
  ).sort((a, b) => a.key.localeCompare(b.key))
}

function getFooterContactCount() {
  return getFooterContactContent().length
}

function getFooterHeadingsContent() {
  return allContent.value.filter(item =>
    item.page === 'footer' && item.key?.includes('_heading')
  ).sort((a, b) => a.key.localeCompare(b.key))
}

function getFooterHeadingsCount() {
  return getFooterHeadingsContent().length
}

function getFooterLegalContent() {
  return allContent.value.filter(item =>
    item.page === 'footer' && (
      item.key?.includes('_copyright') ||
      item.key?.includes('_country_')
    )
  ).sort((a, b) => a.key.localeCompare(b.key))
}

function getFooterLegalCount() {
  return getFooterLegalContent().length
}

// Global settings helpers
function getGlobalSiteInfoContent() {
  return allContent.value.filter(item =>
    item.page === 'global' && (
      item.key === 'site_name' ||
      item.key === 'site_description'
    )
  ).sort((a, b) => a.key.localeCompare(b.key))
}

function getGlobalSiteInfoCount() {
  return getGlobalSiteInfoContent().length
}

function getGlobalHotlineContent() {
  return allContent.value.filter(item =>
    item.page === 'global' && (
      item.key === 'hotline_number' ||
      item.key === 'operating_hours'
    )
  ).sort((a, b) => a.key.localeCompare(b.key))
}

function getGlobalHotlineCount() {
  return getGlobalHotlineContent().length
}

// formatYear removed - using event.year directly from API

// Fetch all data
async function fetchAllContent() {
  contentStore.setLoading(true)
  try {
    const res = await api.get('/content/site-content/')
    allContent.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
    buildImpactStats()
  } catch (err) {
    console.error('Fetch error:', err)
  } finally {
    contentStore.setLoading(false)
  }
}

async function fetchHeroImages() {
  heroImagesLoading.value = true
  try {
    const res = await api.whoWeAreImages.list()
    heroImages.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
  } catch (err) { console.error(err) }
  finally { heroImagesLoading.value = false }
}

async function fetchTeamMembers() {
  teamLoading.value = true
  try {
    const res = await api.teamMembers.list()
    teamMembers.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
  } catch (err) { console.error(err) }
  finally { teamLoading.value = false }
}

async function fetchTimelineEvents() {
  timelineLoading.value = true
  try {
    const res = await api.timeline.list()
    timelineEvents.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
  } catch (err) { console.error(err) }
  finally { timelineLoading.value = false }
}

async function fetchCoreValues() {
  valuesLoading.value = true
  try {
    const res = await api.coreValues.list()
    coreValues.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
  } catch (err) { console.error(err) }
  finally { valuesLoading.value = false }
}

async function fetchProtectionApproaches() {
  approachLoading.value = true
  try {
    const res = await api.protectionApproaches.list()
    protectionApproaches.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
  } catch (err) { console.error(err) }
  finally { approachLoading.value = false }
}

async function fetchOperationsImages() {
  operationsImagesLoading.value = true
  try {
    const res = await api.operationsImages.list()
    operationsImages.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
  } catch (err) { console.error(err) }
  finally { operationsImagesLoading.value = false }
}

// Impact Stats helpers
function buildImpactStats() {
  const regex = /^about_stats_stat_(\d+)_(value|label)$/
  const statsByIndex = {}
  allContent.value.forEach(item => {
    const match = item.key?.match(regex)
    if (!match) return
    const idx = parseInt(match[1], 10)
    const field = match[2]
    if (!statsByIndex[idx]) statsByIndex[idx] = { index: idx, value: '', label: '', valueKey: `about_stats_stat_${idx}_value`, labelKey: `about_stats_stat_${idx}_label` }
    statsByIndex[idx][field] = item.value ?? ''
  })
  impactStats.value = Object.values(statsByIndex).sort((a, b) => a.index - b.index)
  if (impactStats.value.length === 0) {
    impactStats.value = [1,2,3,4,5,6].map(i => ({ index: i, value: '', label: '', valueKey: `about_stats_stat_${i}_value`, labelKey: `about_stats_stat_${i}_label` }))
  }
}

function addImpactStat() {
  const maxIdx = impactStats.value.reduce((m, s) => Math.max(m, s.index), 0)
  const next = maxIdx + 1
  impactStats.value.push({ index: next, value: '', label: '', valueKey: `about_stats_stat_${next}_value`, labelKey: `about_stats_stat_${next}_label` })
}

async function removeImpactStat(stat) {
  if (impactStats.value.length <= 1) return toast.error('At least one card required')
  try {
    await api.delete(`/content/site-content/${stat.valueKey}/`).catch(() => {})
    await api.delete(`/content/site-content/${stat.labelKey}/`).catch(() => {})
    impactStats.value = impactStats.value.filter(s => s.valueKey !== stat.valueKey)
    toast.success('Card removed')
  } catch (err) { toast.error('Failed to remove') }
}

async function saveImpactStats() {
  impactStatsSaving.value = true
  try {
    for (const stat of impactStats.value) {
      await upsertContent({ key: stat.valueKey, value: stat.value, label: `Impact Stat ${stat.index} Value`, page: 'about', type: 'text' })
      await upsertContent({ key: stat.labelKey, value: stat.label, label: `Impact Stat ${stat.index} Label`, page: 'about', type: 'text' })
    }
    toast.success('Impact stats saved')
    await fetchAllContent()
  } catch (err) { toast.error('Failed to save') }
  finally { impactStatsSaving.value = false }
}

async function upsertContent(payload) {
  const exists = allContent.value.find(i => i.key === payload.key)
  if (exists) {
    await api.put(`/content/site-content/${payload.key}/`, { ...payload, is_published: true })
  } else {
    await api.post('/content/site-content/', { ...payload, is_published: true })
  }
}

// Site Content Modal
function openCreateModal() {
  isEditing.value = false
  Object.assign(form, { key: '', label: '', value: '', type: 'text', page: activePage.value, description: '' })
  showModal.value = true
}

function openEditModal(item) {
  isEditing.value = true
  Object.assign(form, { ...item })
  showModal.value = true
}

function closeModal() { showModal.value = false }

async function saveContent() {
  try {
    if (isEditing.value) {
      await api.put(`/content/site-content/${form.key}/`, form)
      toast.success('Content updated')
    } else {
      await api.post('/content/site-content/', form)
      toast.success('Content created')
    }
    await fetchAllContent()
    closeModal()
  } catch (err) { toast.error('Failed to save') }
}

async function togglePublish(item) {
  try {
    await api.put(`/content/site-content/${item.key}/`, { ...item, is_published: !item.is_published })
    toast.success(item.is_published ? 'Unpublished' : 'Published')
    await fetchAllContent()
  } catch (err) { toast.error('Failed') }
}

// Hero Images Modal
function getHeroImageByPosition(pos) { return heroImages.value.find(img => img.position === pos) }

function openHeroImageModal(pos) {
  selectedHeroPosition.value = pos
  const existing = getHeroImageByPosition(pos)
  editingHeroImage.value = existing
  heroImageFile.value = null
  heroImagePreview.value = existing?.image_url || null
  heroForm.value = existing ? { title: existing.title, alt_text: existing.alt_text || '', is_active: existing.is_active } : { title: '', alt_text: '', is_active: true }
  showHeroImageModal.value = true
}

function closeHeroImageModal() {
  showHeroImageModal.value = false
  heroImageFile.value = null
  heroImagePreview.value = null
}

function handleHeroImageChange(e) {
  const file = e.target.files[0]
  if (file) {
    heroImageFile.value = file
    heroImagePreview.value = URL.createObjectURL(file)
  }
}

async function saveHeroImage() {
  heroSaving.value = true
  try {
    const payload = { position: selectedHeroPosition.value, ...heroForm.value }
    if (heroImageFile.value) payload.image = heroImageFile.value
    if (editingHeroImage.value) {
      await api.whoWeAreImages.update(selectedHeroPosition.value, payload)
    } else {
      await api.whoWeAreImages.create(payload)
    }
    toast.success('Image saved')
    await fetchHeroImages()
    closeHeroImageModal()
  } catch (err) { toast.error('Failed to save') }
  finally { heroSaving.value = false }
}

// Team Modal
function openTeamModal(member) {
  editingTeamMember.value = member
  teamImageFile.value = null
  teamImagePreview.value = member?.image_url || member?.image || null
  teamForm.value = member ? { ...member } : { name: '', role: '', bio: '', order: teamMembers.value.length, is_active: true }
  showTeamModal.value = true
}

function closeTeamModal() {
  showTeamModal.value = false
  teamImageFile.value = null
  teamImagePreview.value = null
}

function handleTeamImageChange(e) {
  const file = e.target.files[0]
  if (file) {
    teamImageFile.value = file
    teamImagePreview.value = URL.createObjectURL(file)
  }
}

async function saveTeamMember() {
  teamSaving.value = true
  try {
    const payload = { ...teamForm.value }
    if (teamImageFile.value) payload.image = teamImageFile.value
    else delete payload.image
    if (editingTeamMember.value) {
      await api.teamMembers.update(editingTeamMember.value.id, payload)
    } else {
      await api.teamMembers.create(payload)
    }
    toast.success('Team member saved')
    await fetchTeamMembers()
    closeTeamModal()
  } catch (err) { toast.error('Failed to save') }
  finally { teamSaving.value = false }
}

async function deleteTeamMember() {
  if (!editingTeamMember.value || !confirm('Delete this team member?')) return
  try {
    await api.teamMembers.delete(editingTeamMember.value.id)
    toast.success('Deleted')
    await fetchTeamMembers()
    closeTeamModal()
  } catch (err) { toast.error('Failed') }
}

// Timeline Modal
function openTimelineModal(event) {
  editingTimeline.value = event
  timelineForm.value = event ? { ...event } : { title: '', description: '', year: '', order: timelineEvents.value.length + 1, is_visible: true }
  showTimelineModal.value = true
}

function closeTimelineModal() { showTimelineModal.value = false }

async function saveTimeline() {
  timelineSaving.value = true
  try {
    if (editingTimeline.value) {
      await api.timeline.update(editingTimeline.value.id, timelineForm.value)
    } else {
      await api.timeline.create(timelineForm.value)
    }
    toast.success('Timeline saved')
    await fetchTimelineEvents()
    closeTimelineModal()
  } catch (err) { toast.error('Failed') }
  finally { timelineSaving.value = false }
}

async function deleteTimeline(event) {
  if (!confirm('Delete this event?')) return
  try {
    await api.timeline.delete(event.id)
    toast.success('Deleted')
    await fetchTimelineEvents()
  } catch (err) { toast.error('Failed') }
}

// Core Values Modal
function openValueModal(value) {
  editingValue.value = value
  valueForm.value = value ? { ...defaultValueForm(), ...value } : defaultValueForm()
  showValueModal.value = true
}

function closeValueModal() { showValueModal.value = false }

async function saveValue() {
  valueSaving.value = true
  try {
    if (editingValue.value) {
      await api.coreValues.update(editingValue.value.id, valueForm.value)
    } else {
      await api.coreValues.create(valueForm.value)
    }
    toast.success('Value saved')
    await fetchCoreValues()
    closeValueModal()
  } catch (err) { toast.error('Failed') }
  finally { valueSaving.value = false }
}

async function deleteValue() {
  if (!editingValue.value || !confirm('Delete this value?')) return
  try {
    await api.coreValues.delete(editingValue.value.id)
    toast.success('Deleted')
    await fetchCoreValues()
    closeValueModal()
  } catch (err) { toast.error('Failed') }
}

// Protection Approach Modal
function openApproachModal(approach) {
  editingApproach.value = approach
  approachForm.value = approach ? { ...defaultApproachForm(), ...approach } : defaultApproachForm()
  showApproachModal.value = true
}

function closeApproachModal() { showApproachModal.value = false }

async function saveApproach() {
  approachSaving.value = true
  try {
    if (editingApproach.value) {
      await api.protectionApproaches.update(editingApproach.value.id, approachForm.value)
    } else {
      await api.protectionApproaches.create(approachForm.value)
    }
    toast.success('Step saved')
    await fetchProtectionApproaches()
    closeApproachModal()
  } catch (err) { toast.error('Failed') }
  finally { approachSaving.value = false }
}

async function deleteApproach(approach) {
  if (!confirm('Delete this step?')) return
  try {
    await api.protectionApproaches.delete(approach.id)
    toast.success('Deleted')
    await fetchProtectionApproaches()
  } catch (err) { toast.error('Failed') }
}

// Operations Images Modal
function getOpsImageByPosition(pos) { return operationsImages.value.find(img => img.position === pos) }

function openOpsImageModal(pos, positionInfo) {
  selectedOpsImagePosition.value = pos
  const existing = getOpsImageByPosition(pos)
  editingOpsImage.value = existing
  opsImageFile.value = null
  opsImagePreview.value = existing?.image_url || null
  opsForm.value = existing
    ? { title: existing.title, alt_text: existing.alt_text || '', is_active: existing.is_active }
    : { title: positionInfo?.name || '', alt_text: '', is_active: true }
  showOpsImageModal.value = true
}

function closeOpsImageModal() {
  showOpsImageModal.value = false
  opsImageFile.value = null
  opsImagePreview.value = null
}

function handleOpsImageChange(e) {
  const file = e.target.files[0]
  if (file) {
    opsImageFile.value = file
    opsImagePreview.value = URL.createObjectURL(file)
  }
}

async function saveOpsImage() {
  opsSaving.value = true
  try {
    const payload = { position: selectedOpsImagePosition.value, ...opsForm.value }
    if (opsImageFile.value) payload.image = opsImageFile.value
    if (editingOpsImage.value) {
      await api.operationsImages.update(selectedOpsImagePosition.value, payload)
    } else {
      await api.operationsImages.create(payload)
    }
    toast.success('Image saved')
    await fetchOperationsImages()
    closeOpsImageModal()
  } catch (err) { toast.error('Failed to save image') }
  finally { opsSaving.value = false }
}

async function deleteOpsImage() {
  if (!editingOpsImage.value || !confirm('Delete this image?')) return
  try {
    await api.operationsImages.delete(selectedOpsImagePosition.value)
    toast.success('Image deleted')
    await fetchOperationsImages()
    closeOpsImageModal()
  } catch (err) { toast.error('Failed to delete') }
}

function getOpsPositionInfo(pos) {
  return opsJourneyPositions.find(p => p.value === pos) ||
         opsServicePositions.find(p => p.value === pos) ||
         (pos === 'infrastructure' ? opsInfraPosition : null)
}

// ==================== LIFECYCLE ====================
onMounted(() => {
  fetchAllContent()
  fetchHeroImages()
  fetchTeamMembers()
  fetchTimelineEvents()
  fetchCoreValues()
  fetchProtectionApproaches()
  fetchOperationsImages()
})
</script>

