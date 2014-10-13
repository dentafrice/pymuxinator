import argparse
from pymuxinator.cli import CLI


def main():
    parser = argparse.ArgumentParser(description='Pymuxinator')
    parser.add_argument('project', help='pymuxinator project to start')

    args = parser.parse_args()

    cli = CLI()
    cli.start(args.project)
