from typing import Tuple
from ..enums.item_type_enum import TransacTypeEnum
from ..errors.entity_errors import ParamNotValidated


class Trasancao:
    hora: float
    quantia: float
    tipo: TransacTypeEnum
    saldoNaHora: float

    def __init__(self, hora: str = None, quantia: int = None, tipo: TransacTypeEnum = None, saldoNaHora: int = None):
        validate_quantia = self.validate_quantia(quantia, saldoNaHora)
        if validate_quantia[0] is False:
            raise ParamNotValidated("quantia", validate_quantia[1])
        self.quantia = quantia

        validate_tipo = self.validate_tipo(tipo)
        if validate_tipo[0] is False:
            raise ParamNotValidated("tipo", validate_tipo[1])
        self.tipo = tipo

    @staticmethod
    def validate_quantia(quantia: int, saldoNaHora: int) -> Tuple[bool, str]:
        if quantia != int:
            return (False, "A quantia deve ser um inteiro")
        if quantia > saldoNaHora * 2:
            return (False, "Saldo suspeito")
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

    def to_dict(self):
        return {
            "type": self.tipo,
            "current_balance": self.saldoNaHora,
            "timestamp": self.hora,
            "value": self.quantia
        }
