import csv


def combine_files():
    manufactory_file = "manufactory.csv"
    experiment_file = "experiment.csv"
    report_file = "report.csv"

    manufactory_data = {}
    experiment_data = {}

    # Read manufactory.csv file
    with open(manufactory_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            weapon_id = row["Weapon_id"]
            manufactory_data[weapon_id] = row

    # Read experiment.csv file
    with open(experiment_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            uid = row["ID"]
            experiment_data[uid] = row

    # Merge data based on weapon ID
    merged_data = []
    for uid, experiment_row in experiment_data.items():
        weapon_id = experiment_row["Weapen"]
        merged_row = {
            "ID": experiment_row["ID"],
            "Weapen": experiment_row["Weapen"],
            "Tester": experiment_row["Tester"],
            "Damage": experiment_row["Damage"],
            "Weapon_model": manufactory_data[weapon_id]["Weapon_model"],
            "Factory": manufactory_data[weapon_id]["Factory"],
            "Staff_id": manufactory_data[weapon_id]["Staff_id"],
        }
        merged_data.append(merged_row)

    # Write merged data to report.csv file
    with open(report_file, "w", newline="") as file:
        fieldnames = [
            "ID",
            "Weapen",
            "Tester",
            "Damage",
            "Weapon_model",
            "Factory",
            "Staff_id",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(merged_data)


if __name__ == "__main__":
    combine_files()
