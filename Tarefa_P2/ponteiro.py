def valida_horario(tempo:str) -> bool:
    """
    Faz as verificações necessárias no  horário passado para o programa

    Entrada: 
        - tempo:str  horário passado para o script
    
    Saída:
        - True ou False:bool
    """

    if ":" not in tempo:
        return False

    tempo = tempo.split(":")

    if len(tempo) != 2:
        return False
    
    if (len(tempo[0]) != 2) or (len(tempo[1]) != 2):
        return False
    
    try:
        hora = int(tempo[0])
        minuto = int(tempo[1])
    except:
        return False
    
    if (0 <= hora <= 12) and (0 <= minuto <= 60):
        return True
    
    return False


def calcula_angulo(hora:int, minuto:int) -> float:
    """
    Calcula o menor ângulo entre os ponteiros

    Entrada:
        - hora:int  ponteiro das horas
        - minuto:int   ponteiro dos minutos
    
    Saída:
        - angulo:float   menor ângulo entre os ponteiros
    """

    angulo_hora = (hora % 12) * 30
    angulo_minuto = minuto * 6

    angulo = abs(angulo_minuto - angulo_hora)
    angulo = min(angulo, 360 - angulo)

    return angulo


while True:
    tempo = input("")

    if tempo == "f":
        print("Fim...")
        break
    
    if not valida_horario(tempo):
        print("Input inválido")
        continue

    tempo = tempo.split(":")
    hora = int(tempo[0])
    minuto = int(tempo[1])

    angulo = calcula_angulo(hora, minuto)

    print(f"O menor ângulo é de {angulo}º")



        
