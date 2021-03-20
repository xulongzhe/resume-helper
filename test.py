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
    print(c.resume_id)
    h = resume.chart_history(lago , c.user_id)
    print(h)