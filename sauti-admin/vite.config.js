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
      allowedHosts: ['sauti.local', 'localhost', '127.0.0.1'],
      // hmr block removed for local development
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:8000',
          changeOrigin: true,
          secure: false,
          // rewrite: (path) => path.replace(/^\/api/, ''), // REMOVED: Backend seems to expect /api prefix or similar, let's try sending full path first, OR wait..
          // Actually, earlier curl said:
          // /auth/login/ -> 404
          // /api/auth/login/ -> 404 (wait, curl output ID 1018 said /api/auth/login/ -> 400 Bad Request !!)
          // IF /api/auth/login/ gave 400, it means it HIT the backend but failed validation (missing body).
          // Meaning the backend EXPECTS /api/ prefix?
          // BUT cms/urls.py does NOT have api/.
          // Let me double check curl output 1018.
          // Output 1018: HTTP/1.1 400 Bad Request.
          // Wait, if cms/urls.py has `path('auth/', ...)` at root. Then `/auth/login/` should work.
          // Why did `curl -I -X POST http://127.0.0.1:8000/auth/login/` return 404 in step 1016?
          // That is very strange.
          // Maybe `curl -I` (HEAD) caused 404 if the view doesn't support HEAD? But usually it returns 405.
          // Let's assume the backend has a prefix I missed, OR I should check if `cms/urls.py` is actually used.
          // In `manage.py`, `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')`.
          // `cms/settings.py` -> `ROOT_URLCONF = 'cms.urls'`.

          // Let's look at Step 1018 again.
          // `curl -I -X POST http://127.0.0.1:8000/api/auth/login/` -> 400 Bad Request.
          // This implies `/api/auth/login/` IS the correct URL.
          // How? `cms/urls.py` doesn't show it.
          // Maybe `QUICKSTART.md` mentions it?
          // Step 962: "API Root: http://localhost:8000/api/" 
          // Ah! The valid URL probably includes `/api` via some other mechanism or I misread `cms/urls.py`?
          // Re-reading `cms/urls.py` in step 1020...
          // I feel like I'm crazy. It says: `urlpatterns = [ path('admin/', ...), path('auth/', ...`
          // Unless... `urls.py` shown is not the one running?

          // Regardless, curl confirmed `/api/auth/login/` returns 400 (which means it found the view).
          // So I should NOT strip `/api`.

        },
      },
    },
  };
});