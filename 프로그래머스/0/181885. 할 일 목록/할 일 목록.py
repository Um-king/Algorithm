def solution(todo_list, finished):
    return [todo for finish, todo in zip(finished, todo_list) if not finish]