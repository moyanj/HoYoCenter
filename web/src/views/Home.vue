<script setup lang="ts">
import { useConfigStore } from '@/stores';
import { ElCard, ElRow, ElCol } from 'element-plus';
const configrStore = useConfigStore();
</script>

<template>
    <h1>你好，{{ configrStore.user_name }}！</h1>
    <br>
    <el-row :gutter="16">
        <el-col :span="configrStore.game.ys.enable && configrStore.game.sr.enable ? 12 : 24"
            v-if="configrStore.game.ys.enable">
            <h2>原神</h2>
            <el-card>加载失败。。。</el-card>
        </el-col>
        <el-col :span="configrStore.game.ys.enable && configrStore.game.sr.enable ? 12 : 24"
            v-if="configrStore.game.sr.enable">
            <h2>崩坏：星穹铁道</h2>
            <el-card>加载失败。。。</el-card>
        </el-col>
    </el-row>

</template>
