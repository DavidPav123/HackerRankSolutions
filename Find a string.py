def count_substring(string, sub_string):
    times_found = 0

    for i in range(0,len(string)):
        if str(string).find(sub_string,i, i+len(sub_string)) != (-1): 
            times_found += 1

    return times_found

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)