def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(filename):
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1

    return safe_count

filename = 'input.txt'
print(f"Number of safe reports: {count_safe_reports(filename)}")
