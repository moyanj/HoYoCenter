<script setup lang="ts">
import { ElScrollbar, ElRadioGroup, ElRadio, ElInput, ElButton } from 'element-plus';
import SettingItem from '@/components/SettingItem.vue';
import { useConfigStore } from '@/stores';

const config = useConfigStore();
</script>

<template>
    <h1>设置</h1>
    <el-scrollbar class="content" :always="true">
        <SettingItem label="用户名">
            <el-input v-model="config.user_name" placeholder="请输入用户名" />
        </SettingItem>
        <SettingItem label="主题">
            <el-radio-group v-model="config.theme">
                <el-radio value="light">亮色</el-radio>
                <el-radio value="dark">暗色</el-radio>
                <el-radio value="auto">自动</el-radio>
            </el-radio-group>
        </SettingItem>
        <SettingItem label="危险操作">
            <el-button type="danger" @click="$router.push('/'); config.init = false">重新初始化</el-button>
        </SettingItem>
    </el-scrollbar>
</template>

<style scoped>
.content {
    height: 80vh;
}
</style>
