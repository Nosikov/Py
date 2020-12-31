cars=['bmw','vw','fiat','skoda','lada']
print(cars)
print("***********************")
for car in cars:
    print(car)
print("++++++++++++++++++++++")
for x in cars:
    print(x.upper())
print("-------------------------")
for x in range(1,6):
    print(x)
print("########################")
mynumberlist = list(range(0,10))
print(mynumberlist)
for x in mynumberlist:
    x=x*2
    print(x)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
mynumberlist.sort(reverse=True)
print(mynumberlist)
print("=========================")
print("maximum = " + str(max(mynumberlist)))
print("minimum = " + str(min(mynumberlist)))
print("sum = " + str(sum(mynumberlist)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
cars=['bmw','vw','fiat','skoda','lada']
mycars=cars[1:3]
print(mycars)
mycars=cars[:4]
print(mycars)
mycars=cars[-3:]
print(mycars)
print(">>>>>>>>>>>>>>>>>>>>>>>>>")
cars=['bmw','vw','fiat','skoda','lada']
cars1=cars
cars1.append('volvo')
print(cars)
print(cars1)
cars2=cars[:]
cars2.append("ferari")
print("-------------")
print(cars)
print(cars1)
print(cars2)




