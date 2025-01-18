<script setup lang="ts">
import { ElScrollbar, ElRadioGroup, ElRadio } from 'element-plus';
import SettingItem from '@/components/SettingItem.vue';
import { useConfigStore } from '@/stores';

const config = useConfigStore();
</script>

<template>
    <h1>设置</h1>
    <el-scrollbar class="content" :always="true">
        <SettingItem label="主题">
            <el-radio-group v-model="config.theme">
                <el-radio value="light">亮色</el-radio>
                <el-radio value="dark">暗色</el-radio>
                <el-radio value="auto">自动</el-radio>
            </el-radio-group>
        </SettingItem>
    </el-scrollbar>
</template>

<style scoped>
.content {
    height: 80vh;
}
</style>
