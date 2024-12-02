from collections import Counter

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_lists(self):
        left_list = []
        right_list = []

        with open(self.filename, 'r') as file:
            for line in file:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)

        return left_list, right_list

class ListProcessor:
    def __init__(self, left_list, right_list):
        self.left_list = left_list
        self.right_list = right_list

    def total_distance(self):
        self.left_list.sort()
        self.right_list.sort()

        total_diff = sum(abs(l - r) for l, r in zip(self.left_list, self.right_list))
        return total_diff

    def similarity_score(self):
        right_counter = Counter(self.right_list)

        similarity_score = 0
        for num in self.left_list:
            similarity_score += num * right_counter[num]

        return similarity_score

filename = 'input.txt'
file_reader = FileReader(filename)
left_list, right_list = file_reader.read_lists()

list_processor = ListProcessor(left_list, right_list)
print(list_processor.similarity_score())
print(list_processor.total_distance())
