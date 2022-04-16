# 使用函数 print int input while if break else impore time
# 计算器001
import time
print('计算器')
time.sleep(1)
while True:
    print('注意：小数和分数不可计算')
    b = int(input('请输入第一个数字:'))
    time.sleep(1)
    print('/是除号，*是乘号，-是减号，+是加号，%是整除，**是乘方。')
    q = input("请输入一个符号有(/ * - + % **):")
    c = int(input('请输入第二个数字:'))
    print('开始计算')
    time.sleep(2)
    print('计算结果在下一行')
    if q == "+":
        print(b+c)
        break
    if q == "-":
        print(b-c)
        break
    if q == "*":
        print(b*c)
        break
    if q == "/":
        print(b/c)
        break
    if q == "%":
        print(b % c)
        break
    if q == "**":
        print(b**c)
        break
    else:
        print('请重新输入')
        continue
print('作者AWEkn1')
