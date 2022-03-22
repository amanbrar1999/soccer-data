import re
import os

if os.path.exists("capology_formatted_l1.json"):
  os.remove("capology_formatted_l1.json")

with open('capology_formatted_l1.json', 'a') as new_file:
    file = open("capology_l1.txt", "r").readlines()

    accounting = re.compile('accounting\.formatMoney\(\"(.*)\", \"(.*)\", 0\)')
    accounting_weekly = re.compile('accounting\.formatMoney\(\"(.*)\"\/52, \"(.*)\", 0\)')
    field_regex = re.compile('\'(.*)\':')
    math_round_regex = re.compile('Math.round\(\"(.*)\"\)')
    end_regex = re.compile('},]')
    name_value_regex = re.compile('<a.*>(.*)<\/a>')

    for line in file:
        newline = line
        if 'expiration' in line or 'verified' in line:
            continue
        if accounting.search(line):
            field = field_regex.search(line).group(1)
            newline = f'"{field}": {accounting.search(line).group(1)},\n'
        elif accounting_weekly.search(line):
            field = field_regex.search(line).group(1)
            newline = f'"{field}": {int(accounting_weekly.search(line).group(1))/52},\n'
        elif math_round_regex.search(line):
            field = field_regex.search(line).group(1)
            newline = f'"{field}": {math_round_regex.search(line).group(1)},\n'
        elif field_regex.search(line):
            field = field_regex.search(line).group(1)
            value = line.split(":")[1]
            if field == "name" or field == "club":
                value = f'"{name_value_regex.search(value).group(1)}",\n'
            if field == "club":
                value = value[:-2] + value[-1]
            newline = f'"{field}": {value}'
        elif end_regex.search(line):
            newline = "}]"
        new_file.write(newline)
    
