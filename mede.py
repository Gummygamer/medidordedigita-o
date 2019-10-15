import time

#lendo o tamanho da entrada com tratamento do caso de o tamanho digitado ser inválido
try:
	c = int(input('Digite a quantidade de palavras.'))
except Exception:
	print('Por favor tente de novo digitando um número válido.')
else:		
	if c >= 0:
		for i in range(c):
			#medindo o tempo e atribuindo a palavra digitada a p
			t0 = time.time()
			p = input()
			t1 = time.time()

			s = len(p)

			#verificando o tamanho da palavra e exibindo adequadamente o tempo

			if s >= 9 and s <= 10000:
				tempo = round(t1 - t0, 2)
				print("%.2f" % tempo)
			else:
				print('Palavra de tamanho inadequado.A quantidade de letras deve estar entre 9 e 10000')
	else:
		print('Por favor tente de novo digitando um número positivo.')


