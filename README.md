# US Bikeshare Data Exploration

## Project Overview

This project is an interactive Python script designed to explore bikeshare data for three major US cities: Chicago, New York City, and Washington. Users can filter the data by month, day of the week, or both, to analyze various statistics related to bikeshare usage.

## Features

The script provides the following statistical insights based on user-selected filters:

* **Time Statistics:**
    * Most common month for bikeshare travel.
    * Most common day of the week for bikeshare travel.
    * Most common start hour for bikeshare travel.
* **Station Statistics:**
    * Most commonly used start station.
    * Most commonly used end station.
    * Most frequent combination of start and end stations for trips.
* **Trip Duration Statistics:**
    * Total travel time.
    * Average travel time.
* **User Statistics:**
    * Counts of different user types (e.g., "Subscriber", "Customer").
    * Counts of gender (where available in the dataset).
    * Earliest, most recent, and most common year of birth (where available in the dataset).
* **Raw Data Display:** Option to view raw data rows (5 at a time) upon request during execution.

## How to Run

### Prerequisites

* Python 3.x
* `pandas` library
* `numpy` library

You can install the required Python libraries using pip:
```bash
pip install pandas numpy

## How to Contribute

Contributions are welcome! If you find any issues or have suggestions for improvements,
please feel free to open an issue or submit a pull request on the GitHub repository.
