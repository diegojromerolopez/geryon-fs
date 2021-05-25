import argparse
import os
import shutil
import sys
from cryptography.fernet import Fernet

if __name__ == "__main__":
    current_username = os.getlogin()
    parser = argparse.ArgumentParser(description="Create an empty config file in the path you choose")
    parser.add_argument("-c", "--config", type=str, default=f"/home/{current_username}/.geryonfuse.ini",
                        help="configuration file path where the new configuration file will be created",
                        required=False)
    parser.add_argument("-o", "--overwrite", dest='overwrite', action='store_true',
                        help="configuration file path will be overwritten if it already exists", default=False)
    parser.add_argument("-no", "--no-overwrite", dest='overwrite', action='store_false',
                        help="configuration file path will NOT be overwritten if it already exists", default=True)

    args = parser.parse_args()

    config_path = args.config
    if os.path.isdir(args.config):
        config_path = os.path.join(config_path, ".geryonfuse.ini")
    if os.path.exists(config_path):
        if not args.overwrite:
            parser.error(f"a config file already exists in {config_path}")
            sys.exit(1)
        os.unlink(config_path)

    root_dir_path = os.path.dirname(os.path.abspath(__file__))
    source_config_file_path = os.path.join(root_dir_path, "..",  "resources", ".geryonfuse.ini")
    with open(source_config_file_path, "r") as source_config_file:
        source_config_content = source_config_file.read()
        source_config_content = source_config_content.replace("{{fernet_key}}", Fernet.generate_key().decode())
        with open(config_path, "w") as config_file:
            config_file.write(source_config_content)
