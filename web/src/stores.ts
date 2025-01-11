import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useConfigrStore = defineStore('config', () => {
    const count = ref(0)
    const doubleCount = computed(() => count.value * 2)
    function increment() {
        count.value++
    }

    return { count, doubleCount, increment }
})
const base_api = "http://localhost:8080"
const config = await fetch('/config.json').then(res => res.json());
