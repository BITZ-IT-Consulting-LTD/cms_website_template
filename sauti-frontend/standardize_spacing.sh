#!/bin/bash

# SAUTI 116 - Standardize Spacing System
# This script replaces odd spacing values with standard scale values

echo "=================================================="
echo "SAUTI 116 - Spacing Standardization"
echo "Replacing odd values with standard spacing scale"
echo "=================================================="
echo ""

# Count violations before
P5_COUNT=$(grep -r "p-5[^0-9]" src/ --include="*.vue" | wc -l | tr -d ' ')
PX10_COUNT=$(grep -r "px-10[^0-9]" src/ --include="*.vue" | wc -l | tr -d ' ')
PY5_COUNT=$(grep -r "py-5[^0-9]" src/ --include="*.vue" | wc -l | tr -d ' ')
TOTAL_BEFORE=$((P5_COUNT + PX10_COUNT + PY5_COUNT))

echo "Found odd spacing values:"
echo "  - p-5: $P5_COUNT"
echo "  - px-10: $PX10_COUNT"
echo "  - py-5: $PY5_COUNT"
echo "  - Total: $TOTAL_BEFORE"
echo ""

if [ $TOTAL_BEFORE -eq 0 ]; then
  echo "✅ No odd spacing values found. System is already standardized!"
  exit 0
fi

read -p "Do you want to proceed with standardization? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Aborted."
    exit 1
fi

echo ""
echo "Starting standardization..."
echo ""

# ============================================
# PHASE 1: Replace p-5 with p-6
# ============================================

echo "Phase 1: Replacing p-5 with p-6..."

find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/\bp-5\b/p-6/g' \
  {} +

echo "  ✓ p-5 → p-6"

# ============================================
# PHASE 2: Replace px-10 with px-8
# ============================================

echo "Phase 2: Replacing px-10 with px-8..."

find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/\bpx-10\b/px-8/g' \
  {} +

echo "  ✓ px-10 → px-8"

# ============================================
# PHASE 3: Replace py-5 with py-6
# ============================================

echo "Phase 3: Replacing py-5 with py-6..."

find src/ -name "*.vue" -type f -exec sed -i '' \
  -e 's/\bpy-5\b/py-6/g' \
  {} +

echo "  ✓ py-5 → py-6"

# ============================================
# VERIFICATION
# ============================================

echo ""
echo "Verification..."
echo ""

# Count remaining violations
P5_AFTER=$(grep -r "p-5[^0-9]" src/ --include="*.vue" | wc -l | tr -d ' ')
PX10_AFTER=$(grep -r "px-10[^0-9]" src/ --include="*.vue" | wc -l | tr -d ' ')
PY5_AFTER=$(grep -r "py-5[^0-9]" src/ --include="*.vue" | wc -l | tr -d ' ')
TOTAL_AFTER=$((P5_AFTER + PX10_AFTER + PY5_AFTER))

FIXED=$((TOTAL_BEFORE - TOTAL_AFTER))

echo "Results:"
echo "  - Before: $TOTAL_BEFORE odd values"
echo "  - After: $TOTAL_AFTER odd values"
echo "  - Fixed: $FIXED values"
echo ""

if [ $TOTAL_AFTER -eq 0 ]; then
  echo "✅ SUCCESS! All odd spacing values standardized!"
else
  echo "⚠️  WARNING: $TOTAL_AFTER odd values remaining"
  echo ""
  echo "Remaining violations:"
  grep -r "p-5[^0-9]\|px-10[^0-9]\|py-5[^0-9]" src/ --include="*.vue" | head -10
fi

echo ""
echo "=================================================="
echo "Standardization complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Review changes: git diff"
echo "2. Test application: npm run dev"
echo "3. Commit changes: git add . && git commit -m 'fix: standardize spacing system'"
echo ""
