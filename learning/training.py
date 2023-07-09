import string
import random
import neuron

characters = string.digits + '-.'

learning_rate = 0.01
bias = 1.0
num_epochs = 1000
num_examples = 100

def generate_training_data(num_examples):
    training_set = []
    desired_set = []

    for _ in range(num_examples):
        number = ''.join(random.choices(characters, k=12))
        inputs = [1.0 if char == '-' else 0.0 for char in number]
        desired_output = 1.0 if is_real_number(number) else 0.0
        training_set.append(inputs)
        desired_set.append(desired_output)

    return training_set, desired_set

def is_real_number(number):
    if number.count('-') > 1:
        return False
    if number.count('.') > 1:
        return False
    if not any(char.isdigit() for char in number):
        return False
    if number[0] == '-':
        number = number[1:]
    if '.' in number:
        integer_part, fractional_part = number.split('.')
        if not integer_part.isdigit() or not fractional_part.isdigit():
            return False
    else:
        if not number.isdigit():
            return False
    return True

X, Y = generate_training_data(num_examples)

perceptron = neuron.Perceptron(X, Y, learning_rate, bias)
for _ in range(num_epochs):
    perceptron.learn()

number = input("Digite um número: ")

inputs = [1.0 if char == '-' else 0.0 for char in number]

prediction = perceptron.compute_output(inputs)

if prediction >= 0.5:
    print("Símbolo válido")
else:
    print("Símbolo inválido")
