export interface BaseMiHoYo {
    retcode: number
    message: string
    data: object
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