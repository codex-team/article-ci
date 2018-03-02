from flask import request

import main
import unittest


class MainTestCase(unittest.TestCase):

    def test_appid_is_set(self):
        assert len(main.APP_ID) == 32

    def test_parse_error(self):
        assert main.parse_weather([]) == 'Data error: list indices must be integers or slices, not str'

    def test_convert_temperature(self):
        assert main.parse_weather({'main': {'temp': '300'}}) == 'The temperature is: 26.9°'
        assert main.parse_weather({'main': {'temp': '273.15'}}) == 'The temperature is: 0.0°'

    def test_request(self):
        with main.app.test_client() as c:
            rv = c.get('/?city=Moscow')
            assert request.args['city'] == 'Moscow'
            assert rv.status_code == 200

if __name__ == '__main__':
    unittest.main()