import csv

with open('pl-stats.csv', 'r') as pl_stats:
    with open('pl-stats-formatted.csv', 'w') as pl_state_formatted:
        reader = csv.reader(pl_stats)
        writer = csv.writer(pl_state_formatted)
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
