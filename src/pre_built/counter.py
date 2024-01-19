def count_ocurrences(path: str, word: str) -> int:
    file = open(path, "r")
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    return word_count
path = "/Users/joaojose/Documents/trybe-projects-cs/sd-032-a-project-job-insights/data/jobs.csv"
word = "nurse"
resultado = count_ocurrences(path, word)
print(resultado)