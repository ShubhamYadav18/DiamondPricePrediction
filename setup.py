from setuptools import find_packages,setup
from typing import List

HYEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace ("\n","")for req in requirements]

        if HYEN_E_DOT in requirements:
            requirements.remove(HYEN_E_DOT)
            
        return requirements

setup(
    name="DiamnodPricePrediction",
    version='0.0.1',
    author='Shubham',
    author_email='shubhyadav0018@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)