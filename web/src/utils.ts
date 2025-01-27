import { rpc } from "./api/rpc";
import CryptoJS from 'crypto-js';

export function changeTheme(theme?: string): void {
    const root = document.documentElement;
    if (theme === undefined || theme === 'auto') {
        theme = root.getAttribute('class') === 'dark' ? 'light' : 'dark';
    }
    root.setAttribute('class', theme);
}

export function getTheme(): string | null {
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

export function parseCookies(cookieString: string): Record<string, string> {
    // 初始化对象
    const cookies: Record<string, string> = {};

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

class AesEncryption {
    private secretKey: string;

    constructor(secretKey: string) {
        this.secretKey = secretKey;
    }

    /**
     * 加密字符串
     * @param plaintext 明文字符串
     * @returns 加密后的密文
     */
    public encrypt(plaintext: string): string {
        const ciphertext = CryptoJS.AES.encrypt(plaintext, this.secretKey).toString();
        return ciphertext;
    }

    /**
     * 解密字符串
     * @param ciphertext 密文字符串
     * @returns 解密后的明文
     */
    public decrypt(ciphertext: string): string {
        const bytes = CryptoJS.AES.decrypt(ciphertext, this.secretKey);
        const originalText = bytes.toString(CryptoJS.enc.Utf8);
        return originalText;
    }

    /**
     * 加密字节数组
     * @param plaintextBytes 明文字节数组
     * @returns 加密后的密文字节数组
     */
    public encryptBytes(plaintextBytes: Uint8Array): Uint8Array {
        const plaintext = CryptoJS.lib.WordArray.create(plaintextBytes);
        const ciphertext = CryptoJS.AES.encrypt(plaintext, this.secretKey).ciphertext;
        return CryptoJS.lib.WordArray.create(ciphertext).toByteArray();
    }

    /**
     * 解密字节数组
     * @param ciphertextBytes 密文字节数组
     * @returns 解密后的明文字节数组
     */
    public decryptBytes(ciphertextBytes: Uint8Array): Uint8Array {
        const ciphertext = CryptoJS.lib.WordArray.create(ciphertextBytes);
        const bytes = CryptoJS.AES.decrypt({ ciphertext }, this.secretKey);
        return CryptoJS.lib.WordArray.create(bytes).toByteArray();
    }
}

export function obj2params(obj: Record<string, string | number>): string {
    return Object.keys(obj).map(key => `${key}=${encodeURIComponent(obj[key])}`).join('&');
}

export function obj2cookies(obj: Record<string, string | number>): string {
    return Object.keys(obj).map(key => `${key}=${encodeURIComponent(obj[key])}`).join('; ');
}

export function uuidv4() {
    return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c =>
        (+c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> +c / 4).toString(16)
    );
}
