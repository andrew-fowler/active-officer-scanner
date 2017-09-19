import csv


def get_company_ids_from_csv(filename):
    company_ids = []
    with open(filename, "rt", encoding='ISO-8859-1') as file:
        reader = csv.reader(file)
        for row in reader:
            company_ids.append(row[1])

    return company_ids




