#Program Hitung Nilai Mahasiswa
#Masukkan Input
NIM = input('Masukkan NIM Anda: ')
Nama =input('Masukkan Nama Anda: ')
Alamat = input('Masukkan Alamat Anda: ')
Asal_Sekolah = input('Masukkan Asal_Sekolah Anda: ')
Kode_Prodi = input('Masukkan Kode_Prodi Anda: ')
Nilai_UAS = input('Masukkan Nilai_UAS Anda: ')
Nilai_UTS = input('Masukkan Nilai_UTS Anda: ')
Nilai_TM = input('Masukkan Nilai_TM Anda: ')

#Perhitungan IPK
Nilai_UTS =(Nilai_UTS*30/100);
Nilai_TM =(Nilai_TM*30/100);
Nilai_UAS =(Nilai_UAS*40/100);
IPK = Nilai_UTS+Nilai_TM+Nilai_UAS


print ("NIM      :%d" %NIM)

#Perhitungan Beasiswa
if  "TI" and "SI"
elif 75<IPK<85
    print("Beasiswa 20%")
else 85<IPK<100
    print("Beasiswa 30%")


if  "DKV" and "Teknik Industri"
elif 75<IPK<85
    print("Beasiswa 25%")
else 85<IPK<100
    print("Beasiswa 35%")

