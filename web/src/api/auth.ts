import { MiHoYoApi } from "@/model/endpoint";
import { rpc } from "@/api/rpc";
import { type LtokenByLoginTicketModel } from "@/model/mihoyo";
import { obj2params } from "@/utils";

export async function get_ltoken_by_login_ticket(login_ticket: string, uid: string): Promise<string> {
    let param = {
        login_ticket: login_ticket,
        uid: uid,
        token_types: 2
    }
    let url = MiHoYoApi.ApiTakumiAuthApi + "/getMultiTokenByLoginTicket?" + obj2params(param);
    let res = (await rpc.call("requests.get", [url])) as LtokenByLoginTicketModel;
    let data = res.data;
    return data.list[0].token;
}