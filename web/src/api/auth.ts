import { MiHoYoApi } from "@/model/endpoint";
import { rpc } from "@/api/rpc";
import { type LtokenByLoginTicketModel, type GenerateQrcodeModel, type QrCheckModel } from "@/model/mihoyo";
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

export async function generate_qrcode_url(): Promise<{ url: string, ticket: string }> {
    let url = "https://passport-api.miyoushe.com/account/ma-cn-passport/web/createQRLogin"
    let res = await rpc.call("requests.post", {
        "url": url,
        "headers": {
            "x-rpc-app_id": "bll8iq97cem8",
            "x-rpc-device_id": uuidv4(),
        }
    })


    let result = res.json as GenerateQrcodeModel;
    return result.data;
}

export async function check_qrcode_status(ticket: string): Promise<QrCheckModel> {
    let url = "https://passport-api.miyoushe.com/account/ma-cn-passport/web/queryQRLoginStatus"
    let res = await rpc.call("requests.post", {
        "url": url,
        "headers": {
            "x-rpc-app_id": "bll8iq97cem8",
            "x-rpc-device_id": uuidv4(),
        },
        "data": {
            "ticket": ticket
        }
    })


    let result = res.json as QrCheckModel;
    return result;

}