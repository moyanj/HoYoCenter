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

export var base_api = "/";
if (import.meta.env.DEV) {
    base_api = "http://127.0.0.1:6553/";
} else {
    base_api = "/";
}

export const config = fetch(base_api + 'app/config').then(res => res.json()).then(res => res['data']).then(res => res['config']);
