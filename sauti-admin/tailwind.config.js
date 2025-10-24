/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // Sauti Brand Colors (synced with public frontend)
        primary: {
          50: '#fff4ec',
          100: '#ffe9d9',
          200: '#ffd0b3',
          300: '#ffb18c',
          400: '#ff8c52',
          500: '#CC5500', // Sauti Orange (matching frontend)
          600: '#a64400',
          700: '#7f3400',
          800: '#592500',
          900: '#3b1900',
        },
        gray: {
          50: '#fafafa',
          100: '#f4f4f5',
          200: '#e4e4e7',
          300: '#d4d4d8',
          400: '#a1a1aa',
          500: '#71717a',
          600: '#52525b',
          700: '#3f3f46',
          800: '#27272a',
          900: '#18181b',
        },
        // Utility colors for admin dashboard
        success: {
          500: '#10b981',
          600: '#059669',
        },
        danger: {
          400: '#f87171',
          500: '#ef4444',
          600: '#dc2626',
        },
        warning: {
          500: '#f59e0b',
          600: '#d97706',
        },
        info: {
          500: '#3b82f6',
          600: '#2563eb',
        },
        // Context-specific colors (matching frontend)
        purple: {
          500: '#8b5cf6', // GBV cases
          600: '#7c3aed',
        },
        teal: {
          500: '#14b8a6', // Resources
          600: '#0d9488',
        }
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      }
    },
  },
  plugins: [],
}
