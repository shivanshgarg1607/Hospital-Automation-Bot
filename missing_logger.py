from pathlib import Path
import csv


LOG_FILE = Path("missing_hospitals.csv")


def log_missing_hospital(name, reason):

    file_exists = LOG_FILE.exists()

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Hospital Name", "Reason"])

        writer.writerow([name, reason])

    print(f"Logged: {name}")    