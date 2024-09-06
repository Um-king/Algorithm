def solution(people, limit):
    answer = 0
    people.sort()

    first, end = 0, len(people) - 1

    while first <= end:
        if people[first] + people[end] <= limit:
            first += 1
        end -= 1
        answer += 1

    return answer 