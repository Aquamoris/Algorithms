def character_by_character(first_string, second_string):
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            return False
    return True


def hash_function(string):
    hash_size = 0
    for i in string:
        hash_size += ord(i)
    return hash_size


# def rabin_karp_alg(string, pattern, amount):
#     count = 0
#     length_string, length_pattern = len(string), len(pattern)
#     hash_pattern = hash_function(pattern)
#     for i in range(length_string-length_pattern+1):  # [...+1]
#         hash_string = hash_function(string[i:i+length_pattern])
#         # print('S: ' + string[i:i+length_pattern])
#         # print('P: ' + pattern)
#         if hash_string == hash_pattern:
#             if character_by_character(string[i:i+length_pattern], pattern):
#                 count += 1
#     # print(count, '\n')
#     if count == amount:
#         return True
#     else:
#         return False

def rabin_karp_alg(string, pattern, amount):
    count = 0
    length_string, length_pattern = len(string), len(pattern)
    hash_pattern = hash_function(pattern)

    hash_string = hash_function(string[0:length_pattern])

    for i in range(int(length_string-length_pattern+1)):
        if hash_string == hash_pattern:
            if character_by_character(string[i:i+length_pattern], pattern):
                count += 1
        hash_string -= hash_function(string[i:i+length_pattern])
        hash_string += hash_function(string[i+1:i+length_pattern+1])

    if count == amount:
        return True
    else:
        return False


with open('data.txt', 'r') as f:
    list_of_strings = []
    number_of_strings = int(f.readline())
    for _ in range(number_of_strings):
        list_of_strings.append(f.readline()[:-1])


list_of_searched_strings = []


for i in list_of_strings:
    if rabin_karp_alg(i.split()[1], 'нн', 1) and rabin_karp_alg(i.split()[3], 'р', 2):
        list_of_searched_strings.append(i)


with open('result.txt', 'w') as f:
    for i in list_of_searched_strings:
        f.write(str(i) + '\n')

