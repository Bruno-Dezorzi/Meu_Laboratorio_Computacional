import matplotlib.pyplot as plt


def velocidade(v0,a0,t):
    return v0 + a0*t

def posicao(x0,v0,a0,t):
    return x0 + v0*t + (a0*(t**2))/2

def plotar_posicao_vs_tempo(
        posicoes_iniciais, 
        velocidades_iniciais, 
        aceleracoes_iniciais,
        t):

    for x0, v0, a0, i in zip(
        posicoes_iniciais, 
        velocidades_iniciais, 
        aceleracoes_iniciais,
        range(len(posicoes_iniciais))
        ):

        tempos: list[int]= []
        posicoes: list[float] = []

        for t in range(t + 1):

            tempos.append(t)

            x = posicao(x0,v0,a0,t)

            posicoes.append(x)

        plt.plot(tempos, posicoes, label=f'Posição (m){i+1}')

    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.title('Posição vs Tempo')
    plt.legend()

    plt.tight_layout()
    plt.grid()
    plt.show()


def plotar_velocidade_vs_tempo(
        velocidades_iniciais, 
        aceleracoes_iniciais,
        t):

    for v0, a0, i in zip( 
        velocidades_iniciais, 
        aceleracoes_iniciais,
        range(len(velocidades_iniciais))
        ):

        tempos: list[int]= []
        velocidades: list[float] = []

        for t in range(t + 1):

            tempos.append(t)

            v = velocidade(v0,a0,t)

            velocidades.append(v)

        plt.plot(tempos, velocidades, label=f'Velocidade (m/s){i+1}')
        
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Velocidade vs Tempo')
    plt.legend()

    plt.tight_layout()
    plt.grid()
    plt.show()


def plotar_aceleracao_vs_tempo(
        aceleracoes_iniciais,
        t):

    for a0, i in zip(
        aceleracoes_iniciais,
        range(len(aceleracoes_iniciais))
        ):
        tempos: list[int]= []
        aceleracoes: list[float] = []

        for t in range(t + 1):
            tempos.append(t)
            aceleracoes.append(a0)
        plt.plot(tempos, aceleracoes, label=f'Aceleração (m/s²){i+1}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Aceleração (m/s²)')
    plt.title('Aceleração vs Tempo')
    plt.legend()
    
    plt.tight_layout()
    plt.grid()
    plt.show()
    


def main():

    posicoes_iniciais: list[float] = [0, 5, 10, 15] # m
    velocidades_iniciais: list[float] = [0, 2, 4, 6] # m/s
    aceleracoes_iniciais: list[float] = [1, 2, 3, 4] # m/s²
    t = int(10) # s

    #plotar_posicao_vs_tempo(posicoes_iniciais, velocidades_iniciais, aceleracoes_iniciais,t)
    plotar_velocidade_vs_tempo(velocidades_iniciais, aceleracoes_iniciais,t)
    #plotar_aceleracao_vs_tempo(aceleracoes_iniciais,t)
if __name__ == "__main__":
    main()