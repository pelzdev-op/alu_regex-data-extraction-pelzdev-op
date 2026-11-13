"""
ALU Regex Data Extraction and Validation
----------------------------------------
A beginner-friendly project using Python's built-in `re` module.

Run:
    python main.py

Run automated tests:
    python -m unittest discover -s tests -v
"""

import re

# Each pattern is designed for the formats specified in the assignment.
# These are practical format checks, not complete internet-standard validators.
PATTERNS = {
    "Email addresses": re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    ),
    "URLs": re.compile(
        r"https?://(?:www\.)?(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}"
        r"(?::\d{1,5})?(?:/[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]*)?",
        re.IGNORECASE,
    ),
    "Phone numbers": re.compile(
        r"(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]\d{4}"
    ),
    "Credit card numbers": re.compile(
        r"(?<!\d)(?:\d{4}[ -]){3}\d{4}(?!\d)"
    ),
    "Time": re.compile(
        r"(?<!\w)(?:(?:0?[1-9]|1[0-2]):[0-5]\d\s?[APap][Mm]|"
        r"(?:[01]?\d|2[0-3]):[0-5]\d)(?!\w)"
    ),
    "HTML tags": re.compile(
        r"</?[A-Za-z][A-Za-z0-9:-]*(?:\s+[^<>]*?)?\s*/?>"
    ),
    "Hashtags": re.compile(
        r"(?<!\w)#[A-Za-z0-9_]+"
    ),
    "Currency amounts": re.compile(
        r"(?<![\w.])\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?(?!\d)"
    ),
}

# Names users can type when asked to validate one value.
VALIDATION_OPTIONS = {
    "1": "Email addresses",
    "2": "URLs",
    "3": "Phone numbers",
    "4": "Credit card numbers",
    "5": "Time",
    "6": "HTML tags",
    "7": "Hashtags",
    "8": "Currency amounts",
}

SAMPLE_TEXT = """
Contact us at user@example.com or firstname.lastname@company.co.uk.

Visit https://www.example.com and
https://subdomain.example.org/page.

Call (123) 456-7890, 123-456-7890 or 123.456.7890.

Example card formats: 1234 5678 9012 3456 and 1234-5678-9012-3456.

The meeting starts at 14:30 or 2:30 PM.

HTML examples: <p>, <div class="example">,
<img src="image.jpg" alt="description"> and </p>.

Follow us using #example and #ThisIsAHashtag.

The prices are $19.99 and $1,234.56.
"""


def extract_data(text):
    """
    Extract every occurrence of each supported data type from text.

    Args:
        text (str): The text to search.

    Returns:
        dict: A dictionary whose keys are data types and whose values
              are lists of matches.
    """
    results = {}

    for data_type, pattern in PATTERNS.items():
        results[data_type] = pattern.findall(text)

    return results


def validate_data(data_type, value):
    """
    Validate one complete value against a selected data type.

    `fullmatch` is used so that extra characters before or after the
    value cause validation to fail.
    """
    pattern = PATTERNS.get(data_type)

    if pattern is None:
        raise ValueError(f"Unsupported data type: {data_type}")

    return pattern.fullmatch(value.strip()) is not None


def display_extraction_results(results):
    """Print extraction results in a readable format."""
    print("\n" + "=" * 60)
    print("             DATA EXTRACTION RESULTS")
    print("=" * 60)

    for data_type, matches in results.items():
        print(f"\n{data_type} ({len(matches)} found):")

        if matches:
            for item in matches:
                print(f"  - {item}")
        else:
            print("  No matches found.")

    print("\n" + "=" * 60)


def extract_from_user_text():
    """Allow the user to enter multiple lines for extraction."""
    print("\nPaste or type your text below.")
    print("When you are finished, enter a line containing only END.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    text = "\n".join(lines)
    results = extract_data(text)
    display_extraction_results(results)


def validate_user_input():
    """Display the supported types and validate a value entered by the user."""
    print("\nChoose a data type to validate:")

    for number, data_type in VALIDATION_OPTIONS.items():
        print(f"{number}. {data_type}")

    choice = input("\nEnter your choice (1-8): ").strip()
    data_type = VALIDATION_OPTIONS.get(choice)

    if data_type is None:
        print("Invalid choice. Please select a number from 1 to 8.")
        return

    value = input(f"Enter the {data_type.lower()}: ").strip()

    if validate_data(data_type, value):
        print(f"\nVALID: The value matches the expected {data_type.lower()} format.")
    else:
        print(f"\nINVALID: The value does not match the expected {data_type.lower()} format.")


def main():
    """Main menu for the application."""
    while True:
        print("\n" + "=" * 60)
        print("       ALU REGEX DATA EXTRACTION & VALIDATION")
        print("=" * 60)
        print("1. Extract data from your own text")
        print("2. Validate a single value")
        print("3. Run extraction using sample text")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            extract_from_user_text()
        elif choice == "2":
            validate_user_input()
        elif choice == "3":
            display_extraction_results(extract_data(SAMPLE_TEXT))
        elif choice == "4":
            print("\nThank you for using the Regex Data Extraction System!")
            break
        else:
            print("\nInvalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
