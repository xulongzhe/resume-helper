import resume
import config
import util
from logging import Logger
log: Logger = util.get_log('log/invite.log')
resume.log = log
lago  = config.lago_config['java1']
l = resume.complete_list(lago)
for r in l:
    c = resume.detail_by_id(lago, r['id'])
    c = resume.parse_detail(c)
    h = resume.chart_history(lago , c.user_id)
    for m in h:
        if m['senderId'] == c.user_id:
            print('--' + m['msgContent'])
        else:
            print(m['msgContent'])