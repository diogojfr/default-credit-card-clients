from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    
    requirements=[]

    # reading the requirements.txt file
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        # replacing the '\n' in the string
        requirements = [req.replace('\n','') for req in requirements]

        # removing the '-e .' line
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='default-credit-card-clients',
    version='0.0.1',
    author='Diogo',
    author_email='diogojfr1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)