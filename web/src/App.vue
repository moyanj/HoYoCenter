<script setup lang="ts">
import { RouterView } from 'vue-router';
import { ElMenu, ElMenuItem } from 'element-plus';
</script>

<template>
    <div class="menu">
        <el-menu :collapse="true">
            <div class="title logo" style="">LOGO</div>
            <el-menu-item index="1">开始</el-menu-item>
            <span class="title">游戏</span>
            <el-menu-item index="2">角色</el-menu-item>
            <el-menu-item index="3">抽卡</el-menu-item>
            <el-menu-item index="4">成就</el-menu-item>
            <el-menu-item index="5">米游社</el-menu-item>
        </el-menu>
    </div>
    
    <div class="content"><RouterView /></div>
    
</template>

<style scoped>
.menu {
    width: 150px;
    height: calc(100vh - 10px);
    overflow: auto;
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
    font-size: 17px;
}

.logo {
    line-height: 50px;
    font-size: 20px !important; 
    font-weight: bold;
    text-align: center !important;
    padding-left: 0;
}

.content {
    height: 100vh;
    overflow: auto;
}   
</style>

<style>
#app {
    display: flex;
}
</style>
