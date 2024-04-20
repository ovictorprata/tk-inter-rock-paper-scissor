def conferir_resultado(jogador, pc, label):
    color = 'black'
    if jogador == pc:
        resultado = 'EMPATE'
    elif (jogador == 'pedra' and pc == 'tesoura') or (jogador == 'papel' and pc == 'pedra') or (jogador == 'tesoura' and pc == 'papel'):
        resultado = 'VOCÊ GANHOU!'
        color = 'green'
    else:
        resultado = 'O PC GANHOU!'
        color = 'red'
        
    label.config(text=resultado, fg=color)