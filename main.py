class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        # Default fare calculation
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Calculate the total fare with 10% maintenance charge
        base_fare = super().fare()  # Call the fare method from Vehicle
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

# Create an instance of the Bus class with a seating capacity of 50
bus = Bus(seating_capacity=50)

# Print the calculated fare
print(f"The total fare for the bus ride is INR {bus.fare():.2f}")
