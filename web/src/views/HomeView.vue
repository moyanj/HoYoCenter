<script setup lang="ts">
import { useConfigStore } from '@/stores';
import { ElCard } from 'element-plus';
const configrStore = useConfigStore();
</script>

<template>
    <h1>你好，{{ configrStore.user_name }}！</h1>
    <br>
    <el-card>1212</el-card>

</template>
