def main():

    print("Konversi Detik ke Jam\n")
 
    #Detik
    totaldetik = int(input("Masukkan detik \t: "))
 
    #Konversi
    hh = totaldetik // 3600
    sisadetik = totaldetik % 3600
    mm = sisadetik // 60
    ss = sisadetik % 60
 
    #Hasil
    print("%d detik sama dengan %d:%d:%d" %(totaldetik,hh,mm,ss))
 
if __name__ == "__main__":
    main()