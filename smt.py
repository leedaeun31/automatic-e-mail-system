import smtplib
import pandas as pd
from flask import Flask,render_template,request
from email.mime.text import MIMEText

# flask 설정
app=Flask(__name__)

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
    
    df=pd.DataFrame({
        'order_id': order_order_id,
        'product_id' : print_pr_name,
        'product_colors' : print_color,
        'user_name' : print_us_name,
        'quantity' : order_quantity
    })

    html_table = df.to_html(index=False, classes='table table-striped')

    return html_table

@app.route("/")
def home():
    html_table = get_table()
    return render_template('e-mail_test.html', table=html_table)


# 웹으로부터 승인 / 보류 / 거절중에 하나를 받고 다시 웹으로 전송
@app.route("/send_mail",methods=['POST'])
def send_mail():
    msg=request.form['select']
    html_table = get_table()
    return render_template('e-mail_test.html',msg=msg,table=html_table)

# 웹에서 승인을 선택한 경우    
@app.route("/approve",methods=['POST'])
def approve(): 

    msg=request.form['date'] # 사용자가 선택하 날짜정보 받아오기
    time=request.form['time'] # 사용자가 시간정보 받아오기
    # 메일을 보내기위한 smtplib 라이브러리 설정 
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()

    # 보낼 계정
    smtp.login('20221110@edu.hanbat.ac.kr','dcbv eokd guhw nttn')

    send_msg=MIMEText(f"Delivery Date : {msg} Delivery Time : {time}") # 전송할 메시지 내용
    send_msg['Subject']="Approve" # 전송할 메시지 제목 
    # 보내는 사람 이메일 주소 , 받는 사람 이메일 주소 , 설정 
    smtp.sendmail('20221110@edu.hanbat.ac.kr','idy1618@naver.com',send_msg.as_string())
    
    # smtp 종류
    smtp.quit()
    html_table = get_table()
    return render_template('e-mail_test.html',table=html_table)

@app.route("/Defer",methods=['POST'])
def Defer(): 

    msg=request.form['Defer']
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()

    # 보낼 계정
    smtp.login('20221110@edu.hanbat.ac.kr','dcbv eokd guhw nttn')

    send_msg=MIMEText(f"Reasons for suspension: {msg}")
    send_msg['Subject']="Defer"
    smtp.sendmail('20221110@edu.hanbat.ac.kr','idy1618@naver.com',send_msg.as_string())
    
    smtp.quit()
    html_table = get_table()
    return render_template('e-mail_test.html',table=html_table)

@app.route("/reject",methods=['POST'])
def reject(): 

    msg=request.form['reject']
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()

    # 보낼 계정
    smtp.login('20221110@edu.hanbat.ac.kr','dcbv eokd guhw nttn')

    send_msg=MIMEText(f"Reasons for Reject: {msg}")
    send_msg['Subject']="Reject"
    smtp.sendmail('20221110@edu.hanbat.ac.kr','idy1618@naver.com',send_msg.as_string())
    
    smtp.quit()
    html_table = get_table()
    return render_template('e-mail_test.html',table=html_table)
    
@app.route("/favicon.ico")
def favicon():
    return "",204

if __name__ == '__main__':
    app.run(debug=True)

