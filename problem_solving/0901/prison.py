'''
룩업 테이블: 미리 계산된 값을 저장해 놓은 테이블(리스트) -> 계산 시간을 줄이고, 코드를 간결하게 하기 위해
'''
# 파이프 모양별로 4방향 연결 가능 여부 나타내는 리스트 -> [상, 하, 좌, 우]
pipe = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
# 상하좌우 이동을 위한 dir
di, dj = [-1,1,0,0], [0,0,1,1]
# 상하, 좌우 매칭하기 위한 리스트(상-하, 좌-우)
opp = [1,0,3,2]