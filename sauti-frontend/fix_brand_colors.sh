#!/bin/bash

# SAUTI 116 - Brand Color Compliance Fix
# This script replaces text-black on structural elements with brand colors

echo "=================================================="
echo "SAUTI 116 - Brand Color Compliance"
echo "Replacing text-black on headers with text-secondary"
echo "=================================================="
echo ""

# 1. SocialMediaCarousel.vue
sed -i '' 's/text-3xl font-bold text-black/text-3xl font-bold text-secondary/g' src/components/home/SocialMediaCarousel.vue

# 2. ResourceStats.vue & ResourceStats 2.vue
sed -i '' 's/text-xl font-bold text-black mb-6/text-xl font-bold text-secondary mb-6/g' src/components/resources/ResourceStats.vue
sed -i '' 's/text-xl font-bold text-black mb-6/text-xl font-bold text-secondary mb-6/g' "src/components/resources/ResourceStats 2.vue"

# 3. HelpSteps.vue
sed -i '' 's/text-lg font-bold text-black/text-lg font-bold text-secondary/g' src/components/content/HelpSteps.vue

# 4. BlogList.vue
sed -i '' 's/text-xl font-bold text-black/text-xl font-bold text-secondary/g' src/components/blog/BlogList.vue

# 5. BlogPost.vue (Headers)
sed -i '' 's/font-bold text-black/font-bold text-secondary/g' src/components/blog/BlogPost.vue

# 6. GetHelpButton.vue (Labels)
sed -i '' 's/font-bold text-black/font-bold text-secondary/g' src/components/common/GetHelpButton.vue

# 7. JourneyTimeline fixes (if applicable, ensuring active file is fixed)
# Using text-secondary for the headings that were black
sed -i '' 's/h3 class="text-xl font-bold text-black/h3 class="text-xl font-bold text-secondary/g' "src/components/home/JourneyTimeline 2.vue"

# 8. JourneyTimeline background watermark (black/10 -> secondary/5 for brand consistency)
sed -i '' 's/text-black\/10/text-secondary\/5/g' src/components/home/JourneyTimeline.vue

echo "✅ Replaced text-black headers with text-secondary"
echo ""

# Verification
echo "Verifying remaining black headers..."
grep -r "font-bold text-black" src/ --include="*.vue" | grep "<h"

