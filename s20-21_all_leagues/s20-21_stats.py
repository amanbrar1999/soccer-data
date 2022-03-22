import csv

with open('ps-passing-stats.csv', 'r') as league_stats:
    with open('ps-passing-stats-formatted.csv', 'w') as league_state_formatted:
        reader = csv.reader(league_stats)
        writer = csv.writer(league_state_formatted)
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