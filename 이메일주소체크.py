import re

def check_email(email):
    # 이메일 주소 정규식 패턴d
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # re.search() 함수를 사용하여 패턴 매칭 확인
    match = re.search(pattern, email)
    
    if match:
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")

# 샘플 이메일 주소 10개
sample_emails = [
    "user@example.com",
    "john.doe@company.co.kr",
    "invalid.email@com",
    "another_user123@gmail.com",
    "test.email123@mail-server.org",
    "no_special_characters_email@example.org",
    "missing_at_symbolgmail.com",
    "user@localhost",
    "user@-invalid-domain.com",
    "user@valid-domain-.com"
]

# 각각의 샘플 이메일 주소에 대해 체크 수행
for email in sample_emails:
    check_email(email)
