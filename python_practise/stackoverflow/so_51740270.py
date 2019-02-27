# Stackoverflow question:
# https://stackoverflow.com/questions/51740270/python-dictionary-swap-keyvalue-pair-when-values-exist-in-mutiple-keys

from json import dumps

in_dict = {
    "1A": [
        "mathematics"
    ],
    "1B": [
        "problem-solving",
        "model"
    ],
    "1C": [
        "basic",
        "model"
    ]
}

out_dict = dict()
for subject_code, subject_list in in_dict.items():
    for subject in subject_list:
        out_dict[subject] = out_dict.get(subject, []) + [subject_code]
print(dumps(out_dict, indent=2))

"""
Expected Output:
{
  "mathematics": [
    "1A"
  ],
  "problem-solving": [
    "1B"
  ],
  "model" : [
    "1B" ,
    "1C"
  ],
  "basic": [
    "1C",
  ]
}

"""
