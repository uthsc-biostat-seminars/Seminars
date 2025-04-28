# script to generate announcement in HTML.
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


def generate_seminar_html(template_path=None):
    # Prompt for and parse date
    date_str = input("Enter date of presentation (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%A, %B %d, %Y")

    # Prompt for time and normalize
    time_input = input("Enter time of presentation [default: 2:00pm - 3:00pm]: ") or "2:00pm - 3:00pm"
    time_norm = normalize_time(time_input)

    # Prompt for other details
    zoom_link = input("Enter Zoom registration link: ")
    seminar_site = input("Enter seminar website URL: ")
    title = input("Enter title of the presentation: ")
    speaker = input("Enter speaker name (with title): ")
    affiliation = input("Enter affiliation: ")
    abstract = input("Enter abstract: ")

    # Optional Speaker Bio
    has_bio = input("Does the speaker have a personal web page? [Y/N]: ").strip().lower()
    if has_bio in ('y', 'yes'):
        bio_link = input("Enter speaker bio URL: ")
        bio_section = f"<p><strong>Speaker Bio:</strong> <a href=\"{bio_link}\" target=\"_blank\" rel=\"noopener\">{bio_link}</a></p>\n"
    else:
        bio_section = ''

    # Combine date and time into one block
    date_time_block = f"{formatted_date}, {time_norm} CT"

    data = {
        'date_time_block': date_time_block,
        'zoom_link': zoom_link,
        'seminar_site': seminar_site,
        'title': title,
        'speaker': speaker,
        'affiliation': affiliation,
        'abstract': abstract,
        'bio_section': bio_section
    }

    # Load HTML template
    if template_path:
        with open(template_path, 'r') as f:
            template = f.read()
    else:
        template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Seminar Announcement</title>
</head>
<body>
    <p>The Division of Biostatistics of the Department of Preventive Medicine, UTHSC, invites you to attend the following seminar.</p>
    <p>&nbsp;</p>
    <p><strong>Time:</strong> {date_time_block}</p>
    <p><strong>ZOOM Virtual Room Connection:</strong> <strong><u><a href="{zoom_link}" target="_blank" rel="noopener">Register in advance for this meeting to get the Zoom Link</a></u></strong></p>
    <p><strong>Seminar Website:</strong> <strong><u><a href="{seminar_site}" target="_blank" rel="noopener">{seminar_site}</a></u></strong></p>
    {bio_section}
    <p>&nbsp;</p>
    <p style="text-align: center;"><strong>{title}</strong></p>
    <p style="text-align: center;">{speaker}</p>
    <p style="text-align: center;">{affiliation}</p>
    <p>&nbsp;</p>
    <p>{abstract}</p>
</body>
</html>
"""

    # Generate safe filename
    safe_name = speaker.replace(' ', '_').replace('.', '')
    output_filename = f"{date_str}_{safe_name}.html"

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(template.format(**data))

    print(f"HTML file generated: {output_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate seminar HTML announcement.")
    parser.add_argument('--template', help='Path to custom HTML template file', default=None)
    args = parser.parse_args()
    generate_seminar_html(args.template)
	