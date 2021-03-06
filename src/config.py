from typing import NamedTuple

import rules
import logging
import cookie

# 调试模式
debug = False
# 一天开始的时间
start_hour = 7

# 日志框架
logger = logging.getLogger()
logger.setLevel('INFO')
basic_format = "[%(asctime)s %(levelname)s] %(message)s"
date_format = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(basic_format, date_format)
chlr = logging.StreamHandler()
chlr.setFormatter(formatter)
chlr.setLevel('DEBUG')
fhlr = logging.FileHandler('log/resume.log')
fhlr.setFormatter(formatter)
logger.addHandler(chlr)
logger.addHandler(fhlr)


# ========================== 拉钩网配置类 =======================
class LagoConfig(NamedTuple):
    name: str
    cookie: str
    root_position_id: str
    greeting_id: str
    employ_types: set
    email_receivers: list


lago_config = {
    'java1': LagoConfig(
        name='杭州Java正式',
        cookie=cookie.fetch_cookie('Profile 4'),
        root_position_id="7815536",
        greeting_id="19400766_b_1",
        employ_types={'社招正式'},
        email_receivers=[
            '942980741@qq.com',
            'xulongzhe@uniview.com',
            'konghuadi@uniview.com',
            'wangxiuzi@unview.com'
        ]
    ),
    'java2': LagoConfig(
        name='杭州Java外协',
        cookie=cookie.fetch_cookie('Profile 3'),
        root_position_id='8441573',
        greeting_id='12427350_b_1',
        employ_types={'社招外协'},
        email_receivers=[
            '942980741@qq.com',
            'xulongzhe@uniview.com',
            'konghuadi@uniview.com'
        ]
    ),
    'test': LagoConfig(
        name='杭州测试',
        cookie=cookie.fetch_cookie('Profile 2'),
        root_position_id='8448496',
        greeting_id='20653133_b_1',
        employ_types={'社招正式'},
        email_receivers=[
            '942980741@qq.com',
            'chenpeiqin@uniview.com'
        ]
    ),
    'jinan': LagoConfig(
        name='济南java',
        cookie=cookie.fetch_cookie('Profile 1'),
        root_position_id='7823880',
        greeting_id='16871675_b_1',
        employ_types={'社招正式','应届'},
        email_receivers=[
            '942980741@qq.com',
            'wangxiuzi@uniview.com'
        ]
    )
}

# ========================== 筛选条件配置 =======================
# 本科起薪
bachelor_salary = 8
# 硕士起薪
master_salary = 10
# 正式最大薪资浮动
max_salary_float_formal = 3
# 实习生起薪
intern_salary = 3
# 外协起薪
outsource_salary = 6
# 外协最大薪资浮动
max_salary_float_outsource = 2
# 本科毕业年龄
bachelor_graduate_age = 22
# 毕业季月份
graduate_month = 7
# 最大工作经历阈值，与最大在职时间配合
max_work_exp_num = 3
# 最大年龄
max_age = 28
# 最大延迟毕业年限
max_graduate_delay_years = 2
# 简历筛选规则
matchers = [
    ('社招正式', rules.match_formal),
    ('应届', rules.match_fresh_graduate),
    ('社招外协', rules.match_outsource),
    ('实习生', rules.match_intern)
]

# ========================== 邮件配置 =======================
# 简历下载路径
resume_download_dir = 'download'
# 发送邮箱
email_sender = 'tel15258826527@sina.com'
# 邮箱密码
email_password = '337413c8324ffb81'
# smtp服务器
email_smtp_sever = 'smtp.sina.com'

# 全国大学top200
top_college_china = ['北京大学', '清华大学', '复旦大学', '浙江大学', '南京大学', '上海交通大学', '华中科技大学', '中国科学技术大学', '中国人民大学', '天津大学', '武汉大学',
                     '南开大学', '山东大学', '中山大学', '西安交通大学', '哈尔滨工业大学', '东南大学', '四川大学', '吉林大学', '同济大学', '北京航空航天大学', '北京师范大学',
                     '厦门大学', '西北工业大学', '中南大学', '东北大学', '湖南大学', '大连理工大学', '华南理工大学', '北京理工大学', '兰州大学', '华东师范大学', '中国农业大学',
                     '电子科技大学', '重庆大学', '华中农业大学', '河海大学', '南京农业大学', '华中师范大学', '郑州大学', '中国海洋大学', '西安电子科技大学', '北京科技大学',
                     '南京理工大学', '北京交通大学', '华东理工大学', '北京邮电大学', '合肥工业大学', '南昌大学', '南京航空航天大学', '武汉理工大学', '西南交通大学', '暨南大学',
                     '西南大学', '西北农林科技大学', '东华大学', '西北大学', '中南财经政法大学', '苏州大学', '北京化工大学', '昆明理工大学', '南京师范大学', '上海财经大学',
                     '湖南师范大学', '云南大学', '上海大学', '哈尔滨工程大学', '福州大学', '河南大学', '华南农业大学', '东北师范大学', '北京工业大学', '中国地质大学',
                     '华南师范大学', '宁波大学', '燕山大学', '中国石油大学', '太原理工大学', '上海理工大学', '中国矿业大学', '陕西师范大学', '江南大学', '首都师范大学',
                     '浙江工业大学', '中国石油大学', '浙江师范大学', '河北大学', '对外经济贸易大学', '扬州大学', '江苏大学', '杭州电子科技大学', '辽宁大学', '中央民族大学',
                     '山西大学', '南京工业大学', '齐鲁工业大学', '广东工业大学', '河南科技大学', '山东师范大学', '河北工业大学', '成都理工大学', '武汉科技大学', '福建农林大学',
                     '天津师范大学', '西南财经大学', '福建师范大学', '河南师范大学', '深圳大学', '江西师范大学', '中央财经大学', '北京林业大学', '东北财经大学', '长安大学',
                     '江西财经大学', '南方科技大学', '东北林业大学', '安徽大学', '黑龙江大学', '湘潭大学', '四川农业大学', '上海师范大学', '天津工业大学', '东北农业大学',
                     '湖南农业大学', '南京林业大学', '山东农业大学', '广西大学', '广州大学', '中国地质大学', '华北电力大学', '内蒙古大学', '新疆大学', '南京邮电大学',
                     '浙江工商大学', '安徽师范大学', '华侨大学', '山东科技大学', '西北师范大学', '浙江理工大学', '广西师范大学', '中国矿业大学', '贵州大学', '大连海事大学',
                     '山东财经大学', '长沙理工大学', '中南民族大学', '河南农业大学', '海南大学', '西安理工大学', '湖北大学']
# 世界大学top500
top_college_global = ['麻省理工学院', '斯坦福大学', '哈佛大学', '牛津大学', '加州理工学院', '苏黎世联邦理工学院', '剑桥大学', '伦敦大学学院', '帝国理工学院', '芝加哥大学',
                      '南洋理工大学', '新加坡国立大学', '普林斯顿大学', '康奈尔大学', '宾夕法尼亚大学', '清华大学', '耶鲁大学', '哥伦比亚大学', '洛桑联邦理工学院', '爱丁堡大学',
                      '密歇根大学', '北京大学', '东京大学', '约翰霍普金斯大学', '杜克大学', '香港大学', '曼彻斯特大学', '加州大学伯克利分校', '澳大利亚国立大学', '多伦多大学',
                      '西北大学', '香港科技大学', '伦敦大学国王学院', '京都大学', '麦吉尔大学', '加州大学洛杉矶分校', '首尔国立大学', '墨尔本大学', '纽约大学', '复旦大学',
                      '韩国高等科技学院', '悉尼大学', '新南威尔士大学（悉尼）', '伦敦政治经济学院', '加州大学圣地亚哥分校', '香港中文大学', '昆士兰大学', '卡耐基梅隆大学',
                      '布里斯托大学', '代尔夫特理工大学', '不列颠哥伦比亚大学', '香港城市大学', '巴黎文理研究大学', '浙江大学', '慕尼黑工业大学', '威斯康星大学麦迪逊分校', '布朗大学',
                      '蒙纳士大学', '东京工业大学', '巴黎综合理工大学', '上海交通大学', '华威大学', '慕尼黑大学', '阿姆斯特丹大学', '德克萨斯大学奥斯汀分校', '海德堡大学',
                      '格拉斯哥大学', '华盛顿大学', '台湾大学', '马来亚大学', '大阪大学', '佐治亚理工学院', '哥本哈根大学', '布宜诺斯艾利斯大学', '伊利诺伊大学厄本那',
                      '苏黎世大学', '索邦大学', '杜伦大学', '谢菲尔德大学', '鲁汶大学', '伯明翰大学', '东北大学', '83奥克兰大学', '=83', '莫斯科国立罗蒙诺索夫大学',
                      '莱斯大学', '西澳大利亚大学', '浦项科技大学', '中国科学技术大学', '北卡罗来纳大学教堂山分校', '香港理工大学', '隆德大学', '宾州州立大学', '利兹大学',
                      '成均馆大学', '诺丁汉大学', '南安普顿大学', '波士顿大学', '皇家理工学院', '圣安德鲁斯大学', '俄亥俄州立大学', '埃因霍温科技大学', '墨西哥国立自治大学',
                      '加州大学戴维斯分校', '延世大学', '阿德莱德大学', '赫尔辛基大学', '都柏林三一学院', '华盛顿大学圣路易斯', '日内瓦大学', '普渡大学', '丹麦技术大学',
                      '阿尔伯塔大学', '格罗宁根大学', '名古屋大学', '圣保罗大学', '乌普萨拉大学', '莱顿大学', '奥斯陆大学', '柏林洪堡大学', '南京大学', '乌得勒支大学',
                      '伯尔尼大学', '卡尔斯鲁厄理工学院', '瓦赫宁根大学与研究所', '伦敦大学玛丽皇后学院', '智利天主教大学', '兰开斯特大学', '南加州大学', '柏林自由大学', '根特大学',
                      '北海道大学', '九州大学', '阿尔托大学', '加州大学圣塔芭芭拉分校', '马里兰大学帕克分校', '蒙特利尔大学', '亚琛工业大学', '法国巴黎中央理工-高等电力学院',
                      '查尔姆斯理工大学', '麦克马斯特大学', '匹兹堡大学', '悉尼科技大学', '密歇根州立大学', '奥胡斯大学', '纽卡斯尔大学', '柏林工业大学', '约克大学',
                      '米兰理工大学', '汉阳大学', '巴塞尔大学', '印度理工学院孟买分校', '洛桑大学', '卡迪夫大学', '维也纳大学', '埃默里大学', '明尼苏达大学', '蒙特雷科技大学',
                      '博特拉大学', '里昂高等师范学校', '马来西亚国民大学', '耶路撒冷希伯来大学', '卑尔根大学', '埃克塞特大学', '巴塞罗那大学', '马来西亚理科大学', '鲁汶天主教大学',
                      '佛罗里达大学', '艾伯哈特-卡尔斯-图宾根大学', '弗莱堡大学', '罗彻斯特大学', '巴斯大学', '台湾新竹清华大学', '贝尔法斯特女王大学', '滑铁卢大学', '奥塔哥大学',
                      '比萨圣安娜高等学校', '博洛尼亚大学', '凯斯西储大学', '德累斯顿工业大学', '利物浦大学', '德里印度理工学院', '鹿特丹伊拉斯姆斯大学', '印度科学研究所',
                      '都柏林大学', '阿卜杜勒阿齐兹国王大学', '特温特大学', '巴塞罗那自治大学', '得克萨斯农工大学', '智利大学', '斯德哥尔摩大学', '维也纳科技大学', '马德里自治大学',
                      '阿伯丁大学', '布鲁塞尔自由大学', '早稻田大学', '哥廷根大学', '开普敦大学', '弗吉尼亚大学', '庆应义塾大学', '法赫德国王石油矿产大学', '范德比尔特大学',
                      '罗马大学', '比萨高等师范学院', '雷丁大学', '科罗拉多大学博尔德分校', '哈萨克斯坦国立大学', '达特茅斯学院', '澳大利亚纽卡斯尔大学', '圣母大学', '西安大略大学',
                      '马德里康普顿斯大学', '卧龙岗大学', '坎皮纳斯州立大学', '亚利桑那州立大学', '惠灵顿维多利亚大学', '拉德堡德大学', '马来西亚工艺大学', '特拉维夫大学',
                      '加州大学欧文分校', '阿姆斯特丹自由大学', '拉夫堡大学', '安特卫普大学', '昆士兰科技大学', '台湾成功大学', '乔治城大学', '台湾交通大学', '汉堡大学',
                      '坎特伯雷大学', '科廷大学', '新西伯利亚大学', '伊利诺伊大学芝加哥分校', '卡尔加里大学', '圣彼得堡国立大学', '安第斯大学', '帕多瓦大学', '麦考瑞大学',
                      '墨尔本皇家理工大学', '马斯特里赫特大学', '女王大学', '莱斯特大学', '巴黎政治学院', '波恩莱茵弗里德里希·威廉大学', '贝鲁特美国大学', '纳瓦拉大学',
                      '萨塞克斯大学', '朱拉隆功大学', '庆熙大学', '巴黎高等电信学院', '巴黎高科路桥学院', '台湾科技大学', '布鲁塞尔自由大学', '塔夫斯大学', '哥伦比亚国立大学',
                      '巴黎大学', '哥德堡大学', '以色列理工学院', '武汉大学', '爱尔兰国立大学戈尔韦', '达姆施塔特工业大学', '香港浸会大学', '罗格斯大学', '巴黎第十一大学',
                      '亚利桑那大学', '同济大学', '因斯布鲁克大学', '怀卡托大学', '哈利法大学', '托木斯克州立大学', '筑波大学', '迪肯大学', '印度理工学院-马德拉斯', '迈阿密大学',
                      '南澳大利亚大学', '萨里大学', '卡塔尔大学', '北京师范大学', '哈尔滨工业大学', '斯图加特大学', '达尔豪斯大学', '印度理工学院-卡哈拉格普尔', '沙特国王大学',
                      '渥太华大学', '鲍曼莫斯科国立技术大学', '北卡罗来纳州立大学', '庞培法布拉大学', '梅西大学', '台湾阳明大学', '中山大学', '图尔库大学', '查理大学',
                      '印度理工学院-坎普尔', '伦敦皇家霍洛威大学', '法兰克福大学', '塔斯马尼亚大学', '印度尼西亚大学', '斯特拉斯克莱德大学', '马德里卡洛斯三世大学', '文莱达鲁萨兰国大学',
                      '加泰罗尼亚理工大学-巴塞罗那高科', '塔尔图大学', '莫斯科物理科学与技术学院', '米兰大学', '邓迪大学', '巴黎第一大学', '马萨诸塞大学阿默斯特分校', '西安交通大学',
                      '科隆大学', '伦敦大学东方与非洲研究学院', '科克大学', '格拉茨科技大学', '巴黎-萨克雷高等师范学校', '印第安纳大学布卢明顿分校', '赫瑞瓦特大学', '玛希隆大学',
                      '西蒙弗雷泽大学', '曼海姆大学', '东英吉利大学', '埃尔朗根-纽伦堡大学', '格里菲斯大学', '卡渣玛达大学', '光州科学技术学院', '国立研究大学高等经济学院',
                      '奥尔堡大学', '林雪平大学', '夏威夷大学马尼亚分校', '弗吉尼亚理工学院和州立大学', '伦敦大学伯贝克学院', '国立核研究大学（莫斯科工程物理研究所）', '阿联酋大学',
                      '万隆技术学院', '梨花女子大学', '台湾师范大学', '广岛大学', 'IE商学院', '乔治华盛顿大学', '瓦伦西亚科技大学', '雅盖隆大学', '里斯本大学', '于默奥大学',
                      '耶拿大学', '乌尔姆大学', '布法罗大学纽约州立大学', '东北大学', '阿根廷天主教大学', '于韦斯屈莱大学', '明斯特大学', '都灵理工大学', '伦敦大学城市学院',
                      '华沙大学', '白俄罗斯国立大学', '格勒诺布尔阿尔卑斯大学', '波尔图大学', '犹他大学', '布拉格化学与技术大学', '林肯大学', '菲律宾大学', '里约热内卢联邦大学',
                      '伦敦布鲁内尔大学', '挪威科技大学', '纽约州立大学石溪分校', '东京医科齿科大学', '叶史瓦学院', '维多利亚大学', '乌拉尔联邦大学', '莫斯科国立国际关系学院',
                      '加州大学圣克鲁兹分校', '南开大学', '肯特大学', '埃塞克斯大学', '美国沙迦大学', '堪萨斯大学', '南丹麦大学', '奥卢大学', '巴基斯坦工程与应用科学研究所',
                      '牛津布鲁克斯大学', '詹姆斯库克大学', '康涅狄格大学', '苏丹卡布斯大学', '台北医科大学', '斯特拉斯堡大学', '文莱科技大学', '印度理工学院-卢克里',
                      '伦斯勒理工学院', '斯威本科技大学', '巴勒莫大学', '国立研究托木斯克理工大学', '澳门大学', '特伦托大学', '比萨大学', '特罗姆瑟大学挪威北极大学',
                      '喀山（伏尔加地区）联邦大学', '俄罗斯人民友谊大学', '科罗拉多大学丹佛分校', '神户大学', '坦佩雷大学', '开罗美国大学', '圣加仑大学', '维克森林大学',
                      '华中科技大学', '拉筹伯大学', '国立科技大学-伊斯兰堡', '南方大学', '威特沃特斯兰德大学', '华盛顿州立大学', '科英布拉大学', '韩国外国语大学', '谢里夫科技大学',
                      '田纳西大学诺克斯维尔分校', '美因茨约翰内斯·古腾堡大学', '台湾中山大学', '中央大学', '约翰内斯开普勒大学林茨', '上海大学', '蒂尔堡大学', '拉瓦尔大学',
                      '伦敦大学金史密斯学院', '欧亚国立大学', '内盖夫本古里安大学', '杜兰大学', '伊利诺理工学院', '新里斯本大学', '爱荷华大学', '弗林德斯大学',
                      '那不勒斯菲里德里克第二大学', '康斯坦茨大学', '台湾中央大学', '斯泰伦博斯大学', '都柏林城市大学', '天津大学', '列日大学', '波士顿学院', '波鸿大学',
                      '萨拉戈萨大学', '马德里理工大学', '北京理工大学', '圣彼得堡国立信息技术机械与光学大学', '贝尔格拉诺大学', '彼得大帝圣彼得堡理工大学', '圣保罗联邦大学',
                      '萨斯喀彻温大学', '阿斯顿大学', '奥克兰理工大学', '邦德大学', '千叶大学', '科罗拉多州立大学', '思特雅大学', '佛罗里达州立大学', '一桥大学', '佛罗伦萨大学',
                      '科奇大学', '国立科技大学', '厦门大学', '东国大学', '雅典国立技术大学', '西江大学', '加州大学河滨分校', '波尔多大学', '维尔纽斯大学',
                      '马里兰大学巴尔的摩分校', '俄勒冈州立大学', '北京航空航天大学', '康考迪亚大学', '维尔茨堡大学', '斯旺西大学', '韩国天主教大学', '北京科技大学', '布兰迪斯大学',
                      '哈维里亚那天主教大学', '山东大学', '萨尔州立大学', '西悉尼大学', '横滨市立大学', '秘鲁天主教大学', '佐治亚大学', '德里大学', '新加坡管理大学', '基尔大学',
                      '斯特灵大学', '华南理工大学', '哥伦比亚对外大学', '圣保罗州立大学', '国油科技大学', '阿伯里斯特威斯大学', '长庚大学', '吉林大学', '堪培拉大学',
                      '韦恩州立大学', '阿米尔卡比尔理工大学', '智利圣地亚哥大学', '印度理工学院古瓦哈提分校', '拉彭兰塔拉赫蒂理工大学', '南哈萨克斯坦州立大学', '蒙得维的亚大学', '艾克斯',
                      '特拉华大学', '卡拉津哈尔科夫国立大学', '布拉格捷克技术大学', '蒙彼利埃大学', '东芬兰大学']
# 全国一级学科
top_class_subject = {'吉林师范大学': ['哲学', '教育学', '中国语言文学', '数学', '物理学'], '吉首大学': ['哲学', '体育学'], '西北政法大学': ['哲学'],
                     '西南民族大学': ['哲学', '应用经济学', '民族学', '中国语言文学', '美术学'], '吉林财经大学': ['理论经济学', '应用经济学', '统计学', '工商管理'],
                     '南京财经大学': ['理论经济学', '应用经济学', '统计学', '食品科学与工程', '工商管理'],
                     '浙江财经大学': ['理论经济学', '应用经济学', '统计学', '工商管理', '公共管理'], '安徽财经大学': ['应用经济学', '统计学', '工商管理'],
                     '北京工商大学': ['应用经济学', '计算机科学与技术', '化学工程与技术', '环境科学与工程', '食品科学与工程', '工商管理'],
                     '广东财经大学': ['应用经济学', '工商管理'], '贵州财经大学': ['应用经济学', '马克思主义理论', '工商管理'],
                     '哈尔滨商业大学': ['应用经济学', '食品科学与工程', '工商管理'], '河北经贸大学': ['应用经济学', '统计学', '工商管理'],
                     '河南财经政法大学': ['应用经济学', '工商管理'], '兰州财经大学': ['应用经济学', '统计学'], '陆军勤务学院（原由军事经济学院申报）': ['应用经济学'],
                     '南京审计大学': ['应用经济学', '工商管理'], '山东理工大学': ['应用经济学', '机械工程', '电气工程', '化学工程与技术', '农业工程'],
                     '上海对外经贸大学': ['应用经济学', '外国语言文学', '工商管理'], '西安财经学院': ['应用经济学', '统计学', '工商管理'],
                     '新疆财经大学': ['应用经济学', '统计学', '工商管理'], '云南财经大学': ['应用经济学', '统计学', '管理科学与工程', '工商管理', '公共管理'],
                     '中国地质大学': ['应用经济学', '马克思主义理论', '外国语言文学', '数学', '化学', '地理学', '海洋科学', '地球物理学', '地质学', '机械工程',
                                '仪器科学与技术', '材料科学与工程', '控制科学与工程', '计算机科学与技术', '土木工程', '水利工程', '测绘科学与技术', '地质资源与地质工程',
                                '石油与天然气工程', '环境科学与工程', '软件工程', '安全科学与工程', '管理科学与工程', '工商管理', '公共管理', '设计学'],
                     '中国石油大学': ['应用经济学', '马克思主义理论', '外国语言文学', '数学', '化学', '地球物理学', '地质学', '力学', '机械工程', '材料科学与工程',
                                '动力工程及工程热物理', '控制科学与工程', '计算机科学与技术', '测绘科学与技术', '化学工程与技术', '地质资源与地质工程', '石油与天然气工程',
                                '环境科学与工程', '安全科学与工程', '管理科学与工程', '工商管理'], '重庆工商大学': ['应用经济学', '统计学', '环境科学与工程', '工商管理'],
                     '西华师范大学': ['法学', '政治学', '马克思主义理论', '中国语言文学', '生态学'], '贵州民族大学': ['社会学'],
                     '广西民族大学': ['民族学', '马克思主义理论', '中国语言文学', '外国语言文学', '科学技术史'], '湖北民族学院': ['民族学'],
                     '内蒙古师范大学': ['民族学', '教育学', '心理学', '中国语言文学', '科学技术史', '美术学'], '宁夏大学': ['民族学', '数学', '水利工程', '草学'],
                     '西北民族大学': ['民族学', '中国语言文学', '音乐与舞蹈学'], '西藏民族大学': ['民族学'],
                     '新疆师范大学': ['民族学', '马克思主义理论', '教育学', '体育学', '中国语言文学', '美术学'],
                     '安徽工业大学': ['马克思主义理论', '机械工程', '材料科学与工程', '冶金工程', '计算机科学与技术', '化学工程与技术', '管理科学与工程', '工商管理'],
                     '北方工业大学': ['马克思主义理论', '数学', '机械工程', '控制科学与工程', '计算机科学与技术', '土木工程', '软件工程', '工商管理'],
                     '北华大学': ['马克思主义理论', '风景园林学', '林学'], '渤海大学': ['马克思主义理论', '教育学', '控制科学与工程', '食品科学与工程'],
                     '赣南师范大学': ['马克思主义理论', '教育学'], '贵州师范大学': ['马克思主义理论', '教育学', '心理学', '中国语言文学', '数学', '地理学'],
                     '国防大学（原由南京政治学院申报）': ['马克思主义理论', '新闻传播学', '图书情报与档案管理'],
                     '海南师范大学': ['马克思主义理论', '中国语言文学', '化学', '生态学'],
                     '南昌航空大学': ['马克思主义理论', '光学工程', '仪器科学与技术', '材料科学与工程', '环境科学与工程', '软件工程'],
                     '南通大学': ['马克思主义理论', '机械工程', '信息与通信工程', '基础医学', '临床医学'],
                     '曲阜师范大学': ['马克思主义理论', '教育学', '体育学', '中国语言文学', '外国语言文学', '中国史', '数学', '物理学', '化学', '统计学', '控制科学与工程',
                                '音乐与舞蹈学'],
                     '三峡大学': ['马克思主义理论', '中国语言文学', '电气工程', '计算机科学与技术', '土木工程', '水利工程', '管理科学与工程', '工商管理'],
                     '山西师范大学': ['马克思主义理论', '教育学', '体育学', '化学', '戏剧与影视学'],
                     '武汉纺织大学': ['马克思主义理论', '机械工程', '纺织科学与工程', '环境科学与工程', '管理科学与工程', '设计学'],
                     '西安科技大学': ['马克思主义理论', '机械工程', '土木工程', '测绘科学与技术', '地质资源与地质工程', '矿业工程', '安全科学与工程'],
                     '西华大学': ['马克思主义理论', '动力工程及工程热物理', '食品科学与工程'],
                     '西南科技大学': ['马克思主义理论', '材料科学与工程', '控制科学与工程', '环境科学与工程'], '信阳师范学院': ['马克思主义理论'], '延安大学': ['马克思主义理论'],
                     '重庆交通大学': ['马克思主义理论', '土木工程', '水利工程', '交通运输工程', '管理科学与工程'],
                     '沈阳师范大学': ['教育学', '中国语言文学', '生态学', '公共管理', '音乐与舞蹈学', '美术学'],
                     '空军军医大学（第四军医大学）': ['心理学', '生物学', '生物医学工程', '基础医学', '临床医学', '口腔医学', '公共卫生与预防医学', '中西医结合', '药学',
                                        '中药学', '护理学'], '成都体育学院': ['体育学'], '广州体育学院': ['体育学'], '吉林体育学院': ['体育学'],
                     '南京体育学院': ['体育学'], '山东体育学院': ['体育学'], '上海体育学院': ['体育学'], '沈阳体育学院': ['体育学'], '首都体育学院': ['体育学'],
                     '天津体育学院': ['体育学'], '武汉体育学院': ['体育学'], '西安体育学院': ['体育学'], '北京第二外国语学院': ['中国语言文学', '外国语言文学', '工商管理'],
                     '大连外国语大学': ['外国语言文学'],
                     '国防科技大学': ['外国语言文学', '数学', '物理学', '大气科学', '系统科学', '力学', '机械工程', '光学工程', '仪器科学与技术', '材料科学与工程',
                                '电子科学与技术', '信息与通信工程', '控制科学与工程', '计算机科学与技术', '航空宇航科学与技术', '生物医学工程', '软件工程', '管理科学与工程'],
                     '鲁东大学': ['外国语言文学'], '四川外国语大学': ['外国语言文学'], '天津外国语大学': ['外国语言文学'], '西安外国语大学': ['外国语言文学'],
                     '延边大学': ['外国语言文学', '世界史', '化学', '生物学', '临床医学', '药学'], '北京印刷学院': ['新闻传播学', '美术学', '设计学'],
                     '苏州科技大学': ['世界史', '土木工程', '环境科学与工程', '城乡规划学', '风景园林学'],
                     '桂林电子科技大学': ['数学', '机械工程', '仪器科学与技术', '材料科学与工程', '电子科学与技术', '信息与通信工程', '计算机科学与技术', '软件工程'],
                     '华北理工大学': ['数学', '冶金工程', '化学工程与技术', '公共卫生与预防医学', '护理学'],
                     '陆军工程大学（原解放军理工大学）': ['数学', '机械工程', '光学工程', '电子科学与技术', '信息与通信工程', '计算机科学与技术', '土木工程', '兵器科学与技术',
                                          '软件工程'], '烟台大学': ['数学', '药学'],
                     '中北大学': ['数学', '机械工程', '仪器科学与技术', '材料科学与工程', '信息与通信工程', '计算机科学与技术', '化学工程与技术', '安全科学与工程'],
                     '淮北师范大学': ['化学'], '青海师范大学': ['地理学', '计算机科学与技术'], '大连海洋大学': ['海洋科学', '水产'],
                     '广东海洋大学': ['海洋科学', '食品科学与工程', '水产'], '浙江海洋大学': ['海洋科学', '水产'],
                     '河北医科大学': ['生物学', '基础医学', '临床医学', '中西医结合', '药学'],
                     '吉林农业大学': ['生物学', '食品科学与工程', '作物学', '农业资源与环境', '植物保护', '畜牧学', '兽医学', '农林经济管理'],
                     '中国计量大学': ['生物学', '光学工程', '仪器科学与技术', '材料科学与工程', '控制科学与工程', '管理科学与工程'],
                     '西南林业大学': ['生态学', '林业工程', '风景园林学', '林学'],
                     '成都信息工程大学': ['统计学', '信息与通信工程', '计算机科学与技术', '软件工程', '管理科学与工程'],
                     '长春工业大学': ['统计学', '机械工程', '材料科学与工程', '控制科学与工程', '计算机科学与技术', '化学工程与技术'],
                     '安徽理工大学': ['机械工程', '土木工程', '化学工程与技术', '矿业工程', '环境科学与工程', '安全科学与工程'],
                     '北京信息科技大学': ['机械工程', '仪器科学与技术', '管理科学与工程'], '大连交通大学': ['机械工程', '材料科学与工程', '交通运输工程', '软件工程'],
                     '东北石油大学': ['机械工程', '动力工程及工程热物理', '化学工程与技术', '地质资源与地质工程', '石油与天然气工程'],
                     '湖北工业大学': ['机械工程', '土木工程', '轻工技术与工程', '工商管理', '设计学'],
                     '火箭军工程大学': ['机械工程', '控制科学与工程', '计算机科学与技术', '航空宇航科学与技术', '兵器科学与技术'],
                     '辽宁科技大学': ['机械工程', '控制科学与工程', '化学工程与技术', '软件工程'], '青岛理工大学': ['机械工程', '建筑学', '土木工程', '环境科学与工程'],
                     '上海工程技术大学': ['机械工程', '工商管理'],
                     '沈阳航空航天大学': ['机械工程', '动力工程及工程热物理', '计算机科学与技术', '航空宇航科学与技术', '安全科学与工程', '工商管理', '设计学'],
                     '沈阳建筑大学': ['机械工程', '计算机科学与技术', '建筑学', '土木工程', '城乡规划学', '风景园林学'], '沈阳理工大学': ['机械工程'],
                     '太原科技大学': ['机械工程', '材料科学与工程'], '西安工业大学': ['机械工程', '光学工程', '材料科学与工程', '计算机科学与技术'],
                     '郑州轻工业学院': ['机械工程', '电气工程', '计算机科学与技术', '化学工程与技术', '食品科学与工程', '软件工程'],
                     '重庆理工大学': ['机械工程', '仪器科学与技术', '工商管理'],
                     '海军航空大学（原海军航空工程学院）': ['仪器科学与技术', '电子科学与技术', '信息与通信工程', '控制科学与工程', '航空宇航科学与技术'],
                     '解放军信息工程大学': ['仪器科学与技术', '电子科学与技术', '信息与通信工程', '控制科学与工程', '计算机科学与技术', '测绘科学与技术', '软件工程'],
                     '常州大学': ['材料科学与工程', '计算机科学与技术', '化学工程与技术', '环境科学与工程'], '佳木斯大学': ['材料科学与工程'],
                     '江苏科技大学': ['材料科学与工程', '控制科学与工程', '船舶与海洋工程', '管理科学与工程', '工商管理'],
                     '景德镇陶瓷大学': ['材料科学与工程', '美术学', '设计学'], '内蒙古工业大学': ['材料科学与工程', '动力工程及工程热物理', '化学工程与技术'],
                     '内蒙古科技大学': ['冶金工程'], '海军工程大学': ['动力工程及工程热物理', '电气工程', '信息与通信工程', '控制科学与工程', '船舶与海洋工程', '核科学与技术'],
                     '上海电力学院': ['动力工程及工程热物理', '电气工程', '化学工程与技术'],
                     '空军工程大学': ['电子科学与技术', '信息与通信工程', '控制科学与工程', '计算机科学与技术', '交通运输工程', '航空宇航科学与技术', '兵器科学与技术',
                                '管理科学与工程'], '西安邮电大学': ['电子科学与技术', '信息与通信工程', '计算机科学与技术', '软件工程'],
                     '航天工程大学（原装备学院）': ['信息与通信工程', '航空宇航科学与技术', '兵器科学与技术'],
                     '华东交通大学': ['信息与通信工程', '控制科学与工程', '土木工程', '交通运输工程'],
                     '中国民航大学': ['信息与通信工程', '控制科学与工程', '计算机科学与技术', '交通运输工程', '安全科学与工程'], '安徽工程大学': ['控制科学与工程'],
                     '北京建筑大学': ['控制科学与工程', '建筑学', '土木工程', '测绘科学与技术', '交通运输工程', '环境科学与工程', '城乡规划学', '风景园林学'],
                     '辽宁工业大学': ['控制科学与工程'], '辽宁石油化工大学': ['控制科学与工程', '化学工程与技术'], '西安工程大学': ['控制科学与工程', '纺织科学与工程', '设计学'],
                     '河北工程大学': ['计算机科学与技术'], '安徽建筑大学': ['建筑学', '土木工程', '城乡规划学'], '吉林建筑大学': ['建筑学', '土木工程'],
                     '山东建筑大学': ['建筑学', '土木工程', '城乡规划学'], '华北水利水电大学': ['土木工程', '水利工程', '地质资源与地质工程', '管理科学与工程', '工商管理'],
                     '天津城建大学': ['土木工程', '城乡规划学'],
                     '内蒙古农业大学': ['水利工程', '农业工程', '食品科学与工程', '农业资源与环境', '畜牧学', '兽医学', '林学', '草学', '农林经济管理'],
                     '新疆农业大学': ['水利工程', '畜牧学', '草学', '农林经济管理'], '东华理工大学': ['测绘科学与技术', '地质资源与地质工程', '核科学与技术', '工商管理'],
                     '河北科技大学': ['化学工程与技术', '环境科学与工程'], '江汉大学': ['化学工程与技术'], '上海应用技术大学': ['化学工程与技术'],
                     '沈阳化工大学': ['化学工程与技术'], '石河子大学': ['化学工程与技术', '农业工程', '作物学', '园艺学', '畜牧学', '基础医学', '工商管理'],
                     '西安石油大学': ['化学工程与技术', '石油与天然气工程'], '南华大学': ['矿业工程', '核科学与技术', '软件工程', '安全科学与工程', '基础医学'],
                     '中原工学院': ['纺织科学与工程'], '甘肃农业大学': ['农业工程', '作物学', '园艺学', '畜牧学', '兽医学', '草学'],
                     '黑龙江八一农垦大学': ['农业工程', '食品科学与工程', '兽医学'], '青岛农业大学': ['农业工程', '兽医学'], '沈阳大学': ['环境科学与工程'],
                     '湖南工业大学': ['生物医学工程', '设计学'], '集美大学': ['食品科学与工程', '水产'], '武汉轻工大学': ['食品科学与工程'],
                     '云南农业大学': ['食品科学与工程', '作物学', '农业资源与环境', '植物保护', '畜牧学', '草学'],
                     '江西农业大学': ['风景园林学', '作物学', '畜牧学', '兽医学', '林学', '公共管理'], '北京联合大学': ['软件工程', '工商管理'],
                     '黑龙江科技大学': ['安全科学与工程'], '青海大学': ['作物学', '草学'], '山西农业大学': ['作物学', '园艺学', '农业资源与环境', '畜牧学', '兽医学'],
                     '北京农学院': ['园艺学', '农林经济管理'], '天津农学院': ['水产'],
                     '安徽医科大学': ['基础医学', '临床医学', '口腔医学', '公共卫生与预防医学', '药学', '护理学'],
                     '广西医科大学': ['基础医学', '临床医学', '口腔医学', '公共卫生与预防医学', '药学', '护理学'],
                     '贵州医科大学': ['基础医学', '临床医学', '公共卫生与预防医学', '药学'],
                     '海军军医大学（第二军医大学）': ['基础医学', '临床医学', '公共卫生与预防医学', '中西医结合', '药学', '中药学', '护理学', '公共管理'],
                     '昆明医科大学': ['基础医学', '临床医学', '口腔医学', '公共卫生与预防医学', '药学'], '宁夏医科大学': ['基础医学', '临床医学'],
                     '新乡医学院': ['基础医学', '临床医学'], '徐州医科大学': ['基础医学', '临床医学', '药学'], '广东医科大学': ['临床医学'],
                     '锦州医科大学': ['临床医学'], '新疆医科大学': ['临床医学', '公共卫生与预防医学', '中西医结合', '药学'],
                     '安徽中医药大学': ['中医学', '中西医结合', '中药学'], '福建中医药大学': ['中医学', '中西医结合'], '甘肃中医药大学': ['中医学', '中药学'],
                     '广西中医药大学': ['中医学'], '贵阳中医学院': ['中医学', '中药学'], '河南中医药大学': ['中医学', '中药学'], '湖北中医药大学': ['中医学', '中药学'],
                     '湖南中医药大学': ['中医学', '中西医结合', '药学'], '江西中医药大学': ['中医学', '中西医结合', '中药学'],
                     '辽宁中医药大学': ['中医学', '中西医结合', '药学', '中药学'], '山东中医药大学': ['中医学', '中西医结合', '药学', '中药学'],
                     '陕西中医药大学': ['中医学', '中药学'], '长春中医药大学': ['中医学', '中药学'],
                     '浙江中医药大学': ['中医学', '中西医结合', '药学', '中药学', '护理学'], '河北中医学院': ['中西医结合'], '广东药科大学': ['药学'],
                     '沈阳药科大学': ['药学', '中药学'], '遵义医学院': ['药学'], '北京物资学院': ['管理科学与工程', '工商管理'], '内蒙古财经大学': ['工商管理'],
                     '天津商业大学': ['工商管理'], '北京电影学院': ['艺术学理论', '戏剧与影视学', '美术学'], '北京服装学院': ['艺术学理论', '美术学', '设计学'],
                     '广西艺术学院': ['艺术学理论', '音乐与舞蹈学', '美术学', '设计学'], '广州美术学院': ['艺术学理论', '美术学', '设计学'],
                     '哈尔滨音乐学院': ['艺术学理论', '音乐与舞蹈学'], '湖北美术学院': ['艺术学理论', '美术学', '设计学'],
                     '鲁迅美术学院': ['艺术学理论', '美术学', '设计学'], '南京艺术学院': ['艺术学理论', '音乐与舞蹈学', '戏剧与影视学', '美术学', '设计学'],
                     '上海戏剧学院': ['艺术学理论', '音乐与舞蹈学', '戏剧与影视学', '设计学'], '上海音乐学院': ['艺术学理论', '音乐与舞蹈学', '戏剧与影视学'],
                     '沈阳音乐学院': ['艺术学理论', '音乐与舞蹈学'], '四川美术学院': ['艺术学理论', '戏剧与影视学', '美术学', '设计学'],
                     '西安美术学院': ['艺术学理论', '美术学', '设计学'], '中国美术学院': ['艺术学理论', '戏剧与影视学', '美术学', '设计学'],
                     '中央戏剧学院': ['艺术学理论', '戏剧与影视学'], '北京舞蹈学院': ['音乐与舞蹈学'], '吉林艺术学院': ['音乐与舞蹈学', '戏剧与影视学', '美术学', '设计学'],
                     '四川音乐学院': ['音乐与舞蹈学'], '天津音乐学院': ['音乐与舞蹈学'], '西安音乐学院': ['音乐与舞蹈学'], '星海音乐学院': ['音乐与舞蹈学'],
                     '云南艺术学院': ['音乐与舞蹈学', '戏剧与影视学', '美术学', '设计学'], '中国戏曲学院': ['音乐与舞蹈学', '戏剧与影视学'], '中国音乐学院': ['音乐与舞蹈学'],
                     '中央音乐学院': ['音乐与舞蹈学'], '山东工艺美术学院': ['美术学', '设计学'], '天津美术学院': ['美术学', '设计学'],
                     '中央美术学院': ['建筑学', '艺术学理论', '美术学', '设计学'], '山西财经大学': ['理论经济学', '应用经济学', '马克思主义理论', '统计学', '工商管理'],
                     '温州大学': ['马克思主义理论', '教育学', '中国语言文学', '数学', '化学', '计算机科学与技术'],
                     '天津财经大学': ['理论经济学', '应用经济学', '管理科学与工程', '工商管理', '公共管理'],
                     '大连工业大学': ['控制科学与工程', '纺织科学与工程', '轻工技术与工程', '食品科学与工程', '设计学'],
                     '重庆师范大学': ['马克思主义理论', '教育学', '中国语言文学', '外国语言文学', '考古学', '数学', '美术学'],
                     '山西医科大学': ['生物学', '基础医学', '临床医学', '公共卫生与预防医学', '药学', '护理学'], '河南工业大学': ['食品科学与工程'],
                     '武汉工程大学': ['马克思主义理论', '材料科学与工程', '化学工程与技术'],
                     '桂林理工大学': ['统计学', '材料科学与工程', '土木工程', '地质资源与地质工程', '环境科学与工程', '工商管理'],
                     '浙江农林大学': ['生物学', '生态学', '林业工程', '风景园林学', '农业资源与环境', '林学'],
                     '大连医科大学': ['生物学', '基础医学', '临床医学', '口腔医学', '中西医结合', '药学', '护理学'],
                     '天津科技大学': ['机械工程', '化学工程与技术', '轻工技术与工程', '食品科学与工程', '药学', '管理科学与工程'],
                     '黑龙江中医药大学': ['中医学', '中西医结合', '药学', '中药学'], '上海海洋大学': ['海洋科学', '生物学', '计算机科学与技术', '食品科学与工程', '水产'],
                     '中南林业科技大学': ['生物学', '生态学', '土木工程', '林业工程', '食品科学与工程', '风景园林学', '林学'],
                     '天津理工大学': ['材料科学与工程', '电子科学与技术', '控制科学与工程', '计算机科学与技术', '化学工程与技术', '软件工程', '管理科学与工程', '工商管理'],
                     '青岛科技大学': ['化学', '机械工程', '材料科学与工程', '动力工程及工程热物理', '控制科学与工程', '化学工程与技术', '软件工程'],
                     '济南大学': ['应用经济学', '社会学', '中国语言文学', '化学', '材料科学与工程', '控制科学与工程', '计算机科学与技术', '化学工程与技术', '环境科学与工程',
                              '临床医学', '工商管理'], '安徽农业大学': ['生物学', '生态学', '作物学', '园艺学', '植物保护', '畜牧学', '林学'],
                     '辽宁师范大学': ['马克思主义理论', '教育学', '心理学', '体育学', '中国语言文学', '外国语言文学', '中国史', '数学', '物理学', '化学', '地理学',
                                '生物学', '计算机科学与技术'],
                     '沈阳工业大学': ['机械工程', '仪器科学与技术', '材料科学与工程', '电气工程', '化学工程与技术', '管理科学与工程'],
                     '上海海事大学': ['外国语言文学', '电气工程', '信息与通信工程', '交通运输工程', '管理科学与工程', '工商管理'],
                     '广州医科大学': ['基础医学', '临床医学', '药学', '护理学'], '天津中医药大学': ['中医学', '中西医结合', '药学', '中药学', '护理学'],
                     '大连大学': ['计算机科学与技术', '软件工程'],
                     '陕西科技大学': ['材料科学与工程', '化学工程与技术', '轻工技术与工程', '食品科学与工程', '软件工程', '设计学'],
                     '四川师范大学': ['理论经济学', '教育学', '中国语言文学', '外国语言文学', '数学', '物理学', '戏剧与影视学', '美术学'],
                     '江苏师范大学': ['应用经济学', '马克思主义理论', '教育学', '中国语言文学', '数学', '地理学', '生物学', '统计学', '光学工程'],
                     '成都中医药大学': ['中医学', '中西医结合', '药学', '中药学'], '江西理工大学': ['冶金工程', '矿业工程'],
                     '长江大学': ['地质资源与地质工程', '石油与天然气工程'], '石家庄铁道大学': ['机械工程', '计算机科学与技术', '土木工程', '交通运输工程'],
                     '辽宁工程技术大学': ['力学', '机械工程', '电气工程', '土木工程', '测绘科学与技术', '矿业工程', '软件工程', '安全科学与工程', '管理科学与工程'],
                     '河北师范大学': ['马克思主义理论', '教育学', '体育学', '中国语言文学', '外国语言文学', '考古学', '中国史', '数学', '物理学', '化学', '地理学',
                                '生物学', '生态学', '音乐与舞蹈学', '美术学'], '华东政法大学': ['应用经济学', '法学', '政治学', '马克思主义理论'],
                     '西南石油大学': ['马克思主义理论', '机械工程', '材料科学与工程', '化学工程与技术', '地质资源与地质工程', '石油与天然气工程', '软件工程', '管理科学与工程'],
                     '温州医科大学': ['生物学', '生物医学工程', '临床医学', '药学', '中药学', '护理学'],
                     '兰州理工大学': ['机械工程', '材料科学与工程', '动力工程及工程热物理', '控制科学与工程', '土木工程', '化学工程与技术'],
                     '青岛大学': ['理论经济学', '中国语言文学', '外国语言文学', '物理学', '生物学', '系统科学', '材料科学与工程', '控制科学与工程', '计算机科学与技术',
                              '纺织科学与工程', '软件工程', '基础医学', '临床医学', '护理学', '管理科学与工程', '工商管理'], '云南民族大学': ['社会学', '民族学'],
                     '兰州交通大学': ['机械工程', '土木工程', '交通运输工程', '环境科学与工程'],
                     '南京信息工程大学': ['数学', '大气科学', '科学技术史', '生态学', '信息与通信工程', '计算机科学与技术', '环境科学与工程', '软件工程', '管理科学与工程'],
                     '重庆邮电大学': ['马克思主义理论', '电子科学与技术', '信息与通信工程', '控制科学与工程', '计算机科学与技术', '软件工程', '管理科学与工程'],
                     '湖南科技大学': ['应用经济学', '马克思主义理论', '外国语言文学', '化学', '机械工程', '计算机科学与技术', '土木工程', '安全科学与工程'],
                     '哈尔滨师范大学': ['马克思主义理论', '教育学', '中国语言文学', '外国语言文学', '世界史', '数学', '地理学', '生物学', '戏剧与影视学', '美术学'],
                     '沈阳农业大学': ['农业工程', '食品科学与工程', '风景园林学', '作物学', '园艺学', '农业资源与环境', '植物保护', '兽医学', '农林经济管理'],
                     '首都经济贸易大学': ['理论经济学', '应用经济学', '统计学', '管理科学与工程', '工商管理', '公共管理'],
                     '重庆医科大学': ['基础医学', '临床医学', '口腔医学', '公共卫生与预防医学', '药学', '护理学'],
                     '河南理工大学': ['马克思主义理论', '机械工程', '控制科学与工程', '计算机科学与技术', '测绘科学与技术', '地质资源与地质工程', '矿业工程', '软件工程',
                                '安全科学与工程', '公共管理'],
                     '汕头大学': ['新闻传播学', '数学', '化学', '生物学', '土木工程', '基础医学', '临床医学', '药学', '工商管理'],
                     '河北农业大学': ['生物学', '农业工程', '食品科学与工程', '风景园林学', '作物学', '园艺学', '农业资源与环境', '植物保护', '畜牧学', '兽医学', '林学',
                                '农林经济管理'],
                     '西安建筑科技大学': ['机械工程', '材料科学与工程', '冶金工程', '建筑学', '土木工程', '环境科学与工程', '城乡规划学', '风景园林学', '管理科学与工程',
                                  '美术学'], '云南师范大学': ['马克思主义理论', '教育学', '体育学', '中国语言文学', '数学', '地理学', '农业工程', '戏剧与影视学'],
                     '南京中医药大学': ['中医学', '中西医结合', '药学', '中药学', '护理学'],
                     '东北电力大学': ['动力工程及工程热物理', '电气工程', '控制科学与工程', '计算机科学与技术', '化学工程与技术'],
                     '杭州师范大学': ['马克思主义理论', '教育学', '心理学', '中国语言文学', '外国语言文学', '数学', '物理学', '化学', '生物学', '生态学', '公共管理',
                                '艺术学理论', '美术学'],
                     '哈尔滨理工大学': ['马克思主义理论', '数学', '机械工程', '仪器科学与技术', '材料科学与工程', '电气工程', '控制科学与工程', '计算机科学与技术', '软件工程',
                                 '管理科学与工程', '工商管理'],
                     '长春理工大学': ['马克思主义理论', '物理学', '机械工程', '光学工程', '仪器科学与技术', '材料科学与工程', '电子科学与技术', '信息与通信工程',
                                '计算机科学与技术', '软件工程']}
