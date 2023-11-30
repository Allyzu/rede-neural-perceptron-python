import math

input = 1
output_desire = 0
input_weight = 0.5

learning_rate = 0.01
bias = 1
bias_weight = 0.01

error = math.inf    
iteration = 0

print("Entrada:", input, "Desejado:", output_desire)

while not error == 0:  
    iteration += 1
    print("####### Interações", iteration)
    print("Peso", input_weight)

    sum = (input * input_weight) + (bias * bias_weight)

    def activation(sum):
        if sum >= 0:
            return 1
        else:
            return 0

    output = activation(sum)

    print("Saida", output)

    error = output_desire - output

    print("Erro", error)

    if not error == 0:
        input_weight = input_weight + (learning_rate * error * input)
        bias_weight = bias_weight + (learning_rate * error * bias)

print("REDE TREINADA COM SUCESSO!!!")
