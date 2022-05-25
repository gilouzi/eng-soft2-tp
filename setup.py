import sys
from distutils.core import setup

if __name__ == "__main__":
    if sys.version_info[:2] < (3, 8):
        print('Requires Python version 3.8 or later')
        sys.exit(-1)

    setup(
        name='engsoft2-ecommerce-project',
        packages=['ecommerce'],
        install_requires=[line.strip() for line in open('requirements.txt')],
        version='1.0',
        description='Dependências para o projeto de Engenharia de Software 2',
        author='Ana Flavia de Miranda Silva, Giovanna Louzi Bellonia, Thiago Martin Poppe'
    )
