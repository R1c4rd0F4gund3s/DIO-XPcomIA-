import re

def identificar_bandeira(numero):
    # Remove todos os caracteres que não são dígitos
    numero = re.sub(r"\D", "", numero)
    
    # Lista de bandeiras e seus padrões regex
    bandeiras = [
        {"nome": "Visa",        "regex": r"^4\d{12}(\d{3})?$"},
        {"nome": "MasterCard",  "regex": r"^(5[1-5]\d{14}|2(2[2-9]|[3-6]\d|7[01])\d{12}|2720\d{12})$"},
        {"nome": "American Express", "regex": r"^3[47]\d{13}$"},
        {"nome": "Elo",         "regex": r"^(4011(78|79)\d{10}|(431274|438935|451416|457393|504175|627780|636297|636368|650\d{2}|6516\d{2}|6550\d{2})\d{10})$"},
        {"nome": "Hipercard",   "regex": r"^606282\d{10}(\d{3})?$"},
        {"nome": "Diners Club", "regex": r"^3(0[0-5]|[68]\d)\d{11}$"},
        {"nome": "Discover",    "regex": r"^6(?:011|5\d{2})\d{12}$"},
        {"nome": "JCB",         "regex": r"^(?:2131|1800|35\d{3})\d{11}$"},
    ]
    
    # Verifica cada padrão e retorna a bandeira correspondente
    for bandeira in bandeiras:
        if re.match(bandeira["regex"], numero):
            return bandeira["nome"]
    return "Bandeira desconhecida"

def main():
    print("=== Identificador de Bandeira de Cartão de Crédito ===")
    while True:
        # Solicita ao usuário o número do cartão
        numero = input("Digite o número do cartão (ou 'x' para encerrar): ")
        # Se digitar 'x', encerra o programa
        if numero.lower() == 'x':
            break
        # Identifica a bandeira e exibe o resultado
        bandeira = identificar_bandeira(numero)
        print(f"Bandeira identificada: {bandeira}\n")

if __name__ == "__main__":
    main()

