from typing import Tuple
from ..enums.item_type_enum import TransacTypeEnum
from ..errors.entity_errors import ParamNotValidated


class Trasancao:
    hora: str
    quantia: int
    tipo: TransacTypeEnum
    saldoNaHora: int

    def __init__(self, hora: str=None, quantia: int=None, tipo: TransacTypeEnum=None, saldoNaHora: int=None):
        validate_quantia = self.validate_quantia(quantia, saldoNaHora)
        if validate_quantia[0] is False:
            raise ParamNotValidated("quantia", validate_quantia[1])
        self.quantia = quantia


    @staticmethod
    def validate_quantia(quantia: int, saldoNaHora: int) -> Tuple[bool, str]:
        if quantia > saldoNaHora*2:
            return (False, "Saldo Suspeito")
        if quantia < 0:
            return (False, "Quantia negativa não existe")
        return (True, "")