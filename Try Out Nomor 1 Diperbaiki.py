#Program Hitung Nilai Mahasiswa
#Masukkan Input
NIM = int(input('Masukkan NIM Anda: '))
Nama =input('Masukkan Nama Anda: ')
Alamat = input('Masukkan Alamat Anda: ')
Asal_Sekolah = input('Masukkan Asal_Sekolah Anda: ')
Kode_Prodi = input('Masukkan Kode_Prodi Anda: ')
IPK_Awal = int(input('Masukkan IPK_Awal Anda: '))
Nilai_UAS = int(input('Masukkan Nilai_UAS Anda: '))
Nilai_UTS = int(input('Masukkan Nilai_UTS Anda: '))
Nilai_TM = int(input('Masukkan Nilai_TM Anda: '))

#Perhitungan IPK
import math
Nilai_UTS =(Nilai_UTS*30/100);
Nilai_TM =(Nilai_TM*30/100);
Nilai_UAS =(Nilai_UAS*40/100);
IPS = math.floor(Nilai_UTS+Nilai_TM+Nilai_UAS)

IPK = (IPS + IPK_Awal) / 2


#Perhitungan Beasiswa
if Kode_Prodi == "TI" or "SI":
    if IPK > 75 or < 85:
        print("Maka Beasiswanya adalah 20%")
    elif IPK > 85 or < 100:
        print("Maka Beasiswanya adalah 30%")
    else:
        print("")

if Kode_Prodi == "DKV" or "Teknik Industri":
    if IPK > 75 or < 85:
        print("Maka Beasiswanya adalah 25%")
    elif IPK > 85 or < 00:
        print("Maka Beasiswanya adalah 35%")
    else:
        print("")



