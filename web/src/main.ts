import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import { initConfig, useConfigStore } from './stores'
import { i18n, loadLanguageAsync } from './i18n'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'
import './assets/main.css'


const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)
initConfig(useConfigStore());
loadLanguageAsync(useConfigStore().langauge).then(() => {
    app.mount('#app')
});