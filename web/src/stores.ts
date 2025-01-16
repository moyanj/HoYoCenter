import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export var base_api = "/";
if (import.meta.env.DEV) {
    base_api = "http://127.0.0.1:6553/";
} else {
    base_api = "/";
}

export function initConfig(store: any) {
    try {
        fetch(base_api + "app/config").then((response) => {
            return response.json();
        }).then((data) => {
            store.$patch(data["data"]);
        });
    } catch (e) {
        console.log(e);
    }

    store.$subscribe(syncConfig)
}

async function syncConfig() {
    const config = useConfigStore();
    await fetch(base_api + "app/config", {
        method: "POST",
        body: JSON.stringify(config.$state),
        headers: {
            "Content-Type": "application/json",
        },
    });
}

export const useConfigStore = defineStore('config', {
    state: () => {
        return {
            user_name: "用户",
            theme: "auto",
        }
    }
})

