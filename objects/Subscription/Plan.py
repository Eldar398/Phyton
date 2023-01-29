from settings.subscriptionTypes import SubscriptionTypes


class SubscriptionPlan:

    def __init__(self, subscription_type, address):

        if self.check_corrent_type(subscription_type):
            self.subscription_type = subscription_type
        else:
            self.subscription_type = ''
        self.address = address

    def check_corrent_type(self, current_type):
        subscription_types = SubscriptionTypes.subscriptionTypes
        for subscription_type in subscription_types:
            if subscription_type == current_type:
                return True
        return False
