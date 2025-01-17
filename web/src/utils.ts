import { rpc, type Backend } from "./rpc";

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
        }
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