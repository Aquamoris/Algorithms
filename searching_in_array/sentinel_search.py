def sentinel_search(array, key):
    index, array_length = 0, len(array)
    array.append(key)
    print(array)

    while array[index] != key:
        index += 1

    print(f'We use {index + 1} steps to search and...')
    return f'We have no {key}' if index == array_length else f'Index of {key} is {index}'
  

def reading_from_file(file):
    with open(file, 'r') as f:
        records = int(f.readline())
        data_list = []
        for _ in range(records):
            data_list.append(f.readline().split())
        # data_list = [line.rstrip() for line in data_list]  # delete '/n' with reading
        years = []
        for i in data_list:
            years.append(int(i[2]))
    return years
  
def main():
    years = reading_from_file('data.txt')
    print(sentinel_search(years, 100))
    
    
if __name__ == '__main__':
    main()
