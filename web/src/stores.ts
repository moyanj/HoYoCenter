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
            theme: "auto",
            user_name: "用户",
            game: {
                ys: {
                    enable: false,
                    uid: "",
                },
                sr: {
                    enable: false,
                    uid: "",
                },
                zzz: {
                    enable: false,
                    uid: "",
                },
            },
            user: {
                name: "",
                cookie: "",
                uid: "",
                ltoken_v1: "",
                ltoken_v2: "",
                stoken_v1: "",
                stoken_v2: "",
                game_token: "",
                mid: "",
                cookie_token: "",
                fp: "",
            },
            init: false,
        }
    }
})

