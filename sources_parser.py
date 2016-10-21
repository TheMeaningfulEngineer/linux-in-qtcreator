import re
import ipdb


build_logfile = "build.log"

regex_pattern = '\S*?\.c(?:\n|\s)'
"""
gcc -Wp,-MD,arch/x86/tools/.relocs_common.o.d -Wall -Wmissing-pr     ototypes -Wstrict-prototypes -O2 -fomit-frame-pointer -std=gnu89        -I./tools/include  -c -o arch/x86/tools/relocs_common.o arch/x86/     tools/relocs_common.c
"""

def parse_line(line, regex_pattern):
    pattern_in_line = re.findall(regex_pattern, line)
    pattern_in_line = [unstripped.strip() for unstripped in pattern_in_line]
    return pattern_in_line


def parse_log(build_logfile, regex_pattern):
    source_files = []
    with open(build_logfile, 'r') as build_log:
        for line in build_log:
            pattern_in_line = parse_line(line, regex_pattern)
            source_files.extend(pattern_in_line)
    return source_files



def test_parse_line():
    with open("test_log_entries", 'r') as test_log:
        for line in test_log:
            pattern_in_line = parse_line(line, regex_pattern)
    assert pattern_in_line == ["arch/x86/tools/relocs_64.c"]

 

