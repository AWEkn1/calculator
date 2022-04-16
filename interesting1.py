# 使用函数 print int input while if break else
# 计算器001
print('计算器2')
while True:
    b = int(input('请输入第一个数字(梯形用上底，圆用半径，三角形用底，长方形用长):'))
    print('1=周长 2=面积')
    print('有正方形，长方形，圆，梯形，三角形')
    print('例:“正方形2”=算正方形的面积。')
    a = input("请输入一个公式：")
    c = int(input('请输入第二个数字(正方形和圆不用，梯形用下底，三角形用高，长方形用宽):'))
    e = int(input('请输入第三个数字(梯形用高，其他不用):'))
    if a == "正方形2":
        print(b*b)
        break
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
        d = b+c
        while True:
            print(d*e/2)
            break
        break
    if a == "圆1":
        print(2*3.14*b)
        break
    if a == "圆2":
        print(3.14*b**2)
        break
    if a == "三角形1":
        print(b+b+b)
        break
    if a == "三角形2":
        print(b*a/2)
        break
    else:
        print('stop')
        continue
print('作者AWEkn1')
