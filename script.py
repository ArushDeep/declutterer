import os

# cosmetic element
def box(text):
    # Determine the width of the box based on the string length
    box_width = len(text) + 4

    # Print the top border
    print("+" + "-" * (box_width - 2) + "+")
    
    # Print the string inside the box
    print(f"| {text} |")
    
    # Print the bottom border
    print("+" + "-" * (box_width - 2) + "+")


# calibrating os module
os.chdir(os.path.dirname(os.path.abspath(__file__)))
currentDirectory = os.path.dirname(os.path.abspath(__file__))
print(f"This script is running in {currentDirectory}")


# Updating and Displaying lists
lisFolders = []
lisFiles = []
def updateLis():
  with os.scandir() as entries:
      for entry in entries:
          if entry.is_dir():
              lisFolders.append(str(entry.name))
          else:
              lisFiles.append(str(entry.name))

  lisFiles.remove("script.py")
  lisFiles.remove(".DS_Store")

  print(str("\nDIRECTORY:- "))
  box(str(f"Folders: {lisFolders}"))
  box(str(f"Files: {lisFiles}"))

updateLis()

# Function for renaming FOLDERS
def deFolde(lisFolders):
    lisFolders.sort()

    for index,item in enumerate(lisFolders):
        srcFolder = str(item)
        dstFolder = str(f"Folder-{index+1}")

        os.replace(srcFolder, dstFolder)


# Function to declutter FILES
def deFile(lisFiles):
  # arranging list in asending order with consequitive file types
  for index,item in enumerate(lisFiles):
    lisFiles[index] = lisFiles[index][::-1]

  lisFiles.sort()

  for index,item in enumerate(lisFiles):
    lisFiles[index] = lisFiles[index][::-1]

  
  # returns the file type of the first element in list
  def myex(fileName):
    return str(fileName[fileName.rfind("."):] if "." in lisFiles[0] else "")

  fileExtension = myex(lisFiles[0])
  counter = 1


  for index,item in enumerate(lisFiles):
  
    if myex(lisFiles[index]) != myex(lisFiles[index-1]):
       counter = 1

    srcFile = str(item)
    dstFile = str(f"{counter}{myex(srcFile)}")
    counter+=1

    os.replace(srcFile, dstFile)

try:
  # Calling function for renaming FOLDERS
  deFolde(lisFolders)
  # Calling function for renaming FILES
  deFile(lisFiles)
except Exception as e:
  pass

# Updating and Displaying lists
lisFolders = []
lisFiles = []

updateLis()
