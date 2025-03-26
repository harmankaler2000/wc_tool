"""
    Purpose: Specify what are the actions to be performed for 
             each function that is called for wc_tool
    Owner: Harmandeep Kaur Kaler
    Created On: 25th March 2025
"""

class CommandRouter:
    """
    Class to route the command to the appropriate function
    """

    def __init__(self, args):
        self.args = args

    def route_command(self):
        """
        Function to route the command to the appropriate function
        """
        if self.args.bytes:
            print(f"Byte count to be calculated for file at path {self.args.filename}")
            
        else:
            print("Command not found")
