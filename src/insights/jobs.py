from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path):
        with open(path, 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            self.job_list = [dict(row) for row in csv_reader]

        return self.job_list
    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
