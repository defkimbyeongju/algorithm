def snowman(i, j, gage):
    if arr[i][j] == 3:
        result.append(gage)
        return
    # 옆으로 가는 방법
    if 0<j-1<M and arr[i][j-1] == 1 and (i,j-1) not in stack: # 좌측으로
        snowman(i, j-1, gage)
    if 0<j+1<M and arr[i][j+1] == 1 and (i,j+1) not in stack: # 우측으로
        snowman(i, j+1, gage)
    # 상하로 움직이기
    if 