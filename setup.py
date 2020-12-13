import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cultureg',
    version='1.0.5',
    url='https://github.com/clementinesacre/ProjetProgra',
    packages=setuptools.find_packages(),
    license='',
    author='Cécile Bonnet, Clémentine Sacré',
    author_email='c.bonnet@students.ephec.be, c.sacre@students.ephec.be',
    description='Jeu permettant d\'améliorer sa culture générale sur n\'importe quel sujet. Permet de rajouter des '
                'sujets et d\'en modifier/supprimer.',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

