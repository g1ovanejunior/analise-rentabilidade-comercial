import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

n_pedidos = 5000

produtos = [
    ("PROD-01", "Cadeira Ergonomica Pro", "Mobiliario", "Cadeiras", 1200.00, 780.00),
    ("PROD-02", "Mesa Escritorio L-Shape", "Mobiliario", "Mesas", 1850.00, 1300.00),
    ("PROD-03", "Estante Modular Aco", "Mobiliario", "Estantes", 650.00, 460.00),
    ("PROD-04", "Notebook Corporativo i7", "Tecnologia", "Computadores", 4800.00, 3600.00),
    ("PROD-05", "Monitor Ultrawide 29", "Tecnologia", "Monitores", 1450.00, 1020.00),
    ("PROD-06", "Headset Noise Cancelling", "Tecnologia", "Acessorios", 420.00, 210.00),
    ("PROD-07", "Teclado Mecanico Sem Fio", "Tecnologia", "Acessorios", 350.00, 180.00),
    ("PROD-08", "Kit Papelaria Executiva", "Suprimentos", "Papelaria", 180.00, 85.00),
    ("PROD-09", "Caixa Papel A4 (10 resmas)", "Suprimentos", "Papel", 290.00, 195.00),
    ("PROD-10", "Fragmentadora de Papel", "Suprimentos", "Equipamentos", 540.00, 370.00),
]

estados_regioes = [
    ("MA", "Nordeste"), ("PE", "Nordeste"), ("BA", "Nordeste"), ("CE", "Nordeste"),
    ("SP", "Sudeste"), ("RJ", "Sudeste"), ("MG", "Sudeste"),
    ("PR", "Sul"), ("RS", "Sul"), ("SC", "Sul"),
    ("DF", "Centro-Oeste"), ("GO", "Centro-Oeste"), ("PA", "Norte")
]

segmentos = ["Corporativo", "Pequenas Empresas", "Consumidor Final"]

clientes = [
    (f"CLI-{i:03d}", f"Empresa Comercial {i}" if i % 2 == 0 else f"Cliente Varejo {i}",
     random.choice(segmentos), *random.choice(estados_regioes))
    for i in range(1, 451)
]

data_inicio = datetime(2024, 1, 1)
registros = []

for i in range(1, n_pedidos + 1):
    cli = random.choice(clientes)
    dias_offset = random.randint(0, 620) if int(cli[0].split("-")[1]) <= 60 else random.randint(0, 725)
    data_pedido = data_inicio + timedelta(days=dias_offset)

    prod = random.choice(produtos)
    qtd = random.randint(1, 10)

    if prod[2] == "Mobiliario":
        desconto = random.choice([0.0, 0.10, 0.20, 0.30, 0.40])
    else:
        desconto = random.choice([0.0, 0.05, 0.10, 0.15, 0.25])

    receita_bruta = prod[4] * qtd
    valor_venda = round(receita_bruta * (1 - desconto), 2)
    custo_total = prod[5] * qtd
    lucro = round(valor_venda - custo_total, 2)

    registros.append([
        f"PED-{10000+i}", data_pedido.strftime("%Y-%m-%d"),
        cli[0], cli[1], cli[2], cli[3], cli[4],
        prod[0], prod[1], prod[2], prod[3],
        qtd, desconto, valor_venda, lucro
    ])

colunas = [
    "id_pedido", "data_pedido", "id_cliente", "nome_cliente", "segmento",
    "estado", "regiao", "id_produto", "nome_produto", "categoria",
    "subcategoria", "quantidade", "desconto", "valor_venda", "lucro"
]

df = pd.DataFrame(registros, columns=colunas)
df.to_csv("dados/vendas_brutas.csv", index=False, encoding="utf-8-sig")
print(f"Base gerada com sucesso! {len(df)} pedidos salvos em dados/vendas_brutas.csv")