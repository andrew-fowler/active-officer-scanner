import json

import chwrapper
from requests import HTTPError

from src import config
from src.excel_handling import get_company_ids_from_csv
from src.support import file_exists, get_json_from_file, file_is_older_than_an_hour


def get_stale_company_data():
    if file_exists(config.data_filepath):
        return get_json_from_file(config.data_filepath)
    else:
        raise IOError("No existing company data found in: {}".format(config.data_filepath))


def get_fresh_company_data():
    if file_exists(config.data_cache_filepath) and not file_is_older_than_an_hour(config.data_cache_filepath):
        return get_json_from_file(config.data_cache_filepath)

    companies_data = {'companies': []}
    company_ids = get_company_ids_from_input_file()

    searcher = chwrapper.Search(access_token=config.get_access_token())
    # searcher = chwrapper.Search(access_token=config.access_token)

    for company_id in company_ids:
        company_name = None
        officers_response = None
        try:
            company_name = searcher.profile(company_id).json()['company_name']
        except HTTPError as e:
            print("ERROR: Exception thrown when querying API: {}".format(e))
            exit(1)

        try:
            officers_response = searcher.officers(company_id)
        except HTTPError as e:
            print("ERROR: Exception thrown when querying API: {}".format(e))
            exit(1)

        officers_json = officers_response.json()
        officers = officers_json['items']

        active_officer_records = get_active_officer_records(officers)

        company_record = {'company_name': company_name, 'active_officers': active_officer_records}
        companies_data['companies'].append(company_record)

    with open(config.data_cache_filepath, 'w') as outfile:
        json.dump(companies_data, outfile)

    return companies_data


def get_company_ids_from_input_file():
    return get_company_ids_from_csv("resources/Companies House Numbers.csv")


def get_active_officer_records(officers):
    active_officers = []
    for officer in officers:
        if officer.get('resigned_on') is None:
            active_officers.append({"name": officer['name']})

    return active_officers
