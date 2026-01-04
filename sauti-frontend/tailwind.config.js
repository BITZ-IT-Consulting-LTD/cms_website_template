/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        sauti: {
          blue: '#007BBF',
          yellow: '#FFF200',
          orange: '#FF9933',
          red: '#ED1C24',
          darkGreen: '#006633',
          lightGreen: '#8CC63F',
          black: '#000000',
          white: '#FFFFFF',
          neutral: '#F4F4F5',
        },
      },
      fontFamily: {
        sans: ['"Cronos Pro"', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', '"Helvetica Neue"', 'Arial', '"Noto Sans"', 'sans-serif'],
      },
      boxShadow: {
        'sauti-red': '0 0 12px rgba(237, 28, 36, 0.4)',
      },
      animation: {
        'emergency-glow': 'emergencyGlow 2s ease-in-out infinite',
      },
      keyframes: {
        emergencyGlow: {
          '0%, 100%': { boxShadow: '0 0 0 rgba(237, 28, 36, 0)' },
          '50%': { boxShadow: '0 0 12px rgba(237, 28, 36, 0.4)' },
        },
      },
    },
  },
  plugins: [],
}
