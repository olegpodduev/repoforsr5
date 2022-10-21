def transfer(n,s):
    a=''
    num=n
    while num>0:
        a=str(num%s)+a
        num//=s
    return print("Число",n,"в системе счисления",s,"равно: ",a)

def num():
    while True:
        system=int(input("Введите нужную вам систему счисления(двоичная или восьмеричная): "))
        if system!=8 and system!=2:
            print("Что-то пошло не так. Повторите ввод!")
        if system==2 or system==8:
            break
    return system

num_1=int(input("Введите целое положительное число: "))
sys=num()
transfer(num_1,sys)