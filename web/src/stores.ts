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

    //const config = JSON.parse(xhr.responseText);
    //store.$patch(config);
}

export const useConfigStore = defineStore('config', {
    state: () => {
        return {
            base_api: base_api,
            user_name: "用户",
            theme: "auto",
        }
    },
})

