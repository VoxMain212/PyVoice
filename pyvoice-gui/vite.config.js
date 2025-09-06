import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import electronRenderer from 'vite-plugin-electron-renderer';

export default defineConfig({
  plugins: [
    vue(),
    electronRenderer(), // ← важно!
  ],
  build: {
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['vue', 'vue-router'],
        },
      },
    },
  },
});