#!/usr/bin/env python3


required_fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
temp_required_fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

passports = []
valid_passports = []

with open("input_0401") as input:
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

print(len(valid_passports))