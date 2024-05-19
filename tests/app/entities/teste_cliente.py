import pytest
from src.app.entities.cliente import Cliente
from src.app.errors.entity_errors import ParamNotValidated
class Teste_cliente:
    def teste_cliente(self):
        cliente = Cliente("Tiago", "12345-6", 1000.0, "1234")
        assert cliente.name == "Tiago"
        assert cliente.agencia == "1234"
        assert cliente.saldo_atual == 1000.0
        assert cliente.conta == "12345-6"

#teste nome
    def test_cliente_nome_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(conta= "12345-7", agencia= "1234", saldo_atual=200.50 )

    def test_cliente_nome_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name= 12, conta="12345-7", agencia="1234", saldo_atual=222.20)

#teste conta
    def teste_cliente_conta_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Albuquerque", conta=12345 - 6, aguencia="1234", saldo_atual= 123.40)

    def teste_cliente_conta_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Giovanna", agencia="1234", saldo_atual= 2000.00)

    def teste_cliente_conta_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Karoline", conta="1234-5", agencia="1234", saldo_atual= 300.00)

    def teste_cliente_conta_have_not_character(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Tiago", conta="123457", agencia="1234", saldo_atual= 40.50)

#teste agencia

    def test_cliente_agencia_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Oliveira", conta="12345-7", agencia= 1234, saldo_atual= 2000.00)

    def test_cliente_agencia_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Giovanna Karoline", conta="12345-7", saldo_atual=1234.56)

    def test_cliente_agencia_is_too_long(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Oliveira", conta="12345-7", agencia="12345", saldo_atual= 1234.50)

#teste saldo_atual

    def test_cliente_saldo_atual_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Massuda", conta="12345-7", agencia="12345", saldo_atual="1234.50")

    def test_cliente_saldo_atual_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name="Giovanna Albuquerque", agencia="12345")








