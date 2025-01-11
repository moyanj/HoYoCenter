<script setup lang="ts">
import { useConfigrStore } from '@/stores';
const configrStore = useConfigrStore();
</script>

<template>
    <h1>你好，{{ configrStore.user_name }}！</h1>
</template>
