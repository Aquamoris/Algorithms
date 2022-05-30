def uniform_binary_search(array, key):
    array.sort()
    print(array)
    m, i, count_of_steps = int(len(array)/2), int(len(array)/2), 0
    print(m, i)
    while m != 0:
        if array[i] == key:
            print(f'We use {count_of_steps + 1} steps and')
            return f'Well! Index of {key} is {i}'
        elif array[i] < key:
            i += round(m/2)
            m = int(m/2)
            print(m, i)
            count_of_steps += 1
        elif array[i] > key:
            i -= round(m/2)
            m = int(m/2)
            print(m, i)
            count_of_steps += 1
    return f'We have no {key}'
  
  
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
    print(years)
    print(uniform_binary_search(years, 15))
    
    
if __name__ == '__main__':
    main()
