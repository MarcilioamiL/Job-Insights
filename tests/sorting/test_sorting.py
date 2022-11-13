from src.sorting import sort_by

jobs = [
        {"date_posted": "13.05.2022", "max_salary": 20000, "min_salary": 9000},
        {"date_posted": "05.06.2022", "max_salary": 10000, "min_salary": 5000},
        {"date_posted": "02.07.2022", "max_salary": 5000, "min_salary": 3000},
    ]

result_sort_max = [jobs[0], jobs[1], jobs[2]]
result_sort_min = [jobs[2], jobs[1], jobs[0]]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == result_sort_min

    sort_by(jobs, "max_salary")
    assert jobs == result_sort_max
