#!/usr/bin/python3
"""Module for generating personalized invitation files from a template."""
import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """Generate invitation files based on a template and attendee data."""
    if not isinstance(template, str):
        logging.error("Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        logging.error("Attendees must be a list of dictionaries.")
        return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in ("name", "event_title", "event_date", "event_location"):
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        with open(filename, "w") as f:
            f.write(content)
