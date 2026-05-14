def solution(message, spoiler_ranges):
    n = len(message)

    words = []              # [word, start, end]
    pos_to_word = [-1] * n  # 각 문자 위치가 몇 번째 단어에 속하는지

    # 1. 단어와 위치 저장
    i = 0
    while i < n:
        if message[i] == " ":
            i += 1
            continue

        start = i

        while i < n and message[i] != " ":
            i += 1

        end = i - 1
        word = message[start:i]
        word_idx = len(words)

        words.append([word, start, end])

        for j in range(start, end + 1):
            pos_to_word[j] = word_idx

    # 2. 전체 스포 위치 표시
    covered = [False] * n

    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            covered[i] = True

    # 3. 각 단어별 스포 글자 개수 계산
    remain = [0] * len(words)

    for i in range(n):
        word_idx = pos_to_word[i]

        if word_idx != -1 and covered[i]:
            remain[word_idx] += 1

    # 4. 평문 단어 저장
    normal_words = set()

    for idx, (word, start, end) in enumerate(words):
        if remain[idx] == 0:
            normal_words.add(word)

    # 5. 공개 진행
    opened = [False] * n
    used = set()
    answer = 0

    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            if opened[i]:
                continue

            opened[i] = True

            word_idx = pos_to_word[i]

            if word_idx == -1:
                continue

            if covered[i]:
                remain[word_idx] -= 1

                if remain[word_idx] == 0:
                    word = words[word_idx][0]

                    if word not in normal_words and word not in used:
                        answer += 1
                        used.add(word)

    return answer