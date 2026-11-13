# ALU Regex Data Extraction and Validation

## Project overview

This project uses Python's built-in `re` (regular expressions) module to extract and validate eight types of data from text:

1. Email addresses
2. URLs
3. Phone numbers
4. Credit card number formats
5. Time (12-hour and 24-hour formats)
6. HTML tags
7. Hashtags
8. Currency amounts

The application provides two main capabilities:

- **Data extraction:** Finds all supported matches in a block of text.
- **Field validation:** Checks whether a complete input matches a selected format.

## Technologies

- Python 3
- Python `re` module
- Python `unittest` module

No third-party packages are required.

## Project structure

```text
alu_regex-data-extraction/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── tests/
    ├── __init__.py
    └── test_extraction.py
```

## How to run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

Choose an option from the menu:

- `1` extracts data from text you enter. Type `END` on a separate line when finished.
- `2` validates one value.
- `3` runs extraction on the built-in sample text.
- `4` exits the application.

## How to run the tests

From the project root, run:

```bash
python -m unittest discover -s tests -v
```

The tests check that each pattern extracts the examples and that selected valid and invalid inputs are handled correctly.

## Regular expression patterns

| Data type | Pattern |
|---|---|
| Email | `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b` |
| URL | `https?://(?:www\.)?(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?::\d{1,5})?(?:/[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]*)?` |
| Phone | `(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]\d{4}` |
| Credit card format | `(?<!\d)(?:\d{4}[ -]){3}\d{4}(?!\d)` |
| Time | `(?<!\w)(?:(?:[01]?\d|2[0-3]):[0-5]\d|(?:0?[1-9]|1[0-2]):[0-5]\d\s?[APap][Mm])(?!\w)` |
| HTML tag | `</?[A-Za-z][A-Za-z0-9:-]*(?:\s+[^<>]*?)?\s*/?>` |
| Hashtag | `(?<!\w)#[A-Za-z0-9_]+` |
| Currency | `(?<![\w.])\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?(?!\d)` |

## Important notes and limitations

- These patterns are designed for the assignment's example formats. They are not complete validators for every possible email address, URL, phone-number numbering plan, HTML document, or currency convention.
- The credit-card pattern checks the requested grouping and separators only. It does not verify a card issuer, card length rules beyond the example, or the Luhn checksum.
- The HTML pattern finds tag-shaped strings; it does not parse or validate HTML structure.
- The phone pattern supports the three formats shown in the assignment.
- The currency pattern supports dollar amounts with optional two-decimal cents and correctly grouped thousands, as in the examples.
- Extraction and validation are different: `findall()` searches within a larger text, while `fullmatch()` checks that the entire field contains one matching value.

## Author

Name: Oluwasemilore Ademo  
ALU Email: o.ademo@alustudent.com
GitHub: pelzdev-op
