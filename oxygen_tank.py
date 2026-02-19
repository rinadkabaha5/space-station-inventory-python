from item import Item


class OxygenTank(Item):
    """
    This class represents an Oxygen Tank in the space station.
    It inherits from Item class
    """
    def __init__(self, price: float, capacity_liters: float, expiration_date: str) -> None:
        """
        Constructor for the OxygenTank class

        :param price: The cost of this tank (in station credits)
        :param capacity_liters: Total oxygen capacity in liters
        :param expiration_date: String representing the expiration date
        """
        super().__init__("OXYGEN_TANK", price)
        self._capacity_liters = capacity_liters
        self._expiration_date = expiration_date

    def store(self, module_name: str) -> None:
        """
        Stores the item in the specified module
        :param module_name: the name of the station module where the item is stored
        """
        print(f"Oxygen tank is stored in module {module_name}.")

    def get_category(self) -> str:
        """
        Returns the item's category
        :return: "LIFE_SUPPORT"
        """
        return "LIFE_SUPPORT"

    def is_critical(self) -> bool:
        """
        Checks if the item is critical
        :return: True (every oxygen tank is critical)
        """
        return True

    def print_details(self) -> None:
        """
        Prints full details for the oxygen tank
        """
        # Fix: Removed colons, fixed spelling of Category, fixed 'on' casing
        print(f"Item #{self.get_id()} - {self.get_name()} costs {self.get_price()} credits.")
        print(f"Category: {self.get_category()}.")
        print(f"Capacity: {self._capacity_liters} liters.")
        print(f"Expires on {self._expiration_date}.")
        print(f"Critical: {self.is_critical()}.")