import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/Home.vue";
import SettingView from "@/views/Setting.vue";
import HoYoLabView from "@/views/HoYoLab.vue";
import CharacterView from "@/views/Character.vue";
import CharacterWikiView from "@/views/CharacterWiki.vue";
import MonsterWikiView from "@/views/MonsterWiki.vue";
import FallbackView from "@/views/Fallback.vue";

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
            path: "/character",
            name: "character",
            component: CharacterView,
        },
        {
            path: "/hoyolab",
            name: "hoyolab",
            component: HoYoLabView,
        },
        {
            path: "/wiki/character",
            name: "character_wiki",
            component: CharacterWikiView,
        },
        {
            path: "/wiki/monster",
            name: "monster_wiki",
            component: MonsterWikiView,
        },
        {
            path: "/:pathMatch(.*)*",
            name: "404",
            component: FallbackView,
        },
    ],
});

export default router;
