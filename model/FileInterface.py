"""
Interface which shows how we can add new classes supporting reading from different text files
"""
class FileInterface:
    def __init__(self, path):
        """
        Class constructor
        :param path: path to text file
        """
        pass

    def get_text(self):
        """
        Read data from text file
        :return: text inside file
        """
        pass

