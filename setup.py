import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Gothic Game"
    version="0.0.1",
    author="Charles Crandall",
    author_email="robloxatme.com@gmail.com",
    url="https://github.com/BillSpyro/Gothic-Game",
    description="A more structured skeleton to be used for my game, Gothic.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
