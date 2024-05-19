from abc import ABC, abstractmethod
from typing import List

from ..enums.item_type_enum import TransacTypeEnum

from ..entities.cliente import Cliente


class IItemRepository(ABC):


    @abstractmethod
    def get_all_clients(self) -> List[Cliente]:
        '''
        Returns all the clients in the database
        '''
        pass

    # @abstractmethod
    # def get_item(self, item_id: int) -> Optional[Item]:
    #     '''
    #     Returns the item with the given id.
    #     If the item does not exist, returns None
    #     '''
    #     pass

    # @abstractmethod
    # def create_item(self, item: Item, item_id: int) -> Item:
    #     '''
    #     Creates a new item in the database
    #     '''
    #     pass
    #
    # @abstractmethod
    # def delete_item(self, item_id: int) -> Item:
    #     '''
    #     Deletes the item with the given id.
    #     If the item does not exist, returns None
    #     '''
    #
    # @abstractmethod
    # def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
    #     '''
    #     Updates the item with the given id.
    #     If the item does not exist, returns None
    #     '''
    #     pass
    #
