from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        job_type_list = [item["job_type"] for item in self.jobs_list]
        return list(set(job_type_list))

    def filter_by_multiple_criteria(
        self, jobs: list, filter_criteria: dict
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError(f"{filter_criteria} must be Dictionary!")

        filtered_jobs = []
        for job in jobs:
            if all(
                job.get(key) == value for key, value in filter_criteria.items()
            ):
                filtered_jobs.append(job)

        return filtered_jobs


merda = ProcessJobs()
test = merda.read("data/jobs.csv")
jobs = [
    {"id": 1, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 2, "industry": "Healthcare", "job_type": "PART_TIME"},
    {"id": 3, "industry": "IT", "job_type": "FULL_TIME"},
]

lista = merda.filter_by_multiple_criteria(
    jobs, {"industry": "IT", "job_type": "FULL_TIME"}
)
print("LISTA", lista)
