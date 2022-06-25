if __name__ == '__main__':
    N = int(input())

    arr = []

    for i in range(0, N):
        temp_arr = list(input().split())
        
        if temp_arr[0] == "insert":
            arr.insert(int(temp_arr[1]), int(temp_arr[2]))
        elif temp_arr[0] == "print":
            print(arr)
        elif temp_arr[0] == "remove":
            arr.remove(int(temp_arr[1]))
        elif temp_arr[0] == "append":
            arr.append(int(temp_arr[1]))
        elif temp_arr[0] == "sort":
            arr.sort()
        elif temp_arr[0] == "pop":
            arr.pop()
        elif temp_arr[0] == "reverse":
            arr.reverse()

        temp_arr.clear()
