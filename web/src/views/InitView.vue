<script setup lang="ts">
import { ref } from "vue";
import { rpc } from "@/rpc";
import { useConfigStore } from "@/stores";
import { ElButton, ElCard, ElCheckbox, ElImage } from "element-plus";
import { ta } from "element-plus/es/locales.mjs";

const step = ref(0);
const config = useConfigStore();

function add_game(event: MouseEvent) {
    const target = event.target as HTMLElement;
    var game:string = target.id;
    
    if (game == "") {
        var game = target.parentElement?.id as string;
    }
    
    if (target.classList.contains("disabled")) {
        return;
    }
    if (game == "ys") {
        if (config.game.ys.enable) {
            config.game.ys.enable = false;
        } else {
            config.game.ys.enable = true;
        }
        
    } else if (game == "sr") {
        if (config.game.sr.enable) {
            config.game.sr.enable = false;
        } else {
            config.game.sr.enable = true;
        }
    } else if (game == "zzz") {
        if (config.game.zzz.enable) {
            config.game.zzz.enable = false;
        } else {
            config.game.zzz.enable = true;
        }
    }
}
</script>

<template>
    <el-card class="init-view">
        <div v-if="step === 0">
            <h1>欢迎使用HoYoCenter</h1>
            <el-button @click="step = 1">开始</el-button>
        </div>
        <div v-if="step === 1">
            <h1>请勾选需要的游戏</h1>
            <div class="game-list">
                <el-card class="game-card" :class="{ 'is-selected': config.game.ys.enable }" @click="add_game"><el-image src="/imgs/game-ys.jpg" id="ys"/></el-card>
                <el-card class="game-card" :class="{ 'is-selected': config.game.sr.enable }" @click="add_game"><el-image src="/imgs/game-sr.jpg" id="sr"/></el-card>
                <el-card class="game-card" :class="{ 'is-selected': config.game.zzz.enable }" @click="add_game"><el-image src="/imgs/game-zzz.png" id="zzz"/></el-card>
            </div>
            <br>
            <el-button @click="step = -1">下一步</el-button>
        </div>
        <div v-if="step === -1">
            <h1>完成！</h1>
            <el-button @click="config.init= true">关闭</el-button>
        </div>
    </el-card>
</template>
<style scoped>
.init-view {
    height: 350px;
    width: 400px;
    --el-card-padding: 15px;
}

.game-card {
    height: 100px;
    width: 100px;
    --el-card-padding: 0;
}

.game-list {
    display: flex;
    flex-wrap: wrap;
    gap: 27px;
}

.game-card.is-selected {
    border: 2px solid #409eff;
}

.game-card.disabled {
    opacity: 0.5;
}
</style>