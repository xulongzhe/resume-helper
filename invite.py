import sys
from logging import Logger

import config
import resume
import util

log:Logger = util.get_log('log/invite.log')
resume.log = log

if __name__ == '__main__':
    for key, lago in config.lago_config.items():
        log.info(f'=== 岗位：{key} ===')
        for i in range(1, 5):
            log.info(f'第{i}页')
            position_id, resumes = resume.list(lago, page=i)
            for header in resumes:
                fetchKey = header['resumeFetchKey']
                user_id = header['userId']
                r = resume.detail_by_key(lago, fetchKey)
                detail = r['resume']
                candidate = resume.parse_detail(detail)
                log.info(str(candidate))

                has_chat = r['hasChat']
                if has_chat:
                    log.info('已经聊过，跳过')
                    continue

                if not resume.match_all(candidate):
                    continue
                resume.invite(lago, user_id=user_id, position_id=position_id)
