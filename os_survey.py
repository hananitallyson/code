import subprocess

subprocess.run("clear")

linux_votes = 0
macos_votes = 0
windows_votes = 0
null_votes = 0
vote_loop = "Y"

while vote_loop == "Y" or vote_loop == "":
    print("\n-------- OPERATING SYSTEM SURVEY --------")
    question_loop = True
    while question_loop:
        print("\n(1) Linux\n(2) MacOS\n(3) Windows\n(0) None of the options")
        vote = input("Enter your vote (1/2/3/0): ")

        if vote == "1":
            linux_votes += 1
            question_loop = False
        elif vote == "2":
            macos_votes += 1
            question_loop = False
        elif vote == "3":
            windows_votes += 1
            question_loop = False
        elif vote == "0":
            null_votes += 1
            question_loop = False
        else:
            print("\nError: invalid option.")

    vote_loop = input("\nWould you like to respond to the survey?\nEnter your answer (Y/n): ").upper()
    subprocess.run("clear")

total_votes = linux_votes + macos_votes + windows_votes + null_votes

linux_percentage = round(linux_votes / total_votes * 100)
macos_percentage = round(macos_votes / total_votes * 100)
windows_percentage = round(windows_votes / total_votes * 100)
null_percentage = round(null_votes / total_votes * 100)

print("\n------------------------------------ SURVEY RESULTS ------------------------------------")
print(f"\nTOTAL -> {total_votes} | NULL -> {null_votes} @ {null_percentage}% | Linux -> {linux_votes} @ {linux_percentage}% | MacOS -> {macos_votes} @ {macos_percentage}% | Windows -> {windows_votes} @ {windows_percentage}%\n")

print("[WINNER OS]")
if linux_percentage > macos_percentage and linux_percentage > windows_percentage:
    print(f"Linux @ {linux_percentage}%\n")
elif macos_percentage > windows_percentage and macos_percentage > linux_percentage:
    print(f"MacOS @ {macos_percentage}%\n")
elif windows_percentage > linux_percentage and windows_percentage > macos_percentage:
    print(f"Windows @ {windows_percentage}%\n")
elif linux_percentage == macos_percentage and linux_percentage > windows_percentage:
    print(f"Linux @ {linux_percentage}% and MacOS @ {macos_percentage}%\n")
elif linux_percentage == windows_percentage and linux_percentage > macos_percentage:
    print(f"Linux @ {linux_percentage}% and Windows @ {windows_percentage}%\n")
elif macos_percentage == windows_percentage and macos_percentage > linux_percentage:
    print(f"MacOS @ {macos_percentage}% and Windows @ {windows_percentage}%\n")
elif linux_percentage == macos_percentage == windows_percentage and linux_percentage != 0:
    print(f"Linux @ {linux_percentage}% and MacOS @ {macos_percentage}% and Windows @ {windows_percentage}%\n")
else:
    print(f"{null_percentage}% of the votes were null\n")
