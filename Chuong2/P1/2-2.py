GiaNiemYet=int(input('Nhap Gia Niem Yet: '))
ChietKhau=int(input('Nhap Chiet Khau: '))
VAT=(GiaNiemYet-ChietKhau)*0.01
GiaBan=GiaNiemYet-ChietKhau+VAT
print('Gia ban:',GiaBan)