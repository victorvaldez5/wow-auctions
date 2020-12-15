from wow_client import WowDataClient
from auctions.controller import AuctionDataController
from items.controller import ItemDataTable
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.env')
load_dotenv(env_path)

client = WowDataClient(client_id=os.getenv('wow_app_client_id'), client_secret=os.getenv('wow_app_client_secret'), realmId=73)
auctioneer = AuctionDataController(client=client)
auctioneer.auctions
item_table = ItemDataTable(auctioneer)
item_table._create_item_table()