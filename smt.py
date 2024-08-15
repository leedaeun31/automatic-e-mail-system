import smtplib
from flask import Flask,render_template,request
from email.mime.text import MIMEText

# flask 설정
app=Flask(__name__)

# 시작  페이지 설정 
@app.route("/",methods=['GET'])
def home():
    return render_template('e-mail_test.html')

# 웹으로부터 승인 / 보류 / 거절중에 하나를 받고 다시 웹으로 전송
@app.route("/send_mail",methods=['POST'])
def send_mail():
    msg=request.form['select']
    return render_template('e-mail_test.html',msg=msg)

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

    send_msg=MIMEText(f"승인 날짜 : {msg} 시간 : {time}") # 전송할 메시지 내용
    send_msg['Subject']="승인" # 전송할 메시지 제목 
    # 보내는 사람 이메일 주소 , 받는 사람 이메일 주소 , 설정 
    smtp.sendmail('20221110@edu.hanbat.ac.kr','idy1618@naver.com',send_msg.as_string())
    
    # smtp 종류
    smtp.quit()
    
    return render_template('e-mail_test.html')

@app.route("/Defer",methods=['POST'])
def Defer(): 

    msg=request.form['Defer']
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()

    # 보낼 계정
    smtp.login('20221110@edu.hanbat.ac.kr','dcbv eokd guhw nttn')

    send_msg=MIMEText(f"보류사유: {msg}")
    send_msg['Subject']="보류"
    smtp.sendmail('20221110@edu.hanbat.ac.kr','idy1618@naver.com',send_msg.as_string())
    
    smtp.quit()
    
    return render_template('e-mail_test.html')
@app.route("/reject",methods=['POST'])
def reject(): 

    msg=request.form['reject']
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()

    # 보낼 계정
    smtp.login('20221110@edu.hanbat.ac.kr','dcbv eokd guhw nttn')

    send_msg=MIMEText(f"거절사유: {msg}")
    send_msg['Subject']="거절"
    smtp.sendmail('20221110@edu.hanbat.ac.kr','idy1618@naver.com',send_msg.as_string())
    
    smtp.quit()
    
    return render_template('e-mail_test.html')
    
@app.route("/favicon.ico")
def favicon():
    return "",204


if __name__ == '__main__':
    app.run(debug=True)

