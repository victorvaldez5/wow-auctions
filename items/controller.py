class ItemDataTable:
    auctioneer = None

    def __init__(self, auctioneer) -> None:
        self.auctioneer = auctioneer
        super().__init__()
    
    def _create_item_table(self):
        ids = self.auctioneer.auctions['item_id']
        print(ids)
    


