numbers = [34,54,6,68,57,21,433,56,7]

for i in numbers:
    print(i)
    
name_list = ["Sreekanth","Abhijith","Suhan","Shyam"]
lenght = len(name_list)

while(lenght > 0):
    for i in name_list:
        print(i)
        
    lenght -=1           
    
# break
for i in numbers:
    if i == 54:
        break
    print(i)
    
# continue
for number in numbers:
    if number == 54:
        continue
    print(number)