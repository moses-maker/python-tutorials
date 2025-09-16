"""
for loop

the syntax is :

for iteration_variable membership_operator sequence:
    print(iteration_variable)

> iteration_variable - this is just any variable
> membership_operator - this includes (in, not in) 
> sequence involves the -range() function.
    range(start, stop, step)

        - stop value is ignore


# start , stop
for counter in range(1, 50):
    print(counter)
"""


# start, stop, step
for counter in range(1, 50, 2):
    if counter==5:
        print("Five found")
        continue
    print(counter)