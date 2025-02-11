<script setup lang="ts">
import { ElMenu, ElMenuItem, ElScrollbar } from 'element-plus';
import InitView from './views/Init.vue';
import { logger, changeTheme } from './utils';
import { useRouter } from 'vue-router';
import { useConfigStore } from './stores';
import { ref, watch, onMounted, onUnmounted } from 'vue';

const config = useConfigStore();
const router = useRouter();

function changeMenu(url: string) {
    router.push(url);
}

const active = ref("/");

watch(
    () => router.currentRoute.value.path,
    (newPath) => {
        active.value = "/" + newPath.split("/").slice(1).join("/");
    },
    { immediate: true }
);

const updateTheme = () => {
    if (config.theme === 'auto') {
        const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        changeTheme(isDark ? 'dark' : 'light');
    } else {
        changeTheme(config.theme);
    }
};

onMounted(() => {
    updateTheme();
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', updateTheme);
    window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', updateTheme);
});

onUnmounted(() => {
    window.matchMedia('(prefers-color-scheme: dark)').removeEventListener('change', updateTheme);
    window.matchMedia('(prefers-color-scheme: light)').removeEventListener('change', updateTheme);
});
watch(
    () => config.theme,
    () => {
        updateTheme();
    }
)
</script>

<template>
    <div class="menu">
        <el-menu :collapse="true" :route="true" :default-active="active">
            <div class="title logo">HoYoCenter</div>
            <el-menu-item index="/" @click="changeMenu('/')">
                <img src="./assets/icons/Home.png" class="icon" />开始
            </el-menu-item>
            <span class="title">游戏</span>
            <el-menu-item index="/character" @click="changeMenu('/character')">
                <img src="./assets/icons/Character.png" class="icon" />角色
            </el-menu-item>
            <el-menu-item index="/gacha" @click="changeMenu('/gacha')">
                <img src="./assets/icons/Gacha.png" class="icon" />抽卡
            </el-menu-item>
            <el-menu-item index="/achievement" @click="changeMenu('/achievement')">
                <img src="./assets/icons/Achievement.png" class="icon" />成就
            </el-menu-item>
            <el-menu-item index="/hoyolab" @click="changeMenu('/hoyolab')">
                <img src="./assets/icons/MiYouShe.png" class="icon" />米游社
            </el-menu-item>
            <el-menu-item index="/wiki/character" @click="changeMenu('/wiki/character')">
                <img src="./assets/icons/CharacterWiki.png" class="icon" />角色信息
            </el-menu-item>
            <el-menu-item index="/wiki/monster" @click="changeMenu('/wiki/monster')"><img
                    src="./assets/icons/MonsterWiki.png" class="icon" />怪物信息</el-menu-item>
            <el-menu-item index="/wiki/weapon" @click="changeMenu('/wiki/weapon')"><img
                    src="./assets/icons/WeaponWiki.png" class="icon" />武器信息</el-menu-item>
            <span class="title">设置</span>
            <el-menu-item index="/setting" @click="changeMenu('/setting')">
                <img src="./assets/icons/Setting.png" class="icon" />设置
            </el-menu-item>
        </el-menu>
    </div>

    <div class="content"><router-view />
    </div>
    <div class="initview" v-if="!config.init"><init-view /></div>

</template>

<style scoped>
.menu {
    width: 150px;
    height: calc(100vh - 10px);
    overflow: overlay;
    margin-right: 20px;
    margin-top: 5px;
    margin-bottom: 5px;
}

.menu .el-menu {
    height: 100%;
    width: 100%;
}

.menu .el-menu-item {
    height: calc((100% - 95px) / 9);
}

.menu .title {
    text-align: left;
    padding-left: 5px;
    font-size: 15px;
}

.logo {
    line-height: 45px;
    font-size: 20px !important;
    font-weight: bold;
    text-align: center !important;
    padding-left: 0;
}

.initview {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.icon {
    width: 25px;
    height: 25px;
    margin-right: 5px;
}

.content {
    height: 100%;
    padding: 12px 0;
    margin-right: 12px;
    width: calc(100% - 170px);
}
</style>

<style>
#app {
    display: flex;
}
</style>
