import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
    plugins: [
        vue(),
        vueDevTools()
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
