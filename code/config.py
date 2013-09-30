import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = SCRIPT_DIR+"/../data"

ALL_GTFS_PATHS = {	 "ACTransit": SCRIPT_DIR+"/../data/actransit"}

# Census
CENSUS_API_KEY = "4b415bf262765d14f4c2f534ce3b5f0a4237d980"
MEDIAN_INCOME_TABLE_NAME = 'B19013_001E'

# Skip some MUNI bus routes
MUNI_ALLOWED_ROUTE_SHORT_NAMES = ["49", "30", "38", "22", "1", "14", "5", "9", "47", "31", "8X", "19"]
