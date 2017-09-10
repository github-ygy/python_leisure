#!/usr/bin/env python
# author：ygy


map ={       ###如java中map的用法
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
}

new_map = {
    1:2 ,
    "key1":"new value1"
}

print(map)
print(map["key1"])     ###获取所有value
print(map.keys())       ##获取所有key
print(map.get("key1"))  ###获取value
print("key1" in map)   ###是否存在此key
map.update(new_map)    ###共有key更新，否则新增
print(map)
print(map.items())     ###字段转为列表