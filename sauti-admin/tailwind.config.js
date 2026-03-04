/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // Neutral Palette (Text & Backgrounds)
        neutral: {
          white: '#FFFFFF',
          dark: '#006633', // Sauti Dark Green for dark backgrounds / footer
          textPrimary: '#222222',
          textSecondary: '#555555',
          border: '#DDDDDD',
        },
        // Sauti Brand Colors
        sauti: {
          blue: '#009EDB',
          orange: '#FF9900',
          red: '#EC0000',
          greenLight: '#99CC00',
          greenDark: '#006633',
          yellow: '#FFED00',
        },
        // Semantic Colors (User Feedback)
        success: {
          500: '#99CC00',
          600: '#88BB00',
        },
        warning: {
          500: '#FFED00',
          600: '#E6D600',
        },
        error: {
          500: '#EC0000',
          600: '#CC0000',
        },
        info: {
          500: '#009EDB',
          600: '#007BAA',
        },
        // Legacy support mappings
        primary: {
          50: '#E6F7FF',
          100: '#B3E5FF',
          500: '#009EDB',
          600: '#007BAA',
        },
        secondary: {
          500: '#FF9900',
          600: '#E68A00',
        },
        danger: {
          500: '#EC0000',
          600: '#CC0000',
        },
        purple: {
          500: '#7C3AED',
          600: '#6B2DCC',
        },
        teal: {
          500: '#0D9488',
          600: '#0A746A',
        },
      },
      fontSize: {
        'fluid-xs': 'clamp(0.75rem, 0.7rem + 0.25vw, 0.875rem)',
        'fluid-sm': 'clamp(0.875rem, 0.8125rem + 0.3125vw, 1rem)',
        'fluid-base': 'clamp(1rem, 0.9375rem + 0.3125vw, 1.125rem)',
        'fluid-lg': 'clamp(1.125rem, 1rem + 0.625vw, 1.5rem)',
        'fluid-xl': 'clamp(1.25rem, 1.125rem + 0.625vw, 1.75rem)',
        'fluid-2xl': 'clamp(1.5rem, 1.25rem + 1.25vw, 2rem)',
        'fluid-3xl': 'clamp(1.75rem, 1.375rem + 1.875vw, 3rem)',
        'fluid-4xl': 'clamp(2rem, 1.5rem + 2.5vw, 4rem)',
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
