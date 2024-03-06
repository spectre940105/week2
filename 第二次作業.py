#圓面積＆圓周長

a=float(input("請輸入半徑："))
print("圓周長：",a*2*3.14)
print("圓面積：",a*a*3.14)

#字典

name=str(input("請輸入名字："))
age=int(input("請輸入年齡："))
height=float(input("請輸入身高(M)："))
color=str(input("請輸入喜歡的顏色："))
material={'name':name,'age':age,'height':height,'color':color}
print(material['name'],',',material['age'],'歲,身高',material['height'],'米,喜歡的顏色是',material['color'])

#判斷偶數

a1=input("請輸入整數：")
if(type(a1)==str):
    print("請輸入整數，不是字串or空字符串")
elif(a1=='int'):
    if(a1%2==0):
        print("偶數")
    else:
        print("基數")