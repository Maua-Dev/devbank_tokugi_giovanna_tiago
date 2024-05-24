import time

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .entities.transacao import Trasancao
from .environments import Environments
from datetime import datetime



from .repo.item_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import TransacTypeEnum

from .entities.cliente import Cliente

app = FastAPI()

repo = Environments.get_client_repo()()
repot = Environments.get_transac_repo()()


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
    transac_id = request.get("transac_id")

    validate_transac_id = Trasancao.validate_transac_id(transac_id=transac_id)
    if not validate_transac_id[0]:
        raise HTTPException(status_code=400, detail=validate_transac_id[1])

    transac = repot.get_transac(transac_id)
    if transac is not None:
        raise HTTPException (status_code=409, detail=" Transação já existe")

    n2= request.get("2"),
    n5= request.get("5"),
    n10= request.get("10"),
    n20= request.get("20"),
    n50= request.get("50"),
    n100= request.get("100"),
    n200= request.get("200")
    try:
        transac = Trasancao(quantia=n2*2 + n5*5 + n10*10 + n20*20 + n100*100 + n200*200,
                            tipo=TransacTypeEnum.DEPOSIT, saldoNaHora=1000.0,
                            hora=datetime.fromtimestamp(time.time()))
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail= err.message)
    deposit_response = repot.create_deposit(transac,transac_id)
    return {
        "transac_id":transac_id,
        "transac":deposit_response.to_dict()
    }

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
#
#     item = repo.get_item(item_id)
#
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
#
#     return {
#         "item_id": item_id,
#         "item": item.to_dict()
#     }
#
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
