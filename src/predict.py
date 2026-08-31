import re


# Keywords for each urgency level
HIGH_URGENCY_KEYWORDS = [
    "urgent",
    "immediately",
    "as soon as possible",
    "emergency",
    "critical",
    "can't access",
    "cannot access",
    "not working",
    "stopped working"
]

MEDIUM_URGENCY_KEYWORDS = [
    "soon",
    "problem",
    "issue",
    "error",
    "unable",
    "failed",
    "failure",
    "not responding"
]


def detect_urgency(text):
    """
    Detect urgency using keyword matching.
    """

    text = text.lower()

    # Check high urgency keywords first
    for keyword in HIGH_URGENCY_KEYWORDS:
        if keyword in text:
            return "High"

    # Check medium urgency keywords
    for keyword in MEDIUM_URGENCY_KEYWORDS:
        if keyword in text:
            return "Medium"

    # If no keywords match
    return "Low"


# Test the urgency detector
if __name__ == "__main__":

    test_tickets = [
        "My account is not working and I need help immediately.",
        "I have a problem with my payment.",
        "I would like to know more about this product."
    ]

    for ticket in test_tickets:
        urgency = detect_urgency(ticket)

        print("\nTicket:", ticket)
        print("Urgency:", urgency)