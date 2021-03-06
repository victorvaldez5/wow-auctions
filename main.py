import flask
import os

from wow_client import WowDataClient
from auctions.controller import AuctionDataController
from items.controller import ItemDataTable
from dotenv import load_dotenv
from pathlib import Path

app = flask.Flask(__name__)
app.config["DEBUG"] = True

env_path = Path('.env')
load_dotenv(env_path)

@app.route('/auctions')
def auctions_api():
    client = WowDataClient(client_id=os.getenv('wow_app_client_id'), client_secret=os.getenv('wow_app_client_secret'), realmId=73)
    auctioneer = AuctionDataController(client=client)
    return auctioneer.auctions.to_dict()

app.run()