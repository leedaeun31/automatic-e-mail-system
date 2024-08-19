# 이메일 알림 웹 애플리케이션

이 프로젝트는 Flask를 기반으로 한 웹 애플리케이션으로, 사용자가 선택한 옵션(승인, 보류, 거절)에 따라 이메일 알림을 전송하고 주문 정보를 테이블 형식으로 요약하여 제공합니다.

## 주요 기능

- **주문 정보 표시** <br>
    애플리케이션은 CSV 파일(`OrderDB.csv`, `ProductDB.csv`, `UserDB.csv`)에서 데이터를 읽어와, 결합된 정보를 웹 페이지의 테이블에 표시합니다.
- **이메일 알림** <br>
    사용자의 선택(승인, 보류, 거절)에 따라, 지정된 수신자에게 관련 정보가 포함된 이메일을 전송합니다.
- **동적 테이블 렌더링** <br>
     Pandas를 사용하여 주문 데이터를 동적으로 HTML 테이블로 렌더링합니다.

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

2. **필요한 python 패키지** <br>
    pip install flask pandas

3. **e-mail 설정** <br>
    Python 스크립트에서 발신 이메일과 비밀번호를 본인의 정보로 교체합니다
    ```python
    smtp.login('your_email@gmail.com','your_password')

## 사용 방법

1. **서버 실행**
    ```bash
    python your_script_name.py
    => 'http://127.0.0.1:5000/' 주소에 접속하여 사용

2. **이메일 전송** <br>
    웹 페이지에서 '승인' / '보류' / '거절' 옵션 중 하나를 선택하고, 적절한 정보 입력후 제출하면 이메일로 전송된다.

## 기능별 코드

1. **DB 주문 정보를 테이블 생성**
    ```python
    import pandas as pd

    def get_table():

    orderdb=pd.read_csv('OrderDB.csv')
    productdb=pd.read_csv('ProductDB.csv')
    userdb=pd.read_csv('UserDB.csv')

    order_product_ids=orderdb['product_id'].unique() # orderdb의 제품 id
    product_ids=productdb['product_id'].unique() # productdb의 id
    order_user_ids=orderdb['user_id'].unique() # orderdb의 user id
    user_user_ids=userdb['user_id'].unique() # userdb의 user id

    order_order_id=orderdb['order_id'].unique() # orderdb의 order id
    order_quantity=orderdb['quantity'].unique() #orderdb의 quantity

    print_pr_name=[]
    print_color=[]
    print_us_name=[]

    # orderDB의 proudct_id에 맞는 프린트 제품과 컬러 추출
    for order_product_id in order_product_ids:
        if order_product_id in product_ids: #현재 order_product_id가 product_ids 배열에 있는지 확인합니다.
            # 해당 product_id의 이름을 찾기
            pr_name = productdb[productdb['product_id'] == order_product_id]['name'].values
            color=productdb[productdb['product_id'] == order_product_id]['color'].values
            print_pr_name.append(pr_name[0])  # 이름을 리스트에 추가
            print_color.append(color[0])
    # orderDB의 user_id에 맞는 name 추출
    for order_user_id in order_user_ids:
        if order_user_id in user_user_ids:
            us_name=userdb[userdb['user_id'] == order_user_id]['name'].values
            print_us_name.append(us_name[0])
    
    # 새로운 DataFrame 생성
    df=pd.DataFrame({
        'order_id': order_order_id,
        'product_id' : print_pr_name,
        'product_colors' : print_color,
        'user_name' : print_us_name,
        'quantity' : order_quantity
    })

    # html로 전송
    html_table = df.to_html(index=False, classes='table table-striped')
    
    => map 코드를 사용하면 더 간단하게 생성이 가능하다 

2. **메일 보내기**
    ```python
    def approve(): 

    msg=request.form['date'] # 사용자가 선택하 날짜정보 받아오기
    time=request.form['time'] # 사용자가 시간정보 받아오기
    # 메일을 보내기위한 smtplib 라이브러리 설정 
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()

    # 보낼 계정
    smtp.login('e-mail to be send','your e-mail pw')

    send_msg=MIMEText(f"Delivery Date : {msg} Delivery Time : {time}") # 전송할 메시지 내용
    send_msg['Subject']="Approve" # 전송할 메시지 제목 
    # 보내는 사람 이메일 주소 , 받는 사람 이메일 주소 , 설정 
    smtp.sendmail('e-mail to be send','e-mail to be receive',send_msg.as_string())
    
    # smtp 종류
    smtp.quit()
    html_table = get_table()
    return render_template('e-mail_test.html',table=html_table)

    => 다른 경우도 비슷하다 

