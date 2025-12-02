from setuptools import find_packages, setup

setup(
    name="mcqgen",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2"],
    author="Kriscillia Kong-ndes",
    author_email="kongndes.kriscillia@gmail.com")





