print("Привет, Давай Поиграем")
num = int(input("Выберите Первое число:"))
num2 =  int(input("Выберите Второе число:"))
place = input ("Выберите действие (+, -, *, /):")
if place =="+":
    print(num + num2)
elif place =="-":
        print(num - num2)
elif place =="*":
            print(num * num2)
elif place =="/":
    if num2 ==0:
        print("На Ноль Делить нельзя.")
    else:
       print(num / num2)
else:
    print("Такой Операции НЕТ.")
