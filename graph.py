from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np


MY_FILE = "incident_report.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object"""

    # Open CSV File
    opened_file = open(raw_file)

    # Read CSV File
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Build a data structure to return parsed_data
    parsed_data = []

    # Skip over the first line of the file for the categories
    fields = csv_data.__next__()

    # Iterate over each row of the csv file, zip together fields --> row
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()

    return parsed_data


def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")

    # Create a dict that sums the total incidents per Category
    total_counter = Counter(item["Crime Type"] for item in data_file)

    # Create a dict that holds only the 15 most common crimes
    common_counter = dict(total_counter.most_common(15))

    # Set labels which are based on the keys of our counter
    labels = tuple(common_counter.keys())

    # Set where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, common_counter.values(), width=width)

    # Assign labels and tick lcoation to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give more room so labels won't be cut off
    plt.subplots_adjust(bottom=0.5)

    # Make the overall graph larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save graph
    plt.savefig("Type.png")

    # Close graph
    plt.clf()


if __name__ == "__main__":
    visualize_type()
