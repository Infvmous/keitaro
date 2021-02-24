import json

from keitaro.api import API
from keitaro.utils import (
    generate_random_string, remove_class_related_keys_from_local_symbol_table,
    filter_resource_entities_by_key_value)


class Campaign(API):

    def __init__(self, client, endpoint='campaigns'):
        super(Campaign, self).__init__(client, endpoint)

    def __str__(self):
        return 'campaign'

    def get(self, campaign_id=None):
        """Getting all campaigns or specific one if
        campaign_id is not None"""
        return super(Campaign, self).get(campaign_id)

    def get_deleted(self):
        """Getting all deleted/archived campaigns"""
        return super(Campaign, self).get('deleted')

    def get_streams(self, campaign_id):
        """Gettings streams of campaign with campaign_id"""
        return super(Campaign, self).get(campaign_id, 'streams')

    def clone(self, campaign_id):
        """Cloning campaign by its campaign_id"""
        return super(Campaign, self).post(campaign_id)

    def create(self, *, name, alias=None, type=None,
               state=None, cost_type=None, cookies_ttl=None, cost_value=None,
               cost_currency=None, cost_auto=False, group_id=None, token=None,
               traffic_source_id=None, bind_visitors=None, parameters=None,
               domain_id=None, postbacks=None):
        """Creating new advertising campaign"""
        query_params = remove_class_related_keys_from_local_symbol_table(
            locals())
        query_params['alias'] = generate_random_string()
        return super(Campaign, self).post(**query_params)

    def disable(self, campaign_id):
        """Changing state of campaign to disabled"""
        return super(Campaign, self).post(campaign_id, 'disable')

    def get_by_name(self, name):
        """Returns list of found campaigns by name"""
        return filter_resource_entities_by_key_value(
            self.get().json(), 'name', name)
