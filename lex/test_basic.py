# -*- coding: utf-8 -*-

import sys
import unittest
from lexner import get_named_entities, get_processed_text


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_temp_duration_expressions(self):
        print("\nUnit Testing: temporal expression - duration")
        text = "after 4 years, I got my PhD"
        result = get_named_entities(text)
        self.assertIn( (6, 7, 'TEMP_DURATION', '4 years') , result )

    def test_URI_expressions(self):
        print("\nUnit Testing: URI")
        text = "Web address: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Generic_syntax"
        result = get_named_entities(text)
        self.assertIn( (13, 72, 'URI', 'https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Generic_syntax') , result )

    def test_URI_expressions(self):
        print("\nUnit Testing: URI")
        # case 1
        text = "Web address: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Generic_syntax"
        result = get_named_entities(text)
        self.assertIn( (13, 72, 'URI', 'https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Generic_syntax') , result )
        # case 2
        text = "telnet://192.0.2.16:80/ abc-edf is another december 1998 event"
        result = get_named_entities(text)
        self.assertIn((0, 23, 'URI', 'telnet://192.0.2.16:80/'), result)

    def test_temporal_expressions_date(self):
        print("\nUnit Testing: Temporal Expressions - Date")
        text = "I paid $12.2 on 12.12.2014 for to by a DNS"
        result = get_named_entities(text)
        self.assertIn( (16, 10, 'DATETIMEDIGITAL', '12.12.2014') , result)

    def test_money_currency_expressions(self):
        print("\nUnit Testing: Email Expressions")
        text = "i created an email abc123.fun@msn.com on the mail server"
        result = get_named_entities(text)
        self.assertIn( (19, 6, 'ALPHANUM', 'abc123ddd'), result)

if __name__ == '__main__':
    unittest.main()
