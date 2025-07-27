from taxi import Taxi

def main():
    """Test the Taxi class with a sample scenario."""

    # 1. Create a new Taxi object
    my_taxi = Taxi("Prius 1", 100)

    # 2. Drive the taxi 40 km
    my_taxi.drive(40)