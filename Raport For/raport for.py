nilai = []
keterangan = []

pelajaran = ["PPKN","BAHASA INDONESIA", "AGAMA", "MTK"]
nama = input("Masukkan Nama Siswa : ")
for i in pelajaran:
	data = input(f"Masukkan Nilai {i}: ")
	ket = ""
	if int(data) < 50:
		ket = "Tidak Lulus"
	else:
		ket = "Lulus"
	
	nilai.append(int(data))
	keterangan.append(ket)

keterangan1 = ""
if sum(nilai) < 200:
	keterangan1 = "Tidak Lulus"
else:
	keterangan1 = "Naik Kelas"

h2o = f"\nNama : {nama}\nPPKN : {nilai[0]}\nBAHASA INDONESIA : {nilai[1]}\nAGAMA : {nilai[2]}\nMTK : {nilai[3]}\nPPKN : {keterangan[0]}\nBAHASA INDONESIA : {keterangan[1]}\nAGAMA : {keterangan[2]}\nMTK : {keterangan[3]}\n\nAnda {keterangan1}\nTotal Nilai : {sum(nilai)}"

c1 = open("ReportFor.sekolah",'a')
c1.write(h2o)
c1.close()


print(nama)
print(nilai)
print(keterangan)
print(keterangan1)
print(sum(nilai))