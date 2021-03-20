import os
import sys
import time
import datetime
import config
from config import logger
import mail
import resume

def filter_newly_download(lago, resumes):
    for r in resumes:
        resume_id = r['id']
        name = r['candidateName']
        stage = r['stage']
        if stage == 'OBSOLETE':
            logger.info(f'{name} 已标记为不合适，跳过')
            continue
        detail = resume.detail_by_id(lago, resume_id)
        candidate = resume.parse_detail(detail)
        file_path = f'{config.resume_download_dir}/{lago.name}-{candidate.name}-{candidate.phone}.pdf'
        if os.path.exists(file_path):
            logger.info(f'简历 {os.path.basename(file_path)} 已存在')
        else:
            resume.download(lago, resume_id, file_path)
            yield candidate, file_path


def filter_condition(lago, resumes):
    for candidate, file_path in resumes:
        logger.info(str(candidate))
        emp_type = resume.match_all(lago.employ_types, candidate)
        candidate = candidate._replace(employ_type=emp_type)
        if emp_type:
            yield file_path, candidate


def forward(lago):
    logger.info(f'=== 岗位：{lago.name} ===')
    os.makedirs(config.resume_download_dir, exist_ok=True)
    resumes = resume.history_resume_list(lago)
    downloads = filter_newly_download(lago, resumes)
    need_sends = list(filter_condition(lago, downloads))
    if need_sends:
        m = mail.Email(config.email_sender, config.email_smtp_sever,
                       config.email_sender, config.email_password)
        now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        title = f'{now} 收到 {lago.name} 简历{len(need_sends)}份'
        content = '<table>' + \
            '\n'.join([candidate.html()
                       for _, candidate in need_sends]) + '</table>'
        attaches = [file_path for file_path, _, in need_sends]
        m.send(lago.email_receivers, title, content, attaches)
        logger.info(title)
    else:
        logger.info('没有收到新的简历')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        forward(config.lago_config[sys.argv[1]])
    else:
        if datetime.datetime.now().hour < config.start_hour:
            logger.info('晚上不跑')
            exit()
        for key, lago in config.lago_config.items():
            try:
                forward(lago)
            except Exception as e:
                logger.error(e)
