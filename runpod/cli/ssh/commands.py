'''
RunPod | CLI | SSH | Commands
'''

import click
from prettytable import PrettyTable
from .functions import get_user_pub_keys, generate_ssh_key_pair

@click.group('ssh')
def ssh_cli():
    '''A collection of CLI functions for SSH.'''

@ssh_cli.command('list-keys')
def list_keys():
    '''
    Lists the SSH keys for the current user.
    '''
    key_list = get_user_pub_keys()

    table = PrettyTable(['Key', 'Type', 'Fingerprint'])

    for key in key_list:
        table.add_row((key['name'], key['type'], key['fingerprint']))

    click.echo(table)

@ssh_cli.command('add-key')
@click.option('--profile', default='default', help='The profile to add the key to.')
@click.option('--key', default=None, help='The public key to add.')
@click.option('--key-file', default=None, help='The file containing the public key to add.')
def add_key(profile, key, key_file):
    '''
    Adds an SSH key to the current user account.
    If no key is provided, one will be generated.
    '''
    click.confirm('Would you like to add an SSH key to your account?', abort=True)
    key_name = click.prompt('Please enter a name for this key', default='RunPod-Key', type=str)
    key_name = key_name.replace(' ', '-')

    private_key, _ = generate_ssh_key_pair(profile, key_name)

    click.echo('The key has been added to your account.')
