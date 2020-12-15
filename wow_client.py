from utils.handlers import error_handler
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class WowDataClient(object):
    client = None
    _token = None
    realmId = None
    AUCTIONS_URL = 'https://us.api.blizzard.com/data/wow/connected-realm/{}/auctions'
    ITEM_URL =  'https://us.api.blizzard.com/data/wow/item/{}'

    REQUIRED_PARAMS = {
        'namespace': 'dynamic-us',
        'locale': 'en_us'
    }
    def __init__(self, client_id, client_secret, realmId, *args, **kwargs) -> None:
        self.client = OAuth2Session(client=BackendApplicationClient(client_id=client_id))
        self._token = self.client.fetch_token(token_url="https://us.battle.net/oauth/token", client_id=client_id, client_secret=client_secret)
        self.realmId = realmId
        super().__init__(*args, **kwargs)

    @error_handler
    def _get(self, url, params={}):
        params.update(self.REQUIRED_PARAMS)
        return self.client.get(url, params=params).json()

    def get_auctions(self):
        return self._get(self.AUCTIONS_URL.format(self.realmId))

    def get_item(self, item_id):
        return self._get(self.ITEM_URL.format(self.ITEM_URL))