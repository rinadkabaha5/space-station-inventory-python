import abc


class Item(abc.ABC):
    """
    The Item class represents a general inventory item on the space station
    """
    _COUNTER: int = 0

    def __init__(self, name: str, price: float) -> None:
        """
        Constructor.

        :param name: the name of the item.
        :param price: the price of the item.
        """
        self._name = name
        self._price = price


        Item._COUNTER += 1
        self._item_id = Item._COUNTER

    def get_id(self) -> int:
        """
        Returns the item's id.
        :return: the item's id.
        """
        return self._item_id

    def get_name(self) -> str:
        """
        Returns the item's name.
        :return: the item's name.
        """
        return self._name

    def get_price(self) -> float:
        """
        Returns the item's price.
        :return: the item's price.
        """
        return self._price

    @abc.abstractmethod
    def store(self, module_name: str) -> None:
        """
        Stores the item in the specified module.
        :param module_name: the name of the station module where the item is stored.
        """
        pass

    @abc.abstractmethod
    def get_category(self) -> str:
        """
        Returns a string that represents the item's category (for example: "LIFE_SUPPORT", "LOGISTICS", etc.)
        """
        pass

    @abc.abstractmethod
    def print_details(self) -> None:
        """
        Prints full details for the item.
        """
        pass

    @abc.abstractmethod
    def is_critical(self) -> bool:
        """
        Returns True if the item is critical for the station operation, and False otherwise
        """
        pass

    @staticmethod
    def get_number_of_created_items() -> int:
        """
        Returns the total number of Item instances that were created so far.
        :return: The total number of items created
        """
        return Item._COUNTER
