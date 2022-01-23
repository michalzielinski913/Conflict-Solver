
"""
Interface which shows how we can add new classes supporting writing to different text files
"""
class FileWriterInterface:
    def __init__(self, path):
        """
        Class constructor
        :param path: path to the new file
        """
        pass

    def write_line_to_file(self, line):
        """
        Write single line to text file
        :param line: Text which will be saved
        """
        pass
