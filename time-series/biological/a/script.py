import os
import sys
import re

rootdir = os.getcwd()

for root, subFolders, files in os.walk(rootdir):

    # For each sub-directory:
    for folder in subFolders:

        # Get the current folder path:
        folderPath = os.path.join(root, folder)

        # Walk the sub-directory:
        for subroot, subsubFolders, subfiles in os.walk(folderPath):

            # For each file in the sub-directory:
            for filename in subfiles:

                # Get the current file path:
                filePath = os.path.join(folderPath, filename)

                # Open the file for reading:
                with open( filePath, 'r' ) as f:

                    # Grab the file contents:
                    fileStr = f.read()

                f.close()


                # File all instances of }{ and insert a comma between them:
                fileStr2 =  re.sub('\}\{', '},{', fileStr)



                # Open the file for writing:
                with open( filePath, 'w' ) as f:

                    # Write to the file:
                    f.write(fileStr2)

                f.close()



