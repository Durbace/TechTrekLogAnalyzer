from setuptools import setup, find_packages

setup(
    name='TechTrekLogAnalyzer',
    version='0.1.0',
    packages=find_packages(),
    author='Tech Trek Team',
    url='https://github.com/Durbace/TechTrekLogAnalyzer',
    install_requires=[
        'pandas',  
        'numpy'   
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
