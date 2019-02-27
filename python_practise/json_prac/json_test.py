import simplejson as json

book = dict()
book['bob'] = {'name': 'bob michales', 'address': '12 red street, NJ', 'phone': 98989898}
book['tim'] = {'name': 'tim knitter', 'address': '12 blue street, NY', 'phone': 77777777}
book['sidney'] = {'name': 'sidney carter', 'address': '12 orange street, TX', 'phone': 21212121}
authors = dict()
authors['authors'] = book
json_file = 'book.json_prac'


def load_author():
    json_text = json.dumps(authors, indent=2, sort_keys=True)
    with open(json_file, 'w') as f:
        f.write(json_text)
    print 'JSON write successful:', json_file


def retrieve_author_details():
    s = open(json_file, 'r').read()
    json_dict = json.loads(s)
    for author in json_dict['authors']:
        print '{}: {}, Ph: {}'.format(author,
                                      json_dict['authors'][author]['address'],
                                      json_dict['authors'][author]['phone'])


if __name__ == '__main__':
    load_author()
    retrieve_author_details()