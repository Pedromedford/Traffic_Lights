def parse_input_file(filename):
    with open(filename) as input_file:
        file_lines = [line.split() for line in input_file]

    return file_lines


def get_simulation_info(main_info):
    sim_duration = int(main_info[0])
    num_intersections = int(main_info[1])
    num_streets = int(main_info[2])
    num_cars = int(main_info[3])
    bonus_points = int(main_info[4])

    return sim_duration, num_intersections, num_streets, num_cars, bonus_points


def get_street_info(num_streets, file_lines):
    street_info = {}

    for i in range(num_streets):
        intersect_start = int(file_lines[i][0])
        intersect_finish = int(file_lines[i][1])
        street_name = file_lines[i][2]
        time_to_cross = int(file_lines[i][3])

        street_info[street_name] = [intersect_start, intersect_finish, time_to_cross]

    return street_info


def get_intersection_info(num_streets, file_lines):
    """
    Always On vs Traffic Cycle
    """
    intersection_info = {}

    for i in range(num_streets):

        street_name = file_lines[i][2]
        intersect_finish = int(file_lines[i][1])

        if intersect_finish in intersection_info:

            intersection_info[intersect_finish].append(street_name)

        else:
            intersection_info[intersect_finish] = [street_name]

    return intersection_info


def get_cars_at_intersection(num_streets, file_lines):
    """
    Always On vs Traffic Cycle
    """
    intersection_info = {}

    for i in range(num_streets):


        intersect_finish = int(file_lines[i][1])

        if intersect_finish in intersection_info:

            intersection_info[intersect_finish] +=1

        else:
            intersection_info[intersect_finish] = 1

    return intersection_info

def get_car_info(num_cars, file_lines):
    car_info = {}

    for i in range(num_cars):
        num_streets = int(file_lines[i][0])
        name_streets = file_lines[i][1:]

        car_info[i] = [num_streets, name_streets]

    return car_info


def main():
    # read all lines
    file_lines = parse_input_file("f.txt")

    # info from first line
    sim_duration, num_intersections, num_streets, num_cars, bonus_points = get_simulation_info(file_lines.pop(0))

    # intersection info
    intersection_info = get_intersection_info(num_streets, file_lines)

    # to be moved

    with open("answer_f_2.txt", "w") as output_file:

        output_file.write(str(num_intersections) + "\n")

        for intersection in intersection_info.keys():

            output_file.write(str(intersection) + "\n")
            output_file.write(str(len(intersection_info[intersection])) + "\n")

            for street in intersection_info[intersection]:
                output_file.write(str(street) + " 2\n")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
