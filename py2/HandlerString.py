#!/usr/bin/env python
# author：ygy



name = "ygy {age} {love} "

print(name.capitalize())     ###Ygy 首字符大写
print(name.count("y"))       ###2 统计字符个数
print(name.center(10,"-"))   ####---ygy----
print(name.endswith("gy"))   ###True
print(name.expandtabs(tabsize=30))  ###\t 多少个空格
print(name.find("g"))        ###查找
print(name.format_map({"age":23,"love":"money"}))
print(name.isalnum())        ###是否是阿利伯字符
print(name.isalpha())        ###是否是纯英文字符
print("121".isdecimal())      ###是不是十进制
print("aaaa".isidentifier())  ###是否是一个合法的标识符
print("aaaa".islower())       ###是否是小写
print("aaaa".isdigit())       ###是否是一个数字
print(",".join(["a","b","c"]))  ###
print("  ygy ".strip())    ###ygy  去掉空格 trim