#!/usr/bin/env python
# author：ygy

#print(" hello world ")

#str = " python 字符串"

#print(str," 逗号为拼接符号")


####''' ''' 可以为多行注释，也可以为多行打印，默认行为换行
#name = "ygy"
#age  = "24"

####input 为java中 Scanner sc = new Scanner(System.in);
name = input("名字： ")
# age =int(input("年龄整数： "))   ###默认为str型，转为int型
# salary =float(input("工资浮点数：  "))   ####默认为str型，转为float型
# print(type(age))
# print(type(salary))

### %s 需要str类型 %d 需要整数型  %f 需要浮点型
# msg = '''n\na
# name =%s
# age = %d
# salary=%f
#  '''%(name,age,salary)

#msg2 = ''' n\na
#name = {_name}
#age = {_age}
#salary={_salary}
# '''.format(__name = name,__age = age ,__salary = salary)



# msg3 = '''
#     {_name}
#     name ={_name}   #站位符号，后续赋值
# '''.format(_name = name)



msg4 = '''
    {0}
    name ={0}   #站位符号，后续赋值,使用递增数字，无须指定变量
'''.format(name)

# print(msg)
# print(msg2)
# print(msg3)
print(msg4)






