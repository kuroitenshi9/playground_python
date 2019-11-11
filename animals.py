arr = ["kot", "pies", "pingwin", "alpaka", "osmiorniczka"]

counter = 0
while counter < len(arr):
    a = arr[counter]
    counter += 1
    if a == "alpaka":
        print("*") #continue, break
    print(a)

print("poza pętlą")
print("--------------------------")

for a in arr:
    if a == "alpaka":
        break
    print(a)

print("poza pętlą")
print("--------------------------")

for a in arr:
    if a == "alpaka":
        continue
    print(a)
