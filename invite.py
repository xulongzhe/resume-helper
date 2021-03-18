import sys
import datetime
from logging import Logger

import config
import resume
import util

log: Logger = util.get_log('log/invite.log')
resume.log = log


def invite(lago):
    log.info(f'=== 岗位：{lago.name} ===')
    for i in range(1, 5):
        log.info(f'第{i}页')
        position_id, resumes = resume.list(lago, page=i)
        for header in resumes:
            fetchKey = header['resumeFetchKey']
            user_id = header['userId']
            job_id = header['expectJobId']
            r = resume.detail_by_key(lago, fetchKey, job_id)
            detail = r['resume']
            candidate = resume.parse_detail(detail)
            has_chat = r['hasChat']
            if has_chat:
                log.info('已经聊过，跳过')
                continue

            employ_type = resume.match_all(lago.employ_types, candidate)
            if not employ_type:
                continue
            resume.invite(lago, user_id=user_id, position_id=position_id)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        invite(config.lago_config[sys.argv[1]])
    else:
        if datetime.datetime.now().hour < config.start_hour:
            log.info('晚上不跑')
            exit()
        for key, lago in config.lago_config.items():
            try:
                invite(lago)
            except Exception as e:
                log.error(e)
