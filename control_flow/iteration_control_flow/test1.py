"""
Syntax for while loop

control_variable = value
while condition:
    statements
    control_variable += 1 or -= 1



counter = 5  # 0, 1, 2, 3 ,4 ,5
while counter>0: # True, True, True, True, True
    print(counter) # 0, 1, 2, 3, 4
    if counter==
    counter += 1 # 0+1, 1+1, 2+1, 3+1, 4+1
"""
counter=0
while counter<=10:
    print(counter)
    if counter==5:
        #print("stopped here.")
        #break
        print("Found 5 continue...")
        continue
    counter += 1
