# Geryon-fuse

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
[mongofs]
username =
password =
database =
collection =
host =
```

You can also set the file in other path as long as you pass the path in the config variable to the mount python binary.

### Command to mount the Mongo file system

```bash
python geryon-fs/bin/mount.py --mountpoint /home/USER/tmp/mongofs --config /home/USER/.geryonfs.ini
```

If your config file is in **/home/USER/.geryonfs.ini** you can omit the config parameter:

```bash
python geryon-fs/bin/mount.py --mountpoint /home/USER/tmp/mongofs
```

## Tests



## License
[LICENSE](LICENSE).


## TODOs

- [x] Create config format and allow credentials from there.
- [ ] Include some cypher.
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
