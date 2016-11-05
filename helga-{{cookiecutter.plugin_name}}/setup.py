from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name="helga-{{ cookiecutter.plugin_name }}",
    version=version,
    description=('{{ cookiecutter.plugin_help }}'),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='irc bot {{ cookiecutter.plugin_name }}',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_{{ cookiecutter.plugin_slug }}'],
    zip_safe=True,
    entry_points = dict(
        helga_plugins = [
            '{{ cookiecutter.plugin_slug}} = helga_{{ cookiecutter.plugin_slug }}:{{ cookiecutter.plugin_slug }}',
        ],
    ),
)
