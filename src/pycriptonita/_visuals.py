# arquivo responsável por armazenar as funcionalidades visuais do
# programa
def clear_terminal() -> None:
    """Função que limpa o terminal printando uma escape"""
    print('\033[H\033[2J', end='')
#

def get_ansi_escape(body_font       : int = 0,
                    foreground_color: int = 0,
                    background_color: int = 0) -> str:
    r"""Retorna uma ANSI escape em forma de String recebendo apenas
    três argumentos.

    Parâmetros:
        body_font: valor que determina a fonte, inicialmente
                   como 0

        foreground_color: valor que determina a cor da fonte,
                          inicialmente como 0

        background_color: valor que determina a cor do fundo da
                          fonte, inicialmente como 0
        """

    # inicia lista de resultado com apenas um elemento
    result: list[str] = ['\033[0m']

    # renomeando (mair curto)
    bf, fc, bc = body_font, foreground_color, background_color

    # construindo listas de valores esperados
    expected_bf: list[int] = [1, 2, 3, 4, 7]
    expected_fc: list[int] = list(range(30, 38))
    expected_bc: list[int] = list(range(40, 48))
    case_not_in: list[int] = [4, 33, 41] # já essa, serve só para
                                         # valores substitutos

    # zipando três elementos diferentes no loop:
    #   argumento inserido - lista de arg. esperado - valor reserva
    for val, exp, dfl in zip(
        [bf, fc, bc], [expected_bf, expected_fc, expected_bc], case_not_in
        ):

        # se o argumento inserido for diferente do 'default'(0)
        if val != 0:
            # adiciona na lista final a string formatada por meio
            # de ternário
            result.append(f'\033[{val if val in exp else dfl}m')

    # retorna lista unificada em string
    return ''.join(result)
#

def get_foreground_hex_escape(body_font: int        = 0   ,
                              hex_value: str | None = None) -> str:
    """Função que retorna uma string escape a partir de uma cor
    inserida em formato hexadecimal

    Parâmetros:
        body_font: valor que determina a fonte, inicialmente
                   como 0

        hex_value: cor em hexadecimal
    """

    # inicia lista final com escape de reset
    result: list[str] = ['\033[0m']

    # adiciona um elemento na lista por meio de ternário
    result.append(
        # string com escape do body_font (caso no escopo, caso
        # contrário, 4)
        f'\033[{body_font if body_font in [0, 1, 2, 3, 7] else 4}m'
    )

    # se o valor hexadecimal for nulo
    if hex_value is None:
        # encerre a função retornando
        return ''.join(result)

    # se o valor hexadecimal não é string
    if not isinstance(hex_value, str):
        # encerre a função retornando
        return ''.join(result)

    # se a cor tiver 7 chars e começar com '#', remover prefixo
    if len(hex_value) == 7 and hex_value.startswith('#'):
        # encerre a função retornando
        hex_value = hex_value[1 : ]

    # se o tamnho atual da cor for diferente de 6
    if len(hex_value) != 6:
        # encerre a função retornando
        return ''.join(result)

    # obtendo o rgb separadamente por meio de string slice e list
    # comprehension
    rh, gh, bh = (hex_value[i : i + 2] for i in range(0, 6, 2))

    # lista de valores rgb como int
    final_rgb: list[int] = list()

    # para cada valor em rgb como string
    for val in [rh, gh, bh]:
        # adicione-os na list rgb como int
        final_rgb.append(int(val, base = 16))

    # se qualquer um dos rgbs estiver fora dos limites
    if any((x < 0 or x > 255 for x in final_rgb)):
        # encerre a função retornando
        return ''.join(result)

    # adicionar a lista de resultados a string formatada com o rgb
    result.append(
        '\033[38;2;{};{};{}m'.format(*final_rgb)
    )

    # retorna a lista em forma de string
    return ''.join(result)
#

def print_banner(banner     : list[str] | None = None,
                 ident_val  : int              = 0   ,
                 escape_list: list[str] | None = None) -> None:
    """Função que printa o banner do projeto e não retorna nada.

    Parâmetros:
        banner: lista de strings contendo a arte do projeto

        ident_val: valor no qual será feita a identação

        escape_list: lista com os escapes necessário para a arte,
                     onde:
                        1. elemento  -> cor da fonte principal
                        n. elementos -> cor de todo o resto

                     Para a esse último argumento funcionar, é
                     necessário que ele tenha 4 elementos dentro de
                     si
    """

    # se o banner ou o valor de identação forem inválidos
    if banner is None or ident_val < 0:
        return

    import random as rd

    # iniciando uma nova lista para o banner
    neo_banner: list[str] = list()

    # novo 'escapes' ternário como lista vazia (caso os argumentos de
    # escape sejam nulos) ou uma cópia dos próprios argumentos
    escapes = list() if escape_list is None else escape_list.copy()

    # se o tamanho da lista de escapes for diferente de 4
    if len(escapes) != 4:
        # limpe a lista (caso haja pelo menos 1 elemento)
        escapes.clear()
        # coloque 4 elementos vazios nela
        for _ in range(4):
            escapes.append('')
    #

    # para cada linha do banner original
    for row in banner:

        # criar uma nova linha para ser adicionada no novo banner
        curren_row: list[str] = list()

        # para cada char da linha atual
        for char in row:
            # se o char for um espaço
            if char  == ' ':
                # adicione qualquer escape com exceção do primeiro
                curren_row.append(rd.choice(escapes[1:]))
                # adicione um elemento aleatório dos listados a seguir
                curren_row.append(rd.choice(['0', '1', ' ', ' ', ' ']))
                # NOTE: importante lembrar que quanto mais elementos
                #       repetidos tiverem, mais provável é de ele ser
                #       escolhido

            # mas se o char não for um espaço
            else:
                # adicione o primeiro escape
                curren_row.append(escapes[0])
                # adicione o char
                curren_row.append(char)
        #

        # adicione a linha finalizada ao novo banner
        neo_banner.append(''.join(curren_row))

    # para cada linha no novo banner
    for l in neo_banner:
        # printa a quantidade de espaços para identação
        print(' ' * ident_val, end = '')
        # printa a própria linha
        print(l)

    # reseta as escapes do terminal + new line
    print('\033[0m')
#

def print_menu_options(options_pair   : dict[str : str],
                       index_escape   : str            ,
                       option_escape  : str            ) -> int:
    """Funçao que exibe no terminal as opções recebendo 4 argumentos:

    Parâmetros:
        options_pair: conteúdo das opções, um dicionário constituído
                      de { str : str }

        index_escape: escape usada para estilizar o índice (markador)
                      da opção

        option_escape: escape usada para estilizar o texto da opção
    """
    
    # para cada chave : valor no dicionário
    for k, v in options_pair.items():
        # printar o conteúdo formatado
        print(f'{index_escape}[{k}] {option_escape}{v}\033[0m')

    # new line
    print()
#
