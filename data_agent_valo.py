import os
import random
import string
os.system("cls")  


print(f" {'DATA AGENT ':#^35}")
data = dict()
while True:
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    
    NamaA = input("Enter nama Agent\t: ")
    Role = input("Enter Role (misal: Duelist, Smoker): ")

    
    data[keyFinal] = {
        'NamaA': NamaA,
        'Role': Role,
    }

    opsi = input("input lagi (ya/t) : ").lower()
    if opsi == 't':
        break 
  
# Menampilkan hasil data
print("-" * 40)
print(f"{'Key':<5} {'Nama Agent ':<20} {'Role':<15} ")
print("-" * 40)
for k, v in data.items():
    print(f"{k:<5} {v['Nama Agent']:<20} {v['Role']:<15} ")

# Menampilkan semua data
print("-" * 40)
print("Data Agent :")
print(data)