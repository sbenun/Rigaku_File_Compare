##########################################################
#This script suppose to perform folder and file comparison
#between 2 builds
###########################################################

import os
import filecmp
import zipfile

# Define paths for the folders to be compared
backup_folder = (r'C:\ProgramData\XwinSys\Backup\SBN_test')
folder_under_test = (r'C:\ProgramData\XwinSys\XwinSys_ini')
test_folder_permissions = (r'C:\Program Files\XwinSys\2.14.0.101')

# Initialize lists to store comparison results
dir1_list = []
dir2_list = []
differ_list = []

# Function placeholder for potential zip file extraction (currently not implemented)
def extracting_dir(dir1):
    None


# Function to recursively compare two directories
def compare_folders(dir1, dir2):
    # Create a directory comparison object
    comparison = filecmp.dircmp(dir1, dir2)

    # Find files/folders only in dir1 (backup_folder)
    for name in comparison.left_only:
        dir1_list.append(name)

    # Find files/folders only in dir2 (folder_under_test)
    for name in comparison.right_only:
        dir2_list.append(name)

    # Compare contents of files that exist in both directories
    for name in comparison.common_files:
        file1 = os.path.join(dir1, name)
        file2 = os.path.join(dir2, name)
        # If file contents differ, add to differ_list
        if not filecmp.cmp(file1, file2, shallow=False):
            differ_list.append(name)

    # Recursively compare subdirectories
    for subdir in comparison.common_dirs:
        new_dir1 = os.path.join(dir1, subdir)
        new_dir2 = os.path.join(dir2, subdir)
        compare_folders(new_dir1, new_dir2)


# Call the extraction function (currently does nothing)
extracting_dir(backup_folder)

# Perform the folder comparison
compare_folders(backup_folder, folder_under_test)

# Print the results of the comparison
print(f' - Files or folders that appears only on the backup folder {dir1_list}')
print(f' - Files or folders that appears only on the folder under test {dir2_list}')
print(f' - Files or folders  that differ: {differ_list}')