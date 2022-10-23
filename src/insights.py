from src.jobs import read

"""Conjuntos(set) Um conjunto é uma coleção de elementos únicos e não
ordenados. Conjuntosimplementam operações de união, intersecção e outras."""


def get_unique_job_types(path):
    set_job = set()  # set of unique jobs
    for dado in read(path):  # read the directory
        set_job.add(dado["job_type"])  # add the job type to the list
    return set_job


def filter_by_job_type(jobs, job_type):
    """list comprehension"""
    return [dado for dado in jobs if dado["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them"""
    set_unique_industries = set()
    for dado in read(path):
        if dado["industry"] != "":
            set_unique_industries.add(dado["industry"])
    return set_unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry, list comprehension"""
    return [dado for dado in jobs if dado["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs, the method return true or false"""
    max_salary_set = set()
    for dado_salary in read(path):
        if dado_salary['max_salary'].isdigit():
            max_salary_set.add(int(dado_salary["max_salary"]))
    return max(max_salary_set)


def get_min_salary(path):
    """Get the minimum salary of all jobs"""
    min_salary_set = set()
    for dado_salary in read(path):
        if dado_salary['min_salary'].isdigit():
            min_salary_set.add(int(dado_salary["min_salary"]))
    return min(min_salary_set)


def get_salary_f_complex(j, s):
    if int(j["min_salary"] > j["max_salary"]):
        raise ValueError
    elif type(s) != int:
        raise ValueError
    return j["min_salary"] <= s < j["max_salary"]


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job
    no complexity error"""
    try:
        return get_salary_f_complex(job, salary)
    except KeyError:
        raise ValueError

    except TypeError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
