from collections import deque

def solution(numbers, target):
    answer = 0

    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    n = len(numbers)

    while queue:
        x, index = queue.popleft()

        index += 1
        
        if index < n:
            queue.append([x + numbers[index], index])
            queue.append([x - numbers[index], index])
        else:
            if x == target:
                answer += 1
    return answer