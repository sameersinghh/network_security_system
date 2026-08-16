'''The setup.py file is an essential part of packaging and distributing
python projects.It is used by setup tools (or distribute python versions) 
to define the configuration of your project, such as its metadata, dependencies or more.'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()-> list[str]:
    '''this function gets requirements from requirements.txt'''
    requirement_lst:list[str] = []
    try:
        with open ('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e.':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirement_lst

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sameer Singh",
    author_email="sameersinghh.general@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


