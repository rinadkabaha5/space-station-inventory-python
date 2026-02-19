from typing import List
from item import Item
from oxygen_tank import OxygenTank
from cargo_crate import CargoCrate
from research_sample import ResearchSample

print("WELCOM TO SPACE STATION INVENTORY")

"""
The space station inventory items list
"""
station_inventory: List[Item] = []

"""
The main loop
"""
while True:
    command = input("Please enter a command: ")

    if command == "add_oxygen_tank":
        """
        Receive price
        """
        try:
            price = float(input("Please insert the price of the oxygen tank: "))

            """
            Receive capacity (liters)
            """
            capacity_liters = float(input("Please insert the capacity (liters) of the oxygen tank: "))

            """
            Receive expiration date
            """
            expiration_date = input("Please insert the expiration date of the oxygen tank: ")

            """
            Create a new OxygenTank object, and add it to the <station_inventory> list
            """
            oxygen_tank = OxygenTank(price, capacity_liters, expiration_date)
            station_inventory.append(oxygen_tank)
        except ValueError:
            print("Invalid input")

    elif command == "add_cargo_crate":
        """
        Receive content_type from the user
        """
        try:
            content_type = input("Please insert the content type of the cargo crate: ")

            """
            Receive price_per_kg from the user
            """
            price_per_kg = float(input("Please insert the cargo crate price per KG: "))

            """ 
            Receive weight from the user
            """
            weight_kg = float(input("Please insert the cargo crate weight (in KG): "))

            """
            Create a new CargoCrate object, and add it to the <station_inventory> list
            """
            cargo_crate = CargoCrate(content_type, price_per_kg, weight_kg)
            station_inventory.append(cargo_crate)
        except ValueError:
            print("Invalid input")

    elif command == "add_research_sample":
        """
        Receive experiment_name from the user
        """
        try:
            expermient_name = input("Please insert the experiment name of the research sample: ")

            """
            Receive hazard_level from the user
            """
            hazard_level = int(input("Please insert the hazard level (1-10) of the research sample: "))

            """
            Receive price from the user
            """
            price = float(input("Please insert the price of the research sample: "))

            """
            Create a new ResearchSample object, and add it to the <station_inventory> list
            """
            research_sample = ResearchSample(expermient_name, hazard_level, price)
            station_inventory.append(research_sample)
        except ValueError:
            print("Invalid input")

    elif command == "print":
        """
        Prints all the items in the <station_inventory> list, using the "print_details" method
        """
        for item in station_inventory:
            item.print_details()

    elif command == "store":
        """
        Receives module_name from the user
        """
        module_name = input("Please insert the module name: ")

        """
        Call `store` method with the received <module_name> for all the items in the list
        """
        for item in station_inventory:
            item.store(module_name)

    elif command == "total_value":
        """
        Prints the TOTAL price of all the items in the <station_inventory> list
        """
        total_value = 0.0
        for item in station_inventory:
            total_value += item.get_price()
        print(f"The total price is {total_value}.")

    elif command == "avg_value":
        """
        Prints the AVERAGE price of all the items in the <station_inventory> list
        """
        if len(station_inventory) == 0:
            print("No items in the station inventory.")
        else:
            current_total = 0.0
            for item in station_inventory:
                current_total += item.get_price()

            average_value = current_total / len(station_inventory)
            print(f"The average price is {average_value:.2f}.")

    elif command == "remove":
        """
        Receive the id of the item to remove from the user
        """
        try:
            remove_id = int(input("Please insert the id of the item you want to remove: "))

            """
            If an item with the received id exists - remove the item
            In any case - print an appropriate message
            """
            found = False
            for i, item in enumerate(station_inventory):
                if item.get_id() == remove_id:
                    station_inventory.pop(i)
                    print(f"Item #{remove_id} was removed from the list.")
                    found = True
                    break

            if not found:
                print(f"Item #{remove_id} was not found in the list.")
        except ValueError:
            print("Invalid input")

    elif command == "critical":
        """
        Prints only the critical items in the inventory
        """
        found_critical = False
        for item in station_inventory:
            if item.is_critical():
                item.print_details()
                found_critical = True

        if not found_critical:
            print("No critical items in the station inventory.")

    elif command == "created_items":
        """
        Prints the number of items created so far
        """
        count = Item.get_number_of_created_items()
        print(f"{count} Items created so far.")

    elif command == "exit":
        break
    else:
        print(f"Sorry! The command {command} is unknown. Please try again.")

print("Thank you for using the SPACE STATION INVENTORY system!")