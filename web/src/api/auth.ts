import { MiHoYoApi } from "@/model/endpoint";
import { rpc } from "@/api/rpc";
import { type LtokenByLoginTicketModel, type GenerateHk4eQrcodeModel } from "@/model/mihoyo";
import { obj2params, uuidv4 } from "@/utils";

export async function get_ltoken_by_login_ticket(login_ticket: string, uid: string): Promise<string> {
    let param = {
        login_ticket: login_ticket,
        uid: uid,
        token_types: 2
    }
    let url = MiHoYoApi.ApiTakumiAuthApi + "/getMultiTokenByLoginTicket?" + obj2params(param);
    let res = (await rpc.call("requests.get", [url])).json as LtokenByLoginTicketModel;
    let data = res.data;
    return data.list[0].token;
}

export async function generate_hk4e_qrcode_url(): Promise<string> {
    let url = "https://hk4e-sdk.mihoyo.com/hk4e_cn/combo/panda/qrcode/fetch"
    let res = await rpc.call("requests.post", {
        "url": url,
        "data": {
            "app_id": "8",
            "device": uuidv4(),
        }
    })


    let result = res.json as GenerateHk4eQrcodeModel;
    return result.data.url;
}