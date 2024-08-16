def solution(a, b, c, d):
    num_lst = [a, b, c, d]
    num_dic = {num:num_lst.count(num) for num in set(num_lst)}

    if len(num_dic) == 1:
        return 1111 * a
    elif len(num_dic) == 2:
        value = list(num_dic.values())
        p, q = sorted(num_dic.keys(), key=lambda x:num_dic[x], reverse=True)
        if value[0] != value[1]:
            return (10 * p + q) ** 2
        else:
            return (p + q) * abs(p - q)
    elif len(num_dic) == 3:
        p, q, r = sorted(num_dic.keys(), key=lambda x:num_dic[x], reverse=True)
        return q * r
    else:
        return min(num_lst)