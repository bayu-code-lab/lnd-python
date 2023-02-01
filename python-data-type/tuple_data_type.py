# Deklarasi variable
tup = ("hi", "Python", 2)

# Checking tipe data
print(type(tup))

# Print tuple
print(tup)

# Ambil value yang terdapat di index 1
print(tup[1])

# Slicing tuple index 1 dan diatasnya
print(tup[1:])

# Slicing tuple index 0 dan 1
print(tup[0:1])

# Menggabungkan 2 tuple
print(tup + tup)

# melakukan perulangan menggunakan simbol *
print(tup * 3)

# Menambahkan value kedalam tuple akan mengakibatkan error
tup[2] = "hi"
