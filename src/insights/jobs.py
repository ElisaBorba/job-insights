from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()
        filter_criteria = {}

    def read(self, path: str) -> List[Dict]:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        job_type_list = [item["job_type"] for item in self.jobs_list]
        return list(set(job_type_list))

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


merda = ProcessJobs()
test = merda.read("data/jobs.csv")
lista = merda.get_unique_job_types()

print("TESTAAA", lista)
