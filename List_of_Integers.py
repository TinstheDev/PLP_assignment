# Accept user input for a list of integers
input_string = input("Enter integers separated by spaces: ")

# Convert the input string into a list of integers
int_list = [int(num) for num in input_string.split()]

# Compute the sum of the integers
total_sum = sum(int_list)

# Print the result
print("The sum of the integers is:", total_sum)
