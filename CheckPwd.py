import sys,urllib,urllib2,getpass


class TerminalPwd(urllib2.HTTPPasswordMgr):
    def find_user_password(self,realm,authuri):
        retval = urllib2.HTTPPasswordMgr.find_user_password(self,realm,authuri)

        if retval[0] == None and retval[1] == None:
            #didn't find it in stored values
            username = input("Login required,please input username:")
            password = input("please input password:")
            return(username,password)
        else:
            return retval


url = "http://home.asiainfo.com/"
req = urllib2.Request(url)


opener =  urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPwd()))


fd = opener.open(req)

print ("URL Retrieved:",fd.geturl())
info = fd.info()
for key, value in info.items():
    print "%s           =              %s" % (key,value)
