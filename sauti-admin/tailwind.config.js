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
