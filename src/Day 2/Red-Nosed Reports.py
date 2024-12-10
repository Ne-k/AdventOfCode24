def is_safe(levels):
    if all(levels[i] > levels[i+1] for i in range(len(levels)-1)) or all(levels[i] < levels[i+1] for i in range(len(levels)-1)):
        return all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels)-1))
    return False

def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    return False

def count_safe_reports(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        reports = file.readlines()
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_with_dampener(levels):
            safe_count += 1
    return safe_count

# Input file path
file_path = 'input.txt'

print(count_safe_reports(file_path))
