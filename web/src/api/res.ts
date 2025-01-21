var sr_character_info_cache: null | object = null;

export async function get_ys_character_info(id: number) {
    let res = await fetch("/resources/Genshin/Infomation/Avatar/" + id + ".json");
    if (res.ok) {
        return await res.json();
    } else {
        return null;
    }
}

export async function get_sr_character_info(id: number) {
    if (sr_character_info_cache === null) {
        let res = await fetch("/resources/StarRail/Infomation/Avatar/AvatarInfo.json");
        sr_character_info_cache = await res.json();
    }
    // @ts-ignore
    return sr_character_info_cache[id];

}