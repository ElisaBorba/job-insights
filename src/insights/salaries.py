from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs
from numbers import Real

# from jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary_list = [
            int(item["max_salary"])
            for item in self.jobs_list
            if item["max_salary"].isnumeric()
        ]
        max_salary = max(max_salary_list)
        return max_salary

    def get_min_salary(self) -> int:
        min_salary_list = [
            int(item["min_salary"])
            for item in self.jobs_list
            if item["min_salary"].isnumeric()
        ]
        min_salary = min(min_salary_list)
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if (
            "min_salary" not in job
            or "max_salary" not in job
            or job["min_salary"] is None
            or job["max_salary"] is None
            or job["min_salary"] == ""
            or job["max_salary"] == ""
            or salary is None
            or salary == ""
        ):
            raise ValueError("salaries's values cannot be empty!")

        if not isinstance(job["max_salary"], Real) or not isinstance(
            job["min_salary"], Real
        ):
            raise ValueError("salaries must be numericals!")

        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError("max_salary must be greater than min_salary!")

        min_salary, max_salary = int(job["min_salary"]), int(job["max_salary"])
        if min_salary > max_salary:
            raise ValueError("max_salary must be greater than min_salary!")

        return min_salary <= int(salary) <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass


# instancia = ProcessSalaries()
# instancia.read("data/jobs.csv")

# lista = instancia.jobs_list
# teste = instancia.matches_salary_range({"min_salary": 600}, 700)

# print("PRETENSÃO", teste)
