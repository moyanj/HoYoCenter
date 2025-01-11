<script setup lang="ts">
import { RouterView } from 'vue-router';
import { ElMenu, ElMenuItem, ElScrollbar } from 'element-plus';
import { logger } from './utils';
import { useRouter } from 'vue-router';
import { useConfigrStore } from './stores';

const config = useConfigrStore();
var router = useRouter();

function changeMenu(url: string) {
    logger.info("changeMenu:" + url);
    router.push(url);
}
</script>

<template>
    <div class="menu">
        <el-menu :collapse="true">
            <el-scrollbar>
            <div class="title logo">HoYoCenter</div>
            <el-menu-item index="1" @click="changeMenu('/')">开始</el-menu-item>
            <span class="title">游戏</span>
            <el-menu-item index="2" @click="changeMenu('/character')">角色</el-menu-item>
            <el-menu-item index="3" @click="changeMenu('/chouka')">抽卡</el-menu-item>
            <el-menu-item index="4" @click="changeMenu('/achievement')">成就</el-menu-item>
            <el-menu-item index="5" @click="changeMenu('/hoyolab')">米游社</el-menu-item>
            <el-menu-item index="6" @click="changeMenu('/info/character')">角色信息</el-menu-item>
            <el-menu-item index="7" @click="changeMenu('/info/monster')">怪物信息</el-menu-item>
            <el-menu-item index="8" @click="changeMenu('/info/weapon')">武器信息</el-menu-item>
            <span class="title">设置</span>
            <el-menu-item index="9" @click="changeMenu('/setting')">设置</el-menu-item>
            </el-scrollbar>
        </el-menu>
    </div>
    
    <div class="content"><RouterView /></div>
    
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
    width: 150px;
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
    height: 100vh;
    padding: 12px 0;
}   
</style>

<style>
#app {
    display: flex;
}
</style>
