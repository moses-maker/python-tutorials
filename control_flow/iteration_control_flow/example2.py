
user_input = int(input("Enter range to determine devisors of 2?"))

control_var = 0

even_numbers = 0

odd_numbers = 0

while control_var<user_input:
    if control_var%2==0:
        even_numbers +=control_var
        
    else:
        odd_numbers += control_var

    control_var += 1


print("Total even numbers", even_numbers)
print("Total odd numbers is", odd_numbers)