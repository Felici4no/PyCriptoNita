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


    # importando a função run (teste)
    from .testing import run
