#!/usr/bin/python3

import re
import os
import sys

def main():
    build_logfile = sys.argv[1]
    project_name = sys.argv[2]
    kernel_source_files = parse_log(build_logfile)
    setup_qt_creator_projectfiles(project_name, kernel_source_files)



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

def setup_qt_creator_files_projectfile(project_name, list_of_paths):
    ''' Generate the filename.files file required by QT creator to know what 
    files to open in the IDE'''

    file_name = project_name + ".files"

    with open(file_name, 'w') as sources_file:
        for path in list_of_paths:
            sources_file.write(path + "\n")

def setup_qt_creator_config_projectfile(project_name):

    hardcoded_text = ("#define __KERNEL__ \n"
                      "#include <generated/autoconf.h>\n")
    file_name = project_name + ".config"
    with open(file_name, 'w') as sources_file:
        sources_file.write(hardcoded_text)


def setup_qt_creator_includes_projectfile(project_name):

    hardcoded_text = ("include \n"
                      "arch/x86/include\n")
    file_name = project_name + ".includes"

    with open(file_name, 'w') as sources_file:
        sources_file.write(hardcoded_text)

def setup_qt_creator_creator_projectfile(project_name):
    hardcoded_text = "[General]\n"
    file_name = project_name + ".creator"

    with open(file_name, 'w') as sources_file:
        sources_file.write(hardcoded_text)


def setup_qt_creator_projectfiles(project_name, list_of_paths):
    
    setup_qt_creator_files_projectfile(project_name, list_of_paths)
    setup_qt_creator_config_projectfile(project_name)
    setup_qt_creator_includes_projectfile(project_name)
    setup_qt_creator_creator_projectfile(project_name)


if __name__ == "__main__":
    main()
