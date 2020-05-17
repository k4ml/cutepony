
import os
import sys
import pathlib

import click

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.echo('Hello World!')

@click.command()
def start():
    click.echo('Starting cutepony')

cli.add_command(hello)
cli.add_command(start)

def manage():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv[1:])

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cutepony.settings')
    if len(sys.argv) > 1:
        if sys.argv[1] == 'manage':
            return manage()
    import django;django.setup()
    cli()

if __name__ == '__main__':
    main()
