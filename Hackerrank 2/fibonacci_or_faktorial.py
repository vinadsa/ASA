N = int(input())
arr = [int(x) for x in input().split()]
pilihan = int(input())

def fibonacci_or_faktorial(N, arr, pilihan):
    def fibonacci(N, arr):
        if N < 2:
            return arr[N]
        else:
            return fibonacci(arr[N-1], arr) + fibonacci(arr[N-2], arr)
    def faktorial(N, arr):
        if N < 0:
            return 0
        else:
            return arr[N]
        


