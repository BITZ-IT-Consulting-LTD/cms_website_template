<template>
  <div class="section-padding">
    <div class="container-custom">
      <div class="text-center mb-10">
        <h2 class="mb-2">Reports & Insights</h2>
        <p class="text-gray-600 max-w-3xl mx-auto">Explore the data collected by Sauti Uganda Child Helpline to understand the trends and patterns in child abuse and neglect across the country.</p>
      </div>

      <!-- Filters placeholder -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 mb-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <input class="form-input" placeholder="Search reports by keyword" />
          <select class="form-input"><option>All Regions</option></select>
          <button class="pill pill-primary">Apply Filters</button>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div class="avm-card h-64">
          <h4 class="font-semibold mb-2">Reported Cases by Category</h4>
          <div class="h-40 bg-blue-50 rounded"></div>
        </div>
        <div class="avm-card h-64">
          <h4 class="font-semibold mb-2">Summary</h4>
          <p class="text-gray-600 text-sm">Child Neglect remains the highest reported category, followed by physical abuse. Emotional and sexual abuse continue to be serious concerns.</p>
        </div>
        <div class="avm-card h-64">
          <h4 class="font-semibold mb-2">Reported Cases Over Time</h4>
          <div class="h-40 bg-blue-50 rounded"></div>
        </div>
        <div class="avm-card h-64">
          <h4 class="font-semibold mb-2">Summary</h4>
          <p class="text-gray-600 text-sm">Reported cases show a steady increase over the last five years, reflecting improved awareness and reporting.</p>
        </div>
        <div class="avm-card h-64">
          <h4 class="font-semibold mb-2">Reported Cases by Region</h4>
          <div class="space-y-3">
            <div class="h-2 bg-blue-200 rounded w-4/5"></div>
            <div class="h-2 bg-blue-200 rounded w-2/5"></div>
            <div class="h-2 bg-blue-200 rounded w-3/5"></div>
            <div class="h-2 bg-blue-200 rounded w-1/3"></div>
          </div>
        </div>
        <div class="avm-card h-64">
          <h4 class="font-semibold mb-2">Summary</h4>
          <p class="text-gray-600 text-sm">Central region accounts for the highest volume of reports; targeted outreach is ongoing to improve response in underserved areas.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

