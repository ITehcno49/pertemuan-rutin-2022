
#Tahun kabisat

#membuat variable untuk meminta input pada user

#Jika habis dibagi 400, tahun kabisat
#Jika tidak habis dibagi 400, tetapi habis dibagi 100, bukan tahun kabisat
#Jika tidak habis dibagi 400, tidak habis dibagi 100, tapi habis dibagi 4, tahun kabisat
#Jika tidak habis dibagi 400, tidak habis dibgai 100, tidak habis dibagi 4, bukan tahun kabisat

tahun = int(input())

if tahun % 400 == 0:
    print("tahun kabisat")

elif tahun % 400 != 0 and tahun % 100 == 0 :
    print("bukan tahun kabisat")

elif tahun % 400 != 0 and tahun % 100 != 0 and tahun % 4 == 0:
    print("tahun Kabisat")
   

else:
    print("bukan tahun kabisat")

