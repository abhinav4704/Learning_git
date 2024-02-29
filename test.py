test_cases = int(input())
x = 0

for _ in range(test_cases):
    p, q = map(int, input().split())
    board = []

    for _ in range(p):
        row = list(map(int, input().split()))
        board.append(row)
count = 0
change = True
for i in range(test_cases):
  count = 0
  for i in range(p):
    for j in range(q):
      if board[i][j]==-1:
        pass
      if board[i][j]==0: 
        change = False
          
        if j < q-1:      
          if board[i][j+1]==1:
            board[i][j+1] = 0
            change = True

            
        if i>0: 
          
          if board[i-1][j]==1:
            board[i-1][j] = 0
            change = True
            
        if j>0:
          
          if board[i][j-1]==1:
            board[i][j-1] = 0
            change = True
            
        if i < p-1:
          
          if board[i+1][j]==1:
            board[i+1][j] = 0
            change = True
        if change == True:
          count +=2    

  for i in range(p):
    for j in range(q):
      if board[i][j]== 1:
        x +=1
      else:
        x +=0
  if x>0: 
    print(-1)    
  else:
    print(count,"\n")

