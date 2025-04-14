def calcular_distancia(origem, destino):
    try:
        origem = int(str(origem))
        destino = int(str(destino))
        distancia_km = abs(origem - destino) / 1000.0
        return round(distancia_km, 2)
    except ValueError:
        raise ValueError("Origem e destino devem ser numéricos ou convertíveis em inteiros.")
