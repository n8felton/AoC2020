#!/usr/bin/env python3
import re

required_fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
temp_required_fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

passports = []
valid_passports = []

with open("input_0402") as input:
    passport = []
    for line in input:
        if not line.strip():
            passports.append(passport)
            passport = []
        else:
            _line = line.replace("\n", " ").split()
            passport.extend(_line)
    else:
        passports.append(passport)

for passport in passports:
    fields = []
    for field in passport:
        fields.append(field.split(":")[0])
    fields.sort()
    if fields == temp_required_fields or fields == required_fields:
        valid_passports.append(passport)

valid_data_passports = []

for valid_passport in valid_passports:
    for data in valid_passport:
        field = data.split(":")[0]
        value = data.split(":")[1]
        if field == "byr":
            if int(value) not in range(1920, 2002 + 1):
                break
        if field == "iyr":
            if int(value) not in range(2010, 2020 + 1):
                break
        if field == "eyr":
            if int(value) not in range(2020, 2030 + 1):
                break
        if field == "hgt":
            units = ["cm", "in"]
            if not any([unit in value for unit in units]):
                break
            else:
                height, unit = re.findall(r"(\d+)(cm|in)", value)[0]
                if unit == "cm":
                    if int(height) not in range(150, 193 + 1):
                        break
                if unit == "in":
                    if int(height) not in range(59, 76 + 1):
                        break
        if field == "hcl":
            regex = "#[0-9a-f]{6}"
            match = re.match(regex, value)
            if not match:
                break
        if field == "ecl":
            valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if value not in valid_ecl:
                break
        if field == "pid":
            regex = r"^\d{9}$"
            match = re.match(regex, value)
            if not match:
                break
    else:
        valid_data_passports.append(valid_passport)

print(len(valid_data_passports))