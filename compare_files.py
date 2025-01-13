#####################################################################
# This script performs folder and file comparison
# between 2 builds, the old build which stored as a zip file
# and the new one. The comparison is between the XwinSys_ini folders
#####################################################################

import os
import filecmp
import zipfile


# Function for zip file extraction
def extracting_dir(zip_file_path, destination_folder):
    try:
        with zipfile.ZipFile(zip_file_path,'r') as zip_ref:
            print(f'Extracting content of {zip_file_path}')
            zip_ref.extractall(destination_folder)
            print(f'Extraction complete. Files extracted to: {destination_folder}')
            return True
    except zipfile.BadZipfile:
        print("The file is not a valid zip archive.")
        return False
    except Exception as e:
        print(f'Error occurred: {e}')
        return False


# Function to recursively compare two directories
def compare_folders(dir1, dir2, dir1_list, dir2_list, differ_list):
    # Create a directory comparison object
    comparison = filecmp.dircmp(dir1, dir2)

    # Find files/folders only in dir1 (backup_folder)
    for name in comparison.left_only:
        dir1_list.extend(comparison.left_only)

    # Find files/folders only in dir2 (folder_under_test)
    for name in comparison.right_only:
        dir2_list.extend(comparison.right_only)

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
        compare_folders(new_dir1, new_dir2, dir1_list, dir2_list, differ_list)

def main():
    zip_file_path = input('Enter the path to the ZIP file: ').strip()

    # Append zip extension
    if not zip_file_path.lower().endswith('.zip'):
        zip_file_path += '.zip'

    # Check if destination folder exists

    destination_folder = r'C:\ProgramData\XwinSys\Backup\builds_compare_temp'
    if not os.path.exists(r'C:\ProgramData\XwinSys\Backup\builds_compare_temp'):
        os.makedirs(destination_folder)

    comparison_folder = r'C:\ProgramData\XwinSys\XwinSys_ini'

    # Validation tests
    if not os.path.exists(zip_file_path):
        print("Error: ZIP file does not exist.")
        return

    if not os.path.exists(destination_folder):
        print("Error: Destination folder does not exist.")
        return

    if not os.path.exists(comparison_folder):
        print("Error: Comparison folder does not exist.")
        return

    # Initialize lists to store comparison results
    dir1_list = []
    dir2_list = []
    differ_list = []


    # Extract zip file
    if extracting_dir(zip_file_path, destination_folder):

        # Perform the folder comparison
        compare_folders(destination_folder, comparison_folder, dir1_list, dir2_list, differ_list)

    # Print the results of the comparison
    print('\nComparison Results:')
    print(f' - Files or folders that appears only on the backup folder: {dir1_list}')
    print(f' - Files or folders that appears only on the build under test folder: {dir2_list}')
    print(f' - Files or folders  that differ: {differ_list}')

if __name__ == '__main__':
    main()