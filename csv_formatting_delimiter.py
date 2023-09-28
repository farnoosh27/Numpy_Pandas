## sometimes you need to change the delimiter in your work
import csv

input_file = ''  # Replace with your input file path
output_file = ''  # Replace with your output file path

# Reading the CSV file and writing it with a new delimiter
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=';')
    
    for row in reader:
        writer.writerow(row)

print(f"The CSV file has been converted and saved with ';' as the delimiter as '{output_file}'")
