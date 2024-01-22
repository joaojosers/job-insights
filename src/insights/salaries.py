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

        min_salary = float("inf")

        for job in self.jobs_list:
            salary_range = job.get("min_salary")
            if salary_range and salary_range.isdigit():
                salary = int(salary_range)
                min_salary = min(min_salary, salary)

        return min_salary if min_salary != float("inf") else 0

    # def matches_salary_range(self, job: Dict, salary: str) -> bool:
    #     # Verifica a presença e validade das chaves min_salary e max_salary no dicionário
    #     for key in ["min_salary", "max_salary"]:
    #         if key not in job or (
    #             not isinstance(job[key], (int, float))
    #             and not str(job[key]).isdigit()
    #         ):
    #             raise ValueError(
    #                 f"A chave {key} é obrigatória e deve ter um valor numérico."
    #             )

    #     # Verifica se salary é válido
    #     if salary is not None and (
    #         not isinstance(salary, (int, float)) and not str(salary).isdigit()
    #     ):
    #         raise ValueError("O parâmetro salary deve ter valor numérico.")

    #     # Converte os valores de min_salary, max_salary e salary para números
    #     min_salary, max_salary, salary = map(
    #         float,
    #         (job["min_salary"] or 0, job["max_salary"] or 0, salary or 0),
    #     )

    #     # Verifica se min_salary é maior que max_salary
    #     if min_salary > max_salary:
    #         raise ValueError(
    #             "O valor de min_salary não pode ser maior que max_salary."
    #         )

    #     # Retorna True se o salário estiver dentro da faixa salarial, caso contrário, retorna False
    #     return min_salary <= salary <= max_salary

    # def filter_by_salary_range(
    #     self, jobs: List[dict], salary: Union[str, int]
    # ) -> List[Dict]:
    #     pass


# def matches_salary_range(self, job: Dict, salary: str) -> bool:

#     if (
#         "min_salary" not in job
#         or job["min_salary"] is None
#         or "max_salary" not in job
#         or job["max_salary"] is None
#     ):
#         raise ValueError(
#             "As chaves min_salary e max_salary são obrigatórias."
#         )

#     # Converte os valores de min_salary e max_salary para números
#     try:
#         print(job["min_salary"])
#         min_salary = float(job["min_salary"])
#         max_salary = float(job["max_salary"])
#     except ValueError:
#         raise ValueError(
#             "chaves min_salary e max_salary devem ter valores numéricos."
#         )
#     except TypeError:
#         raise ValueError
#     # Verifica se min_salary é maior que max_salary
#     if min_salary > max_salary:
#         raise ValueError(
#             "O valor de min_salary não pode ser maior que max_salary."
#         )

#     # Converte o valor de salary para número
#     try:
#         salary = float(salary)
#     except TypeError:
#         raise ValueError
#     except ValueError:
#         raise ValueError("O parâmetro salary deve ter valor numérico.")

#     return min_salary <= salary <= max_salary

# def matches_salary_range(self, job: Dict, salary: str) -> bool:
#     # Verifica a presença das chaves min_salary e max_salary no dicionário
#     for key in ['min_salary', 'max_salary']:
#         if key not in job or not str(job[key]).isdigit():
#             raise ValueError(f"A chave {key} é obrigatória e deve ter um valor numérico.")

#     # Converte os valores de min_salary, max_salary e salary para números
#     min_salary, max_salary, salary = map(float, (job['min_salary'], job['max_salary'], salary))

#     # Verifica se min_salary é maior que max_salary
#     if min_salary > max_salary:
#         raise ValueError("O valor de min_salary não pode ser maior que max_salary.")

#     # Retorna True se o salário estiver dentro da faixa salarial, caso contrário, retorna False
#     return min_salary <= salary <= max_salary

# def matches_salary_range(self, job: Dict, salary: str) -> bool:
#     # Verifica a presença e validade das chaves min_salary e max_salary no dicionário
#     for key in ['min_salary', 'max_salary']:
#         if key not in job or (not isinstance(job[key], (int, float)) and not str(job[key]).isdigit()):
#             raise ValueError(f"A chave {key} é obrigatória e deve ter um valor numérico.")

#     # Verifica se salary é válido
#     if not isinstance(salary, (int, float)) and not salary.isdigit():
#         raise ValueError("O parâmetro salary deve ter valor numérico.")

#     # Converte os valores de min_salary, max_salary e salary para números
#     min_salary, max_salary, salary = map(float, (job['min_salary'] or 0, job['max_salary'] or 0, salary or 0))

#     # Verifica se min_salary é maior que max_salary
#     if min_salary > max_salary:
#         raise ValueError("O valor de min_salary não pode ser maior que max_salary.")

#     # Retorna True se o salário estiver dentro da faixa salarial, caso contrário, retorna False
#     return min_salary <= salary <= max_salary
