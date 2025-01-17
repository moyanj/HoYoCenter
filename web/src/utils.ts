import { rpc } from "./rpc";

export function changeTheme(theme?: string) {
    const root = document.documentElement;
    if (theme === undefined || theme === 'auto') {
        theme = root.getAttribute('class') === 'dark' ? 'light' : 'dark';
    }
    root.setAttribute('class', theme);
}

export function getTheme() {
    return document.documentElement.getAttribute('class');
}

type LogLevel = "info" | "warning" | "error" | "debug";

export class logger {
    static _log(text: any, level: LogLevel) {
        if (typeof text === 'object') {
            text = JSON.stringify(text);
        } else {
            text = text.toString();
        }
        console.log(text);
        // @ts-ignore
        rpc.call("log." + level, [text]);
    }
    static info(text: any) {
        this._log(text, "info");
    }
    static warn(text: any) {
        this._log(text, "warning");
    }
    static error(text: any) {
        this._log(text, "error");
    }
    static debug(text: any) {
        this._log(text, "debug");
    }
}

type Cookies = Record<string, string>;

export function parseCookies(cookieString: string): Cookies {
    // 初始化对象
    const cookies: Cookies = {};

    // 判断 cookieString 是否为空
    if (!cookieString) {
        return cookies;
    }

    // 分割字符串
    cookieString.split(';').forEach(cookie => {
        // 去除 cookie 两端的空白字符
        cookie = cookie.trim();

        // 如果 cookie 不包含等号，则跳过
        if (!cookie.includes('=')) {
            return;
        }

        // 分割 cookie
        const [name, value] = cookie.split('=');

        // 去除 name 和 value 两端的空白字符
        const trimmedName = name.trim();

        // 解码 value
        const decodedValue = decodeURIComponent(value);

        // 将 name 和 value 添加到 cookies 对象中
        cookies[trimmedName] = decodedValue;
    });

    // 返回 cookies 对象
    return cookies;
}