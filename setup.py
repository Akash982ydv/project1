from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements from a file and returns them as a list."""
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        
setup(
    name='ml_project',
    version='0.0.1',
    description='A useful module',
    author='Akash Yadav',
    author_email='akash.yadav08280@gmail.com',
    packages=find_packages(), # Automatically finds packages in the directory
    install_requires=get_requirements('requirements.txt') # Project dependencies
)
 