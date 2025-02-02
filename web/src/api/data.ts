import { useConfigStore } from "@/stores";
import { rpc } from "./rpc";
import { ThirdApi } from "./model/endpoint";
import { type EnkaYsInfo, type EnkaSrInfo } from "./model/enka";
import { type GenshinData } from "./model/game_data";
import { ElLoading } from 'element-plus'

async function get_genshin_data_by_enka(): Promise<GenshinData> {
    const config = useConfigStore();
    var rep = await rpc.call("requests.get", [ThirdApi.YsDataApiMap[config.enka.ys] + config.game.ys.uid]);
    var data: EnkaYsInfo = rep.json;
    return {
        nickname: data.playerInfo.nickname,
        level: data.playerInfo.level,
        worldLevel: data.playerInfo.worldLevel,
        signature: data.playerInfo.signature,
        profilePictureID: data.playerInfo.profilePicture.id,
        abyss: {
            floor: data.playerInfo.towerFloorIndex,
            level: data.playerInfo.towerLevelIndex,
        },
        avatarList: data.playerInfo.showAvatarInfoList.map(avatar => ({
            id: avatar.avatarId,
            level: avatar.level,
        })),
    };
}

export async function get_genshin_data() {
    const config = useConfigStore();
    if (config.use_enka) {
        ElLoading.service({
            lock: true,
            text: '正在获取数据...',
            background: 'rgba(0, 0, 0, 0.7)',
        });
        var rep = await get_genshin_data_by_enka();
        ElLoading.service().close();
        return rep;
    }
}

async function get_sr_data_by_enka(): Promise<GenshinData> {
    const config = useConfigStore();
    var rep = await rpc.call("requests.get", [ThirdApi.SrDataApiMap[config.enka.sr] + config.game.sr.uid]);
    var data: EnkaSrInfo = rep.json;
    return {
        nickname: data.detailInfo.nickname,
        level: data.detailInfo.level,
        worldLevel: data.detailInfo.worldLevel,
        signature: data.detailInfo.nickname,
        profilePictureID: data.detailInfo.headIcon,
        abyss: {
            floor: -1,
            level: -1,
        },
        avatarList: data.detailInfo.avatarDetailList.map(avatar => ({
            id: avatar.avatarId,
            level: avatar.level,
        })),
    }
}

export async function get_sr_data() {
    const config = useConfigStore();
    if (config.use_enka) {
        ElLoading.service({
            lock: true,
            text: '正在获取数据...',
            background: 'rgba(0, 0, 0, 0.7)',
        });
        var rep = await get_sr_data_by_enka();
        ElLoading.service().close();
        return rep;
    }
}