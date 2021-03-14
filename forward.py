import os
import sys
import time
from logging import Logger

import config
import mail
import resume
import util

log: Logger = util.get_log('log/forward.log')
resume.log = log

def filter_newly_download(lago, resumes):
    for r in resumes:
        resume_id = r['id']
        name = r['candidateName']
        phone = r['phone']
        file_path = f'{config.resume_download_dir}/{name}-{phone}.pdf'
        if os.path.exists(file_path):
            log.info(f'文件{file_path}已存在')
        else:
            resume.download(lago, resume_id, file_path)
            yield resume_id, file_path


def filter_condition(lago, resumes):
    for resume_id, file_path in resumes:
        detail = resume.detail_by_id(lago, resume_id)
        candidate = resume.parse_detail(detail)
        log.info(str(candidate))
        if resume.match_all(candidate):
            yield file_path, detail


if __name__ == '__main__':

    if len(sys.argv) == 1:
        lago = config.lago_config['java']
        log.info(f'Use config java')
    else:
        config_key = sys.argv[1]
        lago = config.lago_config.get(config_key)
        log.info(f'Use config {config_key}')

    os.makedirs(config.resume_download_dir, exist_ok=True)
    resumes = resume.complete_list(lago)
    downloads = filter_newly_download(lago, resumes)
    need_sends = list(filter_condition(lago, downloads))

    if need_sends:
        mail = mail.Email(config.email_sender, config.email_smtp_sever, config.email_sender, config.email_password)
        now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        title = f'{now} 收到简历{len(need_sends)}份'
        content = ''.join([str(resume.parse_detail(detail)) for _, detail in need_sends])
        attaches = [file_path for file_path, _ in need_sends]
        mail.send(config.email_receivers, title, content, attaches)
        log.info(title)
