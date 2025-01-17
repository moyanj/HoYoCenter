import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { rpc, type Config } from './rpc';

export function initConfig(store: any) {
    rpc.call("data.config").then((config: any) => {
        store.$patch(config);
    });
    store.$subscribe(syncConfig)
}

async function syncConfig() {
    const config = useConfigStore();
    await rpc.call("data.update_config", [config.$state]);
}

export const useConfigStore = defineStore('config', {
    state: (): Config => {
        return {
            user_name: "用户",
            theme: "auto",
        }
    }
})

