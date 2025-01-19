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
        rollupOptions: {
            output: {
                entryFileNames: 'assets/main.js',
                chunkFileNames: 'assets/[name].js',
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
