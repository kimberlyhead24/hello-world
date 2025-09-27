import csv


def combine_files():
    manufactory_data = {}
    with open('manufactory.csv', newline='') as manuf_file:
        reader = csv.DictReader(manuf_file)
        for row in reader:
            manufactory_data[row['Weapon_id']] = {
                'Weapon_model': row['Weapon_model'],
                'Factory': row['Factory'],
                'Staff_id': row['Staff_id']
            }

    combined_rows = []
    with open('experiment.csv', newline='') as exp_file:
        reader = csv.DictReader(exp_file)
        for row in reader:
            weapon_id = row['Weapen']
            # Combine only if weapon exists in manufactory
            if weapon_id in manufactory_data:
                # Merge dictionaries
                combined_row = {
                    'ID': row['ID'],
                    'Weapen': row['Weapen'],
                    'Tester': row['Tester'],
                    'Damage': row['Damage'],
                    'Weapon_model': manufactory_data[weapon_id]['Weapon_model'],
                    'Factory': manufactory_data[weapon_id]['Factory'],
                    'Staff_id': manufactory_data[weapon_id]['Staff_id']
                }
                combined_rows.append(combined_row)

    # Sort by ID (convert to int for numeric sort if needed)
    combined_rows.sort(key=lambda x: int(x['ID']))

    with open('report.csv', 'w', newline='') as report_file:
        fieldnames = ['ID', 'Weapen', 'Tester', 'Damage', 'Weapon_model', 'Factory', 'Staff_id']
        writer = csv.DictWriter(report_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(combined_rows)

    pass


if __name__ == "__main__":
    combine_files()
