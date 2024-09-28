def valida_pos(pos:str) -> bool:
    """
    Valida a pos do cavalo passada para o script
    
    Entrada:
        - pos:str   posição inicial do cabalo

    Saída: 
        - True ou False:bool    validação
    """
    x_ax= "abcdefgh"
    y_ax= [1, 2, 3, 4, 5, 6, 7, 8]

    if (pos[0] in x_ax) and (int(pos[1]) in y_ax):
        return True
    
    return False


def calcula_pos(pos:str) -> list[str]:
    """
    Calcula posições disponíveis para o cavalo pular

    Entrada:
        - pos:str   posição inicial do cavalo

    Saída:
        - pos_val:list[str]    lista com posições válidas
    """

    x_ax= "abcdefgh"

    # Faz a conversão de 'letra num' para 'num num' ('a4' -> (1, 4))
    x, y = x_ax.index(pos[0]) + 1, int(pos[1])

    movimentos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    pos_val = []

    for dx, dy in movimentos:
        novo_x = x + dx
        novo_y = y + dy

        # Verifica se a nova posição está dentro dos limites
        if (1 <= novo_x <= 8) and (1 <= novo_y <= 8):
            pos_val.append((novo_x, novo_y))

    for i in range(len(pos_val)):
        # Converte de volta para o formato 'letra num'  ((1, 4) -> 'a4')
        x, y = pos_val[i]
        x = x_ax[x - 1]
        pos_val[i] = f"{x}{y}"


    return sorted(pos_val)


while True:
    pos = input("")

    if pos == 'f':
        print("Fim...")
        break

    if not valida_pos(pos):
        raise ValueError("Posição inválida")

    pos_disp = calcula_pos(pos)

    print(pos_disp)
