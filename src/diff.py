def get_added_officers(stale_companies_data, fresh_companies_data):
    added_officers = []

    for fresh_company in fresh_companies_data['companies']:
        fresh_company_found_in_stale_data = False

        for stale_company in stale_companies_data['companies']:
            if fresh_company['company_name'] == stale_company['company_name']:
                fresh_company_found_in_stale_data = True

                for fresh_active_officer in fresh_company['active_officers']:
                    fresh_officer_found_in_stale_data = False

                    for stale_active_officer in stale_company['active_officers']:
                        if fresh_active_officer == stale_active_officer:
                            fresh_officer_found_in_stale_data = True

                    if not fresh_officer_found_in_stale_data:
                        added_officers.append({"company_name": fresh_company['company_name'],
                                               "officer_name": fresh_active_officer['name']})

        if not fresh_company_found_in_stale_data:
            print("INFO: company {} not found in old data".format(fresh_company['company_name']))
            print("This means the company '{}' is new (has been added to the excel file).".format(
                fresh_company['company_name']))

    return added_officers


def get_removed_officers(stale_companies_data, fresh_companies_data):
    removed_officers = []
    for stale_company in stale_companies_data['companies']:
        stale_company_found_in_fresh_data = False

        for fresh_company in fresh_companies_data['companies']:
            if fresh_company['company_name'] == stale_company['company_name']:
                stale_company_found_in_fresh_data = True

                for stale_active_officer in stale_company['active_officers']:
                    stale_officer_found_in_fresh_data = False

                    for fresh_active_officer in fresh_company['active_officers']:
                        if fresh_active_officer == stale_active_officer:
                            stale_officer_found_in_fresh_data = True

                    if not stale_officer_found_in_fresh_data:
                        removed_officers.append({"company_name": fresh_company['company_name'],
                                                 "officer_name": stale_active_officer['name']})

        if not stale_company_found_in_fresh_data:
            print("INFO: company {} not found in new data".format(fresh_company['company_name']))
            print("This means the company '{}' has been removed from the excel file.".format(
                fresh_company['company_name']))

    return removed_officers
