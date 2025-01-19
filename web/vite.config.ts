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
        rollupOptions: {
            output: {
                entryFileNames: 'assets/main.js',
                chunkFileNames: (info) => {
                    if (info.moduleIds[0].endsWith(".json")) {
                        return 'assets/langauges/[name].js'
                    }
                    return 'assets/[name].js'
                },
                assetFileNames: (info) => {
                    if (info.names[0].endsWith('.png') || info.names[0].endsWith('.jpg') || info.names[0].endsWith('.svg')) {
                        return 'assets/img/[name].[ext]'
                    }
                    return 'assets/[name].[ext]'
                },
                manualChunks: {
                    framework: ['vue', 'vue-router', 'pinia'],
                    ui: ['element-plus']
                }
            }
        }
    }
})
