### return shape
data = {
    "items": [
        {
            "description": "example description",
            "category": "example category",
            "attributes": [
                {
                    "name": "attribute name",
                    "value": "attribute value"
                }
            ]
        }
    ],
    ## unknownWords words not tied to specific item
    "unknownWords": ["word1", "word2"]
}


blank_item = {
            "description": "",
            "category": "",
            "attributes": [
                {
                    "name": "",
                    "value": ""
                }
            ]
        }

blank_item = {
    "description": "",
    "category": "",
    "attributes": [
        {
            "name": "",
            "value": ""
        }
    ]
}

class Attribute:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

class Item:
    def __init__(self, description: str, category: str, attributes: list[dict]):
        self.description = description
        self.category = category
        self.attributes = [Attribute(attr['name'], attr['value']) for attr in attributes]

def split_on_spaces(s: str) -> list[str]:
    return s.split()


#### function takes an input of string ex: 1/4-20 X 5/8 HEX CAP SCREW GR 5 BLK OX

def generateItems(description: str):
    #### item dictionary and unknown words list to populate
    unknown_words = []
    attributes = {}


    ### map values

    thread_size = description.split('X', 1)[0]

    #### set thread size
    attributes['Thread Size'] = thread_size

    ###  drop extra space on remainder
    remainder = description.split('X', 1)[1][1:]

    length = remainder.split(' ', 1)[0]
    attributes['Length'] = length

    remainder = remainder.split(' ', 1)[1]






    print (thread_size)
    print (length)
    print (split_on_spaces(remainder))

    #if parsed object is uknown add to unkownd words

    for word in remainder:
        if word == 'PLN':
            #set finish to plain

        if word == 'HCS'
            #set cat to HCS


        else:
            unkown_words.append(word)




generateItems('1/4-20 X 5/8 HEX CAP SCREW GR 5 BLK OX')

