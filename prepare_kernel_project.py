#!/usr/bin/python3

import re
import os
import sys


def main():
    build_logfile = sys.argv[1]
    
    kernel_source_files = parse_log(build_logfile)
    qt_project_files = detect_qt_creator_projectfiles()

    modify_qt_creator_projectfiles(qt_project_files, kernel_source_files)



def parse_line(line):
    regex_pattern = '\S*?\.c(?:\n|\s)'
    pattern_in_line = re.findall(regex_pattern, line)
    pattern_in_line = [unstripped.strip() for unstripped in pattern_in_line]
    return pattern_in_line


def parse_log(build_logfile):
    source_files = []
    with open(build_logfile, 'r') as build_log:
        for line in build_log:
            pattern_in_line = parse_line(line)
            source_files.extend(pattern_in_line)
    return source_files

def modify_qt_creator_files_projectfile(filename, list_of_paths):
    ''' Generate the filename.files file required by QT creator to know what 
    files to open in the IDE'''

    with open(filename, 'w') as sources_file:
        for path in list_of_paths:
            sources_file.write(path + "\n")

def modify_qt_creator_config_projectfile(filename):

    hardcoded_text = ("#define __KERNEL__ \n"
                      "#include <generated/autoconf.h> ")
    with open(filename, 'w') as sources_file:
        sources_file.write(hardcoded_text)


def modify_qt_creator_includes_projectfile(filename):

    hardcoded_text = ("include \n"
                      "arch/x86/include ")
    with open(filename, 'w') as sources_file:
        sources_file.write(hardcoded_text)

def modify_qt_creator_projectfiles(projectfiles, list_of_paths):
    
    for projectfile in projectfiles:
        if projectfile.endswith('.files'):
            modify_qt_creator_files_projectfile(projectfile, list_of_paths)
        if projectfile.endswith('.config'):
            modify_qt_creator_config_projectfile(projectfile)
        if projectfile.endswith('.includes'):
            modify_qt_creator_includes_projectfile(projectfile)

def detect_qt_creator_projectfiles():
    ''' Checks for files Qt creator generates when creating a new non QT project'''

    project_files_extensions = (".includes", ".config", ".creator.user", ".creator", ".files")
    files_in_current_dir = [f for f in os.listdir('.') if os.path.isfile(f)]
    project_files = []
    
    for f in files_in_current_dir:
        if f.endswith(project_files_extensions):
            project_files.append(f)

    return project_files


def test_parse_line():
    with open("test_log_entries", 'r') as test_log:
        for line in test_log:
            pattern_in_line = parse_line(line)
    assert pattern_in_line == ["arch/x86/tools/relocs_64.c"]



def test_modify_qt_creator_projectfiles():
    
    mock_project_name = "random1234"
    mock_project_files = [mock_project_name + ".config",
                          mock_project_name + ".files",
                          mock_project_name + ".includes"]
    
    mock_kernel_sources = ["/path/abcd.c",
                           "/path/arm/bob.c"]

    filesfile_content = ("/path/abcd.c\n"
                         "/path/arm/bob.c\n")

    configfile_content = ("#define __KERNEL__ \n"
                          "#include <generated/autoconf.h> ")

    includefile_content = ("include \n"
                           "arch/x86/include ")
    
    #Generating dummy files
    for mockfile in mock_project_files:
        open(mockfile, 'a').close()

    modify_qt_creator_projectfiles(mock_project_files, mock_kernel_sources)

    for modified_mockfile in mock_project_files:
        with open(modified_mockfile, 'r') as mockfile:
            file_content = mockfile.read()
            if modified_mockfile.endswith(".config"):
                assert configfile_content == file_content
            if modified_mockfile.endswith(".files"):
                assert filesfile_content == file_content
            if modified_mockfile.endswith(".includes"):
                assert includefile_content == file_content


if __name__ == "__main__":
    main()
