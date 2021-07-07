def create_report():
    componentes_verificados = set(['caixa de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'componente', 'hub', 'impressora','joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de video', 'placa mãe', 'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])

    qtde_de_componentes_verificados = len(componentes_verificados)
    qtde_de_componentes_com_defeito = len(componentes_com_defeito)

    componentes_ok = componentes_verificados.difference(componentes_com_defeito)

    print(f"Foram verificados {qtde_de_componentes_verificados} componentes.\n")
    print(f"{qtde_de_componentes_com_defeito} componentes apresentaram defeito.\n")

    print(f"Os componentes que podem ser vendidos são:")
    for item in componentes_ok:
        print(item)

create_report()