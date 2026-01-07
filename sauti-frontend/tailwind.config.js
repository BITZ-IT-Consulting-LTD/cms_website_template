/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx,css}',
  ],
  theme: {
    extend: {
      colors: {
        'primary': 'rgb(var(--color-primary) / <alpha-value>)',
        'secondary': 'rgb(var(--color-secondary) / <alpha-value>)',
        'secondary-light': 'rgb(var(--color-secondary-light) / <alpha-value>)',
        'hotline': 'rgb(var(--color-hotline) / <alpha-value>)',
        'emergency': 'rgb(var(--color-emergency) / <alpha-value>)',
        'accent-orange': 'rgb(var(--color-accent-orange) / <alpha-value>)',
        'accent-yellow': 'rgb(var(--color-accent-yellow) / <alpha-value>)',
        'text': 'rgb(var(--color-text) / <alpha-value>)',
        'neutral-black': 'rgb(var(--color-neutral-black) / <alpha-value>)',
        'neutral-white': 'rgb(var(--color-neutral-white) / <alpha-value>)',
        'neutral-offwhite': 'rgb(var(--color-neutral-offwhite) / <alpha-value>)',
        'surface-warm': 'rgb(var(--color-surface-warm) / <alpha-value>)',
      },
      fontFamily: {
        // Sauti 116 Institutional Voice: Cronos Pro is the primary brand typeface.
        // Roboto and system-fonts are used as secondary digital fallbacks.
        sans: ['"Cronos Pro"', 'Roboto', 'ui-sans-serif', 'system-ui', 'sans-serif'],
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
