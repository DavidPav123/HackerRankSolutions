if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    top_score = arr[0]
    runner_up = None

    for i in arr:
        if i > top_score:
            runner_up = top_score
            top_score = i
        if runner_up == None and i < top_score:
            runner_up = i 
        if runner_up != None:
            if i > runner_up and i < top_score:
                runner_up = i 

    print(runner_up)