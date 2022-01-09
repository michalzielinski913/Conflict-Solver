
class Comparator:
    def __init__(self):
        self.dictionary = {}
        self.x = 1
        self.json = ''

    def compare(self, element_one, element_two):
        row = [element_one, element_two]
        self.dictionary[self.x] = row
        if element_one != element_two:
            self.add_element(element_one, element_two)
        self.x += 1

    def add_element(self, element_one, element_two):
        line1 = element_one.replace('\'', '\"')
        line2 = element_two.replace('\'', '\"')
        json_element = {
            'DT_RowId': self.x,
            'FirstFile': line1[:33],
            'SecondFile': line2[:33]
        }
        self.json = self.json + str(json_element) + ','

    def get_json(self):
        self.json = self.json[:-1]
        self.json = self.json.replace('\"', '\\\"')
        self.json = self.json.replace('\'', '\"')
        self.json = '[' + self.json + ']'
        return self.json

    def reset_json(self):
        self.json = ''

    def get_element(self, id_number):
        return self.dictionary[id_number]
