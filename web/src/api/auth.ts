import { MiHoYoApi } from "@/api/model/endpoint";
import { rpc, type Response } from "@/api/rpc";
import { type LtokenByLoginTicketModel, type GenerateQrcodeModel, type QrCheckModel } from "@/api/model/mihoyo";
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

export async function generate_qrcode_url(): Promise<{ url: string, ticket: string, device_id: string }> {
    let url = "https://passport-api.miyoushe.com/account/ma-cn-passport/web/createQRLogin"
    var device_id = uuidv4();
    let res = await rpc.call("requests.post", {
        "url": url,
        "headers": {
            "x-rpc-app_id": "bll8iq97cem8",
            "x-rpc-device_id": device_id,
            "User-Agent": "okhttp/4.9.3",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-rpc-game_biz": "bbs_cn",
            "x-rpc-sys_version": "12",
            "x-rpc-device_name": "Xiaomi MI 6",
            "x-rpc-device_model": "MI 6",
        }
    })


    let result = res.json as GenerateQrcodeModel;
    return {
        "url": result.data.url,
        "ticket": result.data.ticket,
        "device_id": device_id
    };
}

export async function check_qrcode_status(ticket: string, device_id: string): Promise<Response> {
    let url = "https://passport-api.miyoushe.com/account/ma-cn-passport/web/queryQRLoginStatus"
    let res = await rpc.call("requests.post", {
        "url": url,
        "headers": {
            "x-rpc-app_id": "bll8iq97cem8",
            "x-rpc-device_id": device_id,
            "User-Agent": "okhttp/4.9.3",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-rpc-game_biz": "bbs_cn",
            "x-rpc-sys_version": "12",
            "x-rpc-device_name": "Xiaomi MI 6",
            "x-rpc-device_model": "MI 6",
        },
        "data": {
            "ticket": ticket
        }
    })

    console.log(res);
    let result = res;
    return result;

}