# 
import pandas as pd
import os
import sys

def prompt_seminar_details():
    """Prompt the user for seminar details and return as a dict."""
    date = input("Enter date of presentation (YYYY-MM-DD): ")
    speaker = input("Enter speaker name (with title): ")
    affiliation = input("Enter affiliation: ")
    title = input("Enter title of the presentation: ")
    abstract = input("Enter abstract: ")
    return {
        'Date': date,
        'Speaker': speaker,
        'Affiliation': affiliation,
        'Title': title,
        'Abstract': abstract
    }


def confirm_details(details):
    """Display entered details and ask for confirmation."""
    print("\nPlease confirm the entered details:")
    for key, value in details.items():
        print(f"{key}: {value}")
    while True:
        choice = input("Is this correct? [Y]es/[N]o/[C]ancel: ").strip().lower()
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        if choice in ('c', 'cancel'):
            print("Operation cancelled. No changes made.")
            sys.exit(0)
        print("Please enter Y, N, or C.")


def add_upcoming_seminar():
    """Collect, confirm, and append seminar details to the TSV file."""
    while True:
        details = prompt_seminar_details()
        if confirm_details(details):
            break
        print("Let's re-enter the details.\n")

    df = pd.DataFrame([details])
    file_path = "test.tsv"

    # Append to the TSV, writing header only if file does not exist
    if not os.path.isfile(file_path):
        df.to_csv(file_path, sep='\t', index=False)
    else:
        df.to_csv(file_path, sep='\t', index=False, header=False, mode='a')

    print("Entry added to upcoming_seminars.tsv.")


if __name__ == "__main__":
    add_upcoming_seminar()