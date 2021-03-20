import sys
import datetime
from config import logger

import config
import resume




def invite(session):
    logger.info(f'=== 岗位：{session.name} ===')
    for i in range(1, 5):
        logger.info(f'第{i}页')
        position_id, resumes = resume.newly_resume_list(session, page=i)
        for header in resumes:
            fetchKey = header['resumeFetchKey']
            user_id = header['userId']
            job_id = header['expectJobId']
            r = resume.detail_by_key(session, fetchKey, job_id)
            detail = r['resume']
            candidate = resume.parse_detail(detail)
            has_chat = r['hasChat']
            if has_chat:
                logger.info('已经聊过，跳过')
                continue

            employ_type = resume.match_all(session.employ_types, candidate)
            if not employ_type:
                continue
            resume.invite(session, user_id=user_id, position_id=position_id)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        invite(config.lago_config[sys.argv[1]])
    else:
        if datetime.datetime.now().hour < config.start_hour:
            logger.info('晚上不跑')
            exit()
        for key, session in config.lago_config.items():
            try:
                invite(session)
            except Exception as e:
                logger.exception(e)
