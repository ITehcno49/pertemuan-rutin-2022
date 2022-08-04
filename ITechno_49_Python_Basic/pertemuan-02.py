# Operator

a = 10
b = 4
c = 20

print("a = ",a)
print("b = ",b)
print("c = ",c)

print("<<<<<<<<<<<Aritmatika>>>>>>>>>>>>\n")

#Operator aritmatika (+)(-)(*)(/)(%)(**)(//)

#Penjumlahan (+)
hasil = a + b 
print(a,"+",b,"=",hasil)

#Pengurangan (-)
hasil = a - b
print(a,"-",b,"=",hasil)

#Perkalian (*)
hasil = a * b
print(a,"*",b,"=",hasil)

#Pembagian (/)
hasil = a / b
print(a,"/",b,"=",hasil)

#Modulo (%) = sisa pembagian
hasil = a % b
print(a,"%",b,"=",hasil)

#Eksponen/Perpangkatan (**)
hasil = a ** 2
print(a,"**",2,"=",hasil)

#Floor Division (//) = Menghilangkan koma
hasil = a // b
print(a,"//",b,"=",hasil)

'''
Untuk Operasi Aritmatika kalian bisa persingkat misal
saya mau menambahkan nilai a dengan c
'''
a += c # ini sama saja dengan a = a + c 
print(a)



print("\n<<<<<<<<Boolean>>>>>>>>")

#Operator Boolean

x = True
y = False

print("========AND=======")
# untuk and bisa dinotasikan (&) atau (and)
# and akan bernilai True bila kedua nilai True

print(x and x) #True and True = True
print(x and y) #True and False = False
print(y and x) #False and True = False
print(y and y) #False and False = False

print("========OR========")
# untuk OR bisa dinotasikan (|) atau (or)
# OR akan bernilai True bila ada True

print(x or x) #True or True = True
print(x or y) #True or False = True
print(y or x) #False or True = True
print(y or y) #False or False = True

print("========XOR========")
#untuk XOR bisa dinotasikan (^) 
#XOR akan bernilai True bila nilainya beda

print(x ^ x) #True ^ True = False
print(x ^ y) #True ^ False = True
print(y ^ x) #False ^ True = True
print(y ^ y) #False ^ False = False

print("==========NOT==========")
#untuk NOT bisa dinotasikan (~) atau (not)
#NOT berguna untuk merubah nilai BOOLEAN
print(not x) # not True = False
print(not y) # not False = True

print("=======================")
'''
Operator Boolean lain yang penting
(==) equal/ sama dengan akan bernilai True jika kedua nilai dikanan dan kiri sama
(!=)  not equal/ tidak sama dengan akan bernilai True jika kedua nilai dikanan dan kiri beda
(>) lebih besar ,langsung contoh aja
(<) lebih kecil , langsung conotoh aja
(>=) lebih besar sama dengan , langsung contoh aja
(<=) lebih kecil sama dengan , langsung contoh aja
'''

print(10 == 9)
print(10 > 9)
print(10 < 9)
print(10 != 9)

#Kalian bisa coba-coba sendiri biar lebih paham dan ya intinya main-main lah dengan syntax
#Kalo ada eror coba baca dulu erornya siapa tau paham :v
#Sebelum nannya kalo mau nyoba pecahin sendiri lebih bagus
#Kalo eror terus bisa coba tanya

#Salam ITechno 49

