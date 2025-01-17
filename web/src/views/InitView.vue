<script setup lang="ts">
import { ref } from "vue";
import { rpc } from "@/rpc";
import { ElButton } from "element-plus";

const step = ref(0);
</script>

<template>
    <div class="init-view">
        <div v-if="step === 0">
            <h1>欢迎使用HoYoCenter</h1>
            <el-button @click="step = 1">开始</el-button>
        </div>
    </div>
</template>
<style scoped>
.init-view {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
}
</style>