import { defineConfig, loadEnv } from 'vite';
import vue from '@vitejs/plugin-vue';
import { fileURLToPath, URL } from 'node:url';

export default defineConfig(({ mode }) => {
  // Load env vars from the correct file
  const env = loadEnv(mode, process.cwd(), '');

  // Validate that the required env var is set
  if (!env.VITE_BASE_PATH) {
    throw new Error('VITE_BASE_PATH is not defined. Please check your .env file.');
  }

  return {
    // Base path is driven ONLY by the env var
    base: env.VITE_BASE_PATH,

    plugins: [vue()],

    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },

    server: {
      host: true, // Listen on all network interfaces
      port: 5174, // Vite's default port
      allowedHosts: ['sauti.local'],
      hmr: {
        clientPort: 80, // Matches the Nginx port inside the container network
      },
      // Proxy is handled by the top-level Nginx service in docker-compose.dev.yml
    },
  };
});