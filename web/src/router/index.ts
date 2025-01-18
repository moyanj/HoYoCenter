import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import SettingView from "@/views/SettingView.vue";
import HoYoLabView from "@/views/HoYoLabView.vue";
import FallbackView from "@/views/FallbackView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeView,
        },
        {
            path: "/setting",
            name: "setting",
            component: SettingView,
        },
        {
            path: "/hoyolab",
            name: "hoyolab",
            component: HoYoLabView,
        },
        {
            path: "/:pathMatch(.*)*",
            name: "404",
            component: FallbackView,
        },
    ],
});

export default router;
