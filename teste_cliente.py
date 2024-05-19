from tests.app.entities.teste import valida_conta
from tests.app.entities.teste import valida_nome
from tests.app.entities.teste import valida_agencia

#VALIDA_NOME
# Teste 1: Nome válido
resultado = valida_nome("João")
print("Teste 1:", resultado)

# Teste 2: Nome None
resultado = valida_nome(None)
print("Teste 2:", resultado)

# Teste 3: Nome não é uma string
resultado = valida_nome(123)
print("Teste 3:", resultado)

#--------------------------------------------------------
#VALIDA_CONTA
#entrada válida
print(valida_conta("12345-6"))
print(valida_conta("98764-3"))
#teste de conta entrada não válida
print(valida_conta(None))
print(valida_conta((123456)))
print(valida_conta("1234567"))
print(valida_conta(("1234-56")))
#-------------------------------------------------------
#VALIDA_AGENCIA
#entrada válida
print(valida_agencia("1234"))
#entrada não válida
print(valida_agencia(12345))

#-------------------------------------------------------
#VALIDA_SALDO





