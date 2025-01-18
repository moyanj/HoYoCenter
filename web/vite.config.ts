import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import { px2viewport } from '@mistjs/vite-plugin-px2viewport';

export default defineConfig({
    plugins: [
        px2viewport({
            viewportWidth: 1360,
            unitPrecision: 10,
        }),
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
