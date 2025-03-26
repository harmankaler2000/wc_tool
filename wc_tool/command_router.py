"""
    Purpose: Specify what are the actions to be performed for 
             each function that is called for wc_tool
    Owner: Harmandeep Kaur Kaler
    Created On: 25th March 2025
"""

import os

class WordCount:
    """
    Class to route the command to the appropriate function
    """

    def __init__(self, args):
        self.args = args

    @staticmethod
    def check_file_exists(file_name):
        """
        Function to check if the file exists
        """
        return os.path.isfile(file_name)
    
    @staticmethod
    def calculate_bytes(file_name):
        """
        Function to calculate the byte count of a file
        """
        byte_count = os.stat(file_name).st_size
        return byte_count


    @staticmethod
    def calculate_lines(file_name):
        """
        Function to calculate the line count of a file
        """
        # makes use of a generator and is faster than readlines
        with open(file_name, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)

    @staticmethod
    def calculate_words(file_name):
        """
        Function to calculate the word count of a file
        """
        word_count = 0
        # makes use of a generator and is faster than readlines
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                word_count += len(line.split())
        return word_count

    # @staticmethod
    # def calculate_characters(file_name):
    #     """
    #     Function to calculate the word count of a file
    #     """
    #     character_count = 0
    #     # makes use of a generator and is faster than readlines
    #     with open(file_name, 'r', encoding='utf-8') as file:
    #         for line in file:
    #             character_count += len(line)
    #     return character_count

    def route_command(self):
        """
        Function to route the command to the appropriate function
        """
        if not self.check_file_exists(self.args.filename):
            return "File not found"

        if self.args.bytes:
            byte_data = self.calculate_bytes(self.args.filename)
            return str(byte_data) + "    " + self.args.filename

        if self.args.lines:
            no_lines = self.calculate_lines(self.args.filename)
            return str(no_lines) + "    " + self.args.filename

        if self.args.words:
            no_words = self.calculate_words(self.args.filename)
            return str(no_words) + "    " + self.args.filename

        # if self.args.characters:
        #     no_words = self.calculate_characters(self.args.filename)
        #     return str(no_words) + "    " + self.args.filename

        return 'No command specified'
