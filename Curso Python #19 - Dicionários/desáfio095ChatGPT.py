def cadastrar_jogador():
    jogador = dict()
    jogador['Nome'] = input("Nome do Jogador: ")
    tot = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    
    partidas = [int(input(f"Quantos gols na partida {c + 1}? ")) for c in range(tot)]
    
    jogador['gols'] = partidas
    jogador['total'] = sum(partidas)
    
    return jogador


def mostrar_tabela(time):
    print('-=' * 40)
    print("cod", end='')
    for chave in time[0].keys():
        print(f"{chave:<15}", end='')
    print()
    print('-=' * 40)
    for k, v in enumerate(time):
        print(f"{k:>3} ", end='')
        for valor in v.values():
            print(f"{str(valor):<15}", end="")
        print()
    print('-=' * 40)


def mostrar_levantamento(time):
    while True:
        busca = int(input("Mostrar dados de qual jogador? (999 para sair) "))
        
        if busca == 999:
            break
        
        if 0 <= busca < len(time):
            jogador = time[busca]
            print(f" -- LEVANTAMENTO DO JOGADOR: {jogador['Nome']}")
            
            for i, g in enumerate(jogador['gols'], start=1):
                print(f" No jogo {i} fez {g} gol(s)!")
            
        else:
            print(f"ERRO! Não existe jogador com o código {busca}!")
        
        print('-=' * 40)


def main():
    time = list()

    while True:
        jogador = cadastrar_jogador()
        time.append(jogador.copy())
        
        resp = input("Você quer continuar? [S/N]").upper()
        
        if resp != "S":
            break

    mostrar_tabela(time)
    mostrar_levantamento(time)

    print("Volte sempre!")


if __name__ == "__main__":
    main()
