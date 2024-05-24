from typing import Dict, Optional

from src.app.repo.transac_repositorio_interface import TransacRepository
from ..entities .transacao import Trasancao


class TransacRepositoriMock(TransacRepository):
    transacoes:Dict[int,Transacao]

    def __init__(self):
        self.transacoes = {}

    def create_deposit(self, transac:Transacao, transac_id:int) -> Transacao:
        self.transacoes[transac_id] = transac
        return transac


    def get_transac(self,transac_id:int) -> Optional[Trasancao]:
        return self.transacoes.get(transac_id, None)

