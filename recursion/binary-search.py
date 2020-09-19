# 이진 탐색
def binary_search(ls, x, low, high) :
    if low > high :                 # x가 리스트 내에 없다면
        return -1

    i = (low+high) // 2             # 인덱스는 항상 가운데를 탐색하도록 한다.

    if ls[i] == x :                 # 찾았다면 인덱스 반환
        return i
    elif ls[i] < x :                # x가 더 크다면 low를 현재 인덱스에서 1 증가시킨다.
        return binary_search(ls, x, i+1, high)
    else :                          # x가 더 작다면 high를 현재 인덱스에서 1 증가시킨다.
        return binary_search(ls, x, low, i-1)


# 입력
x = int(input())                        # 찾을 값
ls = sorted(map(int, input().split()))    # 검색 리스트(항상 정렬되어있는 리스트내에서의 탐색만 허용된다.)

# 실행
print( binary_search(ls, x, 0, len(ls)-1) )