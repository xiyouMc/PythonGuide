#-*- coding:utf-8 -*-

#中文
__author__ = "Mark"
import sys

# _或者__表示private。 不应该被外部直接引用，但可以调用
def __test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many args')
if __name__ == '__main__':
    __test()
