from lambler.content import LocalFile


def test_should_load_local_file_content_by_using_key_as_path():
    assert LocalFile().load("tests/test_content/my_content.txt") == "Hello, world.\nIt works."
