from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
    This function returns a list of requirements 

    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read line from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                #Ignore empty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author= 'Sandun Munasinghe',
    author_email='sandunmunasinghe2017@gamil.com',
    packages=find_packages(),
    insatall_requires = get_requirements()
)
