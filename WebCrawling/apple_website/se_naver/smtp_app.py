##### getting_started
## naver >> configuration >> CHECK IMAP/SMTP USED >> copy smtp naver address & smtp port (w/ tls)
## https://mail.naver.com/v2/settings/smtp/imap


##### simple
# import smtplib
# from email.mime.text import MIMEText
 
# text = "메일 내용입니다"
# msg = MIMEText(text) 
 
# msg['Subject'] ="이것은 메일제목"
# msg['From'] = '보내는사람이메일'
# msg['To'] = '받는사람이름이나 이메일'
# print(msg.as_string())
 
# s = smtplib.SMTP( '네이버smtp주소' , 포트번호 ) 
# s.starttls() #TLS 보안 처리
# s.login( '네이버아이디' , '비번' ) #네이버로그인
# s.sendmail( '발송자이메일', '수신자이메일', msg.as_string() )
# s.close()
#########################


##### html
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
 
# msg = MIMEMultipart('alternative')
# 내용 = """
# 여기에 HTML로 작성가능
# <h4>bold title</h4>
# <button>btn</button>
# """
# part1 = MIMEText(내용, "html")
# msg.attach(part1)

 
# msg['Subject'] ="이것은 메일제목"
# msg['From'] = '보내는사람이메일'
# msg['To'] = '받는사람이름이나 이메일'
# print(msg.as_string())
 
# s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
# s.starttls() #TLS 보안 처리
# s.login( '네이버아이디' , '비번' ) #네이버로그인
# s.sendmail( '발송자이메일', '수신자이메일', msg.as_string() )
# s.close()
#########################

##### attachment
# import smtplib
# from email.mime.text import MIMEText
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

# text = "메일 내용입니다"
# msg = MIMEMultipart()
# msg['Subject'] ="이것은 메일제목"
# msg['From'] = '보내는자이메일'
# msg['To'] = '받는자이메일또는이름'
# msg.attach(MIMEText(text))
# print(msg.as_string())

# #원하는 파일 rb로 오픈
# with open('보낼파일경로', 'rb') as 파일:
#   part = MIMEBase('application', 'octet-stream')
#   part.set_payload(파일.read())

# #파일 base64 인코딩
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', 'attachment; filename="경로제외보낼파일명"') # attachment; filename="data.xlsx"'
# msg.attach(part)

# s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
# s.starttls()
# s.login( '네이버아이디' , '비번' ) 
# s.sendmail( '보내는사람', '받는사람', msg.as_string() ) 
# s.close()
