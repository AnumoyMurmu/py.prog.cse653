# Initialize counts for perfect squares, perfect cubes, and perfect fifth powers
count_square = 0
count_cube = 0
count_fifth_power = 0

# Iterate through numbers from 1 to 1000
for i in range(1, 1001):
    # Check if 'i' is a perfect square
    if int(i**0.5)**2 == i:
        count_square += 1

    # Check if 'i' is a perfect cube
    cc_cube = round(i**(1/3))
    if cc_cube**3 == i:
        count_cube += 1

    # Check if 'i' is a perfect fifth power
    cc_fifth = round(i**(1/5))
    if cc_fifth**5 == i:
        count_fifth_power += 1

# Print the counts of perfect squares, perfect cubes, and perfect fifth powers
print("Total perfect squares:", count_square)
print("Total perfect cubes:", count_cube)
print("Total perfect fifth powers:", count_fifth_power)
