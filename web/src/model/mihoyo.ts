export interface BaseMiHoYo {
    retcode: number
    message: string
    data: object | null
}

export interface LtokenByLoginTicketModel extends BaseMiHoYo {
    data: {
        list: [
            {
                name: string
                token: string
            }
        ]
    }
}

export interface GenerateQrcodeModel extends BaseMiHoYo {
    data: {
        url: string;
        ticket: string;
    }
}

interface QrCheckUserInfo {
    aid: string;
    mid: string;
    // 其他可能的属性
    [key: string]: any;
}

interface QrCheckRealnameInfo {
    required: boolean;
    action_type: string;
    action_ticket: string;
}

interface QrCheckCreatedScanned {
    status: 'Created' | 'Scanned';
    app_id: string;
    client_type: number;
    created_at: string;
    scanned_at: string;
    tokens: string[];
    user_info: null;
    realname_info: null;
    need_realperson: boolean;
}

interface QrCheckConfirmed {
    status: 'Confirmed';
    app_id: string;
    client_type: number;
    created_at: string;
    scanned_at: string;
    tokens: string[];
    user_info: QrCheckUserInfo;
    realname_info: QrCheckRealnameInfo;
    need_realperson: boolean;
}

export interface QrCheckModel extends BaseMiHoYo {
    data: QrCheckCreatedScanned | QrCheckConfirmed | null;
}