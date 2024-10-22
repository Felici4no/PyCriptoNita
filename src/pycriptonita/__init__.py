"""# pycriptonita

Pasta/pacote responsável por armazena a classe principal e suas
operações.

O pacote por natureza não é capaz de fazer nada de muito importante
pois as funcionalidades estão armazenadas na classes estática
`PyCriptoNita`.

Para usar o program, tente:

>>> from pycriptonita import PyCriptoNita
>>> PyCriptoNita.alguma_func()
"""

# criando a classe no arquivo __init__ para ser chamada de maneira
# estática posteriormente
class PyCriptoNita:
    """Classe principal do programa. Essa mesma não tem praticamente
    nenhuma funcionalidade independente. Na verdade, tudo que ela faz
    é determinar variáveis, constantes e funções como globais para
    depois importá-las e utilizar dentro de suas operações locais
    de forma que simule métodos estáticos.

    Dentro da lista de funções, temos:

    - func 1: explicação
    - func 2: explicação
    - func n: ...
    """

    # definindo as variáveis/constantes globais ---------------------

    # const/vars pertencentes à classe PyCriptoNita (inic. posteri.)
    global BANNER_HEX_COLORS

    # constantes/vars importadas de _consts.py
    global PROGRAM_BANNER, PROGRAM_MENU_OPTIONS, ESC_RST

    # funções importadas de _visuals
    global clear_terminal, get_foreground_hex_escape
    global print_banner, print_menu_options, get_ansi_escape

    # import sendo realizado de fato
    from ._consts import (  # do arquivo _consts
        PROGRAM_BANNER      ,
        PROGRAM_MENU_OPTIONS
    )

    from ._visuals import (      # do arquivo _visuals
        clear_terminal           ,
        get_foreground_hex_escape,
        print_banner             ,
        print_menu_options       ,
        get_ansi_escape
    )

    # consts/vars globais pertencentes à esta classe
    BANNER_HEX_COLORS = [
        get_foreground_hex_escape(1, '#C9EDD2'),
        get_foreground_hex_escape(2, '#429D39'),
        get_foreground_hex_escape(2, '#14690C'),
        get_foreground_hex_escape(2, '#024518')
    ]

    # função principal do program (como já indica o nome)
    def run(previous_text: tuple[str, str] | None = None) -> None:

        # limpar terminal
        clear_terminal()

        # printar mensagem anterior caso seja diferetente de None
        if previous_text is None:
            print()
        else:
            print('{}{}\033[0m'.format(*previous_text))
        #

        # printar banner
        print_banner(PROGRAM_BANNER, 4, BANNER_HEX_COLORS)

        # printar as opções
        print_menu_options(PROGRAM_MENU_OPTIONS  ,
                           get_ansi_escape(1, 33),
                           get_ansi_escape(3)    )

        # obter resposta do usuário
        t = input('\n>>> ')

        # se a resposta não for 'sair'
        if t != 'exit':
            # chame a mesma função mas com o texto de alerta
            PyCriptoNita.run((get_foreground_hex_escape(1, '#D84564'),
                              'Type "exit" to stop the program...'  ))
        #
    #
