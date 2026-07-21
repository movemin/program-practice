bar = "hello world"
foo = bar[-5:]  # "world" -> 원본 변경x 새로 생성
pos = bar[:]  # 전체 복사

# 2번과 3번은 둘다 어쨋든 인덱스 슬라이싱 하므로
# 둘다 생성한다는 측면에서 같다