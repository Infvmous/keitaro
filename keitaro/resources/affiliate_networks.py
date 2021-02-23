from keitaro.api import API


class AffiliateNetwork(API):

    def __init__(self, client, endpoint='affiliate_networks'):
        super(AffiliateNetwork, self).__init__(client, endpoint)

    def get(self, affiliate_network_id=None):
        """Getting all affiliate networks or specific one by its id"""
        return super(AffiliateNetwork, self).get(affiliate_network_id)

    def create(
            self, name, postback_url=None, offer_param=None, offers=None,
            template_name=None, notes=None, pull_api_options=None, state=None):
        """Creating new affiliate network"""
        return super(AffiliateNetwork, self).post(
            name=name,
            postback_url=postback_url,
            offer_param=offer_param,
            offers=offers,
            template_name=template_name,
            notes=notes,
            pull_api_options=pull_api_options,
            state=state)

    def clone(self, affiliate_network_id):
        """Cloning affiliate network by id"""
        return super(AffiliateNetwork, self).post(
            affiliate_network_id, 'clone')