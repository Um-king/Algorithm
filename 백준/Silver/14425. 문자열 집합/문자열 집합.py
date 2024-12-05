n, m = map(int, input().split())

n_lst, m_lst = set(), []

for _ in range(n):
    n_lst.add(input())

for _ in range(m):
    m_lst.append(input())

print(sum((map(lambda x:x in n_lst, m_lst))))