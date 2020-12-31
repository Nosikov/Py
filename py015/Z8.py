string ="Hello World!"
print (string.upper())
print(string)
print("********************")
string=string.upper()
print(string)
print("+++++++++++++++++++++++")
print("hello!".upper())
print("#####################")
print(string.lower())
print(string)
print("$$$$$$$$$$$$$$$$$$$$$$$$")
msg ="abracatabra"
print(msg.count("ra"))
print(msg.count("ra",4))
print(msg.count("ra",4,10))
print(msg.count("ra",4,11))
print("%%%%%%%%%%%%%%%%%%%%%%%%%")
print(msg.find("br"))
print(msg.find("br",2))
print(msg.find("brr"))
print(msg.find("br",2,10))
print(msg.rfind("br"))
print(msg.index("ab"))
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
msg ="abracatabra"
msg.replace("a","o")
print(msg)
print(msg.replace("a","o"))
print(msg)
print(msg.replace("a","o",2))
print("==========================")
print(msg.isalpha())
print("Hello World".isalpha())
print("123456".isdigit())
print("123.456".isdigit())
print("&&&&&&&&&&&&&&&&&&&&&&&&")
"""dig=input("Введите число: ")
if(dig.isdigit()):
    dig=int(dig)
    print(dig)
else:
    print("Число введено неверно")"""
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
d="abc"
print(d.rjust(5))
print(d.rjust(5,"-"))
print(d.rjust(15,"-"))
print(d.ljust(5,"-"))
print(d.ljust(15,"-"))
print(">>>>>>>>>>>>>>>>>>>")
c="Иванов Иван Иванович"
c1=c.split(" ")
print(c)
print(c1)
digs="1, 2, 3 ,6 2,3,4,6  , 7 ,8"
digs1=digs.replace(" ","")
print(digs1)
digs2=digs.replace(" ","").split(",")
print(digs2)
str=", ".join(digs2)
print(str)
print("<<<<<<<<<<<<<<<<<<<<<")
fio="Петр Петрович Сидоров"
fio2=",".join(fio.split())
print(fio2)
print("      hello world \n".strip())
print("      hello world \n".lstrip())
print("      hello world \n".rstrip())






