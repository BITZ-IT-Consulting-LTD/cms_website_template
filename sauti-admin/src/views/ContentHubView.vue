<template>
  <div class="content-hub-view px-6 py-8 max-w-7xl mx-auto">
    <!-- Header -->
    <div class="mb-10">
      <h1 class="text-3xl font-extrabold text-gray-900 tracking-tight">Content Management Hub</h1>
      <p class="mt-2 text-lg text-gray-600">
        Centrally manage all frontend content, from blog posts to homepage sections.
      </p>
    </div>

    <!-- Content Sections Grid -->
    <div class="space-y-12">

      <!-- Primary Editorial Content -->
      <section>
        <div class="flex items-center mb-6">
          <div class="w-1 h-8 bg-blue-600 rounded-full mr-3"></div>
          <h2 class="text-xl font-bold text-gray-800">Editorial & Insights</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <HubCard title="Blog Posts" description="Manage news, articles and announcements." icon="DocumentTextIcon"
            to="/posts" color="bg-orange-50 text-orange-600" />
          <HubCard title="Video Gallery" description="Update the video library and video categories."
            icon="VideoCameraIcon" to="/videos" color="bg-purple-50 text-purple-600" />
          <HubCard title="Download Center" description="Manage PDFs, documents and resources." icon="FolderOpenIcon"
            to="/resources" color="bg-teal-50 text-teal-600" />
          <HubCard title="FAQs" description="Manage frequently asked questions and categories."
            icon="QuestionMarkCircleIcon" to="/faqs" color="bg-green-50 text-green-600" />
        </div>
      </section>

      <!-- Site Architecture -->
      <section>
        <div class="flex items-center mb-6">
          <div class="w-1 h-8 bg-indigo-600 rounded-full mr-3"></div>
          <h2 class="text-xl font-bold text-gray-800">Site Configuration & Pages</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <HubCard title="Homepage Sections" description="Edit hero, CTA, and main page labels." icon="HomeIcon"
            to="/content?tab=home" color="bg-blue-50 text-blue-600" />
          <HubCard title="About Page Text" description="Edit identity, mission and page content."
            icon="InformationCircleIcon" to="/content?tab=about" color="bg-indigo-50 text-indigo-600" />
          <HubCard title="Help Services" description="Manage 'Get Help' service categories and info." icon="CubeIcon"
            to="/services" color="bg-cyan-50 text-cyan-600" />
        </div>
      </section>

      <!-- Page Details -->
      <section>
        <div class="flex items-center mb-6">
          <div class="w-1 h-8 bg-rose-600 rounded-full mr-3"></div>
          <h2 class="text-xl font-bold text-gray-800">About Page Details</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <HubCard title="Organization Team" description="Manage profiles of staff and members." icon="UserGroupIcon"
            to="/team" color="bg-rose-50 text-rose-600" />
          <HubCard title="Timeline Events" description="Manage 'Our Journey' timeline milestones." icon="ClockIcon"
            to="/timeline" color="bg-amber-50 text-amber-600" />
          <HubCard title="Core Values" description="Define and edit organizational core values." icon="HeartIcon"
            to="/core-values" color="bg-pink-50 text-pink-600" />
          <HubCard title="Protection Approach" description="Edit protection services and methodology."
            icon="ShieldCheckIcon" to="/protection-approach" color="bg-emerald-50 text-emerald-600" />
        </div>
      </section>

      <!-- Assets & Contact -->
      <section>
        <div class="flex items-center mb-6">
          <div class="w-1 h-8 bg-gray-600 rounded-full mr-3"></div>
          <h2 class="text-xl font-bold text-gray-800">Connectivity & Assets</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <HubCard title="Media Library" description="Manage images, text, and visual assets for your website."
            icon="PhotoIcon" to="/uploads" color="bg-gray-100 text-gray-700" />
          <HubCard title="Social Media" description="Update social post links and metadata." icon="ShareIcon"
            to="/social-media" color="bg-sky-50 text-sky-600" />
          <HubCard title="Contact Info" description="Official phone, email and address info." icon="PhoneIcon"
            to="/contacts" color="bg-blue-50 text-blue-700" />
          <HubCard title="Legal & Footer" description="Manage privacy policy, terms, and footer content."
            icon="ScaleIcon" to="/legal-footer" color="bg-slate-50 text-slate-600" />
        </div>
      </section>

      <!-- Partners -->
      <section>
        <div class="flex items-center mb-6">
          <div class="w-1 h-8 bg-yellow-600 rounded-full mr-3"></div>
          <h2 class="text-xl font-bold text-gray-800">External Relations</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-1 gap-6">
          <HubCard title="Partners" description="Manage NGOs, government and corporate partner list."
            icon="HandThumbUpIcon" to="/partners" color="bg-yellow-50 text-yellow-700" />
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
  import {
    DocumentTextIcon,
    VideoCameraIcon,
    FolderOpenIcon,
    QuestionMarkCircleIcon,
    HomeIcon,
    InformationCircleIcon,
    CubeIcon,
    UserGroupIcon,
    ClockIcon,
    HeartIcon,
    ShieldCheckIcon,
    PhotoIcon,
    ShareIcon,
    PhoneIcon,
    ScaleIcon,
    HandThumbUpIcon,
    PlusIcon
  } from '@heroicons/vue/24/outline'
  import HubCard from '@/components/content/HubCard.vue'
</script>

<style scoped>
  .content-hub-view {
    animation: fadeIn 0.4s ease-out;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>
