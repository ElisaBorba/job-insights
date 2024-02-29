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
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


merda = ProcessJobs()
test = merda.read("data/jobs.csv")
lista = merda.jobs_list

print("TESTAAA", lista)
