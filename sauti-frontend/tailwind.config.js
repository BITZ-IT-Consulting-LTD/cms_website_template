/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // Updated Brand: black/white and accent orange #CC5500
        primary: {
          50: '#fafafa',
          100: '#f4f4f5',
          200: '#e4e4e7',
          300: '#d4d4d8',
          400: '#a1a1aa',
          500: '#262626', // Neutral dark (text)
          600: '#171717',
          700: '#0f0f10',
          800: '#09090b',
          900: '#000000',
        },
        secondary: {
          50: '#fff4ec',
          100: '#ffe9d9',
          200: '#ffd3b3',
          300: '#ffbd8c',
          400: '#ff9552',
          500: '#CC5500', // Accent Orange
          600: '#a64400',
          700: '#7f3400',
          800: '#592500',
          900: '#3b1900',
        },
        success: {
          500: '#10b981', // Green
          600: '#059669',
        },
        purple: {
          500: '#8b5cf6', // For GBV
          600: '#7c3aed',
        },
        teal: {
          500: '#14b8a6', // For resources
          600: '#0d9488',
        },
        danger: {
          400: '#f87171',
          500: '#ef4444', // Red for critical
          600: '#dc2626',
        },
      },
      fontFamily: {
        sans: ['-apple-system','BlinkMacSystemFont','Inter','system-ui','sans-serif'],
      },
    },
  },
  plugins: [],
}
