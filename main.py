"""
Purpose: Main file for wc_tool creation
Owner: Harmandeep Kaur Kaler
Created On: 25th March 2025
"""
#!/usr/bin/env python3
import sys
import argparse
from wc_tool import command_router

print(f"Argument received: {sys.argv[1]}")


def main():
    """
    Main function for wc_tool creation
    """
    parser = argparse.ArgumentParser(description="Word Count Tool")
    parser.add_argument("-c", "--bytes", help="Print the byte counts", action="store_true")
    parser.add_argument("-w", "--words", help="Print the word counts", action="store_true")
    parser.add_argument("filename", help="File to be processed")
    args = parser.parse_args()
    calculated_data = command_router.CommandRouter(args).route_command()
    # print(calculated_data)
    return calculated_data


if __name__ == "__main__":
    main()
