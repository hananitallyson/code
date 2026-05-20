import subprocess
import json


def main_menu():
    subprocess.run("clear")
    print("---------- CONCLAVE MENU ----------")
    print("(1) PLAYERS")
    print("(2) GAMEMASTERS")
    print("(3) PARTIES")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


def player_menu():
    subprocess.run("clear")
    print("---------- PLAYERS ----------")
    print("(1) NEW PLAYER")
    print("(2) FIND PLAYER")
    print("(3) UPDATE PLAYER")
    print("(4) DELETE PLAYER")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


def gm_menu():
    subprocess.run("clear")
    print("---------- GAMEMASTERS ----------")
    print("(1) NEW GAMEMASTER")
    print("(2) FIND GAMEMASTER")
    print("(3) UPDATE GAMEMASTER")
    print("(4) DELETE GAMEMASTER")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


def party_menu():
    subprocess.run("clear")
    print("---------- PARTIES ----------")
    print("(1) NEW PARTY")
    print("(2) FIND PARTY")
    print("(3) UPDATE PARTY")
    print("(4) DELETE PARTY")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


if __name__ == "__main__":
    option = ""

    while option != 0:
        option = main_menu()

        if option == 1:
            menu_option = player_menu()

            if menu_option == 1:

            elif menu_option == 2:
                pass
            elif menu_option == 3:
                pass
            elif menu_option == 4:
                pass
            elif menu_option == 0:
                pass

        elif option == 2:
            gm_menu()

        elif option == 3:
            party_menu()

        elif option == 0:
            print("Exiting...\n")

