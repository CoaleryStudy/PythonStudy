col, row = map(int, input().split())
matrix = []
for i in range(row):
    input_list = list(input())
    for i in range(len(input_list)):
        if input_list[i] == '.':
            input_list[i] = 0
    matrix.append(input_list)

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*': # 역으로 지뢰라면 각 방향에 1을 더한다.
            calcTarget = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
            for calcUnit in calcTarget:
                x = i + calcUnit[0]
                y = j + calcUnit[1]
                if 0 <= x < row and 0 <= y < col and matrix[x][y] != '*':
                    matrix[x][y] += 1

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()