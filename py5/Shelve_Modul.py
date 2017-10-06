#!/usr/bin/env python
# author：ygy


import  shelve


file = shelve.open("shelve_test")

name = ["ygy","houzi","monkey"]

file["name"] = name

file.close()


















