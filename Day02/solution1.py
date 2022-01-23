# load data from input.txt
input_path = 'input.txt'

with open(input_path) as f:
    lines = f.readlines()
f.close()

data = [line.replace("\n","").split(":") for line in lines]

counter = 0

for el in data:
    policy = el[0]
    pswd = el[1].strip()
    char_range, char = policy.split(" ")
    min_char, max_char = char_range.split("-")
    if pswd.count(char) in range(int(min_char), int(max_char)+1):
        counter += 1

# print("aaabbbccc".count("c") in range(2,3))
print(f"Answer: {counter}")
