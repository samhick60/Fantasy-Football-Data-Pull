from fileinput import close

details_file = "C:/Users/samhi/PyCharmMiscProject/Fantasy Football App/League Details.txt"
text_input_1 = input("Enter new details? (Y/N)")


def League_Details(file_path):
    x = 0
    file = open(file_path, "r")
    lines = file.readlines()
    details = {'money_league' : dict, 'friends_league' : dict, 'APLaLiga': dict }
    sep_league = dict()
    for line in lines:
        key, value = line.split(":")
        sep_league[key.strip()] = value.strip()
        if x == 3:
            details['money_league'] = sep_league
            sep_league = dict()
        elif x == 7 :
            details['friends_league'] = sep_league
            sep_league = dict()
        elif x == 11:
            details['APLaLiga'] = sep_league
            sep_league = dict()
        x = x + 1
    file.close()
    return details

print(League_Details(details_file))