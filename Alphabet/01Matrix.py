import json
from collections import deque

def read_matrix():
  matrix = []
  print("Enter your maze grid (e.g. [[0,0,0],[0,1,0]]: )")

  try:
    return json.loads(input())
  except json.JSONDecodeError:
    print("Invalid input format. Please, follow the correct format!")
    return []
  
def solution(mat):
  if not mat or not mat[0]:
        return []
  
  row, col = len(mat), len(mat[0])
  distances = [[-1 for _ in range(col)] for _ in range(row)]
  queue = deque()

  for r in range(row):
    for c in range(col):
      if mat[r][c] == 0:
        distances[r][c] = 0
        queue.append((r,c))
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  while queue:
    x, y = queue.popleft()

    for dx, dy in directions:
      next_x, next_y = x + dx, y + dy
      if 0 <= next_x < row and 0 <= next_y < col:
        if distances[next_x][next_y] == -1:
          distances[next_x][next_y] = distances[x][y] + 1
          queue.append((next_x,next_y))
  return distances


if __name__ == "__main__":
  mat = read_matrix()
  soln = solution(mat)
  print(json.dumps(soln))