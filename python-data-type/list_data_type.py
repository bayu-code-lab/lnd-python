# Deklatasi Variable
list1 = [1, "hi", "Python", 2]

# Checking tipe data
print(type(list1))

# Print list1
print(list1)

# Ambil value yang terdapat di index 1
print(list1[1])

# Slicing List dengan mengambil index 3 keatas
print(list1[3:])

# Slicing List dengan mengambil index 0 sampai dengan 2
print(list1[0:2])

# Menggabungkan 2 list
print(list1 + list1)

# Melakukan perulangan menggunakan simbol *
print(list1 * 3)

# Tambahkan Key dan Value baru pada dictionary
list1.append('bayu')
print(list1)

# Update value pada index 4
list1[4] = 'Maria'
print(list1)

# delete key 1
del list1[1]
print(list1)
