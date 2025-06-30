numbers=[11,22,33,44,55,66,77,88,99]
key=77
start=0

end=len(numbers)-1
found=False
for i in len(numbers):
    if numbers(1) == key:
        print("Found")
    else:
        print("Not Found")

while start <= end:
    mid=( start + end)//2
    if numbers[mid]==key:
        print("Found element at pos:",mid)
        found=True
    elif key<numbers[mid]:
        end=mid-1
    else:
        start = mid+1

if not found:
    print(f"{key} not found on the list of variables")



