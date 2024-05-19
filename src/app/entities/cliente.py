from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class Cliente:
    name: str
    conta: str
    saldo_atual: float
    agencia: str

    def __init__(self, name: str = None, conta: str = None, saldo_atual: float = None, agencia: str = None):

        valida_nome = self.valida_nome(name)
        if valida_nome[0] is False:
            raise ParamNotValidated("nome", valida_nome[1])
        self.name = name

        valida_conta = self.valida_conta(conta)
        if valida_conta[0] is False:
            raise ParamNotValidated("conta", valida_conta[1])
        self.conta = conta

        valida_saldo = self.valida_saldo(saldo_atual)
        if valida_saldo[0] is False:
            raise ParamNotValidated("saldo atual", valida_saldo[1])
        self.saldo_atual = saldo_atual

        valida_agencia = self.valida_agencia(agencia)
        if valida_agencia[0] is False:
            raise ParamNotValidated("agencia", valida_agencia[1])
        self.agencia = agencia

    @staticmethod
    def valida_nome(nome: str) -> Tuple[bool, str]:
        if nome is None:
            return (False, "O nome é necessário")
        if type(nome) != str:
            return (False, "O nome precisa ser uma string")
        return (True, "")

    @staticmethod
    def valida_conta(conta: str) -> Tuple[bool, str]:
        if conta is None:
            return (False, "A conta é obrigatória")
        if type(conta) != str:
            return (False, "A conta deve ser uma string")
        if len(conta) != 7 or conta[5] != '-':
            return(False, "A conta deve ser do tipo XXXXX-X")

        return (True, "")

    @staticmethod
    def valida_saldo(saldo_atual: float) -> Tuple[bool, str]:
        if saldo_atual is None:
            return (False, "Deve existir um valor")
        if type(saldo_atual) != float:
            return (False, "O saldo deve ser do tipo float")
        return (True, " ")

    @staticmethod
    def valida_agencia(agencia: str) -> Tuple[bool, str]:
        if agencia is None:
            return (False, "A agência é necessária")
        if type(agencia) != str:
            return (False, "A agência deve ser do tipo int")
        if len(agencia) != 4 :
            return(False, "A agência deve ser formada por 4 dígitos")
        return (True, " ")

    @staticmethod
    def to_dict(self):
        return {
            "name": self.name,
            "current_balance": self.saldo_atual,
            "account": self.conta,
            "agency": self.agencia
        }


