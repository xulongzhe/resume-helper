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
            log.info(f'简历 {os.path.basename(file_path)} 已存在')
        else:
            resume.download(lago, resume_id, file_path)
            yield resume_id, file_path


def filter_condition(lago, resumes):
    for resume_id, file_path in resumes:
        detail = resume.detail_by_id(lago, resume_id)
        candidate = resume.parse_detail(detail)
        log.info(str(candidate))
        emp_type = resume.match_all(lago.employ_types, candidate)
        candidate._replace(employ_type=emp_type)
        if emp_type:
            yield file_path, candidate


def forward(lago):
    log.info(f'=== 岗位：{lago.name} ===')
    os.makedirs(config.resume_download_dir, exist_ok=True)
    resumes = resume.complete_list(lago)
    downloads = filter_newly_download(lago, resumes)
    need_sends = list(filter_condition(lago, downloads))
    if need_sends:
        m = mail.Email(config.email_sender, config.email_smtp_sever, config.email_sender, config.email_password)
        now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        title = f'{now} 收到简历{len(need_sends)}份'
        content = '\n'.join([str(candidate) for _, candidate in need_sends])
        attaches = [file_path for file_path, _, in need_sends]
        m.send(lago.email_receivers, title, content, attaches)
        log.info(title)
    else:
        log.info('没有收到新的简历')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        forward(config.lago_config[sys.argv[1]])
    else:
        for key, lago in config.lago_config.items():
            forward(lago)
