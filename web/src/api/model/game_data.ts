export type GenshinData = {
    nickname: string;
    level: number;
    worldLevel: number;
    signature: string;
    profilePictureID: number;
    abyss: {
        floor: number;
        level: number;
    };
    avatarList: {
        id: number;
        level: number;
    }[];
}