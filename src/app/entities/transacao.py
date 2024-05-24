from typing import Tuple
from ..enums.item_type_enum import TransacTypeEnum
from ..errors.entity_errors import ParamNotValidated


class Trasancao:
    hora: float
    quantia: float
    tipo: TransacTypeEnum
    saldoNaHora: float

    def __init__(self, hora: float = None, quantia: float = None, tipo: TransacTypeEnum = None, saldoNaHora: float = None):
        validate_quantia = self.validate_quantia(quantia)
        # validate_quantia = [bool, str]
        if validate_quantia[0] is False:
            raise ParamNotValidated("quantia", validate_quantia[1])
        self.quantia = quantia

        validate_tipo = self.validate_tipo(tipo)
        if validate_tipo[0] is False:
            raise ParamNotValidated("tipo", validate_tipo[1])
        self.tipo = tipo

        validate_hora = self.validate_hora(hora)
        if validate_hora[0] is False:
            raise ParamNotValidated("hora", validate_hora[1])
        self.hora = hora

        validate_saldo = self.validate_saldoNaHora(saldoNaHora)
        if validate_saldo[0] is False:
            raise ParamNotValidated("Saldo", validate_saldo[1])
        self.saldoNaHora = saldoNaHora

    @staticmethod
    def validate_hora(hora:float = None) -> Tuple[bool, str]:
        if hora != float:
            return (False, "O horario deve ser do tipo float")
        if hora < 0:
            return (False, "O horario deve ser um valor válido" )

    @staticmethod
    def validate_quantia(quantia: float) -> Tuple[bool, str]:
        if quantia != float:
            return (False, "A quantia deve ser um inteiro")
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



    def to_dict(self):
        return {
            "type": self.tipo,
            "current_balance": self.saldoNaHora,
            "timestamp": self.hora,
            "value": self.quantia
        }

    @staticmethod
    def validate_transac_id(transac_id:int ) -> Tuple[bool, str]:
        if transac_id is None:
            return (False, "O id da transação não pode ser None")
        if type(transac_id) != int:
            return (False, "O id da transação deve ser um inteiro")
        if transac_id < 0:
            return (False, "O id da transação deve ser maior que zero")
        return (True, "")



