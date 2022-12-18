#!/usr/bin/env python
# coding: utf-8

# In[1]:


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IndividualProject",
    version="0.1.2",
    author="Liana Avagyan",
    author_email="liana_avagyan@edu.aua.am",
    description="Marketing CLV package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avagyanliana/IndividualProject.git",
    packages=setuptools.find_packages(),
    package_data={'package': ['Online_Retail.xlsx']},
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)


# In[ ]:




