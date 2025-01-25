export type EnkaYsInfo = {
    playerInfo: {
        nickname: string;
        level: number;
        signature: string;
        worldLevel: number;
        nameCardId: number;
        finishAchievementNum: number;
        towerFloorIndex: number;
        towerLevelIndex: number;
        showAvatarInfoList: {
            avatarId: number;
            level: number;
            energyType: number;
            costumeId?: number; // 可选字段
        }[];
        showNameCardIdList: number[];
        profilePicture: {
            id: number;
        };
    };
    ttl: number;
    uid: string;
    avatarInfoList: {
        avatarId: number;
        propMap: {
            [key: string]: {
                type: number;
                ival: string;
                val?: string;
            };
        };
        fightPropMap: {
            [key: string]: number;
        };
        skillDepotId: number;
        inherentProudSkillList: number[];
        skillLevelMap: {
            [key: string]: number;
        };
        equipList: {
            itemId: number;
            reliquary?: {
                level: number;
                exp?: number;
                mainPropId: number;
                appendPropIdList: number[];
            };
            flat: {
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
            };
            weapon?: {
                level: number;
                promoteLevel: number;
                affixMap: {
                    [key: string]: number;
                };
            };
        }[];
        fetterInfo: {
            expLevel: number;
        };
        talentIdList?: number[];
        proudSkillExtraLevelMap?: {
            [key: string]: number;
        };
        costumeId?: number;
    }[];
};

export type EnkaSrInfo = {
    detailInfo: {
        worldLevel: number;
        privacySettingInfo: {
            displayCollection: boolean;
            displayRecord: boolean;
            displayRecordTeam: boolean;
            displayOnlineStatus: boolean;
            displayDiary: boolean;
        };
        headIcon: number;
        avatarDetailList: Array<{
            pos?: number;
            relicList: Array<{
                exp?: number;
                mainAffixId: number;
                subAffixList: Array<{
                    affixId: number;
                    cnt: number;
                    step?: number;
                }>;
                tid: number;
                type: number;
                level: number;
                _flat: {
                    props: Array<{
                        type: string;
                        value: number;
                    }>;
                    setName: number;
                    setID: number;
                };
            }>;
            level: number;
            promotion: number;
            skillTreeList: Array<{
                pointId: number;
                level: number;
            }>;
            equipment: {
                rank: number;
                tid: number;
                promotion: number;
                level: number;
                _flat: {
                    props: Array<{
                        type: string;
                        value: number;
                    }>;
                    name: number;
                };
            };
            avatarId: number;
            _assist: boolean;
        }>;
        platform: string;
        recordInfo: {
            achievementCount: number;
            bookCount: number;
            avatarCount: number;
            equipmentCount: number;
            musicCount: number;
            relicCount: number;
            challengeInfo: Record<string, unknown>;
            maxRogueChallengeScore: number;
        };
        uid: number;
        level: number;
        nickname: string;
        isDisplayAvatar: boolean;
        friendCount: number;
    };
    ttl: number;
    uid: string;
};