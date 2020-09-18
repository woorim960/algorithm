# 공간과 시간복잡도를 최대한 줄여보자.

# 피보나치
def fibo(n) :
    global a, b                 # 함수 밖의 imutable 데이터를 제어하기 위해 global 선언

    # 피보나치 구현
    for i in range(2, n+1) :    
        a, b = b, a+b

    return b if n != 0 else a   # 입력 값이 0이면 0 반환

# 찾을 피보나치 값 입력
n = int(input())

# 공간 효율성을 위해 두개의 변수만 선언
a, b = 0, 1

# 실행
print( fibo(n) )