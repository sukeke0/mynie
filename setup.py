from setuptools import setup, find_packages

package_version = '1.0.0'
package_name = 'mynie'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=package_name,
    version=package_version,
    description='Add your own parser to Genie Parser.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='sukeke',
    packages=find_packages(),
    install_requires="genie",
    entry_points={
        'genie.libs.parser': [
            f"{package_name} = {package_name}:add_my_parsers"
        ]
    }
)
