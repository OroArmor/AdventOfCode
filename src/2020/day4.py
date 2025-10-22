import util

test_data: [str] = \
    """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split("\n\n")


def task1(data: [str]):
    valid: int = 0
    for passport in data:
        passport_fields: [str] = passport.replace("\n", " ").split(" ")

        if len(passport_fields) == 8:
            valid += 1
            continue

        if len(passport_fields) == 7:
            has_cid = False
            for field in passport_fields:
                if field.count("cid") >= 1:
                    has_cid = True

            if not has_cid:
                valid += 1


    return valid


def task2(data: [str]):
    valid: int = 0
    for passport in data:
        passport_fields: [str] = passport.replace("\n", " ").split(" ")

        valid_fields = 0
        for field in passport_fields:
            contents = field.split(":")
            if contents[0] == "byr":
                if 1920 <= int(contents[1]) <= 2002:
                    valid_fields += 1

            if contents[0] == "iyr":
                if 2010 <= int(contents[1]) <= 2020:
                    valid_fields += 1

            if contents[0] == "eyr":
                if 2020 <= int(contents[1]) <= 2030:
                    valid_fields += 1

            if contents[0] == "hgt":
                if contents[1].endswith("cm"):
                    if 150 <= int(contents[1][:-2]) <= 193:
                        valid_fields += 1
                if contents[1].endswith("in"):
                    if 59 <= int(contents[1][:-2]) <= 76:
                        valid_fields += 1

            if contents[0] == "hcl":
                if contents[1][0] == "#":
                    try:
                        int(contents[1][1:], 16)
                        valid_fields += 1
                    except:
                        a = "a"
                        # nothing

            if contents[0] == "ecl":
                if "amb blu brn gry grn hzl oth".count(contents[1]) == 1:
                    valid_fields += 1

            if contents[0] == "pid":
                if len(contents[1]) == 9 and contents[1].isnumeric():
                    valid_fields += 1

        if valid_fields == 7:
            valid += 1

    return valid


def parse(data):
    return util.as_double_lines(data)

def main():
    data = util.get(4, 2020)
    # data = test_data
    data = parse(data)
    print(task1(data))
    print(task2(data))


if __name__ == "__main__":
    main()
