import prepare_kernel_project
import pdb

def test_parse_log():
    mock_build_log = "test_files/mock_build_log.log"
    expected_results_file = "test_files/result.files"
    
    with open(expected_results_file, 'r') as expected_results_file:
        expected_results_list = [path.strip() for path in expected_results_file.readlines()]

    actual_results_list = prepare_kernel_project.parse_log(mock_build_log)
    assert expected_results_list == actual_results_list


def test_setup_qt_creator_projectfiles():

    mock_project_name = "test_files/linux"
    mock_kernel_sources = ["arch/x86/tools/relocs_common.c",
                           "scripts/mod/mk_elfconfig.c"]

    expected_project_files = [mock_project_name + ".config",
                          mock_project_name + ".files",
                          mock_project_name + ".includes",
                          mock_project_name + ".creator"]

    expected_filesfile_content = ("arch/x86/tools/relocs_common.c\n"
                                  "scripts/mod/mk_elfconfig.c\n")

    expected_configfile_content = ("#define __KERNEL__ \n"
                                   "#include <generated/autoconf.h>\n")

    expected_includefile_content = ("include \n"
                                    "arch/x86/include\n")

    expected_creatorfile_content = "[General]\n"
    prepare_kernel_project.setup_qt_creator_projectfiles(mock_project_name, mock_kernel_sources)

    for qtcreator_config_path in expected_project_files:
        with open(qtcreator_config_path, 'r') as qtcreator_config_file:
            file_content = qtcreator_config_file.read()
            if qtcreator_config_path.endswith(".config"):
                assert expected_configfile_content == file_content
            if qtcreator_config_path.endswith(".files"):
                assert expected_filesfile_content == file_content
            if qtcreator_config_path.endswith(".includes"):
                assert expected_includefile_content == file_content
            if qtcreator_config_path.endswith(".creator"):
                assert expected_creatorfile_content == file_content
