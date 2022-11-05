def average(seq):
    return sum(seq)/len(seq)


options = {
    "add": sum,
    "avg": average,
    "max": max
}
numbers = [1, 4, 16, 20]

action = input(f"What would you like to do with {numbers}?")  # e.g. add

operation = options.get(action)

if operation:
    operation(numbers)
else:
    print("Action not recognized")
    
print(action)