print "������������..."

option = raw_input("ΪԲ����C��Ϊ����������T�� ")

if option == 'C':
    radius = float(raw_input("����뾶: "))
    area = 3.14159 * radius ** 2
    print "Area: %f" % area
elif option == 'T':
    base = float(raw_input("����ױ�: "))
    height = float(raw_input("�����: "))
    area = 0.5 * base * height
    print "Area: %f" % area
else:
    print "������������Ч�����֣�"

print "�˳���..."
