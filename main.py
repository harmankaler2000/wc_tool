"""
Purpose: Main file for wc_tool creation
Owner: Harmandeep Kaur Kaler
Created On: 25th March 2025
"""
import argparse
from command_routing import command_router

def main():
    """
    Main function for wc_tool creation
    """
    parser = argparse.ArgumentParser(description="Word Count Tool")
    parser.add_argument("-c", "--bytes", help="Print the byte counts", action="store_true")
    parser.add_argument("-w", "--words", help="Print the word counts", action="store_true")
    parser.add_argument("-l", "--lines",
                        help="Print the number of lines in the file", action="store_true")
    parser.add_argument("-m", "--characters",
                        help="Print the number of characters in the file", action="store_true")
    parser.add_argument("filename", help="File to be processed")
    args = parser.parse_args()
    calculated_data = command_router.WordCount(args).route_command()
    return calculated_data


if __name__ == "__main__":
    output = main()
    print(output)
