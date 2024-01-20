from typing import Union, List, Dict
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
        # Inicializa com um valor grande para garantir que qualquer salário seja menor
        min_salary = float("inf")

        for job in self.jobs_list:
            salary_range = job.get("min_salary")
            if salary_range and salary_range.isdigit():
                salary = int(salary_range)
                min_salary = min(min_salary, salary)

        # Retorna 0 se não houver salários válidos
        return min_salary if min_salary != float("inf") else 0

    # def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
    #     pass

    def matches_salary_range(self, job: Dict, salary: str) -> bool:
        # Verifica se as chaves min_salary e max_salary estão presentes no dicionário
        if (
            "min_salary" not in job
            or job["min_salary"] is None
            or "max_salary" not in job
            or job["max_salary"] is None
        ):
            raise ValueError(
                "As chaves min_salary e max_salary são obrigatórias no dicionário."
            )

        # Converte os valores de min_salary e max_salary para números
        try:
            print(job["min_salary"])
            min_salary = float(job["min_salary"])
            max_salary = float(job["max_salary"])
        except ValueError:
            raise ValueError(
                "As chaves min_salary e max_salary devem ter valores numéricos."
            )
        except TypeError:
            raise ValueError
        # Verifica se min_salary é maior que max_salary
        if min_salary > max_salary:
            raise ValueError(
                "O valor de min_salary não pode ser maior que max_salary."
            )

        # Converte o valor de salary para número
        try:
            salary = float(salary)
        except TypeError:
            raise ValueError
        except ValueError:
            raise ValueError("O parâmetro salary deve ter valor numérico.")

        # Retorna True se o salário estiver dentro da faixa salarial, caso contrário, retorna False
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
