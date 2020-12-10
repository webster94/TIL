croitia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
bin = ''
arr = input()
count = 0
for key in croitia:
    arr = arr.replace(key,'_')

print(len(arr))
