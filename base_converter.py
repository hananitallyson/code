import subprocess

def convert_base(n, from_base, to_base):
    if to_base < 2 or to_base > 36:
        print("Base must be between 2 and 36.")
        return
    if n == "0":
        return "0"
    decimal_number = int(n, from_base)
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = ""
    while decimal_number:
        remainder = decimal_number % to_base
        digits += symbols[remainder]
        decimal_number //= to_base
    return digits[::-1]

print("\nWelcome to Base Converter!")
print("Type 'exit' to exit the converter or type 'clear' to clear the terminal.\n")
main = True

while main == True:
    num_list = input("Enter number, current base, and target base (e.g., 45 16 2).\nIf already decimal, just enter number and target base: ")

    if num_list == "exit":
        print("")
        main = False
    elif num_list == "clear":
        subprocess.run(num_list)
    else:
        num_list = num_list.split(" ")
        
        if len(num_list) == 2:
            target_num = num_list[0]
            inicial_base = 10
            target_base = int(num_list[1])
        else:
            target_num = num_list[0]
            inicial_base = int(num_list[1])
            target_base = int(num_list[2])

        if target_base == 2:
            print(f"{target_num} (base {inicial_base}) -> {convert_base(target_num, inicial_base, target_base)} (base {target_base}, i.e. binary)\n")
        elif target_base == 8:
            print(f"{target_num} (base {inicial_base}) -> {convert_base(target_num, inicial_base, target_base)} (base {target_base}, i.e. octal)\n")
        elif target_base == 16:
            print(f"{target_num} (base {inicial_base}) -> {convert_base(target_num, inicial_base, target_base)} (base {target_base}, i.e. hexadecimal)\n")
        else:
            print(f"{target_num} (base {inicial_base}) -> {convert_base(target_num, inicial_base, target_base)} (base {target_base})\n")
