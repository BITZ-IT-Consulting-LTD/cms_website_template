import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig(({ mode }) => {
  return {
    /**
     * IMPORTANT:
     * Each Vue app is served on its own port (8085 / 3001).
     * Assets must be resolved from the app root.
     */
    base: '/',

    plugins: [vue()],

    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },

    /**
     * Dev server configuration
     * Used ONLY when running `npm run dev`
     */
    server: {
      host: true,
      port: 3000,

      /**
       * Development convenience:
       * Proxy API calls to Django to avoid CORS locally.
       * In production, Vue calls Django directly using VITE_API_URL.
       */
      // proxy: {
      //   '/api': {
      //     target: process.env.VITE_API_URL || 'http://localhost:8000',
      //     changeOrigin: true,
      //     secure: false
      //   }
      // }
    },

    /**
     * Build configuration (production)
     */
    build: {
      outDir: 'dist',
      assetsDir: 'assets',
      sourcemap: false
    }
  }
})
