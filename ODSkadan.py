#-*- coding:utf-8 -*-
'''
@author: jun.wen
'''
import re
pattern = re.compile(r'<order_id>(.*?)</order_id><order_sn>(.*?)</order_sn>.*?<user_id>(.*?)</user_id>.*?<buyer>(.*?)</buyer>.*?<pay_type>(.*?)</pay_type>',re.S)
f=open(r'D:\Users\jun.wen\Desktop\kadan2.txt','r')

print "start........"
num=0
for line in f.readlines():
    pay_type = re.findall(pattern,line)
    for i in pay_type:
        if len(i[4])>50:
            num+=1
            print 'order_sn: '+i[1]+' buyer: '+i[3]+'\npay_type: '+i[4]

f.close()
print "----公共"+str(num)+"个--------"