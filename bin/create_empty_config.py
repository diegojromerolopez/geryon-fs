import argparse
import os
import shutil
import sys


if __name__ == "__main__":
    current_username = os.getlogin()
    parser = argparse.ArgumentParser(description="Create an empty config file in the path you choose")
    parser.add_argument("-c", "--config", type=str, default=f"/home/{current_username}/.geryonfuse.ini",
                        help="configuration file path where the new configuration file will be created",
                        required=False)
    args = parser.parse_args()

    config_path = args.config
    if os.path.isdir(args.config):
        config_path = os.path.join(config_path, ".geryonfuse.ini")
    if os.path.exists(config_path):
        parser.error(f"a config file already exists in {config_path}")
        sys.exit(1)

    root_dir_path = os.path.dirname(os.path.abspath(__file__))
    source_config_file_path = os.path.join(root_dir_path, "..",  "resources", ".geryonfuse.ini")
    shutil.copyfile(src=source_config_file_path, dst=config_path)
