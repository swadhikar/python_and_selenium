import webbrowser
from inspect import stack


class HTMLGenerator(object):
    html_head = """<!DOCTYPE html>

<html>
<head>
<style>
table, th, td {{
        border: 1px solid black;
    }}
</style>
<title>{title_string}</title>
</head>
<body>
""".format(title_string='')

    html_tail = """
</body>
</html>"""

    def __init__(self, html_file):
        self.html_file = html_file
        self.write_html(self.html_head)

    @staticmethod
    def get_tag(tag, text):
        """
           Create an html tag of below format
           <tag>text</tag>
        """
        return "<{0}>{1}</{0}>".format(tag, text)

    @staticmethod
    def get_tag_with_attributes(tag, text='', close=True, **kwargs):
        """
           Create an html tag of below format
           <tag attr='attr_val' attr='attr_val'>text</tag>
        """
        html_content = '\n<{}'.format(tag)

        for k, v in kwargs.items():
            html_content += ' {}="{}"'.format(k, v)

        html_content += '>'.format(text)

        if close:
            html_content += '{}</{}>\n'.format(text, tag)

        return html_content

    @staticmethod
    def get_list_tag(items, ordered, **attr):
        """
        :param items    : List of items to be created
        :param ordered  : True for ordered list or False for unordered list
        :param attr     : Keyword args for attribute=value
        :return         : tag of below format
        :example        :
                          items = [1,2,3]
                          <ol>
                            <li>1</li>
                            <li>2</li>
                            <li>3</li>
                          </ol>
        """
        list_tag = 'ul'
        if ordered:
            list_tag = 'ol'

        html_content = '\n'
        if attr:
            html_content += HTMLGenerator.get_tag_with_attributes(list_tag, close=False, **attr)
        else:
            html_content += "<{}>".format(list_tag)

        for item in items:
            html_content += '\n    ' + HTMLGenerator.get_tag('li', item)

        html_content += "\n</{}>".format(list_tag)

        return content

    @staticmethod
    def get_table_tag(table_headers, contents):
        """
        :param table_headers    : Table headers - Type: List eg. ['Name', 'Age', 'Salary']
        :param contents         : Contents of each table - Type: list of lists
                                  eg. [ ['worker1',27,300], ['worker4',25,600] ]
        :return                 : html table tag (pass)
        :example                :
                                    headers = ['Name', 'Age', 'Salary']
                                    content = [['swad', 27, 1000], ['Naren', 27, 5000]]

                                    <table style="width:100%">
                                        <tr>
                                            <th>Name</th>
                                            <th>Age</th>
                                            <th>Salary</th>
                                        </tr>
                                        <tr>
                                            <td>swad</td>
                                            <td>27</td>
                                            <td>1000</td>
                                        </tr>
                                    </table>
        """
        table_tag = HTMLGenerator.get_tag_with_attributes('table', style='width:100%', close=False)

        table_tag += '\n    <tr>'

        for header in table_headers:
            table_tag += '\n        <th>{}</th>'.format(header)

        table_tag += '\n    </tr>'

        for html_content in contents:
            table_tag += '\n    <tr>'

            for element in html_content:
                table_tag += '\n        <td>{}</td>'.format(element)

            table_tag += '\n    </tr>'

        table_tag += "\n</table>"

        return table_tag

    def add_table(self, header, contents):
        table_tag = self.get_table_tag(header, contents)
        self.write_html(table_tag)
        return 1

    def add_tag(self, tag, text='', **attr):
        if attr:
            tag_content = self.get_tag_with_attributes(tag, text, **attr)
        else:
            tag_content = self.get_tag(tag, text)

        self.write_html(tag_content)
        return 1

    def add_html_list(self, items, ordered=True, **attr):
        list_content = self.get_list_tag(items, ordered, **attr)
        self.write_html(list_content)
        return 1

    def write_html(self, html_content='', tail=False):
        if tail:
            html_content = HTMLGenerator.html_tail

        file_mode = 'a'

        # Open for write mode only when init calls
        if stack()[1][3] == '__init__':
            file_mode = 'w'

        with open(self.html_file, file_mode) as f:
            f.write(html_content)

        return 1

    def show_browser(self):
        html_file_path = 'C:\\Users\\swadhi\\Documents\\bitbucket\\pyselenium\\PySelenium' \
                         '\\mini_project\\html_generator\\{}'.format(self.html_file)
        webbrowser.open(html_file_path)
        print ("Browser open initiated successfully!")
        return 1


if __name__ == '__main__':
    html = HTMLGenerator('sample.html')

    bold_text = html.get_tag('b', 'Check out the below table:')
    html.add_tag("p", bold_text, style='color:blue;')

    headers = ['Name', 'Age', 'Salary']
    content = [['swad', 27, 1000], ['Naren', 27, 5000], ['Saibal', 32, 10000], ['Brahmaiah', 27, 50000]]
    html.add_table(headers, content)

    html.add_tag('a', 'Click here to google search!', href='https://www.google.co.in')
    html.add_tag('p', 'sample paragraph in purple in large text', style='font-size:160%;color:purple;')

    html.add_tag('h3', 'Following are the items in the red list:')
    my_list = range(1, 11)
    html.add_html_list(my_list, ordered=False, style="color:red;")

    html.write_html(tail=True)
    # html.show_browser()

