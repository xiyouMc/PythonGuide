import os
print os.name,os.uname()
print os.environ
print  os.environ.get('PATH')
print os.path.abspath('.')
print os.path.join(os.path.abspath('.'),'osTest')
