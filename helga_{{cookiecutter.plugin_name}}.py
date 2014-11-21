from helga.plugins import command

@command('{{ cookiecutter.plugin_name }}', help='{{ cookiecutter.plugin_help }}')
def {{ cookiecutter.plugin_name }} (client, channel, nick, message, cmd, args):
    return 'Success!'
