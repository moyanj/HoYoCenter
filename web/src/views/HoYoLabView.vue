<script setup lang="ts">
import { ref } from "vue";
import { ElRadioGroup, ElRadioButton } from "element-plus";

const url = ref("https://www.miyoushe.com/ys");
</script>

<template>
    <el-radio-group v-model="url" class="sel">
        <el-radio-button label="https://www.miyoushe.com/ys">原神</el-radio-button>
        <el-radio-button label="https://www.miyoushe.com/sr">星铁</el-radio-button>
        <el-radio-button label="https://www.miyoushe.com/bh3">崩坏三</el-radio-button>
        <el-radio-button label="https://www.miyoushe.com/zzz">绝区零</el-radio-button>
    </el-radio-group>
    <iframe :src="url" frameborder="0" width="100%" height="100%" class="if"></iframe>
</template>

<style scoped>
.sel {
    margin-bottom: 10px;
}

.if {
    width: 100%;
    height: 87.5vh;
    overflow-y: hidden;
}
</style>