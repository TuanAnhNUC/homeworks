import time

while True:
    s = int(input('Nhap thu nhap($): '))
    if s<0: # Neu nhap so am thi yeu cau nhap lai
        print('Nhap lai thu nhap')
        continue
    elif s<=10000: # Neu thu nhap nho hon hoac bang 10000 thi thue 10%
        tax = s*0.1
        print('Thue phai nop: ', tax, '$')
        time.sleep(3)
        break
    elif s<=50000: # Neu thu nhap nho hon hoac bang 50000 thi thue 10% cho 10000 dau tien va 20% cho phan con lai
        tax = s*0.1+(s-10000)*0.2
        print('Thue phai nop: ', tax, '$')
        time.sleep(3)
        break

    else:
        tax = 10000*0.1+50000*0.2+(s-50000)*0.4 # Neu thu nhap lon hon 50000 thi thue 10% cho 10000 dau tien, 20% cho 50000 tiep theo va 40% cho phan con lai
        print('Thue phai nop: ', tax, '$')
        time.sleep(3)
        break
