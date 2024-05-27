import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.transacao import Trasancao
from src.app.enums.item_type_enum import TransacTypeEnum

class Teste_Transac:
    def teste_transacoes(self):
        transacao = Trasancao(18, 24556, TransacTypeEnum.DEPOSIT, 500 )
        assert transacao.hora == 18
        assert transacao.quantia == 24556
        assert transacao.tipo == TransacTypeEnum.DEPOSIT
        assert transacao.saldoNaHora == 500

    def teste_transacoes_horaNone(self):
        with pytest.raises(ParamNotValidated):
            Trasancao( quantia=24556, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=500)

    def teste_transacoes_quantiaNone(self):
        with pytest.raises(ParamNotValidated):
            Trasancao( hora=18, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=500)


    def teste_transacoes_tipoNone(self):
        with pytest.raises(ParamNotValidated):
            Trasancao( hora=18, quantia=24556, saldoNaHora=500)

    def teste_transacoes_saldoNaHoraNone(self):
        with pytest.raises(ParamNotValidated):
            Trasancao( hora=18, quantia=24556, tipo=TransacTypeEnum.DEPOSIT)

    def teste_transacoes_hora_diferente_float(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora="ola", quantia=24556, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=500)

    def teste_transacoes_quantia_diferente_float(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora=18, quantia="boia", tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=500)

    def teste_transacoes_tipo_diferente_enum(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora=18, quantia=24556, tipo="baralho", saldoNaHora=500)

    def teste_transacoes_saldoNaHora_diferente_float(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora=18, quantia=24556, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora="bola")

    def teste_transacoes_hora_negativa(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora=-18, quantia=24556, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=500)

    def teste_transacoes_quantia_negativa(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora=18, quantia=-24556, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=500)

    def teste_transacoes_saldoNaHora_negativa(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora=18, quantia=24556, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=-500)

    def teste_transacoes_quantia_zerada(self):
        with pytest.raises(ParamNotValidated):
            Trasancao(hora=18, quantia=0, tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=500)


