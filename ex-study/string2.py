# email = " abc@gmail.com "

# if email.strip() == "abc@gmail.com":
#     print("확인된 이메일")
# else:
#     print("미확인 이메일")
    
# 공백도 문자이다

# email = " abc@gmail.com\n\n"

# print(email)
# print("종료")
# # 해결
# print(email.strip())
# print("종료")

name = " Hong gildong "

if name == "HONG GILDONG":
    print("확인")
else:
    print("미확인")

# 문자열: 대문자, 소문자 구별한다
# 해결
if name.strip().upper() == "HONG GILDONG":
    print("확인")
else:
    print("미확인")
print(f"upper: {name.upper()}, lower: {name.lower()}")