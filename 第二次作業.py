#圓面積＆圓周長

radius=float(input("請輸入半徑："))
print("圓周長：",radius*2*3.14)
print("圓面積：",radius*radius*3.14)

#字典

name=str(input("請輸入名字："))
age=int(input("請輸入年齡："))
height=float(input("請輸入身高(M)："))
color=str(input("請輸入喜歡的顏色："))
material={'姓名':name,'年齡':age,'身高':height,'顏色':color}
output=f'{material["姓名"]},{material["年齡"]}歲,身高{material["身高"]}米,最喜歡的顏色{material["顏色"]}'
print(output)

#判斷偶數
while True:
    try:
        number=input("請輸入整數:")
        number=int(number)
        if(number%2==0):
            print(f"{number}是偶數")
        else:
            print(f"{number}是基數")
        break
    except ValueError:
        print("錯誤,請輸入整數")
    