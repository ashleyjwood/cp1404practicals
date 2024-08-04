from silver_service_taxi import SilverServiceTaxi


def main():
    """Demo the SilverServiceTaxi class."""
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)
    assert luxury_taxi.name == "Hummer"
    assert luxury_taxi.fuel == 200
    assert luxury_taxi.fanciness == 2

    luxury_taxi.drive(18)
    expected_fare = 18 * luxury_taxi.price_per_km + SilverServiceTaxi.flagfall
    assert expected_fare == luxury_taxi.get_fare()

    print(luxury_taxi)
    print(f"Total fare: ${luxury_taxi.get_fare():.2f}")


main()
