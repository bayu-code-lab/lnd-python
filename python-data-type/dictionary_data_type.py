data = {1: 'Jimmy', 2: 'Alex', 3: 'john', 4: 'mike'}

# Print dictionary
print(data)

# Akses value meggunakan keys
print("Nama pertama adalah " + data[1])
print("Nama kedua adalah " + data[4])

# Tambahkan Key dan Value baru pada dictionary
data[5] = 'bayu'
print(data)

# Update value pada key 2
data[2] = 'Maria'
print(data)

# delete key 1
del data[1]
print(data)

print(data.keys())
print(data.values())
