# -*- coding:utf-8 -*- 
# 用户：Ghostraveler
# 开发时间：2022/7/31 7:34 下午

import time
import cv2
from email.mime.image import MIMEImage  #用来构造文件内容的库
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib                          #邮件传递协议

# 授权码
# 授权码根据需要进行更改
pwd = "WNIJZCIN*TMAN**"

# 服务器接口
host = 'smtp.163.com'
port = 25

sender = 'huang341232@163.com'
receiver = '1350749259@qq.com'

def GetPicture():
    # 1.通过opencv调用摄像头拍照并保存本地录像
   cv2.namedWindow('Camera',2)
   # video = "http://admin:admin@192.168.43.1:8081/video"
   cap = cv2.VideoCapture(1)
   while True:
       success,img = cap.read()
       cv2.imshow("Camera",img)

       key = cv2.waitKey(10)
       if key == 27:
           #esc
            break
       if key == 32:
           #空格
           filename = 'frame.jpg'
           cv2.imwrite(filename,img)

   cap.release()
   cv2.destroyWindow("Camera")

def SetMsg():
    # 2.用email库构造邮件内容，以附件的形式插入
    msg = MIMEMultipart('mixed')
    msg['Subject'] = '小鬼子照片'
    msg['From'] = sender  #发送方邮箱
    msg['To'] = receiver       #接收方邮箱

    #邮件正文
    text = '你要的周**小鬼子照片到了'
    text_plain = MIMEText(text,'plain','utf-8')    #正文内容的转码
    msg.attach(text_plain)

    #图片附件(建议完整路径)
    SendImageFile = open('frame.jpg','rb').read()
    image = MIMEImage(SendImageFile)


    image['Content-Disposition'] = 'attachment; filename = "people.png"'
    msg.attach(image)
    return msg.as_string()


def SendEmail(msg):
    #3.用smtplib库发送邮件到指定邮箱
    """
    发送准备好的邮件
    :param msg:
    :return:
    """
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(sender,pwd)
    smtp.sendmail(sender,receiver,msg)
    time.sleep(2)
    smtp.quit()

if __name__ == '__main__':
    GetPicture()
    msg = SetMsg()
    SendEmail(msg)
