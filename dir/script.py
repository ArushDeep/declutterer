import os

def box(text):
    # Determine the width of the box based on the string length
    box_width = len(text) + 4

    # Print the top border
    print("+" + "-" * (box_width - 2) + "+")
    
    # Print the string inside the box
    print(f"| {text} |")
    
    # Print the bottom border
    print("+" + "-" * (box_width - 2) + "+")


currentDirectory = os.getcwd()
box(f"This script is running in {currentDirectory}")

# list of all files
lisFiles = []

# list of all file types
lisFileTypes = []

# list of all folders
lisFolders = []

print(os.listdir(currentDirectory))