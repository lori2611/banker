from api.dao.auction_dao import AuctionDao
from api.utils.redis_utils import create_redis_client


class CampaignBudgetDao(object):  # Todo: Singleton
    CAMPAIGNS_BUDGET_CACHE_KEY = 'campaigns_budget'

    def __init__(self):
        self.redis_client = create_redis_client()
        self.campaign_balance = self._generate_local_bank()

    def get(self, campaign_id):
        return self.campaign_balance.get(campaign_id, 0)

    def update(self, auction_id):
        auction_dao = AuctionDao()
        campaign_id, bid = auction_dao.get(auction_id)

        if campaign_id in self.campaign_balance:
            self.campaign_balance[campaign_id] += bid

    def _generate_local_bank(self):
        # Todo: define an algorithm that gets data from Redis and save hourly campaign budget in campaign_balance dict
        # Every hour or whenever campaign balance becomes lower than a defined threshold (For example: lower than 0.1) -
        # we should ask for a new budget to our local cache
        return {
            '1': 10,
            '2': 20,
            '3': 30,
            '4': 40,
            '5': 50
        }
