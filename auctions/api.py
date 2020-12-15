from wow_client import WowDataClient
from .controller import AuctionDataController
from flask import Flask
import os

app = Flask(__name__)

@app.route('/auctions')
def auctions_api():
    client = WowDataClient(client_id=os.getenv('wow_app_client_id'), client_secret=os.getenv('wow_app_client_secret'), realmId=73)
    auctioneer = AuctionDataController(client=client)
    return auctioneer.auctions.to_dict()
