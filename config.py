from typing import NamedTuple

# 调试模式
debug = False

# 全国大学top200
top_college_china = '北京大学|清华大学|复旦大学|浙江大学|南京大学|上海交通大学|华中科技大学|中国科学技术大学|中国人民大学|天津大学|武汉大学|南开大学|山东大学|中山大学|西安交通大学|哈尔滨工业大学|东南大学|四川大学|吉林大学|同济大学|北京航空航天大学|北京师范大学|厦门大学|西北工业大学|中南大学|东北大学|湖南大学|大连理工大学|华南理工大学|北京理工大学|兰州大学|华东师范大学|中国农业大学|电子科技大学|重庆大学|华中农业大学|河海大学|南京农业大学|华中师范大学|郑州大学|中国海洋大学|西安电子科技大学|北京科技大学|南京理工大学|北京交通大学|华东理工大学|北京邮电大学|合肥工业大学|南昌大学|南京航空航天大学|武汉理工大学|西南交通大学|暨南大学|西南大学|西北农林科技大学|东华大学|西北大学|中南财经政法大学|苏州大学|北京化工大学|昆明理工大学|南京师范大学|上海财经大学|湖南师范大学|云南大学|上海大学|哈尔滨工程大学|福州大学|河南大学|华南农业大学|东北师范大学|北京工业大学|中国地质大学|华南师范大学|宁波大学|燕山大学|中国石油大学|太原理工大学|上海理工大学|中国矿业大学|陕西师范大学|江南大学|首都师范大学|浙江工业大学|中国石油大学|浙江师范大学|河北大学|对外经济贸易大学|扬州大学|江苏大学|杭州电子科技大学|辽宁大学|中央民族大学|山西大学|南京工业大学|齐鲁工业大学|广东工业大学|河南科技大学|山东师范大学|河北工业大学|成都理工大学|武汉科技大学|福建农林大学|天津师范大学|西南财经大学|福建师范大学|河南师范大学|深圳大学|江西师范大学|中央财经大学|北京林业大学|东北财经大学|长安大学|江西财经大学|南方科技大学|东北林业大学|安徽大学|黑龙江大学|湘潭大学|四川农业大学|上海师范大学|天津工业大学|东北农业大学|湖南农业大学|南京林业大学|山东农业大学|广西大学|广州大学|中国地质大学|华北电力大学|内蒙古大学|新疆大学|南京邮电大学|浙江工商大学|安徽师范大学|华侨大学|山东科技大学|西北师范大学|浙江理工大学|广西师范大学|中国矿业大学|贵州大学|大连海事大学|山东财经大学|长沙理工大学|中南民族大学|河南农业大学|海南大学|西安理工大学|湖北大学'
# 世界大学top500
top_college_global = '麻省理工学院|斯坦福大学|哈佛大学|牛津大学|加州理工学院|苏黎世联邦理工学院|剑桥大学|伦敦大学学院|帝国理工学院|芝加哥大学|南洋理工大学|新加坡国立大学|普林斯顿大学|康奈尔大学|宾夕法尼亚大学|清华大学|耶鲁大学|哥伦比亚大学|洛桑联邦理工学院|爱丁堡大学|密歇根大学|北京大学|东京大学|约翰霍普金斯大学|杜克大学|香港大学|曼彻斯特大学|加州大学伯克利分校|澳大利亚国立大学|多伦多大学|西北大学|香港科技大学|伦敦大学国王学院|京都大学|麦吉尔大学|加州大学洛杉矶分校|首尔国立大学|墨尔本大学|纽约大学|复旦大学|韩国高等科技学院|悉尼大学|新南威尔士大学（悉尼）|伦敦政治经济学院|加州大学圣地亚哥分校|香港中文大学|昆士兰大学|卡耐基梅隆大学|布里斯托大学|代尔夫特理工大学|不列颠哥伦比亚大学|香港城市大学|巴黎文理研究大学|浙江大学|慕尼黑工业大学|威斯康星大学麦迪逊分校|布朗大学|蒙纳士大学|东京工业大学|巴黎综合理工大学|上海交通大学|华威大学|慕尼黑大学|阿姆斯特丹大学|德克萨斯大学奥斯汀分校|海德堡大学|格拉斯哥大学|华盛顿大学|台湾大学|马来亚大学|大阪大学|佐治亚理工学院|哥本哈根大学|布宜诺斯艾利斯大学|伊利诺伊大学厄本那|苏黎世大学|索邦大学|杜伦大学|谢菲尔德大学|鲁汶大学|伯明翰大学|东北大学|83奥克兰大学|=83|莫斯科国立罗蒙诺索夫大学|莱斯大学|西澳大利亚大学|浦项科技大学|中国科学技术大学|北卡罗来纳大学教堂山分校|香港理工大学|隆德大学|宾州州立大学|利兹大学|成均馆大学|诺丁汉大学|南安普顿大学|波士顿大学|皇家理工学院|圣安德鲁斯大学|俄亥俄州立大学|埃因霍温科技大学|墨西哥国立自治大学|加州大学戴维斯分校|延世大学|阿德莱德大学|赫尔辛基大学|都柏林三一学院|华盛顿大学圣路易斯|日内瓦大学|普渡大学|丹麦技术大学|阿尔伯塔大学|格罗宁根大学|名古屋大学|圣保罗大学|乌普萨拉大学|莱顿大学|奥斯陆大学|柏林洪堡大学|南京大学|乌得勒支大学|伯尔尼大学|卡尔斯鲁厄理工学院|瓦赫宁根大学与研究所|伦敦大学玛丽皇后学院|智利天主教大学|兰开斯特大学|南加州大学|柏林自由大学|根特大学|北海道大学|九州大学|阿尔托大学|加州大学圣塔芭芭拉分校|马里兰大学帕克分校|蒙特利尔大学|亚琛工业大学|法国巴黎中央理工-高等电力学院|查尔姆斯理工大学|麦克马斯特大学|匹兹堡大学|悉尼科技大学|密歇根州立大学|奥胡斯大学|纽卡斯尔大学|柏林工业大学|约克大学|米兰理工大学|汉阳大学|巴塞尔大学|印度理工学院孟买分校|洛桑大学|卡迪夫大学|维也纳大学|埃默里大学|明尼苏达大学|蒙特雷科技大学|博特拉大学|里昂高等师范学校|马来西亚国民大学|耶路撒冷希伯来大学|卑尔根大学|埃克塞特大学|巴塞罗那大学|马来西亚理科大学|鲁汶天主教大学|佛罗里达大学|艾伯哈特-卡尔斯-图宾根大学|弗莱堡大学|罗彻斯特大学|巴斯大学|台湾新竹清华大学|贝尔法斯特女王大学|滑铁卢大学|奥塔哥大学|比萨圣安娜高等学校|博洛尼亚大学|凯斯西储大学|德累斯顿工业大学|利物浦大学|德里印度理工学院|鹿特丹伊拉斯姆斯大学|印度科学研究所|都柏林大学|阿卜杜勒阿齐兹国王大学|特温特大学|巴塞罗那自治大学|得克萨斯农工大学|智利大学|斯德哥尔摩大学|维也纳科技大学|马德里自治大学|阿伯丁大学|布鲁塞尔自由大学|早稻田大学|哥廷根大学|开普敦大学|弗吉尼亚大学|庆应义塾大学|法赫德国王石油矿产大学|范德比尔特大学|罗马大学|比萨高等师范学院|雷丁大学|科罗拉多大学博尔德分校|哈萨克斯坦国立大学|达特茅斯学院|澳大利亚纽卡斯尔大学|圣母大学|西安大略大学|马德里康普顿斯大学|卧龙岗大学|坎皮纳斯州立大学|亚利桑那州立大学|惠灵顿维多利亚大学|拉德堡德大学|马来西亚工艺大学|特拉维夫大学|加州大学欧文分校|阿姆斯特丹自由大学|拉夫堡大学|安特卫普大学|昆士兰科技大学|台湾成功大学|乔治城大学|台湾交通大学|汉堡大学|坎特伯雷大学|科廷大学|新西伯利亚大学|伊利诺伊大学芝加哥分校|卡尔加里大学|圣彼得堡国立大学|安第斯大学|帕多瓦大学|麦考瑞大学|墨尔本皇家理工大学|马斯特里赫特大学|女王大学|莱斯特大学|巴黎政治学院|波恩莱茵弗里德里希·威廉大学|贝鲁特美国大学|纳瓦拉大学|萨塞克斯大学|朱拉隆功大学|庆熙大学|巴黎高等电信学院|巴黎高科路桥学院|台湾科技大学|布鲁塞尔自由大学|塔夫斯大学|哥伦比亚国立大学|巴黎大学|哥德堡大学|以色列理工学院|武汉大学|爱尔兰国立大学戈尔韦|达姆施塔特工业大学|香港浸会大学|罗格斯大学|巴黎第十一大学|亚利桑那大学|同济大学|因斯布鲁克大学|怀卡托大学|哈利法大学|托木斯克州立大学|筑波大学|迪肯大学|印度理工学院-马德拉斯|迈阿密大学|南澳大利亚大学|萨里大学|卡塔尔大学|北京师范大学|哈尔滨工业大学|斯图加特大学|达尔豪斯大学|印度理工学院-卡哈拉格普尔|沙特国王大学|渥太华大学|鲍曼莫斯科国立技术大学|北卡罗来纳州立大学|庞培法布拉大学|梅西大学|台湾阳明大学|中山大学|图尔库大学|查理大学|印度理工学院-坎普尔|伦敦皇家霍洛威大学|法兰克福大学|塔斯马尼亚大学|印度尼西亚大学|斯特拉斯克莱德大学|马德里卡洛斯三世大学|文莱达鲁萨兰国大学|加泰罗尼亚理工大学-巴塞罗那高科|塔尔图大学|莫斯科物理科学与技术学院|米兰大学|邓迪大学|巴黎第一大学|马萨诸塞大学阿默斯特分校|西安交通大学|科隆大学|伦敦大学东方与非洲研究学院|科克大学|格拉茨科技大学|巴黎-萨克雷高等师范学校|印第安纳大学布卢明顿分校|赫瑞瓦特大学|玛希隆大学|西蒙弗雷泽大学|曼海姆大学|东英吉利大学|埃尔朗根-纽伦堡大学|格里菲斯大学|卡渣玛达大学|光州科学技术学院|国立研究大学高等经济学院|奥尔堡大学|林雪平大学|夏威夷大学马尼亚分校|弗吉尼亚理工学院和州立大学|伦敦大学伯贝克学院|国立核研究大学（莫斯科工程物理研究所）|阿联酋大学|万隆技术学院|梨花女子大学|台湾师范大学|广岛大学|IE商学院|乔治华盛顿大学|瓦伦西亚科技大学|雅盖隆大学|里斯本大学|于默奥大学|耶拿大学|乌尔姆大学|布法罗大学纽约州立大学|东北大学|阿根廷天主教大学|于韦斯屈莱大学|明斯特大学|都灵理工大学|伦敦大学城市学院|华沙大学|白俄罗斯国立大学|格勒诺布尔阿尔卑斯大学|波尔图大学|犹他大学|布拉格化学与技术大学|林肯大学|菲律宾大学|里约热内卢联邦大学|伦敦布鲁内尔大学|挪威科技大学|纽约州立大学石溪分校|东京医科齿科大学|叶史瓦学院|维多利亚大学|乌拉尔联邦大学|莫斯科国立国际关系学院|加州大学圣克鲁兹分校|南开大学|肯特大学|埃塞克斯大学|美国沙迦大学|堪萨斯大学|南丹麦大学|奥卢大学|巴基斯坦工程与应用科学研究所|牛津布鲁克斯大学|詹姆斯库克大学|康涅狄格大学|苏丹卡布斯大学|台北医科大学|斯特拉斯堡大学|文莱科技大学|印度理工学院-卢克里|伦斯勒理工学院|斯威本科技大学|巴勒莫大学|国立研究托木斯克理工大学|澳门大学|特伦托大学|比萨大学|特罗姆瑟大学挪威北极大学|喀山（伏尔加地区）联邦大学|俄罗斯人民友谊大学|科罗拉多大学丹佛分校|神户大学|坦佩雷大学|开罗美国大学|圣加仑大学|维克森林大学|华中科技大学|拉筹伯大学|国立科技大学-伊斯兰堡|南方大学|威特沃特斯兰德大学|华盛顿州立大学|科英布拉大学|韩国外国语大学|谢里夫科技大学|田纳西大学诺克斯维尔分校|美因茨约翰内斯·古腾堡大学|台湾中山大学|中央大学|约翰内斯开普勒大学林茨|上海大学|蒂尔堡大学|拉瓦尔大学|伦敦大学金史密斯学院|欧亚国立大学|内盖夫本古里安大学|杜兰大学|伊利诺理工学院|新里斯本大学|爱荷华大学|弗林德斯大学|那不勒斯菲里德里克第二大学|康斯坦茨大学|台湾中央大学|斯泰伦博斯大学|都柏林城市大学|天津大学|列日大学|波士顿学院|波鸿大学|萨拉戈萨大学|马德里理工大学|北京理工大学|圣彼得堡国立信息技术机械与光学大学|贝尔格拉诺大学|彼得大帝圣彼得堡理工大学|圣保罗联邦大学|萨斯喀彻温大学|阿斯顿大学|奥克兰理工大学|邦德大学|千叶大学|科罗拉多州立大学|思特雅大学|佛罗里达州立大学|一桥大学|佛罗伦萨大学|科奇大学|国立科技大学|厦门大学|东国大学|雅典国立技术大学|西江大学|加州大学河滨分校|波尔多大学|维尔纽斯大学|马里兰大学巴尔的摩分校|俄勒冈州立大学|北京航空航天大学|康考迪亚大学|维尔茨堡大学|斯旺西大学|韩国天主教大学|北京科技大学|布兰迪斯大学|哈维里亚那天主教大学|山东大学|萨尔州立大学|西悉尼大学|横滨市立大学|秘鲁天主教大学|佐治亚大学|德里大学|新加坡管理大学|基尔大学|斯特灵大学|华南理工大学|哥伦比亚对外大学|圣保罗州立大学|国油科技大学|阿伯里斯特威斯大学|长庚大学|吉林大学|堪培拉大学|韦恩州立大学|阿米尔卡比尔理工大学|智利圣地亚哥大学|印度理工学院古瓦哈提分校|拉彭兰塔拉赫蒂理工大学|南哈萨克斯坦州立大学|蒙得维的亚大学|艾克斯|特拉华大学|卡拉津哈尔科夫国立大学|布拉格捷克技术大学|蒙彼利埃大学|东芬兰大学'
# 全国一级学科
top_class_subject = {
    '北京大学': ["计算机科学与技术"]
}
# 本科起薪
bachelor_salary = 8
# 硕士起薪
master_salary = 10
# 最大薪资浮动
max_salary_float = 3

# 最大工作经历阈值，与最大在职时间配合
max_work_exp_num = 3

# 最大年龄
max_age = 30

# 本科毕业年龄
bachelor_graduate_age=22

# 最大延迟毕业年限
max_graduate_delay_years = 2

# 简历下载路径
resume_download_dir = 'download'

# 发送邮箱
email_sender = 'tel15258826527@sina.com'
# 邮箱密码
email_password = '337413c8324ffb81'
# smtp服务器
email_smtp_sever = 'smtp.sina.com'
# 接收邮箱
email_receivers = [
    '942980741@qq.com'
    'xulongzhe@uniview.com',
    'konghuadi@uniview.com'
]


# 拉钩网配置类
class LagoConfig(NamedTuple):
    cookie: str
    root_position_id: str
    greeting_id: str


lago_config = {
    'java': LagoConfig(
        'user_trace_token=20210306183907-8db0762b-31a9-435b-ba9e-e838904cf628; LGUID=20210306183907-ac289fca-17b9-4531-a6c7-6c1bc65082de; _ga=GA1.2.574457393.1615027148; index_location_city=%E6%9D%AD%E5%B7%9E; LG_LOGIN_USER_ID=a77721cdd129f6e5c56256928626a7b236c17231454e61dfd4dfefd846935bfa; LG_HAS_LOGIN=1; privacyPolicyPopup=false; gray=resume; _ga=GA1.3.574457393.1615027148; _putrc=A74EE0545FAEB7E6123F89F2B170EADC; PRE_UTM=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; login=true; unick=%E7%94%A8%E6%88%B78547; sensorsdata2015session=%7B%7D; _gid=GA1.2.707930289.1615600781; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615027148,1615090947,1615092831,1615600781; LGSID=20210313095938-b4145353-a1c4-41a0-83e6-ad3a0ec5dc5e; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615600787; JSESSIONID=ABAAAECABFEACCE77F5E104D5B88F303E127578E6093561; mds_login_authToken="XmqICexMmwhmpxoY0S5HtBA1TrwQlUBdSkHMoer58N7kAlgpn7PdV6NUc7Hc3GicuI71VRpPpFF+35C4GIdq5STSugOp8b0wVKn9QRIWFoTbwdWHU2BjY7drCnFn+T5AHG/PMQp9QAjnc18UPEAVY9hHCJV+wgpslk676NDAUpZ4rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="; mds_u_n=%5Cu7528%5Cu62378547; mds_u_ci=116597; mds_u_cn=%5Cu6d59%5Cu6c5f%5Cu5b87%5Cu89c6%5Cu79d1%5Cu6280%5Cu6709%5Cu9650%5Cu516c%5Cu53f8; mds_u_s_cn=%5Cu5b87%5Cu89c6%5Cu79d1%5Cu6280; gate_login_token=188aa1d3e5e9e21b1fa3b529ae08ad15e5cc2237e6e53d2ddde495f97c77d142; WEBTJ-ID=20210313%E4%B8%8A%E5%8D%889:59:48095948-178294fa3ce6a9-0620a6158f1241-5771133-2073600-178294fa3cfc5f; Hm_lvt_b53988385ecf648a7a8254b14163814d=1615027297,1615090950,1615092835,1615600789; qimo_seosource_551129f0-7fc2-11e6-bcdb-855ca3cec030=%E7%AB%99%E5%86%85; qimo_seokeywords_551129f0-7fc2-11e6-bcdb-855ca3cec030=; qimo_xstKeywords_551129f0-7fc2-11e6-bcdb-855ca3cec030=; href=https%3A%2F%2Feasy.lagou.com%2Fim%2Fchat%2Findex.htm%3F; accessId=551129f0-7fc2-11e6-bcdb-855ca3cec030; X_MIDDLE_TOKEN=c3198eacffd82873b2faa0c4a39143d9; _gat=1; pageViewNum=3; X_HTTP_TOKEN=30f9ba15b7ce436c6341065161333b5dc5b3a7b36d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219400766%22%2C%22first_id%22%3A%22178071e95cff8-0c71bd9d569dde-53e356a-2073600-178071e95d0c35%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2289.0.4389.82%22%2C%22easy_company_id%22%3A%22116597%22%2C%22lagou_company_id%22%3A%22126437%22%7D%2C%22%24device_id%22%3A%22178071e95cff8-0c71bd9d569dde-53e356a-2073600-178071e95d0c35%22%7D; LGRID=20210313101036-3e5da7b2-e9eb-4698-b2fc-96a038241b47; Hm_lpvt_b53988385ecf648a7a8254b14163814d=1615601439; gray=resume',
        "7815536",
        "19400766_b_1"),
    'bigdata': LagoConfig(
        'user_trace_token=20210304212528-781a0192-a0b3-42b5-a490-783c8454cf3f; _ga=GA1.2.389966518.1614864329; LGUID=20210304212529-7e97d6cc-d306-4e98-9498-41c585a25161; LG_HAS_LOGIN=1; privacyPolicyPopup=false; index_location_city=%E6%9D%AD%E5%B7%9E; gray=resume; _ga=GA1.3.389966518.1614864329; _gid=GA1.2.968523312.1615625217; accessId=551129f0-7fc2-11e6-bcdb-855ca3cec030; PRE_UTM=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615346724,1615625217,1615645263,1615729412; sensorsdata2015session=%7B%7D; LGSID=20210314214334-eb992a35-9452-46f4-8ada-9a9a2c9eb0dc; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; LG_LOGIN_USER_ID=4f66f841b7df35d16c4e3a227684a7259cf7ef020f4b43a6ce56d778612deec6; _putrc=4EEDAF119B4AD87D123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B75054; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615729417; JSESSIONID=ABAAABAABJBABFHBE5993C6A9A8524A074D0B59837461F4; mds_login_authToken="QzKD9pOcS6+AAJ/Iuxxh6SBoCHhgStzVsuaWJrzfjhcJIeD7bJJV8mPbbyOWOFffXXTtZVm450u5xYcUeo905RGg5CUidMrmwa7dnkyI435wcjZvWWEdcS4pIPx31es4/C0u7RTv/xdwW3l9D4iwSz7UGgXh7t58N4XI/32FRB94rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="; mds_u_n=%5Cu5218%5Cu6e05; mds_u_ci=116597; mds_u_cn=%5Cu6d59%5Cu6c5f%5Cu5b87%5Cu89c6%5Cu79d1%5Cu6280%5Cu6709%5Cu9650%5Cu516c%5Cu53f8; mds_u_s_cn=%5Cu5b87%5Cu89c6%5Cu79d1%5Cu6280; gate_login_token=6faac7240e1b24a67dfdfea449fd82aae4faf0d1d0a4bf5974394090bd5c285a; WEBTJ-ID=20210314%E4%B8%8B%E5%8D%889:43:47214347-17830fa8566669-09298ed54bbd3-3b710f51-2073600-17830fa85676b5; Hm_lvt_b53988385ecf648a7a8254b14163814d=1615625255,1615645272,1615725399,1615729428; qimo_seosource_551129f0-7fc2-11e6-bcdb-855ca3cec030=%E5%85%B6%E4%BB%96%E7%BD%91%E7%AB%99; qimo_seokeywords_551129f0-7fc2-11e6-bcdb-855ca3cec030=%E6%9C%AA%E7%9F%A5; qimo_xstKeywords_551129f0-7fc2-11e6-bcdb-855ca3cec030=; href=https%3A%2F%2Feasy.lagou.com%2Fdashboard%2Findex.htm%3Ffrom%3Dc_index; X_HTTP_TOKEN=6a66986c0ee5c24c6549275161fc3a61a9b9864081; Hm_lpvt_b53988385ecf648a7a8254b14163814d=1615729455; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212427350%22%2C%22%24device_id%22%3A%22177fd6a85323ed-072dd04d0207ef-3b710f51-1440000-177fd6a85334f5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24os%22%3A%22UNIX%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2288.0.4324.150%22%2C%22easy_company_id%22%3A%22116597%22%2C%22lagou_company_id%22%3A%22126437%22%7D%2C%22first_id%22%3A%22177fd6a85323ed-072dd04d0207ef-3b710f51-1440000-177fd6a85334f5%22%7D; pageViewNum=9; LGRID=20210314214542-c5402eff-0fec-4eb1-b1c2-59c6c93aa899',
        '8362510',
        '12427350_b_1'
    )
}
