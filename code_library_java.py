import os

dicts = []  # contains title, tags and body as keys; for all entries


def iterate_files():
    if os.name == "nt":  # for windows
        os.chdir(os.getcwd() + "\library")
    else:  # for linux
        os.chdir("library")
    for fn in os.listdir():  # iterates through current dictionary
        if os.path.isfile(fn):  # validates 'fn' as a file
            with open(fn, "r", encoding="ISO-8859-1") as f:
                entry = {}
                entry["title"] = f.readline().replace("\n", "")
                f.readline()
                entry["body"] = f.readlines()
                dicts.append(entry)


def print_toc(toc):  # prompts table of content
    print("JAVA CODE LIBRARY".center(80, "="))
    table = []
    for i in toc:
        temp = []
        temp.append(str((toc.index(i) + 1)) + " - " + i["title"])
        table.append(temp)
    col_width = max(len(word) for row in table for word in row) - 6
    for row in table:
        print("".join(word.ljust(col_width) for word in row))
    main()


def print_entry(dict, entry):  # prompts single entry from dicts
    print("\n----------------------------------------")
    print(str(dict[entry - 1]["title"]) + "\n")
    for line in dict[entry - 1]["body"]:
        print(line.replace("\n", ""))
    print("----------------------------------------")
    print("----------------------------------------")
    main()


def main():
    try:
        entry = int(input("\nWhat would you like to read? "))
    except ValueError:
        print("You didn't type in a number. Try again!")
        print_entry(dicts)
    if entry == 0:  # print toc
        print("\n")
        print_toc(dicts)
    else:
        print_entry(dicts, entry)


iterate_files()
print_toc(dicts)
