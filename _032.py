n1, n2 = map(int, input().split())
result_list = [2 ** (x + n1) for x in range(n2 - n1 + 1) if not (x == 1 or x == n2 - n1 - 1)] # 진짜 괴랄하네
print(result_list)