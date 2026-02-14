import sys

def solve():
    line1 = sys.stdin.readline().strip()
    if not line1: return
    n = int(line1)
    
    line2 = sys.stdin.readline().strip()
    if not line2:
        a = []
    else:
        a = list(map(int, line2.split()))

    if n < 3:
        is_ready = True
        for i in range(n - 1):
            if a[i] > a[i+1]:
                is_ready = False
        if is_ready:
            print("YES")
            print(0)
        else:
            print("NO")
        return

    target = list(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]

    def get_counts(arr):
        odds = {}
        evens = {}
        for idx, val in enumerate(arr):
            if (idx + 1) % 2 == 0:
                evens[val] = evens.get(val, 0) + 1
            else:
                odds[val] = odds.get(val, 0) + 1
        return odds, evens

    a_odds, a_evens = get_counts(a)
    t_odds, t_evens = get_counts(target)

    if a_odds != t_odds or a_evens != t_evens:
        print("NO")
        return

    moves = []
    curr_a = list(a)

    for i in range(n):
        target_val = target[i]
        find_idx = -1
        for j in range(i, n):
            if curr_a[j] == target_val and (j % 2 == i % 2):
                find_idx = j
                break
        
        while find_idx > i:
            start = find_idx - 1 
            end = find_idx + 1
            moves.append((start, end))
            
            left = find_idx - 2
            curr_a[left], curr_a[find_idx] = curr_a[find_idx], curr_a[left]
            find_idx -= 2

    print("YES")
    print(len(moves))
    for m in moves:
        print(f"{m[0]} {m[1]}")

if __name__ == "__main__":
    solve()