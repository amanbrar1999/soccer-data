import csv

with open('s19-20-defensive-stats.csv', 'r') as defensive_stats:
    with open('s19-20-defensive-stats-formatted.csv', 'w') as defensive_state_formatted:
        reader = csv.reader(defensive_stats)
        writer = csv.writer(defensive_state_formatted)
        new_columns = []
        i = 0
        for row in reader:
            if i > 1:
                writer.writerow(row)
            elif i == 0:
                new_columns = row
            elif i == 1:
                for i, elem in enumerate(row):
                    if len(new_columns[i]) > 0:
                        new_columns[i] += " " + elem
                    else:
                       new_columns[i] = elem 
                writer.writerow(new_columns)
            i += 1

with open('s19-20-goalie-stats.csv', 'r') as goalie_stats:
    with open('s19-20-goalie-stats-formatted.csv', 'w') as goalie_state_formatted:
        reader = csv.reader(goalie_stats)
        writer = csv.writer(goalie_state_formatted)
        new_columns = []
        i = 0
        for row in reader:
            if i > 1:
                writer.writerow(row)
            elif i == 0:
                new_columns = row
            elif i == 1:
                for i, elem in enumerate(row):
                    if len(new_columns[i]) > 0:
                        new_columns[i] += " " + elem
                    else:
                       new_columns[i] = elem 
                writer.writerow(new_columns)
            i += 1

with open('s19-20-passing-stats.csv', 'r') as passing_stats:
    with open('s19-20-passing-stats-formatted.csv', 'w') as passing_state_formatted:
        reader = csv.reader(passing_stats)
        writer = csv.writer(passing_state_formatted)
        new_columns = []
        i = 0
        for row in reader:
            if i > 1:
                writer.writerow(row)
            elif i == 0:
                new_columns = row
            elif i == 1:
                for i, elem in enumerate(row):
                    if len(new_columns[i]) > 0:
                        new_columns[i] += " " + elem
                    else:
                       new_columns[i] = elem 
                writer.writerow(new_columns)
            i += 1

with open('s19-20-standard-stats.csv', 'r') as standard_stats:
    with open('s19-20-standard-stats-formatted.csv', 'w') as standard_state_formatted:
        reader = csv.reader(standard_stats)
        writer = csv.writer(standard_state_formatted)
        new_columns = []
        i = 0
        for row in reader:
            if i > 1:
                writer.writerow(row)
            elif i == 0:
                new_columns = row
            elif i == 1:
                for i, elem in enumerate(row):
                    if len(new_columns[i]) > 0:
                        new_columns[i] += " " + elem
                    else:
                       new_columns[i] = elem 
                writer.writerow(new_columns)
            i += 1