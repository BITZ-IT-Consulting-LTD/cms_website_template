import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')

  // Only enforce VITE_BASE_PATH in production
  if (mode === 'production' && !env.VITE_BASE_PATH) {
    throw new Error('VITE_BASE_PATH is not defined for production build.')
  }

  return {
    /**
     * 🚨 CRITICAL RULE
     * - DEV  → base MUST be '/'
     * - PROD → base comes from VITE_BASE_PATH
     */
    base: mode === 'development' ? '/' : env.VITE_BASE_PATH,

    plugins: [vue()],

    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },

    server: mode === 'development'
      ? {
        host: true,
        port: 5173,
        allowedHosts: ['sauti.local', 'localhost', '127.0.0.1'],
        proxy: {
          '/api': {
            target: 'http://127.0.0.1:8000',
            changeOrigin: true,
            secure: false,
          },
        },
      }
      : undefined,
  }
})
