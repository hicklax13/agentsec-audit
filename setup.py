from setuptools import setup, find_packages

setup(
    name="agentsec-audit",
    version="1.0.0",
    description="Automated security linter and compliance auditor for autonomous AI agents (OWASP ASI-10)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="AgentSec.dev",
    author_email="connorbhickey@hotmail.com",
    url="https://github.com/hicklax13/agentsec-audit",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.0.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0"
    ],
    entry_points={
        "console_scripts": [
            "agentsec=src.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires=">=3.9",
)
