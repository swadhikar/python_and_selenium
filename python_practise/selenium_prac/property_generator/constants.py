from collections import OrderedDict

guest_portal = OrderedDict()

guest_portal['portalName'] = 'TestPortalName'
guest_portal['portalDesc'] = 'Test Portal for testing guest access'

guest_portal['Portal Settings'] = OrderedDict()
guest_portal['Portal Settings']['checkbox1'] = {'check': False}
guest_portal['Portal Settings']['checkbox2'] = {'check': True}

guest_portal['Advanced Settings'] = OrderedDict()
guest_portal['Advanced Settings']['select1'] = {'option': 'Select this drop down option'}
guest_portal['Advanced Settings']['radiobutton1'] = {'click': True}
guest_portal['Advanced Settings']['checkbox2'] = {'check': True}


def parser(dictionary):
    for k, v in dictionary.items():
        if isinstance(v, OrderedDict):
            print k
            parser(dictionary[k])
        else:
            print "{}{}: {}".format(' ' * i, k, v)

if __name__ == '__main__':
    parser(guest_portal)
