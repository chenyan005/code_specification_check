# Convenção PEP-8 ~~~ Classes devem usar o "CapModel", cada palavra, começa
# com letra maiuscula

# Funções e variaveis devem usar somente letras minusculas e "_" espaços snake

# Constantes devem ser palavras maiusculas separadas por "_"
from typing import Union

from fila_base import FilaBase
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada
from constantes import CODIGO_PRIORITARIO

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self):
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'
    # Padrão Pep-8 ~~Uma linha de espaçamento entre métodos e funções

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente Atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, retorna_estatistica: Classes) -> dict:
        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
