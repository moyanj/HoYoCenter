<script setup lang="ts">
import { ref, type Ref } from "vue";
import { useConfigStore } from "@/stores";
import QrcodeVue from "qrcode.vue";
import { ElButton, ElCard, ElInput, ElImage, ElMessage } from "element-plus";
import { parseCookies } from "@/utils";
import { get_ltoken_by_login_ticket, generate_qrcode_url, check_qrcode_status } from "@/api/auth";

const step: Ref<number> = ref(0);
const ck: Ref<string> = ref("");
const config = useConfigStore();
const qr_code_url = ref("");
var qr_ticket = "";

function add_game(event: MouseEvent) {
    const target = event.target as HTMLElement;
    var game: string = target.id;

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
    }
}

async function analyze_ck() {
    const ck_obj = parseCookies(ck.value);
    let login_ticket = "";
    const uid_key = ["account_id", "ltuid", "ltuid_v2", "account_id_v2", "login_uid"];
    const mid_key = ["account_mid_v2", "ltmid_v2"];

    for (const key of uid_key) {
        if (ck_obj[key] !== undefined) {
            config.user.uid = ck_obj[key];
            break;
        } else {
            alert("未在cookie中找到UID");
            return;
        }
    }

    for (const key of mid_key) {
        if (ck_obj[key] !== undefined) {
            config.user.mid = ck_obj[key];
            break;
        } else {
            alert("未在cookie中找到mid");
            return;
        }
    }

    if (ck_obj["cookie_token"] !== undefined) {
        config.user.cookie_token = ck_obj["cookie_token"];
    } else {
        alert("未在cookie中找到cookie_token");
        return;
    }

    if (ck_obj["login_ticket"] !== undefined) {
        login_ticket = ck_obj["login_ticket"];
    } else {
        alert("未在cookie中找到login_ticket");
        return;
    }
    config.user.ltoken_v1 = await get_ltoken_by_login_ticket(login_ticket, config.user.uid);

    step.value = -1;
}

async function check_qr() {
    if (step.value !== 5) {
        return;
    }
    let qr_info = await check_qrcode_status(qr_ticket);
    console.log(qr_info);
    if (qr_info.retcode === -3501) {
        ElMessage.error("二维码已失效，请重新扫码");
        login_by_qr();
    } else if (qr_info.retcode === -3505) {
        ElMessage.error("扫码登录已取消，请重新扫码");
        login_by_qr();
    } else if (qr_info.retcode === 0) {
        if (qr_info.data?.status === "Confirmed") {
            console.log(qr_info)
        } else {
            setTimeout(check_qr, 1000);
        }
    } else {
        setTimeout(check_qr, 1000);
    }
}

async function login_by_qr() {
    const qr_info = await generate_qrcode_url();
    qr_code_url.value = qr_info.url;
    qr_ticket = qr_info.ticket;
    setTimeout(check_qr, 1000);
    step.value = 5;
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
                <el-card class="game-card" :class="{ 'is-selected': config.game.ys.enable }" @click="add_game"><el-image
                        src="/imgs/game-ys.jpg" id="ys" /></el-card>
                <el-card class="game-card" :class="{ 'is-selected': config.game.sr.enable }" @click="add_game"><el-image
                        src="/imgs/game-sr.jpg" id="sr" /></el-card>
            </div>
            <br>
            <el-button @click="step = 2">下一步</el-button>
        </div>
        <div v-if="step === 2">
            <h1>请选择登录方式</h1>
            <el-button @click="step = 3">游戏UID(仅支持查看展柜角色)</el-button>
            <el-button @click="step = 4">米游社账户</el-button>
        </div>
        <div v-if="step === 3">
            <h1>请输入游戏UID</h1>
            <el-input v-model="config.game.ys.uid" placeholder="请输入原神UID" v-if="config.game.ys.enable"></el-input>
            <el-input v-model="config.game.sr.uid" placeholder="请输入崩坏：星穹铁道UID" v-if="config.game.sr.enable"></el-input>
            <el-button @click="step = -1">完成</el-button>
        </div>
        <div v-if="step === 4">
            <h1>请选择米游社登录方式</h1>
            <el-button @click="login_by_qr()">使用米游社扫码</el-button>
            <el-button @click="step = 6">手动输入Cookie</el-button>

        </div>
        <div v-if="step === 5">
            <h1>请使用米游社扫码登录</h1>
            <qrcode-vue :value="qr_code_url" :size="200"></qrcode-vue>
            <br>
            <el-button @click="step = -1">完成</el-button>
        </div>
        <div v-if="step === 6">
            <h1>请输入Cookie</h1>
            <el-input v-model="ck" placeholder="请输入Cookie" type="textarea" :rows="3"></el-input>
            <br>
            <br>
            <el-button @click="analyze_ck()">完成</el-button>
        </div>
        <div v-if="step === -1">
            <h1>完成！</h1>
            <el-button @click="config.init = true">关闭</el-button>
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

.el-buttton {
    margin-right: 10px;
}

.el-input {
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>