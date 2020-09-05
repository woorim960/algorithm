# 연결된 노드들끼리 리스트에 담아준다.
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [6, 8],
  [1, 7]
]

# 방문 처리를 위한 방문 여부 변수 선언
is_visitable = [False] * 9

# DFS 함수
def dfs(graph, v, is_visitable) :
  is_visitable[v] = True
  print(v, end=' ')

  for i in graph[v] :
    if is_visitable[i] == False :
      dfs(graph, i, is_visitable)

# DFS 실행
dfs(graph, 1, is_visitable)