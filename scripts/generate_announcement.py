import os
import argparse

def generate_seminar_markdown(template_path=None):
    # Prompt user for seminar details
    date = input("Enter date of presentation (YYYY-M-D): ")
    time = input("Enter time of presentation [default: 2:00 PM-3:00 PM CT]: ") or "2:00 PM-3:00 PM CT"
    speaker = input("Enter speaker name (with title): ")
    affiliation = input("Enter affiliation: ")
    title = input("Enter title of the presentation: ")
    abstract = input("Enter abstract: ")
    zoom_link = input("Enter Zoom registration link: ")
    location = input("Enter location (if any): ")
    bio_link = input("Enter HTML link for speaker's bio: ")

    data = {
        'date': date,
        'time': time,
        'speaker': speaker,
        'affiliation': affiliation,
        'title': title,
        'abstract': abstract,
        'zoom_link': zoom_link,
        'location': location,
        'bio_link': bio_link
    }

    # Load template from file if provided, else use the official UTHSC seminar template
    if template_path:
        with open(template_path, 'r') as f:
            template = f.read()
    else:
        template = """The Division of Biostatistics of the Department of Preventive Medicine, UTHSC, invites you to attend the following seminar.  

Time: {date}, {time} CT  

ZOOM Virtual Room Connection: [Register in advance for this meeting to get the Zoom Link]({zoom_link})  

Seminar Website: https://uthsc.edu/preventive-medicine/events.php  

Speaker Bio: {bio_link}  



{title}  

{speaker}  

{affiliation}  



{abstract}
"""

    # Generate the output markdown filename
    safe_name = speaker.replace(' ', '_').replace('.', '')
    output_filename = f"{date}_{safe_name}.md"

    # Write the filled template to the file
    with open(output_filename, 'w') as f:
        f.write(template.format(**data))

    print(f"Markdown file generated: {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate seminar markdown file.")
    parser.add_argument('--template', help='Path to custom markdown template file', default=None)
    args = parser.parse_args()
    generate_seminar_markdown(args.template)