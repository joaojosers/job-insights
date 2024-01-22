from typing import Dict, Union, List
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

    def matches_salary_range(self, job: Dict, salary: Union[str, int]) -> bool:
        # Verifica a presença e validade das chaves min_salary e max_salary no dicionário
        for key in ["min_salary", "max_salary"]:
            if key not in job or (
                not str(job[key]).replace(".", "").isdigit()
            ):
                raise ValueError(
                    f"chave {key} obrigatória com valor numérico."
                )
            #  tratar salary
            try:
                salary == float(salary)
            except (ValueError, TypeError):
                raise ValueError("salary tipo float")

            # Converte os valores de min_salary, max_salary e salary para números
            try:
                min_salary, max_salary, salary = map(
                    float,
                    (
                        job.get("min_salary", 0),
                        job.get("max_salary", float("inf")),
                        salary or 0,
                    ),
                )
            except (ValueError, TypeError):
                raise ValueError("")
        # Verifica se min_salary é maior que max_salary
        if min_salary > max_salary:
            raise ValueError("min_salary não maior que max_salary")

        # Retorna True se o salário estiver dentro da faixa salarial, caso contrário, retorna False
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
