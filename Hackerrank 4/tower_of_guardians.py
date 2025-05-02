# Punya Kevin Adi Santoso
N, P = map(int, input().split())
arr = [int(x) for x in input().split()]

def solve(arr, N, P, i):
    if i == N:
        return "YES"
    if P < arr[i]:
        return "NO"
    return solve(arr, N, P + arr[i], i + 1)

print(solve(arr, N, P, 0))