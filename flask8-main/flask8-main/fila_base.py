# Criando classe abstrata
import abc
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    # type hint
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    # type hint
    senha_atual: str = ""

    # type hint, não retorna nada
    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    # Métodos abstratos forçam as classes filhas a criarem esses métodos
    @abc.abstractmethod
    def gera_senha_atual(self):
        pass

    # type hint, não retorna nada
    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        pass
