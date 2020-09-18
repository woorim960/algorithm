# 이진 탐색
def binary_search(ls, x) :
    i = 0                               # 인덱스 변수 선언
    low, high = 0, len(ls)-1            # low와 high는 검색할 리스트의 시작과 끝 주소를 의미한다.
    while low <= high :
        i = (low+high) // 2             # 인덱스는 항상 가운데를 탐색하도록 한다.
        if ls[i] == x :                 # 찾았다면 인덱스 반환
            return i
        elif ls[i] < x :                # x가 더 크다면 low를 현재 인덱스에서 1 증가시킨다.
            low = i+1
        else :                          # x가 더 작다면 high를 현재 인덱스에서 1 증가시킨다.
            high = i-1
    return -1


# 입력
x = int(input())                        # 찾을 값
ls = sorted(map(int, input().split()))    # 검색 리스트(항상 정렬되어있는 리스트내에서의 탐색만 허용된다.)

# 실행
print( binary_search(ls, x) )