def read_input():
    return [int(el) for el in input().split(", ")], int(input())


def min_cycles_for_job(jobs, job_index):
    sorted_jobs = sorted(
        [(value, index) for (index, value) in enumerate(jobs)]
    )
    cycles = 0
    for (job, index) in sorted_jobs:
        cycles += job
        if index == job_index:
            break
    return cycles


def print_result(res):
    print(res)


(jobs, job_index) = read_input()
result = min_cycles_for_job(jobs, job_index)
print_result(result)


###########################################################################
### simplified - no comprehenison used in min_cycles_for_job func


def read_input():
    return [int(el) for el in input().split(", ")], int(input())


def min_cycles_for_job(jobs, job_index):
    sorted_jobs = []
    for index, value in enumerate(jobs):
        sorted_jobs.append((value, index))
    sorted_jobs = sorted(sorted_jobs)

    cycles = 0
    for job, index in sorted_jobs:
        cycles += job
        if index == job_index:
            break
    return cycles


def print_result(res):
    print(res)


(jobs, job_index) = read_input()
result = min_cycles_for_job(jobs, job_index)
print_result(result)