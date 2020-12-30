from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name='pymatgen_plotly',
    description='Structure visualisation for pymatgen object',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.1.0',
    author='Adam Fekete',
    author_email='adam@fekete.co.uk',
    url='https://github.com/fekad/pymatgen-plotly',
    license='BSD',
    platforms="Linux, Mac OS X, Windows",
    keywords=['Jupyter', 'Widgets', 'IPython'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Jupyter',
    ],
    packages=find_packages(),
    python_requires='>=3.4',
    install_requires=[
        'plotly',
        'pymatgen',
    ],
    extras_require={
        'test': [
            'pytest>=3.6',
        ],
        'docs': [
            'mkdocs',
            'mkdocs-material'
        ],
    },
)

if __name__ == '__main__':
    setup(**setup_args)
