#!/usr/bin/env python
# author：ygy


#####

salary = float(input(" please input your salary:"))

item_list = ((1,"iphone",5280),(2,"mac book pro",22000),(3," tea",25))
shop_cart =[]
sum_cast = 0 ;
for i in item_list:
    print(i)
while True:
    item_no = input(" please input what you want bug:")
    if("q" == item_no):
        break
    item_no = int(item_no)
    sum_cast += item_list[item_no-1][2]
    if(sum_cast>salary):
        print(" you don't have enough money !!!")
        sum_cast-=item_list[item_no-1][2]
        continue
    temp_cart =["",0]   ####还不会如何new 一个 临时链表，囧
    temp_cart[0] = item_list[item_no-1][1]
    temp_cart[1] = item_list[item_no - 1][2]
    shop_cart.append(temp_cart)

print(shop_cart)
print(sum_cast)
