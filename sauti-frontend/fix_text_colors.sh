#!/bin/bash

# SAUTI 116 - Text Color Compliance Automated Fix Script
# This script fixes remaining text-secondary violations in body text
# 
# Usage: ./fix_text_colors.sh
# 
# IMPORTANT: Review all changes before committing!

echo "🎨 SAUTI 116 - Text Color Compliance Fix"
echo "========================================"
echo ""
echo "This script will fix remaining text-secondary violations"
echo "by replacing them with text-black or text-muted."
echo ""
echo "⚠️  IMPORTANT: This will modify files. Make sure you have a backup!"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Aborted."
    exit 1
fi

# Navigate to the sauti-frontend directory
cd "$(dirname "$0")"

echo ""
echo "📋 Starting fixes..."
echo ""

# Counter for changes
total_changes=0

# Pattern 1: Fix <p> tags with text-secondary (but not text-secondary-light)
echo "1️⃣  Fixing body paragraphs (text-secondary → text-black)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l '<p[^>]*text-secondary[^-]' {} \;)
for file in $files_changed; do
    # Only fix <p> tags, not headings
    if grep -q '<p[^>]*class="[^"]*text-secondary[^-]' "$file"; then
        # Use sed to replace text-secondary with text-black in <p> tags only
        sed -i '' 's/\(<p[^>]*class="[^"]*\)text-secondary\([^-]\)/\1text-black\2/g' "$file"
        echo "   ✅ Fixed: $file"
        ((total_changes++))
    fi
done

# Pattern 2: Fix text-secondary/60 → text-muted
echo ""
echo "2️⃣  Fixing muted text (text-secondary/60 → text-muted)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l 'text-secondary/60' {} \;)
for file in $files_changed; do
    sed -i '' 's/text-secondary\/60/text-muted/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

# Pattern 3: Fix text-secondary/70 → text-black/70
echo ""
echo "3️⃣  Fixing subtle text (text-secondary/70 → text-black/70)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l 'text-secondary/70' {} \;)
for file in $files_changed; do
    sed -i '' 's/text-secondary\/70/text-black\/70/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

# Pattern 4: Fix text-secondary/40 → text-black/40
echo ""
echo "4️⃣  Fixing very subtle text (text-secondary/40 → text-black/40)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l 'text-secondary/40' {} \;)
for file in $files_changed; do
    sed -i '' 's/text-secondary\/40/text-black\/40/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

# Pattern 5: Fix text-secondary/50 → text-black/50
echo ""
echo "5️⃣  Fixing subtle labels (text-secondary/50 → text-black/50)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l 'text-secondary/50' {} \;)
for file in $files_changed; do
    sed -i '' 's/text-secondary\/50/text-black\/50/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

# Pattern 6: Fix <span> tags with text-secondary (excluding campaign-header)
echo ""
echo "6️⃣  Fixing span elements (text-secondary → text-black)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l '<span[^>]*text-secondary' {} \;)
for file in $files_changed; do
    # Only fix spans that are NOT campaign-header
    if grep -q '<span[^>]*class="[^"]*text-secondary' "$file" && ! grep -q 'campaign-header[^"]*text-secondary' "$file"; then
        sed -i '' 's/\(<span[^>]*class="[^"]*\)text-secondary\([^-]\)/\1text-black\2/g' "$file"
        echo "   ✅ Fixed: $file"
        ((total_changes++))
    fi
done

# Pattern 7: Fix <input> tags with text-secondary
echo ""
echo "7️⃣  Fixing input elements (text-secondary → text-black)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l '<input[^>]*text-secondary' {} \;)
for file in $files_changed; do
    sed -i '' 's/\(<input[^>]*class="[^"]*\)text-secondary/\1text-black/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

# Pattern 8: Fix <textarea> tags with text-secondary
echo ""
echo "8️⃣  Fixing textarea elements (text-secondary → text-black)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l '<textarea[^>]*text-secondary' {} \;)
for file in $files_changed; do
    sed -i '' 's/\(<textarea[^>]*class="[^"]*\)text-secondary/\1text-black/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

# Pattern 9: Fix <label> tags with text-secondary
echo ""
echo "9️⃣  Fixing label elements (text-secondary → text-black)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l '<label[^>]*text-secondary' {} \;)
for file in $files_changed; do
    sed -i '' 's/\(<label[^>]*class="[^"]*\)text-secondary/\1text-black/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

# Pattern 10: Fix <select> tags with text-secondary
echo ""
echo "🔟 Fixing select elements (text-secondary → text-black)..."
files_changed=$(find src/views src/components -name "*.vue" -type f -exec grep -l '<select[^>]*text-secondary' {} \;)
for file in $files_changed; do
    sed -i '' 's/\(<select[^>]*class="[^"]*\)text-secondary/\1text-black/g' "$file"
    echo "   ✅ Fixed: $file"
    ((total_changes++))
done

echo ""
echo "========================================"
echo "✅ Fix Complete!"
echo ""
echo "📊 Summary:"
echo "   Total files modified: $total_changes"
echo ""
echo "⚠️  IMPORTANT NEXT STEPS:"
echo "   1. Review all changes with: git diff"
echo "   2. Verify headings are still green (text-secondary)"
echo "   3. Test the application visually"
echo "   4. Run: npm run dev"
echo ""
echo "🔍 To verify fixes:"
echo "   grep -r 'text-secondary' src/views src/components | grep -v 'text-secondary-light' | grep -v '<h[1-4]' | grep -v 'campaign-header'"
echo ""
echo "Done! 🎉"
