def solution(signals):
    # 신호등 개수만큼 빈 리스트 생성
    # ex) signals =[[2, 3], [1, 2]] -> table[[],[]]
    table = [[] for _ in range(len(signals))]

    # 신호 패턴 펼치기 i - 신호등 번호, signal - 해당 신호등의 시간 정보
    for i, signal in enumerate(signals):
        # color - 색 번호(0, 1, 2, ..), time 해당 색이 유지되는 시간
        # ex) signal [2, 3] -> 
        # color = 0, time = 2 
        # color = 1, time = 3
        for color, time in enumerate(signal):
            # color를 time 만큼 반복해서 넣기
            for _ in range(time):
                table[i].append(color)

    # 시간 탐색 시작
    # t는 시간(0부터 시작)
    # 실제 시작 t + 1
    t = 0
    answer = -1

    # 시간 루프
    # 충분히 큰 범위까지 탐색(완벽한 방식x 일단 넉넉히)
    while t < 20 ** len(signals):
        # 핵심 조건 - 모든 신호등이 현재 시간에 색이 1인가?
        if all(table[i][t % len(table[i])] == 1 for i in range(len(table))):
            # 정답 처리
            answer = t + 1
            break
        t += 1

    return answer