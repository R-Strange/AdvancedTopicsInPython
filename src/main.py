import os
from src.enterprise import Enterprise
from src.stations import Engineering, Medical, WeaponsSystems, Science, Command
from src.staff import Staff

from typing import Dict

def main():
    
    def create_crewman():

        crewman_name = input("Name your crew member")

        crewman = Staff(crewman_name)

        print(repr(crewman))

        available_stations = list()

        for station in stations_list:
            station.retrieve_bonuses()
            print(station)
            pop_cap = station.section_cap
            current_pop = len(station.staff_list)

            if current_pop < pop_cap:
                available_stations.append(station)


        print("available stations:")

        options_dict: Dict = dict()

        for counter, station in enumerate(available_stations):
            options_dict[counter] = station
            print("{}) {}".format(counter, station.station_name))

        chosen_option: int = int(input("Input the station number"))
        chosen_station = options_dict[chosen_option]
        chosen_station.staff_list.append(crewman)

    print("Welcome. Can you survive your journey?")

    print("Initialising your vessel")

    vessel = Enterprise()

    engineering_station = Engineering()
    medical_station = Medical()
    weapons_systems_station = WeaponsSystems()
    science_station = Science()
    command_station = Command()

    stations_list = [engineering_station, medical_station, weapons_systems_station, science_station, command_station]


    print("Please, assign your staff members. "
          "You have 30 to place in either Engineering, Medical, Weapons Systems, Science or Command. "
          "You will have to assign 6 crew members to each station.")

    for crewman in range(30):
        create_crewman()



if __name__ == "__main__":
    main()
