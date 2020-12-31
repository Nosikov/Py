ifile="../user_names.txt"
myfile=open(ifile,mode='r',encoding='ascii')
#print(myfile.read())
print("*****************************")
#for line in myfile:
#    print("hello " + line)
print("+++++++++++++++++++++++++++++++")
#for num, line in enumerate(myfile, 1):
#    print("hello " +str(num) +" : " + line)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#for num, line in enumerate(myfile, 1):
#    if "Nelly" in line:
#        print("hello " +str(num) +" : " + line)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
ifile="../list_of_passwords.txt"
ofile="../pass.txt"
myfile1=open(ifile,mode='r',encoding='latin_1')
myfile2=open(ofile,mode='w',encoding='latin_1')

for num, line in enumerate(myfile1, 1):
    if "vasya" in line:
        print(str(num) +" : " + line)
        myfile2.write(str(num) +" : " + line)

myfile1.close()
myfile2.close()



