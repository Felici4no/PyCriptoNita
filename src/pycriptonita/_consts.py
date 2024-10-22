# arquivo responsável por armazenar as constantes referentes ao
# projeto

# banner(title screen) do projeto
PROGRAM_BANNER: list[str] = [
    '############################################################',
    '#                                                          #',
    '#                  Welcome to PyCriptoNita                 #',
    '#                                                          #',
    '#              Secure your text with ease and style!       #',
    '#                                                          #',
    '############################################################']

# opções do menu organizadas em dicionário (índice: texto)
PROGRAM_MENU_OPTIONS: dict[str: str] = {
    '1' : 'Encrypt'     ,
    '2' : 'Decrypt'     ,
    '3' : 'Last key'    ,
    '4' : 'Generate key',
    '5' : 'About'       ,
    '6' : 'Quit'
}
