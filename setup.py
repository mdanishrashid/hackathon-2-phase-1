from setuptools import setup, find_packages

setup(
    name="todo-console-app",
    version="0.1.0",
    description="A simple in-memory todo console application",
    author="Administrator",
    author_email="admin@example.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo-cli=src.cli.main:main',
        ],
    },
    python_requires='>=3.13',
    install_requires=[
        # No external dependencies as per specification
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.13",
    ],
)