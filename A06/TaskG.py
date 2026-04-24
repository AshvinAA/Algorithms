#Connecting Words

import sys
from collections import defaultdict, deque


input, output = sys.stdin.readline, sys.stdout.write

nodes, start_word, target_word = input().split()
nodes = int(nodes)

words = [input().strip() for _ in range(nodes)]


def is_reachable(start_word, target_word, words):
    if start_word == target_word:
        return True

    #defaultdict allows us to avoid key errors when accessing keys that don't exists
    words_by_first_char = defaultdict(list)
    #enumerate returns both index/value 
    for idx, word in enumerate(words):
        words_by_first_char[word[0]].append(idx)

    visited = [False] * len(words)
    queue = deque()

    # Initial candidates are words that can follow the start word.
    for idx in words_by_first_char.get(start_word[-1], []):
        visited[idx] = True
        queue.append(idx)

    expanded_first_char = set()

    while queue:
        current_idx = queue.popleft()
        current_word = words[current_idx]

        if current_word == target_word:
            return True

        next_first_char = current_word[-1]
        if next_first_char in expanded_first_char:
            continue

        expanded_first_char.add(next_first_char)

        for next_idx in words_by_first_char.get(next_first_char, []):
            if not visited[next_idx]:
                visited[next_idx] = True
                queue.append(next_idx)

    return False


output("YES\n" if is_reachable(start_word, target_word, words) else "NO\n")

