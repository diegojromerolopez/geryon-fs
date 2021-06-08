import argparse
import configparser
import os
import sys
from fuse import FUSE
from geryonfuse import MongoOperations


if __name__ == "__main__":
    current_username = os.getlogin()
    parser = argparse.ArgumentParser(description="Mount a mongodb instance as a file sytem")
    parser.add_argument("-c", "--config", type=str, default=f"/home/{current_username}/.geryonfuse.ini",
                        help="configuration file", required=False)
    parser.add_argument("-m", "--mountpoint", type=str, help="mount point of the file", required=True)

    args = parser.parse_args()

    if not os.path.exists(args.config):
        parser.error(f"config file {args.config} must exists")
        sys.exit(1)

    if not os.path.exists(args.mountpoint):
        parser.error(f"mountpoint {args.mountpoint} must exists")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(args.config)

    mongo_operations = MongoOperations(config=config)
    FUSE(operations=mongo_operations, mountpoint=args.mountpoint, nothreads=True, foreground=True)

