from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="agentguard",
    version="0.1.0",
    author="Dheeraj Kumar Biswakarma",
    author_email="your@email.com",
    description="Constitutional Governance Kernel for AI Agents — trust decay, approval gates, audit trail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mangomindai/agentguard",
    project_urls={
        "Bug Tracker": "https://github.com/Mangomindai/agentguard/issues",
        "Documentation": "https://github.com/Mangomindai/agentguard#readme",
        "Source": "https://github.com/Mangomindai/agentguard",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "agentguard=agentguard.app:main",
        ],
    },
    keywords=[
        "ai", "agents", "governance", "trust", "security",
        "llm", "langchain", "crewai", "autogen",
        "audit", "approval", "kernel"
    ],
)
