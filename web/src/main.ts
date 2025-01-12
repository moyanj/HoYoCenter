import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import { initConfig, useConfigStore } from './stores'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'
import './assets/main.css'


const app = createApp(App)

app.use(createPinia())
app.use(router)
initConfig(useConfigStore());
app.mount('#app')
