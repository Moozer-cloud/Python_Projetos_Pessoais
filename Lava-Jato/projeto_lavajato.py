from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta


tipo_de_carro = input(
    "################################\n"
    "Categorias Disponíveis:\n[1] Hatch\n[2] Sedan\n[3] SUV\n[4] Picape"
    "\n[5] Utilitário\n[6] Caminhão\n[7] Carreta\n"
    "################################\n\n"
    "Informe qual a categoria do Veículo: "
    )

print(tipo_de_carro)

tempo_hatch = 30
tempo_sedan = 45
tempo_suv = 60
tempo_picape = 90
tempo_utilitario = 120
tempo_caminhao = 150
tempo_carreta = 210

mascara_data_ptbr = ("%d/%m/%Y")
mascara_horario_ptbr = ("%H:%M")

data_atual = datetime.now()

if tipo_de_carro == "1":
    data_estimada = data_atual + timedelta(minutes=tempo_hatch)
    print(
        f"\nCategoria Selecionada: Hatch"
        f"\n-------------------------------------------\n"
        f"Seu Veículo chegou em {data_atual.strftime(mascara_data_ptbr)} às {data_atual.strftime(mascara_horario_ptbr)}\n"
        f"-------------------------------------------\n"
        f"Tempo estimado de finalização: {tempo_hatch} minutos.\n"
        f"-------------------------------------------\n"
        f"Seu Veículo ficará pronto em {data_estimada.strftime(mascara_data_ptbr)} às {data_estimada.strftime(mascara_horario_ptbr)}\n"
        )
elif tipo_de_carro == "2":
    data_estimada = data_atual + timedelta(minutes=tempo_sedan)
    print(
        f"\nCategoria Selecionada: Hatch"
        f"\n-------------------------------------------\n"
        f"Seu Veículo chegou em {data_atual.strftime(mascara_data_ptbr)} às {data_atual.strftime(mascara_horario_ptbr)}\n"
        f"-------------------------------------------\n"
        f"Tempo estimado de finalização: {tempo_sedan} minutos.\n"
        f"-------------------------------------------\n"
        f"Seu Veículo ficará pronto em {data_estimada.strftime(mascara_data_ptbr)} às {data_estimada.strftime(mascara_horario_ptbr)}\n"
        )
elif tipo_de_carro == "3":
    data_estimada = data_atual + timedelta(minutes=tempo_suv)
    print(
        f"\nCategoria Selecionada: Hatch"
        f"\n-------------------------------------------\n"
        f"Seu Veículo chegou em {data_atual.strftime(mascara_data_ptbr)} às {data_atual.strftime(mascara_horario_ptbr)}\n"
        f"-------------------------------------------\n"
        f"Tempo estimado de finalização: {tempo_suv} minutos.\n"
        f"-------------------------------------------\n"
        f"Seu Veículo ficará pronto em {data_estimada.strftime(mascara_data_ptbr)} às {data_estimada.strftime(mascara_horario_ptbr)}\n"
        )
elif tipo_de_carro == "4":
    data_estimada = data_atual + timedelta(minutes=tempo_picape)
    print(
        f"\nCategoria Selecionada: Hatch"
        f"\n-------------------------------------------\n"
        f"Seu Veículo chegou em {data_atual.strftime(mascara_data_ptbr)} às {data_atual.strftime(mascara_horario_ptbr)}\n"
        f"-------------------------------------------\n"
        f"Tempo estimado de finalização: {tempo_picape} minutos.\n"
        f"-------------------------------------------\n"
        f"Seu Veículo ficará pronto em {data_estimada.strftime(mascara_data_ptbr)} às {data_estimada.strftime(mascara_horario_ptbr)}\n"
        )
elif tipo_de_carro == "5":
    data_estimada = data_atual + timedelta(minutes=tempo_utilitario)
    print(
        f"\nCategoria Selecionada: Hatch"
        f"\n-------------------------------------------\n"
        f"Seu Veículo chegou em {data_atual.strftime(mascara_data_ptbr)} às {data_atual.strftime(mascara_horario_ptbr)}\n"
        f"-------------------------------------------\n"
        f"Tempo estimado de finalização: {tempo_utilitario} minutos.\n"
        f"-------------------------------------------\n"
        f"Seu Veículo ficará pronto em {data_estimada.strftime(mascara_data_ptbr)} às {data_estimada.strftime(mascara_horario_ptbr)}\n"
        )
elif tipo_de_carro == "6":
    data_estimada = data_atual + timedelta(minutes=tempo_caminhao)
    print(
        f"\nCategoria Selecionada: Hatch"
        f"\n-------------------------------------------\n"
        f"Seu Veículo chegou em {data_atual.strftime(mascara_data_ptbr)} às {data_atual.strftime(mascara_horario_ptbr)}\n"
        f"-------------------------------------------\n"
        f"Tempo estimado de finalização: {tempo_caminhao} minutos.\n"
        f"-------------------------------------------\n"
        f"Seu Veículo ficará pronto em {data_estimada.strftime(mascara_data_ptbr)} às {data_estimada.strftime(mascara_horario_ptbr)}\n"
        )
elif tipo_de_carro == "7":
    data_estimada = data_atual + timedelta(minutes=tempo_carreta)
    print(
        f"\nCategoria Selecionada: Hatch"
        f"\n-------------------------------------------\n"
        f"Seu Veículo chegou em {data_atual.strftime(mascara_data_ptbr)} às {data_atual.strftime(mascara_horario_ptbr)}\n"
        f"-------------------------------------------\n"
        f"Tempo estimado de finalização: {tempo_carreta} minutos.\n"
        f"-------------------------------------------\n"
        f"Seu Veículo ficará pronto em {data_estimada.strftime(mascara_data_ptbr)} às {data_estimada.strftime(mascara_horario_ptbr)}\n"
        )
else:
    print("Categoria Selecionada incorreta, escolha uma Categoria válida!")
