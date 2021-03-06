# coding=utf-8

SITES = {
    '163': 'netease',
    '56': 'w56',
    'acfun': 'acfun',
    'archive': 'archive',
    'baidu': 'baidu',
    'bandcamp': 'bandcamp',
    'baomihua': 'baomihua',
    'bigthink': 'bigthink',
    'bilibili': 'bilibili',
    'cctv': 'cntv',
    'cntv': 'cntv',
    'cbs': 'cbs',
    'coub': 'coub',
    'dailymotion': 'dailymotion',
    'dilidili': 'dilidili',
    'douban': 'douban',
    'douyin': 'douyin',
    'douyu': 'douyutv',
    'ehow': 'ehow',
    'facebook': 'facebook',
    'fantasy': 'fantasy',
    'fc2': 'fc2video',
    'flickr': 'flickr',
    'freesound': 'freesound',
    'fun': 'funshion',
    'google': 'google',
    'giphy': 'giphy',
    'heavy-music': 'heavymusic',
    'huaban': 'huaban',
    'huomao': 'huomaotv',
    'iask': 'sina',
    'icourses': 'icourses',
    'ifeng': 'ifeng',
    'imgur': 'imgur',
    'in': 'alive',
    'infoq': 'infoq',
    'instagram': 'instagram',
    'interest': 'interest',
    'iqilu': 'iqilu',
    'iqiyi': 'iqiyi',
    'ixigua': 'ixigua',
    'isuntv': 'suntv',
    'joy': 'joy',
    'kankanews': 'bilibili',
    'khanacademy': 'khan',
    'ku6': 'ku6',
    'kuaishou': 'kuaishou',
    'kugou': 'kugou',
    'kuwo': 'kuwo',
    'le': 'le',
    'letv': 'le',
    'lizhi': 'lizhi',
    'magisto': 'magisto',
    'metacafe': 'metacafe',
    'mgtv': 'mgtv',
    'miomio': 'miomio',
    'mixcloud': 'mixcloud',
    'mtv81': 'mtv81',
    'musicplayon': 'musicplayon',
    'naver': 'naver',
    '7gogo': 'nanagogo',
    'nicovideo': 'nicovideo',
    'panda': 'panda',
    'pinterest': 'pinterest',
    'pixnet': 'pixnet',
    'pptv': 'pptv',
    'qingting': 'qingting',
    'qq': 'qq',
    'quanmin': 'quanmin',
    'showroom-live': 'showroom',
    'sina': 'sina',
    'smgbb': 'bilibili',
    'sohu': 'sohu',
    'soundcloud': 'soundcloud',
    'ted': 'ted',
    'theplatform': 'theplatform',
    'tucao': 'tucao',
    'tudou': 'tudou',
    'tumblr': 'tumblr',
    'twimg': 'twitter',
    'twitter': 'twitter',
    'ucas': 'ucas',
    'videomega': 'videomega',
    'vidto': 'vidto',
    'vimeo': 'vimeo',
    'wanmen': 'wanmen',
    'weibo': 'miaopai',
    'veoh': 'veoh',
    'vine': 'vine',
    'vk': 'vk',
    'xiami': 'xiami',
    'xiaokaxiu': 'yixia',
    'xiaojiadianvideo': 'fc2video',
    'ximalaya': 'ximalaya',
    'yinyuetai': 'yinyuetai',
    'miaopai': 'yixia',
    'yizhibo': 'yizhibo',
    'youku': 'youku',
    'iwara': 'iwara',
    'youtu': 'youtube',
    'youtube': 'youtube',
    'zhanqi': 'zhanqi',
    '365yg': 'toutiao',
}

FAKE_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  # noqa
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',  # noqa
}

FAKE_HEADERS_MOBILE = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  # noqa
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',  # noqa
}

# netease
NETEASE_MP3_URL = (
    'http://music.163.com/weapi/song/enhance/player/url?csrf_token='
)
NETEASE_MUSIC_PUBKEY = '010001'
NETEASE_MUSIC_SECKEY = 16 * 'F'
NETEASE_MUSIC_COMMENT_MODULE = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'  # noqa
