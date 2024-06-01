import time
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .entities.transacao import Transacao
from .environments import Environments
from datetime import datetime
from .repo.item_repository_mock import ItemRepositoryMock
from .errors.entity_errors import ParamNotValidated
from .enums.item_type_enum import TransacTypeEnum
from .entities.cliente import Cliente

app = FastAPI()

repo = Environments.get_client_repo()()
repot = Environments.get_transac_repo()()

clienteTeste = repo.get_client(1)

@app.get("/clients/get_all_clients")
def get_all_clients():
    clients = repo.get_all_clients()
    return {
        "clients": [client.to_dict() for client in clients]
    }


@app.get("/")
def get_client(client_id: int):
    validation_cliente_id = Cliente.valida_cliente_id(client_id=client_id)
    if not validation_cliente_id[0]:
        raise HTTPException(status_code=400, detail=validation_cliente_id[1])

    cliente = repo.get_client(client_id)

    if cliente is None:
        raise HTTPException(status_code=404, detail="Client Not Found")

    return {
        "client_id": client_id,
        "client": cliente.to_dict()
    }



@app.post("/deposit", status_code=201)
def create_deposit(request: dict):

    model = {
        "2": 0,
        "5": 0,
        "10": 0,
        "20": 0,
        "50": 0,
        "100": 0,
        "200": 0
    }

    quantia = 0.0

    for chave in request:
        if model.get(chave, None) is not None:
            quantia += float(chave) * float(request[chave])

    if quantia > clienteTeste.saldo_atual*2:
        raise HTTPException(status_code=403, detail="Saldo suspeito")

    clienteTeste.saldo_atual += quantia

    transacao = Transacao(saldoNaHora=clienteTeste.saldo_atual, hora=time.time(), quantia=quantia, tipo=TransacTypeEnum.DEPOSIT)

    repot.cria_transacao(transac=transacao, transac_id=int((transacao.saldoNaHora * transacao.quantia) / 1000))

    return {
        "hora":time.time(),
        "saldoNaHora": clienteTeste.saldo_atual
    }



@app.post("/withdraw", status_code=201)
def create_withdraw(request: dict):

    model = {
        "2": 0,
        "5": 0,
        "10": 0,
        "20": 0,
        "50": 0,
        "100": 0,
        "200": 0
    }

    quantia = 0.0

    for chave in request:
        if model.get(chave, None) is not None:
            quantia += float(chave) * float(request[chave])

    if quantia > clienteTeste.saldo_atual:
        raise HTTPException(status_code=403, detail="Saldo insuficiente")

    clienteTeste.saldo_atual -= quantia

    transacao = Transacao(saldoNaHora=clienteTeste.saldo_atual, hora=time.time(), quantia=quantia, tipo=TransacTypeEnum.DEPOSIT)

    repot.cria_transacao(transac=transacao, transac_id=int((transacao.saldoNaHora * transacao.quantia) / 1000))

    return {
        "hora": time.time(),
        "saldoNaHora": clienteTeste.saldo_atual
    }

@app.get ("/history", status_code=201)
def get_history():
    transacoes = repot.get_all_transactions()
    return {
        "all_transactions": [transacao.to_dict() for transacao in transacoes]
    }



# @app.post("/items/create_item", status_code=201)
# def create_item(request: dict):
#     item_id = request.get("item_id")
#
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
#
#     item = repo.get_item(item_id)
#     if item is not None:
#         raise HTTPException(status_code=409, detail="Item already exists")
#
#     name = request.get("name")
#     price = request.get("price")
#     item_type = request.get("item_type")
#     if item_type is None:
#         raise HTTPException(status_code=400, detail="Item type is required")
#     if type(item_type) != str:
#         raise HTTPException(status_code=400, detail="Item type must be a string")
#     if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
#         raise HTTPException(status_code=400, detail="Item type is not a valid one")
#
#     admin_permission = request.get("admin_permission")
#
#     try:
#         item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
#     except ParamNotValidated as err:
#         raise HTTPException(status_code=400, detail=err.message)
#
#     item_response = repo.create_item(item, item_id)
#     return {
#         "item_id": item_id,
#         "item": item_response.to_dict()
#     }
#
# @app.delete("/items/delete_item")
# def delete_item(request: dict):
#     item_id = request.get("item_id")
#
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
#
#     item = repo.get_item(item_id)
#
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
#
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
#
#     item_deleted = repo.delete_item(item_id)
#
#     return {
#         "item_id": item_id,
#         "item": item_deleted.to_dict()
#     }
#
# @app.put("/items/update_item")
# def update_item(request: dict):
#     item_id = request.get("item_id")
#
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
#
#     item = repo.get_item(item_id)
#
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
#
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
#
#     name = request.get("name")
#     price = request.get("price")
#     admin_permission = request.get("admin_permission")
#
#     item_type_value = request.get("item_type")
#     if item_type_value != None:
#         if type(item_type_value) != str:
#             raise HTTPException(status_code=400, detail="Item type must be a string")
#         if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
#             raise HTTPException(status_code=400, detail="Item type is not a valid one")
#         item_type = ItemTypeEnum[item_type_value]
#     else:
#         item_type = None
#
#     item_updated = repo.update_item(item_id, name, price, item_type, admin_permission)
#
#     return {
#         "item_id": item_id,
#         "item": item_updated.to_dict()
#     }
#
#
#
# handler = Mangum(app, lifespan="off")
