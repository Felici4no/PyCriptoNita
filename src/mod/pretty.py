def clearTerminal() -> None:

    print('\033[H\033[2J', end = '')

def getEscape(body_font       : int = 0,
              foreground_color: int = 0,
              background_color: int = 0) -> str:

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

