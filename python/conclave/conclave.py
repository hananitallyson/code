import subprocess
import json

with open("db.json", "r", encoding="utf-8") as db:
    database = json.load(db)


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
    option = -1

    while option != 0:
        option = main_menu()

        if option == 1:
            menu_option = player_menu()

            if menu_option == 1:
                subprocess.run("clear")
                print("---------- CREATE PLAYER ----------")
                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["players"].append(
                    {"name": name, "email": email, "phone": phone}
                )

                with open("db.json", "w", encoding="utf-8") as db:
                    json.dump(database, db, indent=4, ensure_ascii=False)

                print("\nPlayer created successfully!")

                input("\nPress ENTER to continue...")

            elif menu_option == 2:
                subprocess.run("clear")
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
                    subprocess.run("clear")
                    print("---------- FIND PLAYER ----------")
                    print(f"NAME: {database['players'][position]['name']}")
                    print(f"EMAIL: {database['players'][position]['email']}")
                    print(f"PHONE NUMBER: {database['players'][position]['phone']}")
                else:
                    print("\nPlayer not found!")

                input("\nPress ENTER to continue...")
            elif menu_option == 3:
                subprocess.run("clear")
                print("---------- UPDATE PLAYER ----------")

                yes = ""
                player_index = ""
                while yes != "Y":
                    player_index = int(input("SELECT THE PLAYER BY NUMBER (e.g. 1): "))
                    print(f"\nYOU CHOOSE {database['players'][player_index]['name']}")
                    yes = input("CONTINUE? (Y/N): ").upper()

                subprocess.run("clear")
                print("---------- UPDATE PLAYER ----------")
                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["players"][player_index]["name"] = name
                database["players"][player_index]["email"] = email
                database["players"][player_index]["phone"] = phone

                with open("db.json", "w", encoding="utf-8") as db:
                    json.dump(database, db, indent=4, ensure_ascii=False)

                print("\nPlayer updated successfully!")

                input("\nPress ENTER to continue...")

        elif option == 2:
            gm_menu()

        elif option == 3:
            party_menu()

        elif option == 0:
            print("\nExiting...\n")

