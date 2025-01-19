import { createI18n } from 'vue-i18n';

const i18n = createI18n({
    locale: 'zh-cn', // 设置默认语言
    fallbackLocale: 'zh-cn', // 设置备用语言
    messages: {}, // 初始时不加载任何语言包
});

// 异步加载语言包
function loadLanguageAsync(lang: string) {
    return import(`./locales/${lang}.json`)
        .then(msgs => {
            i18n.global.setLocaleMessage(lang, msgs.default);
            i18n.global.locale = lang;
        });
}

export { i18n, loadLanguageAsync };