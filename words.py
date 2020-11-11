import StringIO
import csv

a_list_from_csv_file = [['for', 'bar'], [1, 2]]
out_fd = StringIO.StringIO()
writer = csv.writer(out_fd, delimiter='|')
for row in a_list_from_csv_file:
    writer.writerow(row)
print out_fd.getvalue()