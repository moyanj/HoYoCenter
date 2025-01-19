<script setup lang="ts">
import { ElCard } from 'element-plus';
const props = defineProps<{ label: string }>()
</script>

<template>
    <el-card class="item">
        <div class="title"><span>{{ props.label }}</span></div>

        <slot></slot>
    </el-card>
</template>

<style scoped>
.item {
    --el-card-padding: 15px;
    --el-card-border-radius: 10px;
    margin-bottom: 12px;
}

.title {
    font-size: 18px;
    margin-bottom: 10px;
}
</style>