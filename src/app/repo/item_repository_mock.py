from typing import Dict, Optional, List

from ..enums.item_type_enum import TransacTypeEnum
from ..entities.cliente import Cliente
from .item_repository_interface import IItemRepository


class ItemRepositoryMock(IItemRepository):
    clientes: Dict[int, Cliente]
    
    def __init__(self):
        self.clientes = {
            1: Cliente(nome="Tiago Tokugi", agencia="9999", conta="99999-9", saldo_atual=1000.0)
        }
        
    def get_all_clients(self) -> List[Cliente]:
        return self.clientes.values()
    
    # def get_item(self, item_id: int) -> Optional[Item]:
    #     return self.items.get(item_id, None)
    #
    # def create_item(self, item: Item, item_id: int) -> Item:
    #
    #     self.items[item_id] = item
    #     return item
    #
    # def delete_item(self, item_id: int) -> Item:
    #     item = self.items.pop(item_id, None)
    #     return item
    #
    #
    # def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
    #     item = self.items.get(item_id, None)
    #     if item is None:
    #         return None
    #
    #     if name is not None:
    #         item.name = name
    #     if price is not None:
    #         item.price = price
    #     if item_type is not None:
    #         item.item_type = item_type
    #     if admin_permission is not None:
    #         item.admin_permission = admin_permission
    #     self.items[item_id] = item
    #
    #     return item
    #
    #
    #