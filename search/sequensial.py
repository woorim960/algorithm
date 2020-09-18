# 순차 탐색
def sequensial_search(ls, x) :
    for i in range(len(ls)) :
        if ls[i] == x :
            return i
    return -1

# 입력
x = int(input())                        # 찾을 값
ls = sorted(map(int, input().split()))    # 검색 리스트

# 실행
print( sequensial_search(ls, x) )