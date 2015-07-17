#coding:utf-8
'''
Created on 2015年7月17日

@author: jun.wen
'''
import urllib,urllib2
import cookielib
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Bugzilla:
    
    def __init__(self):
        self.loginUrl = 'https://bugzilla.tools.xxoo.com/bugzilla/index.cgi'
        self.getBugs = 'https://bugzilla.tools.xxoo.com/bugzilla/buglist.cgi?cmdtype=runnamed&namedcmd=%E6%88%91%E7%9A%84%E6%9C%AA%E5%85%B3%E9%97%AD%E7%9A%84bugs&list_id=416796'
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({'Bugzilla_login':'username','Bugzilla_password':'password','Bugzilla_restrictlogin':'on','GoAheadAndLogIn':'1','GoAheadAndLogIn':'Log_in'})
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        
        self.id = []
        self.status = []
        self.assignee = []
        self.summary = []
        
    def getPage(self):
        request = urllib2.Request(url = self.loginUrl,data = self.postdata)
        result = self.opener.open(request)
        result = self.opener.open(self.getBugs)
        return result.read()
    
    def getData(self):
        page = self.getPage()
        myItems = re.findall('<table class="bz_buglist".*?>.*?</table>',page,re.S)
        for item in myItems:
            return item
    
        
