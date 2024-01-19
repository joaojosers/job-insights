from src.pre_built.counter import count_ocurrences


def test_counter():
    # path = "/Users/joaojose/Documents/trybe-projects-cs/sd-032-a-project-job-insights/data/jobs.csv"
    path = "data/jobs.csv"
    word = "nurse"
    assert count_ocurrences(path, word) == 276
