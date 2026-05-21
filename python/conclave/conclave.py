import subprocess
import json

with open("db.json", "r", encoding="utf-8") as db:
    database = json.load(db)


def clear():
    subprocess.run("clear")


def save_database():
    with open("db.json", "w", encoding="utf-8") as db:
        json.dump(database, db, indent=4, ensure_ascii=False)


def main_menu():
    clear()
    print("---------- CONCLAVE MENU ----------")
    print("(1) PLAYERS")
    print("(2) GAMEMASTERS")
    print("(3) PARTIES")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


def player_menu():
    clear()
    print("---------- PLAYERS ----------")
    print("(1) NEW PLAYER")
    print("(2) FIND PLAYER")
    print("(3) UPDATE PLAYER")
    print("(4) DELETE PLAYER")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


def gm_menu():
    clear()
    print("---------- GAMEMASTERS ----------")
    print("(1) NEW GAMEMASTER")
    print("(2) FIND GAMEMASTER")
    print("(3) UPDATE GAMEMASTER")
    print("(4) DELETE GAMEMASTER")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


def party_menu():
    clear()
    print("---------- PARTIES ----------")
    print("(1) NEW PARTY")
    print("(2) FIND PARTY")
    print("(3) UPDATE PARTY")
    print("(4) DELETE PARTY")
    print("(0) EXIT")
    option = input("\n *  Choose your option: ")
    return int(option)


if __name__ == "__main__":
    option = -1

    while option != 0:
        option = main_menu()

        if option == 1:
            menu_option = player_menu()

            if menu_option == 1:
                clear()
                print("---------- CREATE PLAYER ----------")
                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["players"].append(
                    {"name": name, "email": email, "phone": phone}
                )

                save_database()

                print("\nPlayer created successfully!")

                input("\nPress ENTER to continue...")

            elif menu_option == 2:
                clear()
                print("---------- FIND PLAYER ----------")
                name = input("SEARCH BY NAME: ")

                player_list_size = len(database["players"])
                position = 0
                find = False

                while (position < player_list_size) and not find:
                    if name == database["players"][position]["name"]:
                        find = True
                    else:
                        position += 1

                if find:
                    clear()
                    print("---------- FIND PLAYER ----------")
                    print(f"NAME: {database['players'][position]['name']}")
                    print(f"EMAIL: {database['players'][position]['email']}")
                    print(f"PHONE NUMBER: {database['players'][position]['phone']}")
                else:
                    print("\nPlayer not found!")

                input("\nPress ENTER to continue...")

            elif menu_option == 3:
                yes = ""
                player_index = ""

                while yes != "Y":
                    clear()
                    print("---------- UPDATE PLAYER ----------")

                    player_index = (
                        int(input("SELECT THE PLAYER BY NUMBER (e.g. 1): ")) - 1
                    )

                    print(f"\nYOU CHOOSE {database['players'][player_index]['name']}")
                    yes = input("CONTINUE? (Y/N): ").upper()

                clear()
                print("---------- UPDATE PLAYER ----------")

                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["players"][player_index]["name"] = name
                database["players"][player_index]["email"] = email
                database["players"][player_index]["phone"] = phone

                save_database()

                print("\nPlayer updated successfully!")

                input("\nPress ENTER to continue...")

            elif menu_option == 4:
                yes = ""
                player_index = ""

                while yes != "Y":
                    clear()
                    print("---------- DELETE PLAYER ----------")

                    player_index = (
                        int(input("SELECT THE PLAYER BY NUMBER (e.g. 1): ")) - 1
                    )

                    print(f"\nYOU CHOOSE {database['players'][player_index]['name']}")
                    yes = input("CONTINUE? (Y/N): ").upper()

                clear()
                print("---------- DELETE PLAYER ----------")

                database["players"].pop(player_index)

                save_database()

                print("\nPlayer deleted successfully!")

                input("\nPress ENTER to continue...")

        elif option == 2:
            menu_option = gm_menu()

            if menu_option == 1:
                clear()
                print("---------- CREATE GAMEMASTER ----------")

                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["gamemasters"].append(
                    {"name": name, "email": email, "phone": phone}
                )

                save_database()

                print("\nGamemaster created successfully!")

                input("\nPress ENTER to continue...")

            elif menu_option == 2:
                clear()
                print("---------- FIND GAMEMASTER ----------")

                name = input("SEARCH BY NAME: ")

                gm_list_size = len(database["gamemasters"])
                position = 0
                find = False

                while (position < gm_list_size) and not find:
                    if name == database["gamemasters"][position]["name"]:
                        find = True
                    else:
                        position += 1

                if find:
                    clear()
                    print("---------- FIND GAMEMASTER ----------")
                    print(f"NAME: {database['gamemasters'][position]['name']}")
                    print(f"EMAIL: {database['gamemasters'][position]['email']}")
                    print(f"PHONE NUMBER: {database['gamemasters'][position]['phone']}")
                else:
                    print("\nGamemaster not found!")

                input("\nPress ENTER to continue...")

            elif menu_option == 3:
                yes = ""
                gm_index = ""

                while yes != "Y":
                    clear()
                    print("---------- UPDATE GAMEMASTER ----------")

                    gm_index = (
                        int(input("SELECT THE GAMEMASTER BY NUMBER (e.g. 1): ")) - 1
                    )

                    print(f"\nYOU CHOOSE {database['gamemasters'][gm_index]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                clear()
                print("---------- UPDATE GAMEMASTER ----------")

                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["gamemasters"][gm_index]["name"] = name
                database["gamemasters"][gm_index]["email"] = email
                database["gamemasters"][gm_index]["phone"] = phone

                save_database()

                print("\nGamemaster updated successfully!")

                input("\nPress ENTER to continue...")

            elif menu_option == 4:
                yes = ""
                gm_index = ""

                while yes != "Y":
                    clear()
                    print("---------- DELETE GAMEMASTER ----------")

                    gm_index = (
                        int(input("SELECT THE GAMEMASTER BY NUMBER (e.g. 1): ")) - 1
                    )

                    print(f"\nYOU CHOOSE {database['gamemasters'][gm_index]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                clear()
                print("---------- DELETE GAMEMASTER ----------")

                database["gamemasters"].pop(gm_index)

                save_database()

                print("\nGamemaster deleted successfully!")

                input("\nPress ENTER to continue...")

        elif option == 3:
            menu_option = party_menu()

            if menu_option == 1:
                clear()
                print("---------- CREATE PARTY ----------")
                gamemaster_id = int(input("GAMEMASTER ID (e.g. 1): ")) - 1
                players = input("PLAYERS IDs (e.g. 1 3 5): ").split(" ")
                number_of_players = len(players)
                game = input("GAMERULES: ")

                player_names = []
                for player_id in players:
                    index = int(player_id) - 1
                    player_names.append(database["players"][index]["name"])

                database["parties"].append(
                    {
                        "gamemaster": database["gamemasters"][gamemaster_id]["name"],
                        "number_of_players": number_of_players,
                        "players": player_names,
                        "game": game,
                    }
                )

                save_database()

                print("\nParty created successfully!")

                input("\nPress ENTER to continue...")

            elif menu_option == 2:
                clear()
                print("---------- FIND PARTY ----------")

                party_index = int(input("SEARCH BY PARTY NUMBER: ")) - 1

                if 0 <= party_index < len(database["parties"]):
                    clear()
                    print("---------- FIND PARTY ----------")

                    print(
                        f"GAMEMASTER: {database['parties'][party_index]['gamemaster']}"
                    )

                    print(f"GAME: {database['parties'][party_index]['game']}")

                    print(
                        f"NUMBER OF PLAYERS: {database['parties'][party_index]['number_of_players']}"
                    )

                    print("PLAYERS:")

                    for player in database["parties"][party_index]["players"]:
                        print(f"- {player}")

                else:
                    print("\nParty not found!")

                input("\nPress ENTER to continue...")

        elif option == 0:
            print("\nExiting...\n")

