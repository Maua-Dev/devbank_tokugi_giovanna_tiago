from abc import ABC, abstractmethod
from ..entities.transacao import Transacao


class TransacRepository(ABC):
    @abstractmethod
    def create_deposit(self, transac:Transacao, transac_id:int) -> Transacao:
        '''
        create new deposit transact in the database
        '''
        pass
