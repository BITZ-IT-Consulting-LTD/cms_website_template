/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // Neutral Palette (Text & Backgrounds)
        neutral: {
          white: '#FFFFFF',
          dark: '#006633', // Sauti Dark Green for dark backgrounds
          textPrimary: '#222222', // Primary text (very dark gray)
          textSecondary: '#555555', // Secondary text (subheadings, captions)
          border: '#DDDDDD', // Borders, disabled states
        },
        // Sauti Brand Colors
        sauti: {
          blue: '#009EDB', // Information, primary actions
          orange: '#FF9900', // Secondary actions
          red: '#EC0000', // Error, danger, urgent/emergency
          greenLight: '#99CC00', // Success
          greenDark: '#006633', // Dark green (footer, dark backgrounds)
          yellow: '#FFED00', // Warning
        },
        // Semantic Colors (User Feedback)
        success: {
          500: '#99CC00', // Sauti Light Green
          600: '#88BB00',
        },
        warning: {
          500: '#FFED00', // Sauti Yellow
          600: '#E6D600',
        },
        error: {
          500: '#EC0000', // Sauti Red
          600: '#CC0000',
        },
        info: {
          500: '#009EDB', // Sauti Blue
          600: '#007BAA',
        },
        // Legacy support (mapped to new colors)
        primary: {
          50: '#E6F7FF',
          100: '#B3E5FF',
          500: '#009EDB', // Sauti Blue
          600: '#007BAA',
        },
        secondary: {
          500: '#FF9900', // Sauti Orange
          600: '#E68A00',
        },
        danger: {
          500: '#EC0000', // Sauti Red
          600: '#CC0000',
        },
      },
      fontFamily: {
        sans: ['-apple-system','BlinkMacSystemFont','Inter','system-ui','sans-serif'],
      },
    },
  },
  plugins: [],
}
