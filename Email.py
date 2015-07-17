#coding:utf-8
'''
Created on 2015年7月17日

@author: jun.wen
'''
import smtplib  
import bugzilla
from email.mime.text import MIMEText  

bugs = bugzilla.Bugzilla()
bugTable = bugs.getData()

mailto_list=["email@163.com"] 
mail_host="smtp.163.com"  #设置服务器
mail_user="username"    #用户名
mail_pass="password"   #口令 
mail_postfix="163.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="bugzilla"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
    
if __name__ == '__main__':  
    if send_mail(mailto_list,"未关闭的bugs",bugTable):  
        print "Send success"  
    else:  
        print "Send fail"
