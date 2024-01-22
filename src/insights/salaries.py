# from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0

        for job in self.jobs_list:
            salary_range = job.get("max_salary")
            if salary_range and salary_range.isdigit():
                salary = int(salary_range)
                max_salary = max(max_salary, salary)

        return max_salary

    def get_min_salary(self) -> int:

        min_salary = float("inf")

        for job in self.jobs_list:
            salary_range = job.get("min_salary")
            if salary_range and salary_range.isdigit():
                salary = int(salary_range)
                min_salary = min(min_salary, salary)

        return min_salary if min_salary != float("inf") else 0
