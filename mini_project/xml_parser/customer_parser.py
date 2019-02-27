"""
    @description : Python program that manipulates customer xml. It supports features like add, update and remove customer details.
    @requirement : Place the file 'customer.xml' in the same path as this script.
    @author      : Swadhikar, C
"""
import xml.etree.ElementTree as ET

customer_xml = 'customer.xml'


class Singleton:

    __instance = {}

    @classmethod
    def get_xml_parser(cls):
        if not cls.__instance:
            print 'Instance not present. Creating...'
            cls.__instance['a'] = ET.parse(customer_xml)
        else:
            print 'Instance already created. Returning...'
        return cls.__instance['a']


class Customer:

    @classmethod
    def display_customers(cls):
        xml_tree = Singleton.get_xml_parser()

        for elem in xml_tree.getroot():
            print 'Customer id =', elem.attrib.get('customerId')
            for s in elem:
                print str(s.tag).capitalize(), '=', s.text
            print

    @classmethod
    def get_all_customer_ids(cls):
        id_list = []
        xml_tree = Singleton.get_xml_parser()

        for elem in xml_tree.getroot():
            cid = elem.attrib.get('customerId')
            if cid:
                id_list.append(cid)

        return id_list

    @classmethod
    def delete_customer(cls, customer_id):
        xml_tree = Singleton.get_xml_parser()
        root = xml_tree.getroot()

        for elem in root:
            if elem.attrib.get('customerId') == customer_id:
                root.remove(elem)
                xml_tree.write(customer_xml)
                print "Successfully removed customer id:", customer_id
                return 1

        print "Unable to find element:", customer_id
        return 0

    @classmethod
    def add_customer(cls, cid, name, title, phone):
        xml_tree = Singleton.get_xml_parser()
        root_elem = xml_tree.getroot()

        for elem in root_elem:
            c_id = elem.attrib.get('customerId')
            if c_id == cid:
                print "Customer with id '{}' already exists. Please try again.".format(cid)
                return 0

        customer = ET.Element('customer', customerId=cid)

        c_name = ET.SubElement(customer, 'name')
        c_title = ET.SubElement(customer, 'title')
        c_phone = ET.SubElement(customer, 'phone')

        c_name.text = name
        c_title.text = title
        c_phone.text = phone

        root_elem.append(customer)
        xml_tree.write(customer_xml)

        print "\nCustomer added successfully!"
        return 1

    @classmethod
    def update_customer(cls, customer_id, sub_element, new_value):
        xml_tree = Singleton.get_xml_parser()
        customer_element = None

        for elem in xml_tree.getroot():
            if customer_id == elem.attrib.get('customerId'):
                customer_element = elem
                break

        if customer_element is None:
            print "Unable to find customer with id: '{}'".format(customer_id)
            return 0

        for child in customer_element.iter():
            if child.tag == sub_element:
                child.text = new_value
                xml_tree.write(customer_xml)
                print "Modified element '{}' successfully with value: '{}'".format(sub_element, new_value)
                return 1

        print "Unable to find child element: '{}'. Adding".format(sub_element)
        new_sub_element = ET.SubElement(customer_element, sub_element)
        new_sub_element.text = new_value
        xml_tree.write(customer_xml)

        print "Added element '{}' successfully with value: '{}'".format(sub_element, new_value)
        return 1


def get_input(text, required=False):
    text += "\n>> "
    user_input = raw_input(text)
    if required:
        while not user_input:
            user_input = raw_input(text)
    return user_input


def main():
    user_msg = """
    Please select an option to perform (1 to 4 and 5 to exit):
    1. Add Customer
    2. Update Customer
    3. Remove Customer
    4. Display Customer
    5. Exit Program"""

    option = int(get_input(user_msg, required=True))

    if option == 1:
        print "\nAdding a new customer...\n"

        cid = get_input("Please enter a customer id", required=True)

        if cid in Customer.get_all_customer_ids():
            print "Customer id '{}' already exists. Please try again...".format(cid)
            main()

        c_name = get_input("Please enter a customer name", required=True)
        c_title = get_input("Please enter a customer title")
        c_phone = get_input("Please enter a customer phone")

        print "Values entered: {},{},{},{}".format(cid, c_name, c_title, c_phone)
        Customer.add_customer(cid, c_name, c_title, c_phone)

    elif option == 2:
        cid = get_input('Please enter a customer id to update')

        if cid not in Customer.get_all_customer_ids():
            print "Customer id '{}' does not exists. Please try again...".format(cid)
            main()

        user_msg = """
        Please enter the tag to update (name, title, phone)

        (If any a tag which does not exist is typed, a new sub tag under customer element will be created)
        """

        c_tag = get_input(user_msg, required=True)
        c_value = get_input("Enter a value")

        print "Values entered: {},{},{}".format(cid, c_tag, c_value)

        Customer.update_customer(cid, c_tag, c_value)

    elif option == 3:
        cid = get_input('Please enter a customer id to delete', required=True)

        if cid not in Customer.get_all_customer_ids():
            print "Customer id '{}' does not exists. Please try again...".format(cid)
            main()

        Customer.delete_customer(cid)
    elif option == 4:
        Customer.display_customers()
    elif option == 5:
        exit(0)
    else:
        print "That's an invalid option. Please retry...\n"

    main()


if __name__ == '__main__':
    main()