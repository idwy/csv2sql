import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
                    "-u",
                    "--username",
                    type=str,
                    help="username of the sql database",
                    default="DEFAULT_USER",
                    )
parser.add_argument(
                    "-p",
                    "--password",
                    type=str,
                    help="password of the sql database",
                    default="DEFAULT_PASSWORD",
                    )
args = parser.parse_args()
