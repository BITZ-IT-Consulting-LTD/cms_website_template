/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx,css}',
  ],
  theme: {
    extend: {
      colors: {
        /* ============================================
           SAUTI 116 CENTRALIZED COLOR SYSTEM
           Total: 16 Colors (Brand-Compliant)
           ============================================ */

        // BRAND COLORS (7) - From Official Guidelines
        'primary': 'rgb(var(--color-primary) / <alpha-value>)',
        'secondary': 'rgb(var(--color-secondary) / <alpha-value>)',
        'secondary-light': 'rgb(var(--color-secondary-light) / <alpha-value>)',
        'hotline': 'rgb(var(--color-hotline) / <alpha-value>)',
        'emergency': 'rgb(var(--color-emergency) / <alpha-value>)',
        'accent-yellow': 'rgb(var(--color-accent-yellow) / <alpha-value>)',
        'text': 'rgb(var(--color-text) / <alpha-value>)',

        // TECHNICAL NECESSITIES (4) - Web Implementation
        'primary-dark': 'rgb(var(--color-primary-dark) / <alpha-value>)',
        'neutral-black': 'rgb(var(--color-neutral-black) / <alpha-value>)',
        'neutral-white': 'rgb(var(--color-neutral-white) / <alpha-value>)',
        'neutral-offwhite': 'rgb(var(--color-neutral-offwhite) / <alpha-value>)',

        // SOCIAL MEDIA (5) - Platform Requirements
        'whatsapp': 'rgb(var(--color-whatsapp) / <alpha-value>)',
        'whatsapp-hover': 'rgb(var(--color-whatsapp-hover) / <alpha-value>)',
        'facebook': 'rgb(var(--color-facebook) / <alpha-value>)',
        'facebook-hover': 'rgb(var(--color-facebook-hover) / <alpha-value>)',
        'twitter': 'rgb(var(--color-twitter) / <alpha-value>)',

        /* ============================================
           NOTE: For UI states, use opacity variants:
           - Borders: primary/20, secondary/15
           - Disabled: black/40
           - Muted: black/60
           - Subtle backgrounds: primary/5, secondary/5
           ============================================ */
      },
      fontFamily: {
        // Cronos Pro - Official Brand Typography (11pt base)
        sans: ['cronos-pro', 'Cronos Pro', 'Georgia', 'serif'],
        body: ['cronos-pro', 'Cronos Pro', 'Georgia', 'serif'],
        heading: ['cronos-pro', 'Cronos Pro', 'Georgia', 'serif'],
      },
      boxShadow: {
        'glow-hotline': '0 0 12px rgb(var(--color-hotline) / 0.4)',
        'glow-emergency': '0 0 12px rgb(var(--color-emergency) / 0.4)',
      },
      animation: {
        'hotline-glow': 'hotlineGlow 2s ease-in-out infinite',
        'emergency-glow': 'emergencyGlow 2s ease-in-out infinite',
      },
      keyframes: {
        hotlineGlow: {
          '0%, 100%': { boxShadow: '0 0 0 rgb(var(--color-hotline) / 0)' },
          '50%': { boxShadow: '0 0 12px rgb(var(--color-hotline) / 0.4)' },
        },
        emergencyGlow: {
          '0%, 100%': { boxShadow: '0 0 0 rgb(var(--color-emergency) / 0)' },
          '50%': { boxShadow: '0 0 12px rgb(var(--color-emergency) / 0.4)' },
        },
      },
    },
  },
  safelist: [
    'animate-emergency-glow',
    'animate-hotline-glow',
    'shadow-glow-emergency',
    'shadow-glow-hotline',
    'bg-emergency/90',
    'bg-hotline/90',
    'border-neutral-white/20',
  ],
  plugins: [],
}
