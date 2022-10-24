from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "Python") == 1639
    assert count_ocurrences("src/jobs.csv", "Java") == 676
    assert count_ocurrences("src/jobs.csv", "JavaScript") == 122
    assert count_ocurrences("src/jobs.csv", "C++") == 236
    assert count_ocurrences("src/jobs.csv", "PHP") == 36
    assert count_ocurrences("src/jobs.csv", "R") == 544538
    assert count_ocurrences("src/jobs.csv", "C#") == 57
