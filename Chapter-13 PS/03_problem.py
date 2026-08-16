# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

# table = [str(7 * i)for i in range(1, 11)]
table = [str(f"7 * {i} = {7 * i}") for i in range(1, 11)]
# table = [str("7 * {} = {}".format(i, 7 * i)) for i in range(1, 11)]
vertical_format = "\n".join(table)

print(vertical_format)