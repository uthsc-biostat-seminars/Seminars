# script to generate announcement in markdown. 
import os
import argparse
from datetime import datetime

# Helper to normalize time format and uppercase AM/PM
def normalize_time(time_input):
    parts = [p.strip() for p in time_input.split('-')]
    normalized = []
    for p in parts:
        if len(p) >= 2 and p[-2:].lower() in ('am', 'pm'):
            time_str = p[:-2].strip()
            mer = p[-2:].upper()
            normalized.append(f"{time_str}{mer}")
        else:
            normalized.append(p)
    return ' - '.join(normalized)


def generate_seminar_markdown(template_path=None):
    # Prompt for and parse date
    date_str = input("Enter date of presentation (YYYY-M-D): ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%A, %B %d, %Y")

    # Prompt for time and normalize
    time_input = input("Enter time of presentation [default: 2:00pm - 3:00pm]: ") or "2:00pm - 3:00pm"
    time_norm = normalize_time(time_input)

    # Prompt for other details
    speaker = input("Enter speaker name (with title): ")
    affiliation = input("Enter affiliation: ")
    title = input("Enter title of the presentation: ")
    abstract = input("Enter abstract: ")
    zoom_link = input("Enter Zoom registration link: ")
    location = input("Enter location (if any): ")

    # Optional Speaker Bio
    has_bio = input("Does the speaker have a personal web page? [Y/N]: ").strip().lower()
    if has_bio in ('y', 'yes'):
        bio_link = input("Enter HTML link for speaker's bio: ")
        bio_section = f"Speaker Bio: {bio_link}  \n\n"
    else:
        bio_link = ''
        bio_section = ''

    data = {
        'formatted_date': formatted_date,
        'time': time_norm,
        'speaker': speaker,
        'affiliation': affiliation,
        'title': title,
        'abstract': abstract,
        'zoom_link': zoom_link,
        'location': location,
        'bio_section': bio_section
    }

    # Load template
    if template_path:
        with open(template_path, 'r') as f:
            template = f.read()
    else:
        template = """The Division of Biostatistics of the Department of Preventive Medicine, UTHSC, invites you to attend the following seminar.  \n
Time: {formatted_date}, {time} CT  \n
ZOOM Virtual Room Connection: [Register in advance for this meeting to get the Zoom Link]({zoom_link})  \n
Seminar Website: https://uthsc.edu/preventive-medicine/events.php  \n
{bio_section}{title}  \n
{speaker}  \n
{affiliation}  \n
{abstract}  \n
Location: {location}
"""

    # Generate the output markdown filename
    safe_name = speaker.replace(' ', '_').replace('.', '')
    output_filename = f"{date_str}_{safe_name}.md"

    with open(output_filename, 'w') as f:
        f.write(template.format(**data))

    print(f"Markdown file generated: {output_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate seminar markdown file.")
    parser.add_argument('--template', help='Path to custom markdown template file', default=None)
    args = parser.parse_args()
    generate_seminar_markdown(args.template)
