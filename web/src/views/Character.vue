<script setup lang="ts">
import { ElSelect, ElOption, ElRow, ElCol } from 'element-plus';
import { useConfigStore } from '@/stores';
import { get_genshin_data } from '@/api/data';
import CharacterCard from '@/components/CharacterCard.vue';
import { ref, watch } from 'vue';

const config = useConfigStore();
const game = ref('ys');

const data = ref();

watch(game, async (newValue, oldValue) => {
    if (newValue === 'ys') {
        data.value = await get_genshin_data();
    } else {
        data.value = config.game.sr;
    }
}, {
    immediate: true
});
</script>

<template>
    <el-row :gutter="16">
        <el-col :span="6">
            <el-select v-model="game" placeholder="请选择游戏" class="sel">
                <el-option label="原神" value="ys" key="ys"></el-option>
                <el-option label="崩坏：星穹铁道" value="sr" key="sr"></el-option>
            </el-select>
        </el-col>
        <el-col :span="3">
            <a>{{ data?.nickname }}</a>
        </el-col>
        <el-col :span="3">
            <a>UID: {{ game === "ys" ? config.game.ys.uid : config.game.sr.uid }}</a>
        </el-col>
    </el-row>
    <br>
    <el-row :gutter="16">
        <el-col :span="3" v-for="c in data?.avatarList">
            <character-card :game="game" :character="c.id"></character-card>
        </el-col>
    </el-row>
</template>

<style scoped>
.sel {
    width: 100%;
    margin-right: 20px;
}
</style>