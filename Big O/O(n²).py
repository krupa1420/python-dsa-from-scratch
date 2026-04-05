# O(n²) - Quadratic Time
# Nested loops over the same input.
def print_nos(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print("Time complexity is O(n²)") 
print_nos(10)