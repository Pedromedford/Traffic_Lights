

def parse_input_file(filename):

    file_lines = []

    with open (filename) as input_file:

       file_lines = [ line.split() for line in input_file]

    return file_lines

def get_simulation_info(main_info):

    sim_duration = int(main_info[0])
    num_intersections = int(main_info[1])
    num_streets = int(main_info[2])
    num_cars = int(main_info[3])
    bonus_points = int(main_info[4])

    return(sim_duration,num_intersections,num_streets,num_cars,bonus_points)

def get_street_info(num_streets,file_lines):

    street_info = {}

    for i in range (num_streets):

        intersect_start = int(file_lines[i][0])
        intersect_finish = int(file_lines[i][1])
        street_name = file_lines[i][2]
        time_to_cross = int(file_lines[i][3])

        street_info[street_name] = [intersect_start, intersect_finish, time_to_cross]

    return street_info

def get_car_info(num_cars,file_lines):

    car_info = {}

    for i in range (num_cars):

        num_streets = int(file_lines[i][0])
        name_streets = file_lines[i][1:]

        car_info[i] = [num_streets, name_streets]

    return car_info


def main():

    file_lines = parse_input_file("a.txt")
    sim_duration,num_intersections,num_streets,num_cars,bonus_points = get_simulation_info(file_lines.pop(0))

    street_info = get_street_info(num_streets,file_lines)
    file_lines = file_lines[num_streets:]

    car_path_info = get_car_info(num_cars,file_lines)


    print(street_info)
    print(car_path_info)
    print("\nDuration:",sim_duration,"\nIntersections:",num_intersections,"\nStreets:",num_streets,"\nCars:",
          num_cars,"\nBonus Points:", bonus_points)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

