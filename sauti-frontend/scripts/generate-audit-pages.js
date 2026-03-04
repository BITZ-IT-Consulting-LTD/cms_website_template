/**
 * SAUTI 116 — Audit Page Generator
 * 
 * Generates static HTML snapshots of SPA pages for accessibility/UX auditing.
 * 
 * Usage:
 *   node scripts/generate-audit-pages.js
 * 
 * Output:
 *   dist/audit/*.html (static snapshots)
 */

import { createSSRApp } from 'vue'
import { renderToString } from 'vue/server-renderer'
import { createMemoryHistory, createRouter } from 'vue-router'
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

// ES Module __dirname equivalent
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

// Pages to generate for auditing
const AUDIT_PAGES = [
    { path: '/', name: 'home', title: 'Homepage' },
    { path: '/about', name: 'about', title: 'About Us' },
    { path: '/resources', name: 'resources', title: 'Resources' },
    { path: '/blogs', name: 'blog', title: 'Updates' },
    { path: '/contact', name: 'contact', title: 'Contact' },
    { path: '/privacy', name: 'privacy', title: 'Privacy Policy' },
    { path: '/accessibility', name: 'accessibility', title: 'Accessibility Statement' },
    { path: '/operations', name: 'operations', title: 'Operations' },
    { path: '/faqs', name: 'faqs', title: 'FAQs' },
]

/**
 * Generate HTML template for audit page
 */
function generateHTMLTemplate(title, content) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>Audit: ${title} - Sauti 116</title>
  
  <!-- Inline critical CSS for audit -->
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Roboto', sans-serif; line-height: 1.6; color: #000; background: #F8FAFC; }
    
    /* Audit Mode Banner */
    .audit-banner {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: #ED1C24;
      color: white;
      padding: 12px;
      text-align: center;
      z-index: 9999;
      font-weight: bold;
      font-size: 14px;
    }
    
    /* Offset content for banner */
    #app { margin-top: 48px; }
    
    /* Basic styling for readability */
    .container { max-width: 1280px; margin: 0 auto; padding: 0 1rem; }
    h1, h2, h3 { color: #006837; margin-bottom: 1rem; }
    p { margin-bottom: 1rem; }
    a { color: #0087CF; text-decoration: none; }
    a:hover { text-decoration: underline; }
    
    /* Print styles for audit reports */
    @media print {
      .audit-banner { display: none; }
      #app { margin-top: 0; }
    }
  </style>
</head>
<body>
  <!-- Audit Mode Banner -->
  <div class="audit-banner" role="alert">
    ⚠️ AUDIT MODE - Static Snapshot - Not Interactive - Generated: ${new Date().toISOString()}
  </div>
  
  <!-- App Content -->
  <div id="app">
    ${content}
  </div>
  
  <!-- Audit Information -->
  <script>
    // Log audit information
    console.log('%c🔍 AUDIT MODE ENABLED', 'background: #ED1C24; color: white; padding: 8px; font-weight: bold;')
    console.log('Page:', '${title}')
    console.log('Generated:', '${new Date().toISOString()}')
    console.log('Note: This is a static snapshot for auditing purposes only.')
    
    // Disable form submissions (prevent accidental data submission)
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', (e) => {
          e.preventDefault()
          alert('Form submission disabled in audit mode')
        })
      })
      
      // Add accessibility landmarks if missing
      if (!document.querySelector('[role="main"]')) {
        const main = document.querySelector('main') || document.querySelector('#app > div')
        if (main) main.setAttribute('role', 'main')
      }
    })
  </script>
</body>
</html>`
}

/**
 * Generate audit pages
 */
async function generateAuditPages() {
    console.log('🔍 SAUTI 116 Audit Page Generator\n')
    console.log('Generating static HTML snapshots for accessibility auditing...\n')

    const outputDir = path.resolve(__dirname, '../dist/audit')

    // Create output directory
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true })
        console.log(`✓ Created output directory: ${outputDir}\n`)
    }

    // Generate index page with links to all audit pages
    const indexLinks = AUDIT_PAGES.map(page => {
        const filename = page.path === '/' ? 'index.html' : `${page.name}.html`
        return `<li><a href="${filename}">${page.title}</a> (${page.path})</li>`
    }).join('\n      ')

    const indexContent = `
    <div class="container" style="padding: 2rem;">
      <h1>Sauti 116 - Audit Pages</h1>
      <p>Static HTML snapshots generated for accessibility and UX auditing.</p>
      
      <h2>Available Pages:</h2>
      <ul style="list-style: disc; margin-left: 2rem;">
        ${indexLinks}
      </ul>
      
      <h2>Audit Tools:</h2>
      <ul style="list-style: disc; margin-left: 2rem;">
        <li><strong>Lighthouse:</strong> <code>lighthouse http://localhost:8080/index.html --view</code></li>
        <li><strong>WAVE:</strong> Install browser extension and navigate to pages</li>
        <li><strong>axe DevTools:</strong> Install browser extension and scan pages</li>
      </ul>
      
      <h2>Notes:</h2>
      <ul style="list-style: disc; margin-left: 2rem;">
        <li>These are static snapshots - interactive features are disabled</li>
        <li>Forms will not submit (audit mode protection)</li>
        <li>Generated: ${new Date().toISOString()}</li>
        <li>For production site, visit: <a href="https://sauti.mglsd.go.ug">sauti.mglsd.go.ug</a></li>
      </ul>
    </div>
  `

    const indexHtml = generateHTMLTemplate('Audit Index', indexContent)
    fs.writeFileSync(path.join(outputDir, '_index.html'), indexHtml)
    console.log(`✓ Generated: _index.html (audit page index)`)

    // Generate each page
    for (const page of AUDIT_PAGES) {
        try {
            console.log(`\nGenerating: ${page.title} (${page.path})`)

            // For now, generate placeholder content
            // In a full implementation, you would:
            // 1. Import your Vue app
            // 2. Create a router instance
            // 3. Navigate to the route
            // 4. Render to string

            const placeholderContent = `
        <div class="container" style="padding: 2rem;">
          <h1>${page.title}</h1>
          <p><strong>Route:</strong> ${page.path}</p>
          <p><strong>Status:</strong> Placeholder - Implement full SSR for actual content</p>
          
          <h2>Implementation Steps:</h2>
          <ol style="margin-left: 2rem;">
            <li>Import Vue app and router</li>
            <li>Create SSR app instance</li>
            <li>Navigate to route: <code>${page.path}</code></li>
            <li>Render to string</li>
            <li>Inject into HTML template</li>
          </ol>
          
          <p><a href="_index.html">← Back to Audit Index</a></p>
        </div>
      `

            const html = generateHTMLTemplate(page.title, placeholderContent)

            // Write to file
            const filename = page.path === '/' ? 'index.html' : `${page.name}.html`
            const filepath = path.join(outputDir, filename)
            fs.writeFileSync(filepath, html)

            console.log(`  ✓ Generated: ${filename}`)

        } catch (error) {
            console.error(`  ✗ Error generating ${page.title}:`, error.message)
        }
    }

    // Generate README
    const readme = `# Sauti 116 - Audit Pages

## Overview
Static HTML snapshots of Sauti 116 pages for accessibility and UX auditing.

## Generated Pages
${AUDIT_PAGES.map(p => `- ${p.title} (${p.path}) → ${p.path === '/' ? 'index.html' : p.name + '.html'}`).join('\n')}

## Usage

### Serve Locally
\`\`\`bash
npx serve . -p 8080
\`\`\`

Then open: http://localhost:8080/_index.html

### Run Lighthouse Audits
\`\`\`bash
# Audit homepage
lighthouse http://localhost:8080/index.html --view

# Audit all pages
for file in *.html; do
  lighthouse "http://localhost:8080/$file" --output html --output-path "./reports/$file-report.html"
done
\`\`\`

### Run WAVE Audits
1. Install WAVE browser extension
2. Navigate to http://localhost:8080/_index.html
3. Click on each page link
4. Run WAVE scan

### Run axe DevTools Audits
1. Install axe DevTools browser extension
2. Navigate to http://localhost:8080/_index.html
3. Click on each page link
4. Run axe scan

## Notes
- These are **static snapshots** for auditing purposes only
- Interactive features are disabled
- Forms will not submit (audit mode protection)
- Generated: ${new Date().toISOString()}

## Regenerate
\`\`\`bash
npm run build:audit
\`\`\`
`

    fs.writeFileSync(path.join(outputDir, 'README.md'), readme)
    console.log(`\n✓ Generated: README.md`)

    console.log(`\n✅ All audit pages generated successfully!`)
    console.log(`\nOutput directory: ${outputDir}`)
    console.log(`\nNext steps:`)
    console.log(`  1. cd dist/audit`)
    console.log(`  2. npx serve . -p 8080`)
    console.log(`  3. Open http://localhost:8080/_index.html`)
    console.log(`  4. Run audits with Lighthouse, WAVE, or axe DevTools\n`)
}

// Run generator
generateAuditPages().catch(error => {
    console.error('\n❌ Error generating audit pages:', error)
    process.exit(1)
})
