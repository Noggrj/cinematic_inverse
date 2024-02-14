import math

a1 = 20
a2 = 10
ponto_x = 20.36 
ponto_y = 17.3

d = (ponto_x**2 + ponto_y**2 - a1**2 - a2**2) / (2 * a1 * a2)

# Verifique se o valor dentro da raiz quadrada está no intervalo [-1, 1]
sqrt_value = max(0, min(1, 1 - d**2))
theta_2 = math.degrees(math.atan(math.sqrt(sqrt_value) / d))

print('Theta 2: %g' % theta_2)
print('Cotovelo Abaixo Teta 2: %g' % (theta_2 + 90))
print('Cotovelo Acima Teta 2: %g' % (math.degrees(math.atan(-math.sqrt(sqrt_value) / d)) + 90))

alfa_siciliano = math.degrees(math.atan2(ponto_y, ponto_x))
beta_siciliano_1 = (ponto_x**2 + ponto_y**2 + a1**2 - a2**2) / (2 * a1 * math.sqrt(ponto_x**2 + ponto_y**2))
beta_siciliano_2 = math.degrees(math.acos(max(-1, min(1, beta_siciliano_1))))

print('Cotovelo Abaixo Teta 1: %g' % (beta_siciliano_2 - alfa_siciliano))
print('Cotovelo Acima Teta 1: %g' % (beta_siciliano_2 + alfa_siciliano))

print("Execucao concluida")

