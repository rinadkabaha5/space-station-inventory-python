from item import Item


class ResearchSample(Item):
    """
    The ResearchSample class represents a research sample item
    """

    def __init__(self, experiment_name: str, hazard_level: int, price: float) -> None:
        """
        Constructor for ResearchSample

        :param experiment_name: the name of the experiment
        :param hazard_level: hazard level from 1 to 10
        :param price: the cost of the sample
        """
        super().__init__("RESEARCH_SAMPLE", price)
        self._experiment_name = experiment_name
        self._hazard_level = hazard_level

    def store(self, module_name: str) -> None:
        """
        Stores the item in the specified module
        """

        print(f"Research sample for experiment {self._experiment_name} is stored in module {module_name} with hazard level {self._hazard_level}.")

    def get_category(self) -> str:
        """
        Returns the item's category
        """
        return "SCIENCE"

    def is_critical(self) -> bool:
        """
        Returns True if hazard_level is greater than or equal to 8
        """
        return self._hazard_level >= 8

    def print_details(self) -> None:
        """
        Prints full details for the research sample
        """

        print(f"Item #{self.get_id()} - {self.get_name()} '{self._experiment_name}' belongs to {self.get_category()} category.")
        print(f"Hazard level: {self._hazard_level}.")
        print(f"Cost: {self.get_price()} credits.")
        print(f"Critical: {self.is_critical()}.")