from typing import Union, List, Dict

from src.insights.jobs import ProcessJobs

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
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass


# MAX_SALARY = 383416

# instancia = ProcessSalaries()
# instancia.read("data/jobs.csv")

# lista = instancia.jobs_list
# max = instancia.get_max_salary()
# min = instancia.get_min_salary()

# print("MAX SALARY", max)
# print("MIN SALARY", min)
