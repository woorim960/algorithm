'''
자신과 자신 앞에 있는 모든 원소들과 비교해서 
자신보다 작은 것이 있으면 자신의 위치랑 바꾼다.
자신의 위치에는 항상 가장 작은 값이 위치해있게 되는 정렬.
'''

# 교환 정렬
def exchange(n, ls) :
    for i in range(n-1) :
        for j in range(i+1, n) :
            if ls[i] > ls[j] :
                ls[i], ls[j] = ls[j], ls[i]
    return ls

# 입력
ls = list(map(int, input().split()))

# 실행
print( exchange(len(ls), ls) )