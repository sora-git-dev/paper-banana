from setuptools import setup, find_packages

setup(
    name="paperbanana",
    version="1.0.0",
    description="AI-Powered Academic Diagram Generator",
    author="PaperBanana Team",
    author_email="team@paper-banana.net",
    url="https://github.com/sora-git-dev/paper-banana",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "diffusers>=0.21.0",
        "pillow>=9.0.0",
        "numpy>=1.24.0",
        "svgwrite>=1.4.0",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
