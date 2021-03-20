from typing import NamedTuple


class Candidate(NamedTuple):
    resume_id: str
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
