# 합병 정렬
def merge_sort(ls) :
    n = len(ls)				# 여러번 호출되기에 미리 선언해준다.
    if n <= 1 : return ls               # 리스트의 길이가 1이면 자기 자신 반환

    u = merge_sort(ls[:n//2])           # 반으로 나눈 좌측 리스트
    v = merge_sort(ls[n//2:])           # 반으로 나눈 우측 리스트
    return merge(u, v)                  # 합병

# 합병 => 각 원소를 비교하여 크기 순으로 정렬하면서 합친다.
def merge(u, v) :
    ls = []                             # 정렬된 요소가 담길 리스트
    i = j = 0                           # 인덱스
    u_max, v_max = len(u), len(v)       # while문에서 매번 조건 검사시 len()을 호출하지 않도록 미리 할당

    while i < u_max and j < v_max :     # 비교가 마무리될 때까지 반복
        # 작은 것 순서대로 삽입
        if u[i] <= v[j] :               
            ls.append(u[i])
            i += 1
        else : 
            ls.append(v[j])
            j += 1
    
    # 비교 후 남은 리스트를 마지막에 합쳐준다.
    if i > j :
        ls += v[j:]
    else :
        ls += u[i:]

    return ls

# 정렬할 리스트 입력
ls = list(map(int, input().split()))

# 실행
print( merge_sort(ls) )
