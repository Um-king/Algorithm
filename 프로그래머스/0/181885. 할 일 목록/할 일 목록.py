def solution(todo_list, finished):
    return [j for i,j in zip(finished, todo_list) if not i]