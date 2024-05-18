from typing import Tuple
from ..enums.item_type_enum import TransacTypeEnum
from ..errors.entity_errors import ParamNotValidated


class Trasancao:
    hora: float
    quantia: float
    tipo: TransacTypeEnum
    saldoNaHora: float

    def __init__(self, hora: float = None, quantia: float = None, tipo: TransacTypeEnum = None, saldoNaHora: float = None):
        validate_quantia = self.validate_quantia(quantia, saldoNaHora)
        # validate_quantia = [bool, str]
        if validate_quantia[0] is False:
            raise ParamNotValidated("quantia", validate_quantia[1])
        self.quantia = quantia

        validate_tipo = self.validate_tipo(tipo)
        if validate_tipo[0] is False:
            raise ParamNotValidated("tipo", validate_tipo[1])
        self.tipo = tipo

    @staticmethod
    def validate_hora(hora:float = None) -> Tuple[bool, str]:
        if hora != float:
            return (False, "O horario deve ser do tipo float")
        if hora < 0:
            return (False, "O horario deve ser um valor válido" )

    @staticmethod
    def validate_quantia(quantia: float, saldoNaHora: float) -> Tuple[bool, str]:
        if quantia != float:
            return (False, "A quantia deve ser um inteiro")
        if quantia > saldoNaHora * 2:
            return (False, "Deposito suspeito")
        if quantia < 1:
            return (False, "Quantia deve ser maior do que 1")
        return (True, "")

    @staticmethod
    def validate_tipo(tipo: TransacTypeEnum) -> Tuple[bool, str]:
        if tipo is None:
            return (False, "tipo de transação deve ser especificado")
        if type(tipo) != TransacTypeEnum:
            return (False, "O tipo deve existir em TransacTypeEnum")
        return (True, "")

    @staticmethod
    def validate_saldoNaHora(saldoNaHora: float = None ) -> Tuple[bool, str]:
        if saldoNaHora != float:
            return (False, "O saldo é deve ser do tipo float")
        if saldoNaHora < 0:
            return (False, "O saldo não pode ser negativo")


    @staticmethod
    def to_dict(self):
        return {
            "type": self.tipo,
            "current_balance": self.saldoNaHora,
            "timestamp": self.hora,
            "value": self.quantia
        }


