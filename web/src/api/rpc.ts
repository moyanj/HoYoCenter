export var base_api = "";
if (import.meta.env.DEV) {
    base_api = "http://127.0.0.1:6553"; // 修复了链接格式
} else {
    base_api = "";
}

export interface GameConfig {
    enable: boolean;
    uid: string;
}

export interface UserConfig {
    name: string;
    cookie: string;
    uid: string;
    ltoken_v1: string;
    ltoken_v2: string;
    stoken_v1: string;
    stoken_v2: string;
    game_token: string;
    mid: string;
    cookie_token: string;
    fp: string;
}

export interface Config {
    theme: string;
    user_name: string;
    game: {
        ys: GameConfig;
        sr: GameConfig;
        zzz: GameConfig;
    };
    user: UserConfig;
    init: boolean;
}

export interface Backend {
    "data.config": () => Config;
    "data.urls": () => object;
    "data.build_info": () => object;
    "data.update_config": (config: object) => void;
    "log.info": (msg: string) => void;
    "log.error": (msg: string) => void;
    "log.debug": (msg: string) => void;
    "log.warning": (msg: string) => void;
    "requests.get": (url: string, params?: object, headers?: object) => object;
    "requests.post": (url: string, params?: object, headers?: object) => object;
    "requests.req": (method: string, url: string, params?: object, headers?: object) => object;
}

type MethodName<T> = keyof {
    [K in keyof T as T[K] extends (...args: any) => any ? K : never]: T[K];
};

type MethodReturnType<T, M extends keyof T> = T[M] extends (...args: any) => infer R ? R : never;

class RPC<T> {
    private id: number;
    private url: string;
    constructor(url: string) {
        this.url = url;
        this.id = 0;
    }
    async call<M extends MethodName<T>>(method: M, params: any = []): Promise<MethodReturnType<T, M>> {
        const requestPayload = {
            jsonrpc: "2.0",
            method: method as string,
            params,
            id: this.id++,
        };
        const response = await fetch(this.url, {
            method: "POST",
            body: JSON.stringify(requestPayload),
            headers: {
                "Content-Type": "application/json",
            }
        });
        if (!response.ok) {
            throw new Error(`RPC call failed with status ${response.status}`);
        }
        const result = await response.json();
        if ("error" in result) {
            throw new Error(result.error.message);
        }
        return result.result;
    }
}
export const rpc = new RPC<Backend>(base_api + "/api");
export default rpc;