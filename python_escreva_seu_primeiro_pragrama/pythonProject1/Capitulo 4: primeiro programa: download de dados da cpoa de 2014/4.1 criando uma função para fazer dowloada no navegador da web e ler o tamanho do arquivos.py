# 4.1 criando uma função para fazer dowloada no navegador da web e ler o tamanho do arquivos
##indereço do buffe size
BUFF_SIZE = 1024
def dowloadLength(response, output, length):
  times = length / BUFF_SIZE
  if length % BUFF_SIZE > 0:
    times += 1
  for time in range(times):
    output.write(response.read(BUFF_SIZE))
    print("Dowloaded %d " % (((time * BUFF_SIZE)/length)*100))


# criando outra função para download na web

def dowload(response, output):
  totalDowloaded = 0
  while True:
    data = response.read(BUFF_SIZE)
    totalDowloaded += len(data)
    if not data:
      break
    output.write(data)
    print(f"Downloaded {bytes}".format(bytes = totalDowloaded))
