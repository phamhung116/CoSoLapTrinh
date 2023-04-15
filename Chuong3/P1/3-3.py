kw=float(input('Tieu thu='))
if kw>=1 and kw<=100:tien=550*kw
elif kw>=101 and kw<=150:tien=100*550+(kw-100)*750
elif kw>=151 and kw<=200:tien=100*550+50*750+(kw-150)*950
elif kw>=201:tien=100*550+50*750+50*950+(kw-200)*1350
phaitra=tien+tien*0.1
print('Phai tra=',phaitra,sep='')