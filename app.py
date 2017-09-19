# List of company numbers
# Grab officers for each company
# Create a file of all officers
# Be able to re-run, compare to original, calling out changes
# Update data with new data
import json

from src.data_handling import get_fresh_company_data, get_stale_company_data
from src.diff import get_added_officers, get_removed_officers

fresh_companies_data = get_fresh_company_data()
stale_companies_data = get_stale_company_data()

added_officers = get_added_officers(stale_companies_data, fresh_companies_data)
removed_officers = get_removed_officers(stale_companies_data, fresh_companies_data)

for officer in added_officers:
    print("{0} added {1}".format(officer['company_name'], officer['officer_name']))

for officer in removed_officers:
    print("{0} removed {1}".format(officer['company_name'], officer['officer_name']))

if len(added_officers) == 0 and len(removed_officers) == 0:
    print("No changes were found in active officers")

# Write new data file
filename = "data/fresh_data.json"
with open(filename, 'w') as outfile:
    json.dump(fresh_companies_data, outfile)
