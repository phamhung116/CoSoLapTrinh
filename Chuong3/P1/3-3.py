kw=float(input('Tieu thu='))
if kw>=1 and kw<=100: gia=550
elif kw>=101 and kw<=150: gia=750
elif kw>=151 and kw<=200: gia=950
elif kw>=201: tien=kw*1350
tien=kw*gia+0.1
print('Phai tra=',tien)