# 使用函数 print int input while if break else import time sleep
# 计算器
# import print int input while if break else import time sleep
# 有图形公式和加减乘除的计算器
import time
time.sleep(1)
print('计算器 有图形公式和加减乘除的计算器。')
print('如果有什么问题或建议，请联系我(在彩蛋里哦)。')
print('按下Enter,go')
while True:
    w = 3.14
    print('注意1.小数和分数不可计算， 公式或符号不想用直接按Enter,  (你别两个都不想用)')
    print('2.平行四边形=长方形，所以没有平行四边形')
    b = int(input('请输入第一个数字(梯形用上底，圆用半径，三角形用底，长方形/体用长):'))
    print('1=周长 4=长度 2=面积 3=体积')
    print('3.1 表示体积2')
    print('有正方形，长方形，圆，梯形，三角形，长方体，正方体，环形')
    print('例:正方形1=算正方形的周长。')
    print('正方形2=长方形2')
    a = input("请输入一个公式")
    print('/是除号，*是乘号，-是减号，+是加号，%是整除，**是乘方。')
    q = input("请输入一个符号有(/ * - + % **):")
    c = int(input('请输入第二个数字(梯形用下底，三角形用高，长方形/体用宽，圆用直径):'))
    e = int(input('请输入第三个数字(梯形和长方体是高，其他不用):'))
    k = int(input('请输入第四个数字(梯形是腰，用于梯形周长，其他不用):'))
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
    if a == "长方体1":
        jh = b+int(e)+c
        while True:
            print(jh*4)
            break
        break
    if a == "长方体2":
        lk = b*c+c*e+c*a
        while True:
            print(lk*2)
            break
        break
    if a == "长方体4":
        print(b*q)
        break
    if a == "长方体3":
        lk = b*c+c*e+c*a
        while True:
            mb = lk*2
            while True:
                print(mb*k)
                break
            break
        break
    if a == "长方体3.1":
        print(b*c*k)
    if a == "正方体1":
        print(b*12)
        break
    if a == "正方体2":
        print(b*b*6)
        break
    if a == "正方体4":
        print(b*b)
        break
    if a == "环形2":
        erw = w*b
        iuy = w*c
        while True:
            print(erw-iuy)
            break
        break
    if a == "正方体3":
        cz = b*b*6
        while True:
            print(cz*e)
            break
        break
    if a == "正方体3.1":
        print(b*b*b)
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
time.sleep(119)
print('两分钟之后关闭窗口')
print('作者AWEkn1')
time.sleep(1)
