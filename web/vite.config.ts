import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import topLevelAwait from 'vite-plugin-top-level-await';

export default defineConfig({
    plugins: [
        vue(),
        vueDevTools(),
        topLevelAwait()
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        },
    },
    build: {
        target: 'es6',
        rollupOptions: {
            output: {
                manualChunks: {
                    framework: ['vue', 'vue-router', 'pinia'],
                    ui: ['element-plus']
                }
            }
        }
    }
})
