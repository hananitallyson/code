dist = float(input("Escreva a distância total em km (ex: 25.5): "))
tempo = input("Escreva o tempo total (ex: 1h30): ")
lista = tempo.split("h")

tempo_hora = int(lista[0])
tempo_min = int(lista[1])

tempo = tempo_hora + tempo_min / 60
velocidade_km = dist / tempo
velocidade_ms = velocidade_km / 3.6

print("Velocidade média do ciclista (km/h): %.2f Km/h"%velocidade_km)
print("Velocidade média do ciclista (m/s): %.2f m/s"%velocidade_ms)

