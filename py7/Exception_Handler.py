#!/usr/bin/env python
# author：ygy



map = {
    "name":"ygy",
    "age":22
}

try:
    a = map["desc"]
except Exception as e:
    print("not this key",e)
else:
    print(" 运行ok ")
finally:
    print(" 无论运行ok 不ok 都会执行")