string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
l=len(string)
total=0
while(len(string)>0):
    letter=string[0]
    i=0
    no_of_times=0
    for i in range(0,len(string)):
        if letter==string[i]:
            no_of_times += 1
    if no_of_times%2==1:
        total +=1
    string=string.replace(string[0],"")
if total>1:
    found=False
else:
    found=True
    
if not found:
    print("NO")
else:
    print("YES")