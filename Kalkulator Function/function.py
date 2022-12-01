def Penjumlahan(n1, n2):
	return n1 + n2

def Pengurangan(n1, n2):
	return n1 - n2

def Perkalian(x, y):
	return x * y

def Pembagian(n1, n2):
	return n1 / n2

def GetSisa(n1, n2):
	return n1 % n2

print("="*50)
print("\t\tKalkulator Funtion")
print("\n\n\n\t\t\t\tBy : Kimin")
print("="*50)
print("Silahkan Pilih Jenis Operasi : ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Sisa Bagi")
pilih = int(input("Operasi : "))
nilai1 = float(input("Masukkan Nilai 1 : "))
nilai2 = float(input("Masukkan Nilai 2 : "))
if pilih == 1:
	hasil = Penjumlahan(nilai1, nilai2)
elif pilih == 2:
	hasil = Pengurangan(nilai1, nilai2)
elif pilih == 3:
	hasil = Perkalian(nilai1, nilai2)
elif pilih == 4:
	hasil = Pembagian(nilai1, nilai2)
elif pilih == 5:
	hasil = GetSisaSisa(nilai1, nilai2)
print(hasil)
# x =13