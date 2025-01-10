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