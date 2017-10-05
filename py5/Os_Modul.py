#!/usr/bin/env python
# author：ygy


import  os

#运行shell命令
os.system(" command ")

#获取当前目录
print(os.getcwd()) #F:\pythonProjectHome\python_leisure\py5
#改变当前目录
# os.chdir("F:\pythonProjectHome")
# print(os.getcwd()) #F:\pythonProjectHome
#获取当前目录
print(os.curdir) #   .
#返回当前目录的父目录
print(os.pardir) #   ..
#创建多级目录
# os.makedirs(r"C:\\temp\\python")   #单级目录mkdir
#若内容为空，则递归删除所有目录
# os.removedirs(r"C:\\temp\\python") #单级目录rmdir
print("sep:",os.sep)   # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print("linesep:",os.linesep)#     输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.path.abspath(path)  #返回path规范化的绝对路径
# os.path.split(path)  #将path分割成目录和文件名二元组返回
# os.path.dirname(path)  #返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)  #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  #如果path是绝对路径，返回True
# os.path.isfile(path)  #如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  #如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间


























