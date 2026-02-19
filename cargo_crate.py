from item import Item


class CargoCrate(Item):
    """
    The CargoCrate class represents a cargo crate item in the space
    station inventory.
    """

    def __init__(self, content_type: str, price_per_kg: float, weight_kg: float) -> None:
        """
        Constructor for CargoCrate
        :param content_type: what is inside (e.g. "food", "tools", "research")
        :param price_per_kg: price per kg
        :param weight_kg: the weight of the crate
        """
        super().__init__("CARGO_CRATE", price_per_kg * weight_kg)
        self._content_type = content_type
        self._weight_kg = weight_kg

    def store(self, module_name: str) -> None:
        """
        Stores the item in the specified module
        """
        print(f"Cargo crate with {self._content_type} is stored in module {module_name}.")

    def get_category(self) -> str:
        """
        Returns the item's category
        """
        return "LOGISTICS"

    def is_critical(self) -> bool:
        """
        Returns True if the content type is one of: "food", "medical"
        """

        return self._content_type in ["food", "medical"]

    def print_details(self) -> None:
        """
        Prints full details for the cargo crate
        """

        print(
            f"Item #{self.get_id()} - {self.get_name()} ({self._content_type}) belongs to {self.get_category()} category.")
        print(f"Weight: {self._weight_kg} kg,")
        print(f"Total cost: {self.get_price()} credits.")
        print(f"Critical: {self.is_critical()}.")