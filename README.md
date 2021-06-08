# Geryon-fuse

[![License](https://img.shields.io/badge/License-BSD-blue.svg)](https://opensource.org/licenses/BSD)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintainability](https://api.codeclimate.com/v1/badges/ca3b1b760bd7d47c6cef/maintainability)](https://codeclimate.com/github/diegojromerolopez/geryon-fuse/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ca3b1b760bd7d47c6cef/test_coverage)](https://codeclimate.com/github/diegojromerolopez/geryon-fuse/test_coverage)

**WARNING: this project is a prototype, don't use it for actual and important files.
I DECLINE ALL RESPONSIBILITY OF LOST DATA OR OTHER CATASTROPHE YOU SUFFER WHEN USING THIS CODE**

A fuse-based driver for Mongo databases written in Python.

![Geryon fighting with Heracles](resources/geryon.jpg)

[Geryon image](https://www.britishmuseum.org/collection/image/182489001) by courtesy of the British Museum with
CC BY-NC-SA 4.0 license.


## Use

### Configuration file
Make sure you have a file /home/USER/.geryonfs.ini with the following structure:

```
[logger]
name = geryon-fuse
level = debug
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s


[mongofs]
username =
password =
database =
collection =
host =
```

The logger section is not mandatory.

You can also set the file in other path as long as you pass the path in the config variable to the mount python binary.

The easiest way to create an empty configuration file is by calling the create_empty_config script: 

```bash
python geryon-fuse/bin/create_empty_config.py --config /home/USER/my_drives/.geryonfs.ini
```

If you want your config file to be in **/home/USER/.geryonfuse.ini** (recommended) you can omit the config parameter:

```bash
python geryon-fuse/bin/create_empty_config.py
```

### Mount a Mongo file system

```bash
python geryon-fuse/bin/mount_mongofs.py --mountpoint /home/USER/tmp/mongofs --config /home/USER/.geryonfs.ini
```

If your config file is in **/home/USER/.geryonfuse.ini** you can omit the config parameter:

```bash
python geryon-fuse/bin/mount_mongofs.py --mountpoint /home/USER/tmp/mongofs
```

## Tests
TODO.


## License
[BSD 2-clause license](LICENSE).


## TODOs

- [x] Create config format and allow credentials from there.
- [ ] Include some encryption.
- [ ] Include some content checksum.
- [ ] Make docker image with tests.
- [ ] IC in some server that offers free minutes.
- [ ] Measure performance. 


## Collaboration

Collaborations are encouraged. If you're interested, contact me at diegojromerolopez@gmail.com.


## Acknowledgments
  
  * [Writing a FUSE filesystem in Python](https://www.stavros.io/posts/python-fuse-filesystem/)
    by Stavros Korokithakis.
  * [https://github.com/dsoprea/GDriveFS](GDriveFS) project.


## FAQs

### Why the name?

As far as I know, MongoDB took its name from humongous (i.e. enormous), Geryon was a monster from Greek mythology that
lived in Erytheia (current [Cádiz](https://en.wikipedia.org/wiki/C%C3%A1diz)). As he was a giant,
I thought it could be a good name for a MongoDB driver.
