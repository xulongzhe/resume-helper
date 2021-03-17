import datetime

import config
from resume import Candidate


def match_fresh_graduate(candidate: Candidate) -> list:
    reasons = []
    if not candidate.fresh_graduate:
        reasons.append('非应届生')

    # 非本科和硕士不考虑
    if candidate.education not in ['本科', '硕士']:
        reasons.append('学历本科以下或专升本')

    # 薪资预期过高的不要
    provide_salary = candidate.out_school_years + (
        config.bachelor_salary if candidate.education == '本科' else config.master_salary) + config.max_salary_float_formal
    if candidate.expect_least_salary > provide_salary:
        reasons.append(
            f'预期薪资过高：{candidate.education} 毕业{candidate.out_school_years}年 {candidate.expect_least_salary}k（建议{provide_salary}k）')

    if candidate.age > config.max_age:
        reasons.append(f'年龄过大：{candidate.age}')
    return reasons


def match_intern(candidate: Candidate) -> list:
    reasons = []
    if datetime.datetime.now().year - candidate.graduate_year < 1:
        reasons.append('实习时间不足1年')

    # 非本科和硕士不考虑
    if candidate.education not in ['本科', '硕士']:
        reasons.append('学历本科以下或专升本')

    # 薪资预期过高的不要
    provide_salary = config.intern_salary + config.max_salary_float_formal
    if candidate.expect_least_salary > provide_salary:
        reasons.append(
            f'预期薪资过高：{candidate.education} 毕业{candidate.out_school_years}年 {candidate.expect_least_salary}k（建议{provide_salary}k）')

    if candidate.age > config.max_age:
        reasons.append(f'年龄过大：{candidate.age}')
    return reasons


def match_outsource(candidate: Candidate) -> list:
    reasons = []

    # 没毕业
    if candidate.out_school_years <= 0:
        reasons.append('还没毕业')

    # 毕业延迟年份过多
    if candidate.graduate_delay_year > config.max_graduate_delay_years:
        reasons.append(f'毕业延迟年份过多: {candidate.graduate_delay_year}')

    # 非本科和硕士不考虑
    if candidate.education not in ['本科', '硕士']:
        reasons.append('学历本科以下或专升本')

    # 薪资预期过高的不要
    provide_salary = candidate.out_school_years + config.outsource_salary + config.max_salary_float_formal
    if candidate.expect_least_salary > provide_salary:
        reasons.append(
            f'预期薪资过高：{candidate.education} 毕业{candidate.out_school_years}年 {candidate.expect_least_salary}k（建议{provide_salary}k）')

    if candidate.age > config.max_age:
        reasons.append(f'年龄过大：{candidate.age}')

    return reasons


def match_formal(candidate: Candidate):
    reasons = []

    # 没毕业
    if candidate.out_school_years <= 0:
        reasons.append('还没毕业')

    # 毕业延迟年份过多
    if candidate.graduate_delay_year > config.max_graduate_delay_years:
        reasons.append(f'毕业延迟年份过多: {candidate.graduate_delay_year}')

    # 非本科和硕士不考虑
    if candidate.education not in ['本科', '硕士']:
        reasons.append('学历本科以下或专升本')

    # 大学
    if candidate.college_name not in config.top_college_global and \
            candidate.college_name not in config.top_college_china and \
            candidate.subject not in config.top_class_subject.get(candidate.college_name, []):
        reasons.append(f'学校排名靠后并且非一级学科： {candidate.college_name} {candidate.subject}')

    # 薪资预期过高的不要
    provide_salary = candidate.out_school_years + (
        config.bachelor_salary if candidate.education == '本科' else config.master_salary) + config.max_salary_float_formal
    if candidate.expect_least_salary > provide_salary:
        reasons.append(
            f'预期薪资过高：{candidate.education} 毕业{candidate.out_school_years}年 {candidate.expect_least_salary}k（建议{provide_salary}k）')

    if candidate.age > config.max_age:
        reasons.append(f'年龄过大：{candidate.age}')

    return reasons
