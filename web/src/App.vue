<script setup>
import { ElMenu, ElMenuItem, ElScrollbar } from 'element-plus';
import { logger, changeTheme } from './utils';
import { useRouter } from 'vue-router';
import { useConfigStore } from './stores';
import { ref, watch, onMounted, onUnmounted } from 'vue';

const config = useConfigStore();
const router = useRouter();

function changeMenu(url) {
    logger.info("changeMenu:", url);
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
</script>

<template>
    <div class="menu">
        <el-menu :collapse="true" :route="true" :default-active="active">
            <el-scrollbar>
            <div class="title logo">HoYoCenter</div>
            <el-menu-item index="/" @click="changeMenu('/')">开始</el-menu-item>
            <span class="title">游戏</span>
            <el-menu-item index="/character" @click="changeMenu('/character')">角色</el-menu-item>
            <el-menu-item index="/chouka" @click="changeMenu('/chouka')">抽卡</el-menu-item>
            <el-menu-item index="/achievement" @click="changeMenu('/achievement')">成就</el-menu-item>
            <el-menu-item index="/hoyolab" @click="changeMenu('/hoyolab')">米游社</el-menu-item>
            <el-menu-item index="/info/character" @click="changeMenu('/info/character')">角色信息</el-menu-item>
            <el-menu-item index="/info/monster" @click="changeMenu('/info/monster')">怪物信息</el-menu-item>
            <el-menu-item index="/info/weapon" @click="changeMenu('/info/weapon')">武器信息</el-menu-item>
            <span class="title">设置</span>
            <el-menu-item index="/setting" @click="changeMenu('/setting')">设置</el-menu-item>
            </el-scrollbar>
        </el-menu>
    </div>
    
    <div class="content"><RouterView /></div>
    
</template>

<style scoped>
.menu {
    width: 150px;
    height: calc(100% - 10px);
    overflow: overlay;
    margin-right: 20px;
    margin-top: 5px;
    margin-bottom: 5px;
}

.menu .el-menu {
    height: 100%;
    width: 100%;
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

.content {
    height: 100%;
    padding: 12px 0;
}   
</style>

<style>
#app {
    display: flex;
}
</style>
