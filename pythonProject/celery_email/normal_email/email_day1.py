# 1 导入模块
import smtplib
from email.mime.text import MIMEText  #往邮件中写内容的对象
from email.header import Header      # 邮件头中写东西

# 2 发送方和接收方配置
# 发件方邮箱：谁发送的
msg_from='3359824413@qq.com'
# 生成的密码：不能泄露
password='ypevaepjhwzvchca'
# 发送给谁
msg_to='3113217659@qq.com'
# 右键主题
subject = "非常重要，女朋友跟别人跑了"  # 主题
content = "骗你的，不用担心，丝毫不慌"
# 生成一个MIMEText对象（还有一些其它参数）
msg = MIMEText(content)
# 放入邮件主题
msg['Subject'] = subject
# 放入发件人
msg['From'] = msg_from
# 放入收件人
msg['To'] = msg_to
try:
    # 通过ssl方式发送，服务器地址，端口
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 登录到邮箱
    s.login(msg_from, password)
    # 发送邮件：发送方，收件方，要发送的消息
    s.sendmail(msg_from, msg_to, msg.as_string())
    print('成功')
except s.SMTPException as e:
    print(e)
finally:
    s.quit()