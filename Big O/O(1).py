# O(1) - Constant Time
# rule for simplifying 
# 1. drop constant. eg O(2n) : answer is O(n)
# 2. drop non - dominants. eg O(2n² + n) : answer is only O(n²)
def add_items(n):
    return n + n + n 

print("Time complexity is O(n²)") #only 1 operation
print(add_items(1))