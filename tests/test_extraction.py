import unittest

from main import PATTERNS, extract_data, validate_data


class TestRegexDataExtraction(unittest.TestCase):

    def test_email_extraction(self):
        text = "Email user@example.com and firstname.lastname@company.co.uk"
        self.assertEqual(
            extract_data(text)["Email addresses"],
            ["user@example.com", "firstname.lastname@company.co.uk"],
        )

    def test_url_extraction(self):
        text = "Visit https://www.example.com and https://subdomain.example.org/page"
        self.assertEqual(
            extract_data(text)["URLs"],
            ["https://www.example.com", "https://subdomain.example.org/page"],
        )

    def test_phone_extraction(self):
        text = "(123) 456-7890, 123-456-7890, 123.456.7890"
        self.assertEqual(
            extract_data(text)["Phone numbers"],
            ["(123) 456-7890", "123-456-7890", "123.456.7890"],
        )

    def test_credit_card_extraction(self):
        text = "1234 5678 9012 3456 and 1234-5678-9012-3456"
        self.assertEqual(
            extract_data(text)["Credit card numbers"],
            ["1234 5678 9012 3456", "1234-5678-9012-3456"],
        )

    def test_time_extraction(self):
        text = "Meet at 14:30 or 2:30 PM"
        self.assertEqual(extract_data(text)["Time"], ["14:30", "2:30 PM"])

    def test_html_extraction(self):
        text = '<p>Text</p> <div class="example"> <img src="image.jpg" alt="description">'
        self.assertEqual(
            extract_data(text)["HTML tags"],
            ["<p>", "</p>", '<div class="example">', '<img src="image.jpg" alt="description">'],
        )

    def test_hashtag_extraction(self):
        text = "Use #example and #ThisIsAHashtag"
        self.assertEqual(
            extract_data(text)["Hashtags"],
            ["#example", "#ThisIsAHashtag"],
        )

    def test_currency_extraction(self):
        text = "Prices: $19.99 and $1,234.56"
        self.assertEqual(
            extract_data(text)["Currency amounts"],
            ["$19.99", "$1,234.56"],
        )

    def test_valid_email(self):
        self.assertTrue(validate_data("Email addresses", "user@example.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_data("Email addresses", "userexample.com"))

    def test_valid_time(self):
        self.assertTrue(validate_data("Time", "14:30"))
        self.assertTrue(validate_data("Time", "2:30 PM"))

    def test_invalid_time(self):
        self.assertFalse(validate_data("Time", "25:70"))
        self.assertFalse(validate_data("Time", "13:30 PM"))

    def test_valid_phone(self):
        self.assertTrue(validate_data("Phone numbers", "(123) 456-7890"))

    def test_invalid_phone(self):
        self.assertFalse(validate_data("Phone numbers", "1234567890"))

    def test_all_eight_patterns_exist(self):
        self.assertEqual(len(PATTERNS), 8)


if __name__ == "__main__":
    unittest.main()
