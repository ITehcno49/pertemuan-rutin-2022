#Pertemuan 1

print("Hello World")
# key-word <print()> adalah keyword untuk memberikan output ke console sesuai apa yang ada di dalam tanda kurung <()>
# pada contoh ini menggunakan tipe data string yang bertuliskan "Hello World"

#Variable
a = 10 
b = 40
c = a + b
# a dan b itu disebut dengan variable sedangkan 10 dan 40 adalah nilai dari variable
# pada variable c dimasukan varibale a dan b dan diberi operasi penjumlahan
print(a) # output-nya 10
print(b) # output-nya 40
print(c) # output-nya 50

#Tipe data
integer = 100                      # integer adalah tipe data berupa angka . Kalian bebas memasuka angka manapun
string = "Angkatan 25"          # string adalah tipe data berupa karakter ditandai dengan tanda kutip2 diawal dan akhir "contoh"
desimal = 48.9                      # float atau desimal merupakan tipe data yang memuat angka desimal ditandai ada titik
boolean = True                      # boolean adalah tipe data yang memuat True dan False

print(integer)
print(string)
print(desimal)
print(boolean)

#Casting
    #Merubah Tipe Data
'''
key-word casting

str() merubah tipe data menjadi string
int() merubah tipe data menjadi integer
bool() merubah tipe data menjadi boolean
float() merubah tipe data menjadi float/desimal

'''
angka1 = 400
angka2 = 600

#sebelum di casting tipe data masih integer
print(angka1 + angka2) #output-nya 1000

#setelah di casting tipe data menjadi string
print(str(angka1) + str(angka2)) #output-nya 400600


# Input user

a = input("Masukan nama : ") #syntax input() berguna untuk meminta input pada user
print("Hallo " + a) 