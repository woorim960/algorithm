'''
자신과 자신 바로 옆의 원소와 비교하여
더 작은 값을 앞으로 배치하는 정렬

+ 교환 정렬과 다르다.
'''

# 버블 정렬
def bouble(n, ls) :
    for i in range(n-1, -1, -1) :       # 맨 끝에서 1씩 감소하는게 포인트(끝 데이터는 정렬된 상태기에 다시 검사하지 않기 위함)
        for j in range(n-1) :
            if ls[j] > ls[j+1] :
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls

# 입력
ls = list(map(int, input().split()))

# 실행
print( bouble(len(ls), ls) )