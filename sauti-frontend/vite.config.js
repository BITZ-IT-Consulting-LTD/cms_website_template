import { loadEnv } from 'vite';
import vue from '@vitejs/plugin-vue';
import { fileURLToPath, URL } from 'node:url';

export default ({ mode }) => {
  // Load env file based on `mode`
  const env = loadEnv(mode, process.cwd(), '');

  const basePath = env.VITE_BASE_PATH;

  // Build-time guard to ensure VITE_BASE_PATH is set
  if (basePath === undefined) {
    throw new Error('VITE_BASE_PATH is not defined in your .env file.');
  }

  console.log(`Vite build mode: ${mode}`);
  console.log(`Using base path: ${basePath}`);

  return {
    // Use the basePath from the .env file
    base: basePath,

    plugins: [vue()],

    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },

    server: {
      host: true,
      port: 3000,
      proxy: {
        '/api': {
          target: env.VITE_API_URL || 'http://localhost:8000',
          changeOrigin: true,
          secure: false,
          rewrite: (path) => {
            const target = env.VITE_API_URL || 'http://localhost:8000';
            if (target.replace(/\/+$/, '').endsWith('/api')) {
              return path.replace(/^\/api/, '');
            }
            return path;
          }
        }
      }
    },

    build: {
      outDir: 'dist',
      assetsDir: 'assets',
      sourcemap: false
    }
  };
};
