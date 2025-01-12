<script setup lang="ts">
import { useConfigStore } from '@/stores';
const configrStore = useConfigStore();
</script>

<template>
    <h1>你好，{{ configrStore.user_name }}！</h1>
</template>
