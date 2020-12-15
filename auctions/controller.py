import pandas as pd
class AuctionDataController:
    client = None
    auctions = []

    def __init__(self, client):
        self.client = client
        self.auctions = self._set_auctions()

    def _clean_auctions(self, auctions):
        cleaned = auctions['auctions']
        cleaned = list(map(lambda x: {'transaction_id': x['id'], 'item_id': x['item']['id'], **x}, cleaned))
        return pd.DataFrame(cleaned)

    def _set_auctions(self):
        return self._clean_auctions(self.client.get_auctions())
        

