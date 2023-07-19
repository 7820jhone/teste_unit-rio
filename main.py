def calcular_valor_total(valor_unitario: float, quantidade: int) -> float:
    '''
    Calcula o valor total de um produto com base em seu valor unitario e quantidade,
    dos descontos aplicáveis.

    Args:
	    valor_unitario (float): Valor unitario do produto.
	    quantidade (int): Quantidade desejada do produto.

    Returns:
	    Tuple[float, float]: Tupla contendo os valores sem desconto e com desconto.
    '''
    # No desconto completo de até 1, é o valor do desconto.
    # Ex: se multiplicar o valor por 1, é o mesmo valor ou seja, sem desconto 
    desconto = 1
    
    # Calcula o desconto com base na quantidade de produtos comprados
    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    # Calcula o valor total com e sem desconto
    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    # Retorna uma tupla contendo os valores com e sem desconto
    return valor_sem_desconto, valor_com_desconto

if __name__ == '__main__':
    valor_unitario = float(input('Valor unitário do produto: '))
    quantidade = int(input('Quantidade: '))

    valor_sem_desconto, valor_com_desconto = calcular_valor_total(valor_unitario, quantidade)

    print(f'Valor total sem desconto: {valor_sem_desconto:.2f} R$')
    print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')