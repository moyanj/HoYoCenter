export class MiHoYoApi {
    static readonly ApiGeetest = "https://api.geetest.com";
    static readonly ApiV6Geetest = "https://apiv6.geetest.com";

    static readonly ApiTakumi = "https://api-takumi.mihoyo.com";
    static readonly ApiTakumiAuthApi = `${MiHoYoApi.ApiTakumi}/auth/api`;
    static readonly ApiTakumiBindingApi = `${MiHoYoApi.ApiTakumi}/binding/api`;
    static readonly ApiTakumiRecord = "https://api-takumi-record.mihoyo.com";
    static readonly ApiTakumiCardApi = `${MiHoYoApi.ApiTakumiRecord}/game_record/app/card/api`;
    static readonly ApiTakumiCardWApi = `${MiHoYoApi.ApiTakumiRecord}/game_record/app/card/wapi`;
    static readonly ApiTakumiEvent = `${MiHoYoApi.ApiTakumi}/event`;
    static readonly ApiTakumiEventCalculate = `${MiHoYoApi.ApiTakumiEvent}/e20200928calculate`;
    static readonly ApiTakumiRecordApi = `${MiHoYoApi.ApiTakumiRecord}/game_record/app/genshin/api`;
    static readonly ApiTakumiRecordAapi = `${MiHoYoApi.ApiTakumiRecord}/game_record/app/genshin/aapi`;

    static readonly AppMihoyoReferer = "https://app.mihoyo.com";
    static readonly AppAuthApi = `${MiHoYoApi.AppMihoyoReferer}/account/auth/api`;

    static readonly BbsApi = "https://bbs-api.mihoyo.com";
    static readonly BbsApiUserApi = `${MiHoYoApi.BbsApi}/user/wapi`;

    static readonly Hk4eApi = "https://hk4e-api.mihoyo.com";
    static readonly Hk4eApiAnnouncementApi = `${MiHoYoApi.Hk4eApi}/common/hk4e_cn/announcement/api`;
    static readonly Hk4eApiGachaInfoApi = `${MiHoYoApi.Hk4eApi}/event/gacha_info/api`;

    static readonly PassportApi = "https://passport-api.mihoyo.com";
    static readonly PassportApiAuthApi = `${MiHoYoApi.PassportApi}/account/auth/api`;
    static readonly PassportApiV4 = "https://passport-api-v4.mihoyo.com";

    static readonly SdkStatic = "https://sdk-static.mihoyo.com";
    static readonly SdkStaticLauncherApi = `${MiHoYoApi.SdkStatic}/hk4e_cn/mdk/launcher/api`;
    static readonly WebStaticMihoyoReferer = "https://webstatic.mihoyo.com";

    static readonly LauncherApi = "https://sdk-static.mihoyo.com/hk4e_cn/mdk/launcher/api";
    static readonly LauncherContentApi = `${MiHoYoApi.LauncherApi}/content`;
    static readonly LauncherResourceApi = `${MiHoYoApi.LauncherApi}/resource`;

    static readonly LauncherApi_sr = "https://api-launcher.mihoyo.com/hkrpg_cn/mdk/launcher/api";
    static readonly LauncherContentApi_sr = `${MiHoYoApi.LauncherApi_sr}/content`;
    static readonly LauncherResourceApi_sr = `${MiHoYoApi.LauncherApi_sr}/resource`;

    static readonly AnnouncementQuery = "game=hk4e&game_biz=hk4e_cn&lang=zh-cn&bundle_id=hk4e_cn&platform=pc&region=cn_gf01&level=55&uid=100000000";
}

export class ThirdApi {
    static readonly HuTaoApi = "https://homa.snapgenshin.com";
    static readonly HuTaoRecordApi = `${ThirdApi.HuTaoApi}/Record`;
    static readonly HuTaoStatisticsApi = `${ThirdApi.HuTaoApi}/Statistics`;
    static readonly HuTaoStatisticsWeaponApi = `${ThirdApi.HuTaoStatisticsApi}/Weapon`;
    static readonly HuTaoStatisticsTeamApi = `${ThirdApi.HuTaoStatisticsApi}/Team`;
    static readonly HuTaoStatisticsAvatarApi = `${ThirdApi.HuTaoStatisticsApi}/Avatar`;

    static readonly EnkaApi = "https://enka.network/api/uid/"
    static readonly MicroGGEnka = "https://profile.microgg.cn/api/uid/"

    static readonly EnkaSRAPI = "https://enka.network/api/hsr/uid/"
    static readonly AvocadoApi = "https://avocado.wiki/v1/raw/info/"
    static readonly MiHoMoSRApi = "https://api.mihomo.me/sr_info/"

    static readonly YsDataApiMap = {
        "enka": ThirdApi.EnkaApi,
        "microgg": ThirdApi.MicroGGEnka,
    }
    static readonly SrDataApiMap = {
        "enka": ThirdApi.EnkaSRAPI,
        "avocado": ThirdApi.AvocadoApi,
        "mihomo": ThirdApi.MiHoMoSRApi,
    }
}
