import optparse
import os

from fuse import FUSE
from mongofs.mongooperations import MongoOperations


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-m", "--mountpoint", dest="mountpoint",
                      help="mount point of the file", metavar="MOUNTPOINT")
    (options, args) = parser.parse_args()
    if not options.mountpoint:
        parser.error('mountpoint is required')
    if not os.path.exists(options.mountpoint):
        parser.error(f'mountpoint {options.mountpoint} must exists')

    # TODO: pass as arguments
    username = os.environ["DB_USERNAME"]
    password = os.environ["DB_PASSWORD"]
    database = os.environ["DB_NAME"]
    collection = os.environ["DB_COLLECTION"]
    host = os.environ["DB_HOST"]
    mongo_operations = MongoOperations(username=username, password=password, database=database, host=host,
                                       collection=collection)
    FUSE(operations=mongo_operations, mountpoint=options.mountpoint, nothreads=True, foreground=True)

