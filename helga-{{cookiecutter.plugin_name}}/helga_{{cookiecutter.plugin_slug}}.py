from helga.plugins import command

@command('{{ cookiecutter.plugin_slug }}', help='{{ cookiecutter.plugin_help }}')
def {{ cookiecutter.plugin_slug }}(client, channel, nick, message, cmd, args):
    return 'Success!'
