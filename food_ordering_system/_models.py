import itertools
from enum import Enum
from selection_strategies import LowestPriceRestaurantStrategy

lowest_price_strategy = LowestPriceRestaurantStrategy()



class Somato(object):
    """
    has multiple restaurants
    selects a restaurant based on strategy
    accepts order only if one/more restaurant are selected for that order
    """
    def __init__(self, selection_strategy):
        self.restaurants = list()
        self.selection_strategy = selection_strategy

    def add_restaurant(self, name, menu):
        self.restaurants.append(Restaurant(name, menu))

    def update_menu(self, name, menu):
        for restaurant in self.restaurants:
            if restaurant.name == name:
                restaurant.menu = dict(itertools.chain(restaurant.menu.items(), menu.items()))

    def is_order_fulfillable(self, order_items):
        """

        :param order_items:
        :return: list of restaurants or None

        """
        pass

    def select_restaurant(self, order_items):
        selected_restaurants = self.selection_strategy.find_restaurants(order_items)
        pass

class Restaurant(object):
    """
    has an name
    has a menu
    has a max processing capacity of items
    prepares and dispatches food
    """
    def __init__(self, name, menu):
        self.name = name
        self.menu = Menu(menu)

class Menu(object):
    """
    has multiple items
    """
    def __init__(self, menu):
        self.menu_items = [{k,v} for k,v in menu.items]

    pass

#
# class MenuItem(object):
#     """
#     has name
#     has price
#
#     """
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
#     pass


class User(object):
    """
    has name
    """
    def __init__(self, name):
        self.name = name


class ORDER_STATUS(Enum):
    received = 1
    cancelled = 2
    assigned = 3
    delivered = 4


class Order(object):
    """
    has a user
    has multiple orderitems
    is assigned to a restaurant
    has states
    """

    def __init__(self, user, order_items):
        self.user = user
        self.order_items = [{k,v} for k,v in order_items.items]
        self.order_status = ORDER_STATUS.received

#
# class OrderItems(object):
#     pass