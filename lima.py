def streets():
    streets = []

    street_id = []
    street_name = []
    intersections_amount = []

    with open ("Lima-calles.csv") as textFile:
        for line in textFile:
            street = [item.strip() for item in line.split(';')]
            streets.append(street)

            street_id.append(street[0])
            street_name.append(street[1])
            intersections_amount.append(street[2])
            print(street)
    #print(streets)

def intersections():
    intersections = []

    registry_id = []
    street_id = []
    street_name = []
    origin_id = destiny_id = []
    intersection_origin_id = intersection_destiny_id = []
    distance = []
    speed = []
    cost = []
    inverse_cost = []
    latitude_of_6 = length_of_6 = []
    latitude_of_7 = length_of_7 = []

    with open ("Lima-intersecciones.csv") as textFile:
        for line in textFile:
            intersection = [item.strip() for item in line.split(';')]
            intersections.append(intersection)

            registry_id.append(intersection[0])
            street_id.append(intersection[1])
            street_name.append(intersection[2])

            origin_id.append(intersection[3])
            destiny_id.append(intersection[4])

            intersection_origin_id.append(intersection[5])
            intersection_destiny_id.append(intersection[6])

            distance.append(intersection[7])
            speed.append(intersection[8])
            cost.append(intersection[9])
            inverse_cost.append(intersection[10])
            latitude_of_6.append(intersection[11])
            length_of_6.append(intersection[12])
            latitude_of_7.append(intersection[13])
            length_of_7.append(intersection[14])

            print(intersection)