# Geryon-fs

**WARNING: this project is a prototype, don't use it for actual and important files.
I DECLINE ALL RESPONSIBILITY OF LOST DATA OR OTHER CATASTROPHE YOU SUFFER**

A fuse-based driver for Mongo databases writter in Python.

![Geryon fighting with Heracles](resources/geryon.jpg)

[Geryon image](https://www.britishmuseum.org/collection/image/182489001) by courtesy of the British Museum with
CC BY-NC-SA 4.0 license.

## Use

### Environment variables
Make sure you have this environment variables or create your own main python file that
reads from a config file.

DB_PASSWORD=<your pass>;
DB_NAME=<your db>;
DB_COLLECTION=<your collection>;
DB_HOST=<your db host>;
DB_USERNAME=<your username>

### Command to mount the Mongo file system

```bash
python mongofs-drive/main.py
```

## License
[LICENSE](LICENSE)

## TODOs

  * [] Create config format and allow credentials from there.
  * [] Make docker image with tests.
  * [] IC in some server that offers free minutes.

## Acknowledgments
  
  * [Writing a FUSE filesystem in Python](https://www.stavros.io/posts/python-fuse-filesystem/)
    by Stavros Korokithakis.
  * [https://github.com/dsoprea/GDriveFS](GDriveFS) project.
