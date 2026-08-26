<template>
    <div class="p-6">
        <!-- Page Header -->
        <PageHeader title="General Feedback"
            description="View and manage messages submitted via the website contact form."
            action-label="Download All (CSV)" :action-icon="ArrowDownTrayIcon" @action="downloadAllCsv" />

        <!-- Stats -->
        <StatsGrid>
            <StatCard label="Total Messages" :value="stats.total" :icon="ChatBubbleLeftRightIcon" color="blue" />
            <StatCard label="Pending Review" :value="stats.pending" :icon="ClockIcon" color="amber" />
            <StatCard label="Reviewed" :value="stats.processed" :icon="CheckCircleIcon" color="green" />
        </StatsGrid>

        <!-- Status Filter -->
        <div class="flex flex-wrap gap-2 mb-8">
            <button v-for="tab in statusTabs" :key="tab.key" @click="statusFilter = tab.key"
                class="px-4 py-2 rounded-xl text-xs font-black uppercase tracking-wider transition-all border"
                :class="statusFilter === tab.key
                    ? 'bg-gray-900 text-white border-gray-900 shadow-md'
                    : 'bg-white text-gray-500 border-gray-200 hover:border-gray-300'">
                {{ tab.label }}
                <span class="ml-1.5 px-1.5 py-0.5 rounded-full text-[10px]"
                    :class="statusFilter === tab.key ? 'bg-white/20' : 'bg-gray-100'">
                    {{ tab.count }}
                </span>
            </button>
        </div>

        <!-- Loading State -->
        <LoadingState v-if="loading" message="Loading messages..." />

        <!-- Empty State -->
        <EmptyState v-else-if="messages.length === 0" title="No Messages Found"
            message="When users submit feedback on the contact page, they will appear here."
            :icon="ChatBubbleLeftRightIcon" />

        <!-- Messages List: grouped when "All" is selected, flat single list otherwise -->
        <div v-else class="space-y-10">
            <section v-for="group in visibleSections" :key="group.key">
                <h2 v-if="group.showHeading" class="text-sm font-black uppercase tracking-wider mb-4 flex items-center gap-2" :class="group.headingClass">
                    <span class="w-2 h-2 rounded-full" :class="group.dotClass"></span>
                    {{ group.title }} ({{ group.items.length }})
                </h2>
                <p v-if="group.items.length === 0" class="text-sm text-gray-400 italic px-1">{{ group.emptyText }}</p>
                <div v-else class="space-y-4">
                    <div v-for="msg in group.items" :key="msg.id"
                        class="bg-white rounded-3xl shadow-sm border overflow-hidden group hover:shadow-lg transition-all duration-300"
                        :class="msg.is_archived ? 'border-gray-200 bg-gray-50/40' : (msg.is_processed ? 'border-green-100 bg-green-50/20' : 'border-gray-100')">
                        <div class="p-6 flex flex-col md:flex-row gap-6">
                            <div class="flex-1">
                                <div class="flex items-center gap-3 mb-2">
                                    <h3 class="text-lg font-bold text-gray-900">{{ msg.name || 'Anonymous User' }}</h3>
                                    <span v-if="msg.email" class="text-sm text-blue-600 font-medium">{{ msg.email }}</span>
                                    <span class="text-xs text-gray-400 font-bold ml-auto">{{ formatDate(msg.submitted_at) }}</span>
                                </div>
                                <p class="text-gray-700 leading-relaxed bg-gray-50/50 p-4 rounded-2xl border border-gray-100 italic">
                                    "{{ msg.message }}"
                                </p>
                                <p v-if="msg.is_processed && msg.reviewed_by_name" class="mt-2 text-xs text-green-700 font-semibold">
                                    Reviewed by {{ msg.reviewed_by_name }}<span v-if="msg.reviewed_at"> · {{ formatDate(msg.reviewed_at) }}</span>
                                </p>
                            </div>
                            <div class="flex md:flex-col justify-between items-end shrink-0 gap-4">
                                <span v-if="msg.is_archived" class="flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-full bg-gray-100 text-gray-500 border border-gray-200">
                                    <span class="w-2 h-2 rounded-full bg-gray-400"></span>
                                    Archived
                                </span>
                                <span v-else class="flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-full"
                                    :class="msg.is_processed ? 'bg-green-50 text-green-700 border border-green-100' : 'bg-amber-50 text-amber-700 border border-amber-100'">
                                    <span class="w-2 h-2 rounded-full"
                                        :class="msg.is_processed ? 'bg-green-500' : 'bg-amber-500 animate-pulse'"></span>
                                    {{ msg.is_processed ? 'Reviewed' : 'Pending' }}
                                </span>
                                <div class="flex gap-2">
                                    <button @click="downloadOne(msg.id)"
                                        class="p-2 bg-blue-50 hover:bg-blue-100 rounded-xl text-blue-500 hover:text-blue-700 transition-all border border-transparent hover:border-blue-200"
                                        title="Download PDF">
                                        <ArrowDownTrayIcon class="h-5 w-5" />
                                    </button>
                                    <template v-if="!msg.is_archived">
                                        <button v-if="!msg.is_processed" @click="setProcessed(msg.id, true)"
                                            class="px-4 py-2 bg-blue-600 text-white text-xs font-black rounded-xl hover:bg-blue-700 transition-all shadow-md shadow-blue-100">
                                            Mark Reviewed
                                        </button>
                                        <button v-else @click="setProcessed(msg.id, false)"
                                            class="px-4 py-2 bg-gray-100 text-gray-600 text-xs font-black rounded-xl hover:bg-gray-200 transition-all">
                                            Mark Unreviewed
                                        </button>
                                        <button @click="setArchived(msg.id, true)"
                                            class="p-2 bg-gray-50 hover:bg-gray-200 rounded-xl text-gray-400 hover:text-gray-700 transition-all border border-transparent hover:border-gray-200"
                                            title="Archive">
                                            <ArchiveBoxIcon class="h-5 w-5" />
                                        </button>
                                    </template>
                                    <button v-else @click="setArchived(msg.id, false)"
                                        class="px-4 py-2 bg-gray-100 text-gray-600 text-xs font-black rounded-xl hover:bg-gray-200 transition-all">
                                        Unarchive
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script setup>
    import { ref, computed, onMounted, watch } from 'vue';
    import { useRouter, useRoute } from 'vue-router';
    import { api, downloadBlobResponse } from '@/utils/api';
    import { useToast } from 'vue-toastification';
    import { PageHeader, StatsGrid, StatCard, LoadingState, EmptyState } from '@/components/admin';
    import {
        ChatBubbleLeftRightIcon,
        ClockIcon,
        CheckCircleIcon,
        ArchiveBoxIcon,
        EnvelopeIcon,
        ArrowDownTrayIcon
    } from '@heroicons/vue/24/outline';

    const router = useRouter();
    const route = useRoute();
    const toast = useToast();
    const messages = ref([]);
    const loading = ref(true);

    const VALID_STATUSES = ['all', 'pending', 'reviewed', 'archived'];
    const statusFilter = ref(VALID_STATUSES.includes(route.query.status) ? route.query.status : 'all');

    // Keep the selection in the URL so a refresh (or navigating away and back)
    // doesn't bounce the admin back to "All" while working through the archive.
    watch(statusFilter, (value) => {
        router.replace({ query: { ...route.query, status: value === 'all' ? undefined : value } });
    });

    const stats = computed(() => {
        const active = messages.value.filter(m => !m.is_archived);
        return {
            total: messages.value.length,
            pending: active.filter(m => !m.is_processed).length,
            processed: active.filter(m => m.is_processed).length,
        };
    });

    const pendingMessages = computed(() => messages.value.filter(m => !m.is_processed && !m.is_archived));
    const reviewedMessages = computed(() => messages.value.filter(m => m.is_processed && !m.is_archived));
    const archivedMessages = computed(() => messages.value.filter(m => m.is_archived));

    const statusTabs = computed(() => [
        { key: 'all', label: 'All', count: messages.value.length },
        { key: 'pending', label: 'Pending', count: pendingMessages.value.length },
        { key: 'reviewed', label: 'Reviewed', count: reviewedMessages.value.length },
        { key: 'archived', label: 'Archived', count: archivedMessages.value.length },
    ]);

    // The three groups, reused both for the "All" grouped view and (filtered
    // to a single entry) for a specific status's flat view, so the card
    // markup is defined exactly once.
    const groups = computed(() => [
        {
            key: 'pending',
            title: 'Pending Review',
            items: pendingMessages.value,
            headingClass: 'text-amber-600',
            dotClass: 'bg-amber-500 animate-pulse',
            emptyText: 'No feedback is waiting to be reviewed.',
        },
        {
            key: 'reviewed',
            title: 'Reviewed / Read',
            items: reviewedMessages.value,
            headingClass: 'text-green-600',
            dotClass: 'bg-green-500',
            emptyText: 'No messages have been reviewed yet.',
        },
        {
            key: 'archived',
            title: 'Archived',
            items: archivedMessages.value,
            headingClass: 'text-gray-500',
            dotClass: 'bg-gray-400',
            emptyText: 'No messages have been archived.',
        },
    ]);

    const visibleSections = computed(() => {
        if (statusFilter.value === 'all') {
            return groups.value.map(g => ({ ...g, showHeading: true }));
        }
        const match = groups.value.find(g => g.key === statusFilter.value);
        return match ? [{ ...match, showHeading: false, emptyText: 'No messages in this status.' }] : [];
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

    const setProcessed = async (id, value) => {
        try {
            await api.feedback.update(id, { is_processed: value });
            toast.success(value ? 'Message marked as reviewed' : 'Message moved back to pending');
            await fetchMessages();
        } catch (error) {
            console.error('Error updating message:', error);
            toast.error('Failed to update message');
        }
    };

    const setArchived = async (id, value) => {
        try {
            await api.feedback.update(id, { is_archived: value });
            toast.success(value ? 'Message archived' : 'Message restored');
            await fetchMessages();
        } catch (error) {
            console.error('Error updating message:', error);
            toast.error('Failed to update message');
        }
    };

    const downloadOne = async (id) => {
        try {
            const response = await api.feedback.exportPdf(id);
            downloadBlobResponse(response, `feedback-${id}.pdf`);
        } catch (error) {
            console.error('Error downloading feedback PDF:', error);
            toast.error('Failed to download PDF');
        }
    };

    const downloadAllCsv = async () => {
        try {
            const response = await api.feedback.exportCsv({ status: statusFilter.value });
            const today = new Date().toISOString().split('T')[0];
            downloadBlobResponse(response, `general-feedback-${statusFilter.value}-${today}.csv`);
        } catch (error) {
            console.error('Error downloading feedback CSV:', error);
            toast.error('Failed to download CSV');
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
