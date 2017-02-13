import sys,urllib,urllib2


url = "http://mail.126.com"

req = urllib2.Request(url)
fd = urllib2.urlopen(req)


print ("URL Retrieved:",fd.geturl())
info = fd.info()
for key, value in info.items():
    print "%s           =              %s" % (key,value)

while True:
    data = fd.read(1024)
    if not len(data):
            break
    print data
