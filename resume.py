import datetime
import json
import re
import time
from logging import Logger
from typing import NamedTuple

import requests

import config

log: Logger = None


def request_internal(method, headers, payload, url):
    if config.debug:
        log.info(f"请求：{url}")
    text = requests.request(method, url, headers=headers, data=payload).text
    if config.debug:
        log.info(f"响应：{text}")
    time.sleep(20)
    resp = json.loads(text)
    return resp


def request_download(headers, url, path):
    if config.debug:
        log.info(f"请求：{url}")
    response = requests.request('GET', url, headers=headers, data={})
    with open(path, "wb") as code:
        code.write(response.content)
    time.sleep(3 if config.debug else 10)
    log.info(f"下载简历：{path}")


def complete_list(lago):
    url = "https://easy.lagou.com/can/new/list.json"
    payload = {}
    headers = {
        'authority': 'easy.lagou.com',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'x-anit-forge-code': 'c9c65a1c-52ed-4300-89f8-3ae30c19dc55',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'x-anit-forge-token': 'bdc48c56-0771-4b67-97a3-d836508be0b4',
        'origin': 'https://easy.lagou.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://easy.lagou.com/resume/list.htm?can=false&famousCompany=0&needQueryAmount=false&pageNo=3',
        'accept-language': 'zh-CN,zh;q=0.9,ta;q=0.8,en;q=0.7',
        'cookie': lago.cookie
    }

    j = request_internal('POST', headers, payload, url)
    return j['content']['rows']


def list(lago, page):
    url = "https://easy.lagou.com/talent/rec/%s.json?positionId=%s&showId=51fdfb4d4979458ba247963f62f6633b&notSeen=false&strongly=false" % (
        page, lago.root_position_id)
    payload = {}
    headers = {
        'authority': 'easy.lagou.com',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'x-anit-forge-code': '96f9dfb0-8de0-4363-90f1-d7018580a4b0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-anit-forge-token': '2a59077e-c25c-4184-9f9e-06be432b06db',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': (
                'https://easy.lagou.com/talent/index.htm?positionId=%s&showId=51fdfb4d4979458ba247963f62f6633b&notSeen=false&strongly=false&tab=rec&pageNo=%s' % (
            lago.root_position_id, page)),
        'accept-language': 'zh-CN,zh;q=0.9,ta;q=0.8,en;q=0.7',
        'cookie': lago.cookie
    }
    j = request_internal('GET', headers, payload, url)

    current_position_id = j['content']['data']['currentPosition']['positionId']
    result_list = j['content']['data']['page']['result']
    return current_position_id, result_list


def detail_by_key(lago, fetch_key, expect_job_id):
    url = f"https://easy.lagou.com/search/resume/fetchResume.json?resumeFetchKey={fetch_key}==&expectJobId={expect_job_id}"

    payload = {}
    headers = {
        'authority': 'easy.lagou.com',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'x-anit-forge-code': '96f9dfb0-8de0-4363-90f1-d7018580a4b0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-anit-forge-token': '2a59077e-c25c-4184-9f9e-06be432b06db',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://easy.lagou.com/talent/index.htm?positionId=7815536&showId=51fdfb4d4979458ba247963f62f6633b&notSeen=false&strongly=false&tab=rec&pageNo=1&show_id=51fdfb4d4979458ba247963f62f6633b',
        'accept-language': 'zh-CN,zh;q=0.9,ta;q=0.8,en;q=0.7',
        'cookie': lago.cookie
    }

    j = request_internal('GET', headers, payload, url)
    return j['content']['data']['data']


def detail_by_id(lago, resume_id):
    url = f"https://easy.lagou.com/resume/order/{resume_id}.json?"
    payload = {}
    headers = {
        'authority': 'easy.lagou.com',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'x-anit-forge-code': '',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'x-anit-forge-token': '',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://easy.lagou.com/can/new/index.htm?can=true&famousCompany=0&needQueryAmount=true&pageNo=1&pageSize=20&stage=NEW',
        'accept-language': 'zh-CN,zh;q=0.9,ta;q=0.8,en;q=0.7',
        'cookie': lago.cookie
    }

    j = request_internal('GET', headers, payload, url)
    return j['content']['data']['resumeVo']


def invite(lago, user_id, position_id):
    log.info('符合条件, 发送邀请')

    url = (f"https://easy.lagou.com/im/chat/colleagueChatInfo.json?cUserId={user_id}&positionId={position_id}")

    payload = {}
    headers = {
        'authority': 'easy.lagou.com',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'x-anit-forge-code': 'ed411628-6d85-4181-8ee7-0566fef47007',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'x-anit-forge-token': '0c2c9280-4587-4e48-bf9a-96a2a86c002d',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://easy.lagou.com/talent/index.htm?positionId=7815536&showId=fb812673629f43f28ff64c2d4d584039&notSeen=false&strongly=false&tab=rec&pageNo=1&show_id=fb812673629f43f28ff64c2d4d584039',
        'accept-language': 'zh-CN,zh;q=0.9,ta;q=0.8,en;q=0.7',
        'cookie': lago.cookie
    }

    j = request_internal('GET', headers, payload, url)
    session_id = j['content']['data']['sameCAndPositionChatInfo']['sessionId']

    url = f"https://easy.lagou.com/im/session/batchCreate/{session_id}.json"

    payload = (f"greetingId={lago.greeting_id}&positionId={position_id}&inviteDeliver=true")
    headers = {
        'authority': 'easy.lagou.com',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'x-anit-forge-code': 'ed411628-6d85-4181-8ee7-0566fef47007',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-anit-forge-token': '0c2c9280-4587-4e48-bf9a-96a2a86c002d',
        'origin': 'https://easy.lagou.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://easy.lagou.com/talent/index.htm?positionId=7815536&showId=fb812673629f43f28ff64c2d4d584039&notSeen=false&strongly=false&tab=rec&pageNo=1&show_id=fb812673629f43f28ff64c2d4d584039',
        'accept-language': 'zh-CN,zh;q=0.9,ta;q=0.8,en;q=0.7',
        'cookie': lago.cookie
    }

    request_internal('POST', headers, payload, url)


def send_msg(position_id, user_id, msg):
    url = "https://easy.lagou.com/im/chat/send/{user_id}.json"

    payload=f"content={msg}&attach=9rchwz5diyc&lagouPositionId={position_id}&msgType=0"
    headers = {
    'authority': 'easy.lagou.com',
    'accept': 'application/json, text/plain, */*',
    'x-anit-forge-code': '3ecc0238-c1e6-4377-9551-240fded53905',
    'x-requested-with': 'XMLHttpRequest',
    'x-anit-forge-token': 'fdcc0155-88b8-4885-980d-d3562c1e7187',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://easy.lagou.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://easy.lagou.com/im/chat/index.htm?',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': lago.cookie
    }
    
    request_internal('POST', headers, payload, url)


def download(lago, resume_id, path):
    url = f"https://easy.lagou.com/resume/download.htm?resumeId={resume_id}&preview=2"
    headers = {
        'authority': 'easy.lagou.com',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://easy.lagou.com/resume/list.htm?can=false&famousCompany=0&needQueryAmount=false&pageNo=1',
        'accept-language': 'zh-CN,zh;q=0.9,ta;q=0.8,en;q=0.7',
        'cookie': lago.cookie
    }
    request_download(headers, url, path)


class Candidate(NamedTuple):
    name: str
    sex: str
    age: int
    employ_type: str
    phone: str
    email: str
    education: str
    birthday: str
    expect_least_salary: int
    college_name: str
    subject: str
    graduate_year: int
    fresh_graduate: bool
    work_years: int
    out_school_years: int
    over_year_work: bool
    work_exp_num: int
    graduate_delay_year: int
    
    def html(self):
        return f'''
        <tr>
        <td>{self.employ_type}</td>
        <td>{self.name}</td>
        <td>{self.sex} </td>
        <td>{self.college_name} </td>
        <td>{self.education} </td>
        <td>{self.subject}</td>
        <td>{self.graduate_year}毕业 </td>
        <td>毕业{self.out_school_years}年</td>
        <td>工作{self.work_years}年</td>
        <td>{self.work_exp_num}段经历{'' if self.over_year_work else ' 均未超过一年'}</td>
        <td>{self.birthday} </td>
        <td>{str(self.age) + '岁' if self.age > 0 else '年龄未知'}</td>
        <td>{self.phone} </td>
        <td>{self.email}</td>
        <td>{self.expect_least_salary}k</td>
        </tr>
        '''

    def __str__(self):
        return f"{self.employ_type} {self.name} {self.sex} {self.college_name} {self.education} {self.subject} {self.graduate_year}毕业 毕业{self.out_school_years}年 工作{self.work_years}年（{self.work_exp_num}段经历{'' if self.over_year_work else ' 均未超过一年'}） 预期{self.expect_least_salary}k {self.birthday} {str(self.age) + '岁' if self.age > 0 else '年龄未知'} {self.phone} {self.email}"


def parse_detail(detail):
    name = detail['name']
    age = int(detail['ageNum'])
    sex = detail['sex']
    phone = detail.get('phone', '')
    email = detail.get('email', '')
    # 判定学历
    match_education = re.match('小学|初中|高中|专科|本科|硕士|博士', detail['highestEducation'])
    if match_education:
        highest_education = match_education.group()
    else:
        highest_education = '未知'
    for school in detail['educationExperiences']:
        education = school['education']
        if '大专' in education and '本科' in highest_education:
            highest_education = '专升本'
            break

    birthday = detail['birthday']
    birthyear = detail['birthYear']
    salarys = detail['expectJob']['salarys']
    expect_least_salary = int(salarys.split('-')[0].rstrip('k'))
    college = detail['latestEducationExperience']
    college_name = college['schoolName']
    subject = college['professional']
    graduate_date = college['endDate']
    graduate_year = date_to_year(graduate_date)
    out_school_years = datetime.datetime.now().year - graduate_year

    if highest_education == '本科' and birthyear > 0:
        delay_year = graduate_year - birthyear - config.bachelor_graduate_age
        graduate_delay_year = 0 if delay_year < 0 else delay_year
    else:
        graduate_delay_year = 0

    now = datetime.datetime.now()

    # 毕业季前，今年毕业的是应届，毕业季后，明年毕业的是应届
    fresh_graduate = (now.month <= config.graduate_month and now.year == graduate_year) \
            or (now.month > config.graduate_month and now.year + 1 == graduate_year)


    workYear = detail['workYear']
    work_years = workYear.rstrip('年') if workYear.endswith('年') else 0
    work_experiences = detail['workExperiences']
    work_exp_num = len(work_experiences)
    over_year_work = has_over_year_work(work_experiences)
    return Candidate(name=name,
                     age=age,
                     sex=sex,
                     employ_type='待定',
                     phone=phone,
                     email=email,
                     education=highest_education,
                     birthday=birthday,
                     expect_least_salary=expect_least_salary,
                     college_name=college_name,
                     subject=subject,
                     graduate_year=graduate_year,
                     fresh_graduate=fresh_graduate,
                     work_years=work_years,
                     out_school_years=out_school_years,
                     work_exp_num=work_exp_num,
                     over_year_work=over_year_work,
                     graduate_delay_year=graduate_delay_year
                     )


def date_to_year(date):
    if date == '至今':
        return datetime.datetime.now().year
    try:
        year = datetime.datetime.strptime(date, '%Y.%m').year
    except:
        year = datetime.datetime.strptime(date, '%Y').year
    return year


def has_over_year_work(work_experiences):
    for w in work_experiences:
        try:
            start = w['startDate']
            end = w['endDate']
        except:
            # 未填写在职时间
            continue
        now = datetime.datetime.now()
        start_time = now if start == '至今' else datetime.datetime.strptime(start, '%Y.%m')
        end_time = now if end == '至今' else datetime.datetime.strptime(end, '%Y.%m')
        if (end_time - start_time).days > 365:
            return True
    return False


def match_all(employ_types: set, candidate: Candidate):
    for employ_type, match in config.matchers:
        if employ_type not in employ_types:
            continue
        reasons = match(candidate)
        if reasons:
            log.info(f'{candidate.name} 不符合{employ_type}条件：\n' + '\n'.join(f'\t{i + 1}. {r}' for i, r in enumerate(reasons)))
        else:
            log.info(f'{candidate.name} 符合{employ_type}条件')
            return employ_type
    return None

