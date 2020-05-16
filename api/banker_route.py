import json
from flask import request

from api.banker_api import app
from api.dao.auction_dao import AuctionDao
from api.dao.campaign_budget_dao import CampaignBudgetDao

campaign_budget_dao = CampaignBudgetDao()


@app.route("/api/budget/<string:campaign_id>", methods=['GET', 'OPTIONS'])
def get_campaign_budget(campaign_id):
    auction_id = request.values.get('auction_id')
    bid = float(request.values.get('bid'))
    budget = campaign_budget_dao.get(campaign_id)

    if budget >= bid:
        # Todo: saving auction can be async in order to response ASAP
        auction_dao = AuctionDao()
        auction_dao.set(auction_id, campaign_id, bid)
        return json.dumps({'success': True})

    return json.dumps({'success': False})


@app.route("/api/budget/update", methods=['POST', 'OPTIONS'])
def update_campaign_budget(auction_id, did_win):
    if not did_win:
        campaign_budget_dao.update(auction_id)

    return json.dumps({'success': True})


