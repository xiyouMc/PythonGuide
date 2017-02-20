import StringIO
f = StringIO.StringIO()
f.write('hello\n')
f.write(' ')
f.write('world\n')
print f.getvalue()
f.close()

t = StringIO.StringIO('hello\nworld\nTks\n')
while True:
    s = t.readline()
    if s == '':
        break
    print(s.strip())
t.close()
