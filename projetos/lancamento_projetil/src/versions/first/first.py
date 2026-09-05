import math as m

def alcance_maximo(xo,vo,t,ang):
    vox = vo * m.cos(ang)
    return  xo + vox*t

def altura_maxima(yo,vo,t,g,ang):
    voy = vo * m.sin(ang)
    return yo + voy*t - (g*(t**2))/2


def lancamento_trajetoria(xo,yo,vo,g,ang,t_voo):
    H_max = 0
    while True:
        dt = 0.01
        t_voo += dt
        A = alcance_maximo(xo,vo,t_voo,ang)
        H = altura_maxima(yo,vo,t_voo,g,ang)
        H_max = H if H_max < H else H_max
        A_f = A
        if H <= 0 and t_voo > 0:
            break
            
    print(f"Alcance Máximo: {A_f:.2f} metros")
    print(f"Altura Máxima: {H_max:.2f} metros")
    print(f"Tempo de voo de: {t_voo:.2f} segundos")

def main():
    g = 10  # m/s^2
    xo = 0 # m
    yo = 0 # m
    vo = 10 # m/s
    ang = m.radians(45) # graus
    t_voo = 0
    lancamento_trajetoria(xo,yo,vo,g,ang,t_voo)


if __name__ == "__main__":
    main()
