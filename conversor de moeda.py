import requests

def obter_cotacao(moeda_base, moeda_destino):
    url = f"https://api.exchangerate.host/latest?base={moeda_base.upper()}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao obter dados da API.")
        return None

    dados = resposta.json()
    try:
        taxa = dados["rates"][moeda_destino.upper()]
        return taxa
    except KeyError:
        print("Moeda não encontrada.")
        return None

def conversor():
    print("=== Conversor de Moedas ===")
    base = input("Moeda de origem (ex: USD): ").upper()
    destino = input("Moeda de destino (ex: BRL): ").upper()
    try:
        valor = float(input(f"Quantos {base} você deseja converter? "))
    except ValueError:
        print("Valor inválido!")
        return

    taxa = obter_cotacao(base, destino)
    if taxa:
        convertido = valor * taxa
        print(f"{valor:.2f} {base} = {convertido:.2f} {destino} (Taxa: {taxa:.4f})")

# Executa o conversor
conversor()
