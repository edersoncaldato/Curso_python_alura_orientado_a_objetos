from Restaurante import Restaurante

restaurante_praca = Restaurante('Praça do Zé', 'Bar', True)
restaurante_praca.alterar_status()
restaurante_praca.receber_avaliacao('Claúdio', 3)
restaurante_praca.receber_avaliacao('Pedro', 4)
restaurante_praca.receber_avaliacao('Pedro', 3)
restaurante_pizza = Restaurante('Pizzaria do Tião', 'Pizzaria',True)
restaurante_pizza = Restaurante('Salgados Novidade', 'Salgados',True)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()