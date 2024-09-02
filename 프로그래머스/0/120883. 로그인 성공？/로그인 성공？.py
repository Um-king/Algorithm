def solution(id_pw, db):
    dic = dict(db)
    if id_pw in db:
        return "login"
    elif id_pw[0] not in dic:
        return "fail"
    else:
        return "wrong pw"