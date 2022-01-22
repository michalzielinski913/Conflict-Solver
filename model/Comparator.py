"""
Comparator class is responsible for parsing two text files and all operations related to comparing them
"""
class Comparator:
    def __init__(self):
        """
        Class constructor, It initializes some fields of class
        """
        self.dictionary = {}
        self.x = 1
        self.json = ''

    def compare(self, element_one, element_two):
        """
        Compare two elements, if they are not equal add them to difference list
        :param element_one: Element one
        :param element_two: Element two
        """
        row = [element_one, element_two]
        self.dictionary[self.x] = row
        if element_one != element_two:
            self.add_element(element_one, element_two)
        self.x += 1

    def add_element(self, element_one, element_two):
        """
        Add difference list element to UI
        :param element_one: First elements
        :param element_two: Second elements
        """
        line1 = element_one.replace('\'', '\"')
        line2 = element_two.replace('\'', '\"')
        json_element = {
            'DT_RowId': self.x,
            'FirstFile': line1[:33],
            'SecondFile': line2[:33]
        }
        self.json = self.json + str(json_element) + ','

    def get_json(self):
        """
        Return json containing all elements which will be displayed in UI
        :return: json string with elements to display in UI
        """
        self.json = self.json[:-1]
        self.json = self.json.replace('\"', '\\\"')
        self.json = self.json.replace('\'', '\"')
        self.json = '[' + self.json + ']'
        return self.json

    def reset_json(self):
        """
        Reset class field containing json string
        :return:
        """
        self.json = ''

    def get_element(self, id_number):
        """
        Return two chunks with the same difference id
        :param id_number: difference id of two chunks which user wants
        :return: two string elements
        """
        return self.dictionary[id_number]

    def solve_conflict(self, id_number, option, new_text):
        """
        Solve specific conflict
        :param id_number: Conflict ID
        :param option: How user wants to solve conflict
        :param new_text: If user wants custom value provides it
        """
        if option == "textOne":
            return
        elif option == "textTwo":
            self.dictionary[id_number][0] = self.dictionary[id_number][1]
        elif option == "custom":
            self.dictionary[id_number][0] = new_text

    def get_first_column(self):
        """
        Generator returning only first text chunks.
        Used for generating third file
        :return: generator returning chunks of first file
        """
        for i in range(len(self.dictionary)):
            yield self.dictionary[i+1][0]
