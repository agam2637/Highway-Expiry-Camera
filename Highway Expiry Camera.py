import matplotlib.pyplot as plt


def main():
    """
    This function aims to read the file which has the list of highway vehicles
    and take action
    """

    expired_cars = 0
    expired_trucks = 0
    expired_buses = 0
    speeds = []

    with open('HighwayData.csv', 'r') as f:
        lines = f.readlines()

        for line in lines:
            info = [item.strip() for item in line.strip().split('-')]
            vehicle_type = info[0]
            plate = info[1]
            speed = info[2]

            if check_expiry(plate) is True:
                if vehicle_type == 'truck':
                    expired_trucks += 1
                elif vehicle_type == 'car':
                    expired_cars += 1
                elif vehicle_type == 'bus':
                    expired_buses += 1

            speeds.append(int(speed))

    average = find_average_speed(speeds)
    make_graph([expired_trucks, expired_cars, expired_buses, average])


def check_expiry(plate: str) -> bool:
    """
    This function aims to check if the vehicle has a expired plate or not
    """
    with open('ExpiredPlate.csv', 'r') as s:
        lines = s.readlines()

        for line in lines:
            info = line.strip()
            if plate.strip() == info:
                return True

    return False


def find_average_speed(speeds_list: list[int]) -> int:
    """
    This function aims to calculate the average speed
    """
    total = 0
    for i in speeds_list:
        total += i

    average_speed = total // len(speeds_list)

    return average_speed


def make_graph(y: list[int]):
    """
    This function aims to launch the graph of
     the data which is read from the file
    """

    x = ['truck', 'car', 'bus', 'average speed']

    plt.bar(x,y)

    plt.xlabel('Vehicle Types')
    plt.ylabel('Expired Vehicles')
    plt.title('Number of Expired Vehicles On Highway')

    plt.show()


if __name__ == "__main__":
    main()
