import re


def extract_multiplications(memory):
    mul_pattern = re.compile(r'mul\(\d+,\d+\)')
    control_pattern = re.compile(r"do\(\)|don't\(\)")

    total_sum = 0
    enabled = True

    i = 0

    while i < len(memory):
        if memory[i:i + 3] == 'mul':
            if enabled:
                match = mul_pattern.match(memory, i)
                if match:
                    numbers = re.findall(r'\d+', match.group())
                    result = int(numbers[0]) * int(numbers[1])
                    total_sum += result
                    i = match.end()
                    continue

        control_match = control_pattern.match(memory, i)
        if control_match:
            if control_match.group() == "do()":
                enabled = True
            elif control_match.group() == "don't()":
                enabled = False
            i = control_match.end()
            continue

        i += 1

    return total_sum


def main():
    with open('input.txt', 'r') as file:
        memory = file.read()

    total_sum = extract_multiplications(memory)
    print(total_sum)


if __name__ == "__main__":
    main()
