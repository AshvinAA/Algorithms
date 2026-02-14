import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    t = next(it)
    out_lines = []
    for _ in range(t):
        n = next(it)
        id_num = [next(it) for _ in range(n)]
        marks = [next(it) for _ in range(n)]

        arr = [(marks[i], id_num[i], i) for i in range(n)]

        sorted_arr = sorted(arr, key=lambda x: (-x[0], x[1]))

        pos = [0] * n
        for sorted_pos, (_, _, orig_idx) in enumerate(sorted_arr):
            pos[orig_idx] = sorted_pos

        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or pos[i] == i:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[j]
                cycle_size += 1
            if cycle_size > 0:
                swaps += cycle_size - 1

        out_lines.append(f"Minimum swaps: {swaps}")
        for mark, idv, _ in sorted_arr:
            out_lines.append(f"ID: {idv} Mark: {mark}")

    sys.stdout.write("\n".join(out_lines) + "\n")


if __name__ == '__main__':
    main()

