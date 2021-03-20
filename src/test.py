import resume
import config
import sys
import datetime
from config import logger

def replay(session):    
    newly_resume_list = resume.history_resume_list(session)
    for summary in newly_resume_list:
        id = summary['id']
        detail = resume.detail_by_id(session, id)
        candidate = resume.parse_detail(detail)
        conversation = resume.chart_history(session , candidate.user_id)
        for one in conversation:
            sender = one['senderId']
            if one['msgType'] != 0:
                continue
                
            if one['senderId'] == candidate.user_id:
                print('--' + one['msgContent'])
            else:
                print('-' + one['msgContent'])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        replay(config.lago_config[sys.argv[1]])
    else:
        if datetime.datetime.now().hour < config.start_hour:
            logger.info('晚上不跑')
            exit()
        for key, session in config.lago_config.items():
            try:
                replay(session)
            except Exception as e:
                logger.exception(e)
