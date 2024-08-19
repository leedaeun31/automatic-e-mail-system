# 이메일 알림 웹 애플리케이션

이 프로젝트는 Flask를 기반으로 한 웹 애플리케이션으로, 사용자가 선택한 옵션(승인, 보류, 거절)에 따라 이메일 알림을 전송하고 주문 정보를 테이블 형식으로 요약하여 제공합니다.

## 주요 기능

- **주문 정보 표시**: 애플리케이션은 CSV 파일(`OrderDB.csv`, `ProductDB.csv`, `UserDB.csv`)에서 데이터를 읽어와, 결합된 정보를 웹 페이지의 테이블에 표시합니다.
- **이메일 알림**: 사용자의 선택(승인, 보류, 거절)에 따라, 지정된 수신자에게 관련 정보가 포함된 이메일을 전송합니다.
- **동적 테이블 렌더링**: Pandas를 사용하여 주문 데이터를 동적으로 HTML 테이블로 렌더링합니다.

## 필요 조건

- Python 3.x
- Flask
- Pandas
- SMTP 접근 권한(예: Gmail)

## 설치 방법

1. **저장소 클론**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

2. **필요한 python 패키지** 
    pip install flask pandas

3. **e-mail 설정**
    Python 스크립트에서 발신 이메일과 비밀번호를 본인의 정보로 교체합니다
    ```python
    smtp.login('your_email@gmail.com','your_password')

## 사용 방법

1. **서버 실행**
    ```bash
    python your_script_name.py
    => 'http://127.0.0.1:5000/' 주소에 접속하여 사용

2. **이메일 전송**
    웹 페이지에서 '승인' / '보류' / '거절' 옵션 중 하나를 선택하고, 적절한 정보 입력후 제출하면 이메일로 전송된다.
