from io import IOBase
from os.path import exists, splitext
import inspect
import json


class Json(object):
    """ Json utilities container """

    def __init__(self, json_input):
        self.__input = json_input
        self.__dictionary = dict()
        self.__text = str()
        self.__type = str
        self.__parse()

    def __is_json_file(self):
        """ Check if json file """
        if str(self.__input).endswith('.json'):
            return True
        return False

    def __parse_dict(self):
        print("Parsing json from python dictionary input")
        self.__dictionary = self.__input
        self.__text = json.dumps(self.__input)
        self.__type = dict
        return 1

    def __parse_file(self):
        print("Parsing json from file: " + self.__input)

        if not exists(self.__input):
            raise Exception('JSON file not found: ' + self.__input)

        with open(self.__input) as file_obj:
            content = file_obj.read()

        self.__type = IOBase
        self.__parse_content(content)

    def __parse_string(self):
        print("Parsing json from string input")
        self.__parse_content(self.__input)

    def __parse_content(self, content):
        if not content:
            return 0

        self.__dictionary = json.loads(content)
        self.__text = json.dumps(self.__dictionary)
        return 1

    def __parse(self):
        """ Parse the given json string or file """
        if self.__type == dict:
            return self.__parse_dict()
        elif self.__is_json_file():
            return self.__parse_file()
        else:
            return self.__parse_string()

    def __formatted_string(self, sort=False, indents=4):
        if self.__type == dict:
            return json.dumps({k: v for k, v in self.__input.items()}, sort_keys=sort, indent=indents)

        return json.dumps(self.__dictionary, sort_keys=sort, indent=indents)

    def __assert_type(self, check_type):
        cur_frame = inspect.currentframe()
        cal_frame = inspect.getouterframes(cur_frame, 2)
        method_name = cal_frame[1][3]
        json_txt = self.__text.strip()
        start_char = json_txt[0]

        if check_type == dict and start_char == '[':
            print('Library method "{}.{}()" not supported for array of json objects'
                  .format(self.__class__.__name__, method_name))
            return 0

        if check_type == list and start_char == '{':
            print('Library method "{}.{}()" not supported for dictionary type json objects'
                  .format(self.__class__.__name__, method_name))
            return 0

        return 1

    @staticmethod
    def __file_name(filename):
        if '.' in filename:
            return splitext(filename)[0] + '.json'

        if not filename.endswith('.json'):
            return filename + '.json'

        return filename

    # Dictionary type json public APIs
    @property
    def dictionary(self):
        return self.content(string_format=False)

    @property
    def text(self):
        return self.__text

    @property
    def type(self):
        return self.__type

    def content(self, string_format=True):
        """
        Get json content as plain string or dictionary

        @param      string_format   Flag to format as string
        @return                     json string (flag on), json dictionary (flag off)
        """
        if not self.__assert_type(dict):
            return ''
        return str(self.__dictionary) if string_format else self.__dictionary

    def print(self, sort=False, indents=4):
        """
        Print formatted json content

        @param      indents     Number of spaces to indent
        @param      sort        Flag to sort keys
        @return                 (None)
        """
        print(self.__formatted_string(sort, indents))

    def write_file(self, filename, sort=False, indents=4):
        """
        Write formatted json content in to file

        @param      filename    Output file name
        @param      sort        Flag to sort keys
        @param      indents     Number of spaces to indent
        @return                 1 (success), Exception (fail)
        """
        content = self.__formatted_string(sort, indents)
        filename = self.__file_name(filename)

        with open(filename, 'w') as file_obj:
            file_obj.write(content)

        print('Written JSON content to file: ' + filename)
        return 1

    def get_keys(self):
        """
        Returns list of keys associated with the json content

        @return     key_list    List of all keys
        """
        if not self.__assert_type(dict):
            return []
        return list(self.__dictionary.keys())

    def get_values(self):
        """
        Returns list of values associated with the all keys in json

        @return     value_list    List of all values
        """
        if not self.__assert_type(dict):
            return []
        return list(self.__dictionary.values())

    def get_items(self):
        """
        Returns a list of tuple of key and value pairs associated with json file

        @return     items_list  Tuple of all items
        """
        if not self.__assert_type(dict):
            return []
        return list(self.__dictionary.items())

    def get(self, key):
        """
        Return value of json key

        @param      key     JSON Key
        @return     value   Value associated with json key (if exists), None (if not exists)
        """
        if not self.__assert_type(dict):
            return None
        return self.__dictionary.get(key)

    # Array type json public APIs
    def get_element_at_index(self, index):
        if not self.__assert_type(list):
            return None

        contents = self.__dictionary
        max_index = self.num_elements - 1

        if index > max_index or index < 0:
            print('Index must be in range: 0 - {}. Got index: {}'.format(max_index, index))
            return None

        return contents[index]

    def get_elements(self):
        if not self.__assert_type(list):
            return []
        return self.__dictionary

    @property
    def num_elements(self):
        if not self.__assert_type(list):
            return 0
        return len(self.__dictionary)

    @staticmethod
    def is_valid(json_string):
        try:
            json.loads(json_string)
        except ValueError:
            print("Json string is invalid!")
            return False

        return True

    def __str__(self):
        return self.__formatted_string(sort=False, indents=4)

    def __repr__(self):
        return self.__formatted_string(sort=True, indents=4)


if __name__ == '__main__':

    string = """
    {"customers": [{"address": "nagpur","id": 525,"name": "robin sharma"},{"address": "chennai","id": 526,"name": "alex pandian"},{"address": "kolkata","id": 527,"name": "saurabh mishra"}],"market-share": true,"profits": null}
    """
    j = Json(string)
    print(Json.is_valid(j.text))
    print(j.type)
    j.write_file('abc')