def clear_terminal() -> None:
    """Limpa todo o conteúdo que foi printado no terminal.
    Não retorna nada
    """

    print('\033[H\033[2J', end = '')

def get_escape(body_font       : int = 0,
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

    Funcionamento: 
        A função irá iniciar uma lista com apenas um elemento
        (\033[0m). Após isso, os argumentos passados na função serão
        colocados em variáveis de nome mais curto.

        Serão iniciadas também outras quatro listas:
            1. lista de valores esperados para body_font
            2. lista de valores esperados para foreground_color
            3. lista de valores esperados para background_color
            4. list contendo um valor adicional para cada uma das
               listas geradas acima

        Agora, será feito um loop for a partir da função zip com
        todos os elementos criados até agora.

        Se o argumento inserido for diferente de 0 (fora do padrão),
        então adicione uma string a lista final de resultados por
        meio de operação ternária:
            se o valor inserido estiver na lista de valores
            esperados, insere, se não, coloque o valor substituto
            determinado na lista 'case_not_in'.

        Quando o loop encerrar, a função retorna uma string que junta
        todos os elementos da string de resultados
    """

    result: list[str] = ['\033[0m']

    bf, fc, bc = body_font, foreground_color, background_color

    expected_bf: list[int] = [1, 2, 3, 4, 7]
    expected_fc: list[int] = list(range(30, 38))
    expected_bc: list[int] = list(range(40, 48))
    case_not_in: list[int] = [4, 33, 41]


    for val, exp, dfl in zip([bf, fc, bc],
                             [expected_bf, expected_fc, expected_bc],
                             case_not_in):
        
        if val != 0:
            result.append(f'\033[{val if val in exp else dfl}m')

    return ''.join(result)

