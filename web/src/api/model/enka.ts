type AvatarInfo = {
    avatarId: number;
    level: number;
    energyType: number;
    costumeId?: number; // 可选字段
};

// 定义玩家信息类型
type PlayerInfo = {
    nickname: string;
    level: number;
    signature: string;
    worldLevel: number;
    nameCardId: number;
    finishAchievementNum: number;
    towerFloorIndex: number;
    towerLevelIndex: number;
    showAvatarInfoList: AvatarInfo[];
    showNameCardIdList: number[];
    profilePicture: {
        id: number;
    };
};

type Prop = {
    type: number;
    ival: string;
    val?: string;
}

type FightPropMap = {
    [key: string]: number;
}

type Reliquary = {
    level: number;
    exp?: number;
    mainPropId: number;
    appendPropIdList: number[];
}

type Flat = {
    nameTextMapHash: string;
    rankLevel: number;
    itemType: string;
    icon: string;
    equipType: string;
    setNameTextMapHash: string;
    reliquarySubstats?: {
        appendPropId: string;
        statValue: number;
    }[];
    reliquaryMainstat?: {
        mainPropId: string;
        statValue: number;
    };
    weaponStats?: {
        appendPropId: string;
        statValue: number;
    }[];
}

type Equip = {
    itemId: number;
    reliquary?: Reliquary;
    flat: Flat;
    weapon?: {
        level: number;
        promoteLevel: number;
        affixMap: {
            [key: string]: number;
        }
    }
}

type FetterInfo = {
    expLevel: number;
}

type Avatar = {
    avatarId: number;
    propMap: {
        [key: string]: Prop;
    };
    fightPropMap: FightPropMap;
    skillDepotId: number;
    inherentProudSkillList: number[];
    skillLevelMap: {
        [key: string]: number;
    };
    equipList: Equip[];
    fetterInfo: FetterInfo;
    talentIdList?: number[];
    proudSkillExtraLevelMap?: {
        [key: string]: number;
    };
    costumeId?: number;
}

export interface EnkaYsInfo {
    playerInfo: PlayerInfo;
    ttl: number;
    uid: string;
    avatarInfoList: Avatar[];
}