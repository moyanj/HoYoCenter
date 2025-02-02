<script setup lang="ts">
import { ElSelect, ElOption, ElRow, ElCol, ElDialog } from 'element-plus';
import { useConfigStore } from '@/stores';
import { get_genshin_data, get_sr_data } from '@/api/data';
import { get_ys_character_info, get_sr_character_info } from '@/api/res';
import CharacterCard from '@/components/CharacterCard.vue';
import { ref, watch } from 'vue';

const config = useConfigStore();
const game = ref('ys');
const show_character_dialog = ref(false);
const data = ref();
const character_info = ref();

watch(game, async (newValue, oldValue) => {
    if (newValue === 'ys') {
        data.value = await get_genshin_data();
    } else if (newValue === 'sr') {
        data.value = await get_sr_data();
    }
}, {
    immediate: true
});

function show_character(id: number) {
    if (game.value === 'ys') {
        get_ys_character_info(id).then(res => {
            character_info.value = res;
            show_character_dialog.value = true;
        });
    } else if (game.value === 'sr') {
        get_sr_character_info(id).then(res => {
            character_info.value = res;
            show_character_dialog.value = true;
        });
    }
}
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
    <el-row :gutter="12">
        <el-col :span="3" v-for="c in data?.avatarList">
            <character-card :game="game" :character="c.id" @click="show_character(c.id)"></character-card>
        </el-col>
    </el-row>

    <el-dialog v-model="show_character_dialog" title="角色详情" width="50%">
        <div v-if="game === 'ys'">
            {{ character_info?.Name }}
        </div>
        <div v-if="game === 'sr'">
            <h3>{{ character_info?.name === "{NICKNAME}" ? data.nickname : character_info?.name }}</h3>
        </div>
    </el-dialog>
</template>

<style scoped>
.sel {
    width: 100%;
    margin-right: 20px;
}
</style>