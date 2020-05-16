import json

from api.utils.redis_utils import create_redis_client


class AuctionDao(object):
    AUCTIONS_CACHE_KEY = 'campaigns_auctions'

    def __init__(self):
        # Todo: we should save it to the DB, but for now - we will use Redis
        self.redis_client = create_redis_client()

    def get(self, auction_id):
        result = self.redis_client.hget(self.AUCTIONS_CACHE_KEY, auction_id)

        if result is not None:
            result = json.loads(result)
            return result.get('campaign_id'), result.get('bid')

        # Todo: handle errors while avoiding exceptions
        print(f"An error occurred: auction_id={auction_id} not found")

    def set(self, auction_id, campaign_id, bid):
        self.redis_client.hset(self.AUCTIONS_CACHE_KEY, auction_id, json.dumps({
            'campaign_id': campaign_id,
            'bid': bid
        }))
