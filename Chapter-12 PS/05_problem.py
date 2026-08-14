# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter the number for table: "))

# table = [n*i for i in range(1, 11)]
table = [f"{n} x {i} = {n * i}" for i in range(1, 11)]
print(table)
with open("Chapter-12 PS/tables.txt", "a") as t:
    # t.write(f"Table of {n}: {str(table)} \n")
    t.write(f"\nTable of {n}\n")
    t.write("\n".join(table) + "\n")