# 이름 과목 성적 메시지


def prt_comments(name, sub, score, msg):
    print(f"안녕하세요, {name}님")
    print(f"{name}님, {sub} 성적 점수 알려드립니다.")
    print(f"{name}님 성적 점수는 {score}점 입니다.")
    print(msg)


args = input().strip().split()
prt_comments(*args)  # 아웃 패킹 -> 각자 알아서 자리로 간다
args = input().strip().split()
prt_comments(*args)
args = input().strip().split()
prt_comments(*args)
args = input().strip().split()
prt_comments(*args)