import configparser
import os
import unittest
import fuse
from mongofs.mongooperations import MongoOperations


class TestMongoOperations(unittest.TestCase):
    def setUp(self):
        current_username = os.getlogin()
        config_path = os.environ.get('config_path', f'/home/{current_username}/.geryonfs.ini')
        config = configparser.ConfigParser()
        config.read(config_path)
        self.mongo_operations = MongoOperations(config)
        self.mongo_operations.wipe()

    def test_read(self):
        self.mongo_operations.create(path="/my_file")
        self.mongo_operations.write(path="/my_file", buf=b"this is the content")
        content = self.mongo_operations.read(path="/my_file", length=256)
        self.assertEqual(b"this is the content", content)

    def test_read_non_existent_file(self):
        with self.assertRaises(fuse.FuseOSError) as context:
            self.mongo_operations.read(path="/this/file/does/not/exists", length=256)
        self.assertEqual("[Errno 5] Input/output error", str(context.exception))

    def test_mkdir(self):
        res = self.mongo_operations.mkdir(path="/my")
        self.assertEqual(0, res)

    def test_mkdir_non_existent_path(self):
        with self.assertRaises(fuse.FuseOSError) as context:
            self.mongo_operations.mkdir(path="/my/path/for/mkdir")
        self.assertEqual("[Errno 5] Input/output error", str(context.exception))

    def test_rmdir(self):
        self.mongo_operations.mkdir(path="/my")
        self.mongo_operations.mkdir(path="/my/path1")
        self.mongo_operations.mkdir(path="/my/path2")

        files_before_rmdir = list(self.mongo_operations.readdir(path="/my"))
        res_rmdir = self.mongo_operations.rmdir(path="/my/path1")
        files_after_rmdir = list(self.mongo_operations.readdir(path="/my"))

        self.assertListEqual([".", "..", "path1", "path2"], files_before_rmdir)
        self.assertListEqual([".", "..", "path2"], files_after_rmdir)
        self.assertEqual(0, res_rmdir)

    def test_open_non_existent_file(self):
        path = "/my_file"
        with self.assertRaises(fuse.FuseOSError) as context:
            self.mongo_operations.open(path=path)
        self.assertEqual("[Errno 13] Permission denied", str(context.exception))

    def test_create(self):
        self.mongo_operations.create(path="/my_file")
        content = self.mongo_operations.read(path="/my_file", length=256)
        self.assertEqual(b"", content)

    def test_create_non_existent_path(self):
        with self.assertRaises(fuse.FuseOSError) as context:
            self.mongo_operations.create(path="/this/path/does/not/exist")
        self.assertEqual("[Errno 5] Input/output error", str(context.exception))

    def test_write_file(self):
        path = "/my_file"
        binary_text = b"this is some binary text"

        self.mongo_operations.create(path=path)
        res_write = self.mongo_operations.write(path=path, buf=binary_text)
        actual_text = self.mongo_operations.read(path=path, length=512)

        self.assertEqual(24, res_write)
        self.assertEqual(binary_text, actual_text)

    def test_write_non_existent_file(self):
        with self.assertRaises(fuse.FuseOSError) as context:
            self.mongo_operations.write(path="/non_existent_file", buf=b"this is some binary text")
        self.assertEqual("[Errno 5] Input/output error", str(context.exception))

    def test_truncate(self):
        path = "/my_file"
        binary_text = b"this is some binary text"

        self.mongo_operations.create(path=path)
        self.mongo_operations.write(path=path, buf=binary_text)
        text_before_truncating = self.mongo_operations.read(path=path, length=512)
        self.mongo_operations.truncate(path=path)
        text_after_truncating = self.mongo_operations.read(path=path, length=512)

        self.assertEqual(binary_text, text_before_truncating)
        self.assertEqual(b"", text_after_truncating)
