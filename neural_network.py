import math
# input

# processing - weights & biases, activation function


# activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1-x)

# output


# how to represent stuff on the computer?


# output - will be a certain color - red, yellow, blue

x = 5

print(sigmoid(x))
print(sigmoid_derivative(x))