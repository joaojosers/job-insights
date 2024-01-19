from typing import List
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path):
        with open(path, "r", newline="") as file:
            csv_reader = csv.DictReader(file)
            self.jobs_list = [dict(row) for row in csv_reader]

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set()

        for job in self.jobs_list:
            job_type = job.get("job_type", "")

            if job_type:
                unique_job_types.add(job_type)
        print(unique_job_types)
        return list(unique_job_types)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


# process = ProcessJobs()
# process.read("data/jobs.csv")
# result = process.get_unique_job_types()
# print(result)
