from setuptools import setup, find_packages

version = '1.0.0'

setup(name="helga-{{ cookiecutter.plugin_name }}",
      version=version,
      description=('{{ cookiecutter.plugin_help }}'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot {{ cookiecutter.plugin_name }}',
      author='{{ cookiecutter.plugin_author }}',
      author_email='{{ cookiecutter.plugin_email }}',
      license='LICENSE',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga-{{ cookiecutter.plugin_name }}'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins = [
              '{{ cookiecutter.plugin_name}}= helga_{{ cookiecutter.plugin_name }}:{{ cookiecutter.plugin_name }}',
          ],
      ),
)
