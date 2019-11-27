import abc  # Python's built-in abstract class library


class RestaurantSelectionStrategyAbstract(object):
    """You do not need to know about metaclasses.
    Just know that this is how you define abstract
    classes in Python."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def find_restaurants(self, order_items):
        """Required Method"""


class LowestPriceRestaurantStrategy(RestaurantSelectionStrategyAbstract):
    def find_restaurants(self, order_items):
       pass
