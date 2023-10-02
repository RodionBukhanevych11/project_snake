from setuptools import find_packages, setup


with open("requirements.txt") as file:
    requirements = file.read().splitlines()


setup(
    name="snake-project",
    description="Snake project",
    package_dir = {"": "src"},
	install_requires=requirements,
    python_requires=">=3.9,<=3.10",
	packages = find_packages(where="src"),
    include_package_data = True
)