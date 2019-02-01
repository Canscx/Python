print "计算器启动中..."

option = raw_input("为圆输入C，为三角形输入T： ")

if option == 'C':
    radius = float(raw_input("输入半径: "))
    area = 3.14159 * radius ** 2
    print "Area: %f" % area
elif option == 'T':
    base = float(raw_input("输入底边: "))
    height = float(raw_input("输入高: "))
    area = 0.5 * base * height
    print "Area: %f" % area
else:
    print "错误！请输入有效的文字！"

print "退出中..."
