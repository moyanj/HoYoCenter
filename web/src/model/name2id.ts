import sr from "@/assets/name2id/sr.json";
import ys from "@/assets/name2id/ys.json";

export function get_id_sr(name: string) {
    if (name in sr) {
        // @ts-ignore
        return sr[name];
    } else {
        return -1;
    }
}

export function get_id_ys(name: string) {
    if (name in ys) {
        // @ts-ignore
        return ys[name];
    } else {
        return -1;
    }
}