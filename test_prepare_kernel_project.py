import prepare_kernel_project


def test_parse_log():
    mock_build_log = "test_files/mock_build_log.log"
    expected_results_file = "test_files/result.files"
    
    with open(expected_results_file, 'r') as expected_results_file:
        expected_results_list = [path.strip() for path in expected_results_file.readlines()]

    actual_results_list = prepare_kernel_project.parse_log(mock_build_log)
    assert expected_results_list == actual_results_list



def test_modify_qt_creator_projectfiles():

    mock_project_name = "test_files/random1234"
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

    prepare_kernel_project.modify_qt_creator_projectfiles(mock_project_files, mock_kernel_sources)

    for modified_mockfile in mock_project_files:
        with open(modified_mockfile, 'r') as mockfile:
            file_content = mockfile.read()
            if modified_mockfile.endswith(".config"):
                assert configfile_content == file_content
            if modified_mockfile.endswith(".files"):
                assert filesfile_content == file_content
            if modified_mockfile.endswith(".includes"):
                assert includefile_content == file_content

