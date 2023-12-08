from setuptools import setup,find_packages
from typing import List 

hypenEdot ='-e.'
def getReq(filepath:str)-> List[str]:
    req=[]
    with open(filepath) as fileObj:
        req=fileObj.readlines()
        req=[x.replace("\n","") for x in req]
    if hypenEdot in req:
        req.remove(hypenEdot)
    return req
        


setup(
    
    name='mlprojects',
    version='1.0',
    author='Gursagar',
    packages=find_packages(),
    install_requires=getReq("D:/ML_pr/requirements.txt")
    
)
