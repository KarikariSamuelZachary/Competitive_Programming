if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(arr, reverse = True)
    if len(arr) == n:
        Winner = max(arr)
        arr = [num for num in arr if num != Winner]
        Runner_up = max(arr)
            
print(Runner_up)