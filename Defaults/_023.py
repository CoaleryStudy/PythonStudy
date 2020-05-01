score_list = list(map(int, input().split()))

isHaveInvalidScore = False
for score in score_list:
    if not 0 <= score <= 100:
        print('잘못된 점수')
        isHaveInvalidScore = True
        break
if not isHaveInvalidScore:
    avg = sum(score_list) / 4
    if avg >= 80:
        print('합격')
    else:
        print('불합격')