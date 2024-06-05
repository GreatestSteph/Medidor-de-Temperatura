# biblioteca para o sensor DHT*
import adafruit_dht
# biblioteca para selecionar GPIO
import board
dhtDevice = adafruit_dht.DHT11(board.D18)


# Função para ler os valores do sensor DHT11 e imprimir
def mostra_temperatura():
   try:
       # Lê os valores do sensor DHT11
       temperatura_c = dhtDevice.temperature
       temperatura_f = temperatura_c * (9 / 5) + 32
       umidade = dhtDevice.humidity
      
       # Imprime os valores
       print("Temperatura: {:.1f} F / {:.1f} C Umidade: {}% ".format(temperatura_f, temperatura_c, umidade))
   except RuntimeError as error:
       # Em caso de erro, imprime a mensagem de erro
       print(error.args[0])
   except Exception as error:
       # Sai do programa em caso de erro
       dhtDevice.exit()
       raise error


# Loop principal
while True:
   # Chama a função para ler e imprimir os valores
   mostra_temperatura()
  
   # Pergunta ao usuário se deseja ver o resultado novamente
   decisao_usuario = input("Deseja ver o resultado novamente? (s/n): ")
  
   # Verifica a resposta do usuário
   if decisao_usuario.lower() != 's':
       break  # Sai do loop se a resposta não for 's'


