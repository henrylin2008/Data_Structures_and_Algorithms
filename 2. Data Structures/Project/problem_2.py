# Finding Files
# For this problem, the goal is to write code for finding all files under a directory (and all
# directories beneath it) that end with ".c"
#
# Here is an example of a test directory listing, which can be downloaded here:
#
# ./testdir
# ./testdir/subdir1
# ./testdir/subdir1/a.c
# ./testdir/subdir1/a.h
# ./testdir/subdir2
# ./testdir/subdir2/.gitkeep
# ./testdir/subdir3
# ./testdir/subdir3/subsubdir1
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir4
# ./testdir/subdir4/.gitkeep
# ./testdir/subdir5
# ./testdir/subdir5/a.c
# ./testdir/subdir5/a.h
# ./testdir/t1.c
# ./testdir/t1.h

# Python's os module will be useful—in particular, you may want to use the following resources:
#
# os.path.isdir(path)
#
# os.path.isfile(path)
#
# os.listdir(directory)
#
# os.path.join(...)
#
# Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are
# not allowed to use os.walk().
#
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """

    paths = []

    if os.path.exists(path):
        for item in os.listdir(path):
            path_items = os.path.join(path, item)

            if os.path.isfile(path_items) and path_items.endswith(suffix):  # base case
                paths.append(path_items)
            elif os.path.isdir(path_items):
                paths += find_files(suffix, path_items)      # recursive call
    else:  # edge case if path does not exist
        return "Path does not exist"

    return paths


# print files in current directory
# print(os.listdir("."))

# Test case if the file exist
print(os.path.isfile("testdir/subdir1/a.h"))  # return True if the file exists

# Test if the file ending with .py
print("./test.py".endswith(".py"))    # return True if the file ending with .py extension

# test if any file ending with .h in a given directory
test1 = find_files(".h", "testdir/subdir5/")
print(test1)     # return a list of files that ending with .h extension in the given directory

# test edge case with non existing file and directory
test2 = find_files(".non", "nonexist")
print(test2)    # return "Path does not exist" if no such path

# edge case non-exist file in the subdirectory
test3 = find_files(".h", "testdir/nonexist")
print(test3)    # return "Path does not exist" if no such path

# test to get file/s ending with .h in the given directory and the subdirectories
test4 = find_files(".h", "testdir")
print(test4)  # prints files with .h extension

# test to get non-existing file/s ending with .text in the current directory and the subdirectories
test5 = find_files(".txt", "testdir")
print(test5)  # prints a list of files ending with .txt extension in current directory/subdirectories

# test to get file/s ending with .c in the given directory and the subdirectories
test6 = find_files(".c", "testdir")
print(test6)  # prints files with .c extension
