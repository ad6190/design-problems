class Somato(object):
    """
    has multiple restaurants
    selects a restaurant based on strategy
    accepts order only if one/more restaurant are selected for that order
    """
    pass


class Restaurant(object):
    """
    has a menu
    has a max processing capacity of items
    prepares and dispatches food


    """
    pass


class Menu(object):
    """
    has multiple items
    """
    pass


class MenuItem(object):
    """
    has name
    has price

    """
    pass


class User(object):
    """
    has name
    """
    pass


class Order(object):
    """
    has a user
    has multiple orderitems
    is assigned to a restaurant
    has states
    """
    pass


class OrderItems(object):
    pass