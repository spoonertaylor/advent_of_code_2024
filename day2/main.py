# Advent of Code, Day 2
def read_input():
  reports = []
  with open("input_file.txt") as f:
    for line in f:
      reports.append([int(char) for char in line.strip().split(" ")])
  return reports

def is_safe(report):
    # Check to make sure always increasing or decreasing
    # If not true, not a safe report
    if report != sorted(report) and report != sorted(report, reverse = True):
        return False

    i = 1
    safe = True
    while i < len(report) and safe:
        diff = report[i-1] - report[i]
        if abs(diff) > 3 or diff == 0:
            safe = False
        i += 1
    return(safe)

def count_reports(reports):
    safe_reports = 0
    for r in reports:
        if is_safe(r):
            safe_reports += 1
    return safe_reports

def new_is_safe(report):
    # Go through each number, if you remove it and the report is safe
    # then the new report is safe
    if is_safe(report):
        return True
    else:
        for i in range(len(report)):
            report_new = report[:i] + report[(i+1):]
            if is_safe(report_new):
                return True
            else:
                continue
        return False

def count_fixed_reports(reports):
    safe_reports = 0
    for r in reports:
        if new_is_safe(r):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    reports = read_input()

    safe = count_reports(reports)
    print(f"Safe reports: {safe}")
    new_safe = count_fixed_reports(reports)
    print(f"New safe reports {new_safe}")
