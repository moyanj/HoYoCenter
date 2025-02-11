<script setup lang="ts">
import { ElScrollbar, ElRadioGroup, ElRadio, ElInput, ElButton, ElMessageBox } from 'element-plus';
import SettingItem from '@/components/SettingItem.vue';
import { useConfigStore } from '@/stores';
import { rpc } from '@/api/rpc';
import { ref, type Ref } from 'vue';
import { useRouter } from 'vue-router';

const config = useConfigStore();
const build_info: Ref<any> = ref({});
const router = useRouter();

const confirmReset = () => {
    ElMessageBox.confirm('此操作将重新初始化配置，所有设置将恢复到默认值。是否继续?', '警告', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
    }).then(() => {
        router.push('/');
        config.$reset();
    }).catch(() => {
        // 取消操作
    });
};


rpc.call("data.build_info").then((data) => {
    build_info.value = data;
}).catch((error) => {
    ElMessageBox.alert('获取构建信息失败，请检查网络连接或联系管理员。', '错误', {
        type: 'error',
    });
});
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
        <SettingItem label="原神数据API" v-if="config.use_enka && config.game.ys.enable">
            <el-radio-group v-model="config.enka.ys">
                <el-radio value="enka">Enka</el-radio>
                <el-radio value="microgg">MicroGG</el-radio>
            </el-radio-group>
        </SettingItem>
        <SettingItem label="崩坏：星穹铁道数据API" v-if="config.use_enka && config.game.sr.enable">
            <el-radio-group v-model="config.enka.sr">
                <el-radio value="enka">Enka</el-radio>
                <el-radio value="avocado">Avocado</el-radio>
                <el-radio value="mihomo">MiHoMo</el-radio>
            </el-radio-group>
        </SettingItem>
        <SettingItem label="关于">
            <a>v{{ build_info.version || '未知' }} | {{ build_info.branch || 'main' }}-{{ build_info.commit || '未知'
                }}</a><br>
            <a>构建时间: {{ build_info.build_time || '未知' }}</a>
        </SettingItem>
        <SettingItem label="危险操作">
            <el-button type="danger" @click="confirmReset">重新初始化</el-button>
        </SettingItem>
    </el-scrollbar>
</template>

<style scoped>
.content {
    height: 80vh;
}
</style>