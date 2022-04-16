# 使用函数 print int input while if break else import time sleep
# 计算器
# import print int input while if break else import time sleep
# 有图形公式和加减乘除的计算器
import time
time.sleep(1)
print('计算器 有图形公式和加减乘除的计算器。')
print('更新:添加图形公式计算。')
print('如果有什么问题或建议，请联系我(在彩蛋里哦)。')
time.sleep(2)
while True:
    w = 3.14
    print('注意1.小数和分数不可计算， 公式或符号不想用直接按Enter,  (你别两个都不想用)')
    print('2.平行四边形=长方形，所以没有平行四边形')
    b = int(input('请输入第一个数字(梯形用上底，圆用半径，三角形用底，长方形用长):'))
    print('1=周长 2=面积')
    print('有正方形，长方形，圆，梯形，三角形')
    print('例:正方形1=算正方形的周长。')
    print('正方形2=长方形2')
    a = input("请输入一个公式")
    print('/是除号，*是乘号，-是减号，+是加号，%是整除，**是乘方。')
    q = input("请输入一个符号有(/ * - + % **):")
    c = int(input('请输入第二个数字(梯形用下底，三角形用高，长方形用宽，圆用直径):'))
    e = input('请输入第三个数字(梯形是高，用于梯形面积，其他不用):')
    k = input('请输入第四个数字(梯形是腰，用于梯形周长，其他不用):')
    print('开始计算')
    time.sleep(2)
    print('计算结果在下一行')
    if a == "正方形1":
        print(4*b)
        break
    if a == "长方形2":
        print(b*c)
        break
    if a == "长方形1":
        d = b+c
        while True:
            print(d*2)
            break
        break
    if a == "梯形2":
        d = int(b)+c
        while True:
            print(d*int(e)/2)
            break
        break
    if a == "梯形1":
        print(b+c+e+k)
        break
    if a == "圆1":
        print(w*c)
        break
    if a == "圆2":
        print(w*b)
        break
    if a == "三角形1":
        print(b+b+b)
        break
    if a == "三角形2":
        print(b*c/2)
        break
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
    if q == "AWEkn1":
        print('这是一个彩蛋')
        time.sleep(1)
        print('bilibili:AWEgh1 UID;517169863 ')
        print('Xbox:AWEkn1')
        print('giee:AWEkn1')
        print('github:AWEkn1')
        print('邮箱:a13579003@outlook.com/3502384248@qq.com')
        print('qq:3502384248')
        print('alingmuich.com')
        break
    else:
        print('请重新输入！(注意事项看那没！！！)')
        time.sleep(1)
        print('注意1.小数和分数不可计算， 数字， 公式或符号不想用直接按Enter,  (你别都不想用)')
        print('2.平行四边形=长方形，所以没有平行四边形')
        time.sleep(10)
        continue
time.sleep(1)
print('作者AWEkn1')
