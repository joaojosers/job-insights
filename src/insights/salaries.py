from typing import Dict, Tuple, Union, List
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

    def validate_salary(self, salary: Union[str, int]) -> float:
        try:
            return float(salary)
        except (ValueError, TypeError):
            raise ValueError("salary deve ser do tipo float")

    def is_numeric_key_present(self, job: Dict, key: str) -> bool:
        return key in job and str(job[key]).replace(".", "").isdigit()

    def extract_salary_range(self, job: Dict):
        min_salary = float(job.get("min_salary", 0))
        max_salary = float(job.get("max_salary", float("inf")))
        return min_salary, max_salary

    def check_numeric_key(self, job: Dict, key: str) -> None:
        if not self.is_numeric_key_present(job, key):
            raise ValueError(f"Chave {key} obrigatória com valor numérico.")

    def get_salary_range(self, job: Dict) -> Tuple[float, float]:
        try:
            return self.extract_salary_range(job)
        except (ValueError, TypeError):
            raise ValueError("Erro ao extrair faixa salarial")

    def matches_salary_range(self, job: Dict, salary: Union[str, int]) -> bool:
        for key in ["min_salary", "max_salary"]:
            self.check_numeric_key(job, key)

        min_salary, max_salary = self.get_salary_range(job)

        if min_salary > max_salary:
            raise ValueError("Erro ao validar salary/conversão float")

        validated_salary = self.validate_salary(salary)

        return min_salary <= validated_salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
