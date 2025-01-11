export function changeTheme(theme?: string) {
    const root = document.documentElement;
    if (theme === undefined) {
        theme = root.getAttribute('class') === 'dark' ? 'light' : 'dark';
    }
    root.setAttribute('class', theme);
}

export function getTheme() {
    return document.documentElement.getAttribute('class');
}

export class console {
    static async _log(text: string, type: string) {
        fetch(`/console?text=${text}&type=${type}`);
    }
    static async log(...args: any[]) {
        if (getTheme() === 'dark') {
            console.log(...args);
        }
    }
}