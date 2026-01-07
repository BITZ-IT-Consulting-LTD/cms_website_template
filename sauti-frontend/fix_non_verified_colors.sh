#!/bin/bash

# SAUTI 116 - Replace Non-Verified Colors with 16-Color System
# This script replaces all gray-* and accent-orange usage with verified colors

echo "=================================================="
echo "SAUTI 116 - Color Compliance Fix"
echo "Replacing non-verified colors with 16-color system"
echo "=================================================="
echo ""

# Count violations before
GRAY_COUNT=$(grep -r "gray-" src/ --include="*.vue" | wc -l | tr -d ' ')
ACCENT_ORANGE_COUNT=$(grep -r "accent-orange" src/ --include="*.vue" | wc -l | tr -d ' ')
TOTAL_BEFORE=$((GRAY_COUNT + ACCENT_ORANGE_COUNT))

echo "Found violations:"
echo "  - gray-* usage: $GRAY_COUNT"
echo "  - accent-orange usage: $ACCENT_ORANGE_COUNT"
echo "  - Total: $TOTAL_BEFORE"
echo ""

read -p "Do you want to proceed with the fix? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Aborted."
    exit 1
fi

echo ""
echo "Starting replacement..."
echo ""

# ============================================
# PHASE 1: Replace accent-orange with hotline
# ============================================

echo "Phase 1: Replacing accent-orange with hotline..."

find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/accent-orange/hotline/g' \
  {} +

echo "  ✓ accent-orange → hotline"

# ============================================
# PHASE 2: Replace gray backgrounds
# ============================================

echo "Phase 2: Replacing gray backgrounds..."

# Very light backgrounds
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/bg-gray-50/bg-primary\/5/g' \
  {} +
echo "  ✓ bg-gray-50 → bg-primary/5"

# Light backgrounds
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/bg-gray-100/bg-primary\/10/g' \
  {} +
echo "  ✓ bg-gray-100 → bg-primary/10"

# Medium backgrounds
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/bg-gray-200/bg-secondary\/10/g' \
  {} +
echo "  ✓ bg-gray-200 → bg-secondary/10"

# ============================================
# PHASE 3: Replace gray text
# ============================================

echo "Phase 3: Replacing gray text..."

# Disabled text
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/text-gray-300/text-black\/30/g' \
  -e 's/text-gray-400/text-black\/40/g' \
  {} +
echo "  ✓ text-gray-300/400 → text-black/30-40"

# Muted text
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/text-gray-500/text-black\/50/g' \
  -e 's/text-gray-600/text-black\/60/g' \
  {} +
echo "  ✓ text-gray-500/600 → text-black/50-60"

# Dark text
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/text-gray-700/text-black\/70/g' \
  -e 's/text-gray-800/text-black\/80/g' \
  -e 's/text-gray-900/text-black/g' \
  {} +
echo "  ✓ text-gray-700/800/900 → text-black/70-80-100"

# ============================================
# PHASE 4: Replace gray borders
# ============================================

echo "Phase 4: Replacing gray borders..."

# Light borders
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/border-gray-100/border-primary\/10/g' \
  -e 's/border-gray-200/border-primary\/15/g' \
  {} +
echo "  ✓ border-gray-100/200 → border-primary/10-15"

# Medium borders
find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/border-gray-300/border-primary\/20/g' \
  -e 's/border-gray-400/border-primary\/25/g' \
  {} +
echo "  ✓ border-gray-300/400 → border-primary/20-25"

# ============================================
# PHASE 5: Replace hover states
# ============================================

echo "Phase 5: Replacing hover states..."

find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/hover:bg-gray-50/hover:bg-primary\/5/g' \
  -e 's/hover:bg-gray-100/hover:bg-primary\/10/g' \
  -e 's/hover:bg-gray-200/hover:bg-secondary\/10/g' \
  -e 's/hover:bg-gray-800/hover:bg-neutral-black/g' \
  {} +
echo "  ✓ hover:bg-gray-* → hover:bg-primary/* or hover:bg-neutral-black"

# ============================================
# VERIFICATION
# ============================================

echo ""
echo "Verification..."
echo ""

# Count remaining violations
GRAY_AFTER=$(grep -r "gray-" src/ --include="*.vue" | wc -l | tr -d ' ')
ACCENT_ORANGE_AFTER=$(grep -r "accent-orange" src/ --include="*.vue" | wc -l | tr -d ' ')
TOTAL_AFTER=$((GRAY_AFTER + ACCENT_ORANGE_AFTER))

FIXED=$((TOTAL_BEFORE - TOTAL_AFTER))

echo "Results:"
echo "  - Before: $TOTAL_BEFORE violations"
echo "  - After: $TOTAL_AFTER violations"
echo "  - Fixed: $FIXED violations"
echo ""

if [ $TOTAL_AFTER -eq 0 ]; then
  echo "✅ SUCCESS! All non-verified colors replaced!"
else
  echo "⚠️  WARNING: $TOTAL_AFTER violations remaining"
  echo ""
  echo "Remaining violations:"
  grep -r "gray-" src/ --include="*.vue" | head -10
  grep -r "accent-orange" src/ --include="*.vue" | head -10
fi

echo ""
echo "=================================================="
echo "Fix complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Review changes: git diff"
echo "2. Test application: npm run dev"
echo "3. Commit changes: git add . && git commit -m 'fix: replace non-verified colors with 16-color system'"
echo ""
