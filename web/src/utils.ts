import { base_api } from './stores';


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

export class logger {
    static _log(text: any, type: string) {
        console.log(text);
        if (typeof text === 'object') {
            text = JSON.stringify(text);
        }
        fetch(`${base_api}log?msg=${text.toString()}&type=${type}`);
    }
    static info(text: any) {
        this._log(text, 'INFO');
    }
    static warn(text: any) {
        this._log(text, 'WARNNING');
    }
    static error(text: any) {
        this._log(text, 'ERROR');
    }
    static debug(text: any) {
        this._log(text, 'DEBUG');
    }
}