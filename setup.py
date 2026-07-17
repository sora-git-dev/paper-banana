from setuptools import setup


setup(
    name="paperbanana",
    version="1.0.1",
    description="Lightweight academic diagram generator demo",
    author="PaperBanana Team",
    url="https://github.com/sora-git-dev/paper-banana",
    py_modules=["inference"],
    install_requires=["pyyaml>=6.0"],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
