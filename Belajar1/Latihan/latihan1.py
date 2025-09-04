# Latihan konversi satuan temperature

#Konversi Celcius ke Satuan lain

print("\n===PROGRAM KONVERSI TEMPERATUR===\n")

celcius_input = float(input("Masukan suhu dalam Celcius : "))
print("Suhu yang anda masukan =", celcius_input, "Celcius")

# Reamur
reamur = (4/5) * celcius_input
print(reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius_input) + 32
print(fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius_input + 273
print(kelvin, "Kelvin")


###Fahrenheit to Kelvin
iFahrenheit = float(input("Masukan suhu dalam Fahrenheit : "))
f_to_c = (5/9)* (iFahrenheit-32) #Konversi dulu dari fahrenheit ke celcius
c_to_k = f_to_c + 273 #terus dari celcius ke kelvin
print(c_to_k, "Kelvin dari", iFahrenheit, " Fahrenheit")

###Kelvin to Fahrenheit
iKelvin = float(input("Masukan suhu dalam Kelvin : "))
k_to_c = iKelvin - 273
c_to_f = ((9/5) * k_to_c) + 32
print(c_to_f, "Fahrenheit dari", iKelvin, "Kelvin")

