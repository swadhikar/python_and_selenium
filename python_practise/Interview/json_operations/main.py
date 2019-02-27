import yaml
import json

json_in_file = 'in.json_prac'
config_file = 'config.json_prac'
yml_in_file = 'in.yml'

def load_json():
    with open(json_in_file) as json_obj:
        json_content = json.load(json_obj)
        # json_content = json.loads(json_obj.read())    # Loads a string
        print("Finish loading json_prac object!")

    return json_content


def write_config(dictionary):
    with open(config_file, 'w') as config:
        json.dump(dictionary, config)
        print("Finish writing config data!")


def read_yml_config():
    with open(yml_in_file) as yml_obj:
        config = yaml.load(yml_obj)

    for section in config:
        print(section)
        print('   ', config[section])

def main():
    # write_config(load_json())
    read_yml_config()

if __name__ == '__main__':
    main()