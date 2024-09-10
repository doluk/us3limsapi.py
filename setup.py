# coding: utf-8

"""
    UltraScan 3 LIMS Database Instance API

    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user's US3 LIMS credentials and sending them with every request as header `Us-Email` and `Us-Password`. Alternatively Basic Auth can be used.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "US3 Lims Api Wrapper"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "aiohttp >= 3.0.0",
    "aiohttp-retry >= 2.8.3",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="UltraScan 3 LIMS Database Instance API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "UltraScan 3 LIMS Database Instance API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    A more machine-accessible version of the UltraScan 3 LIMS functionality. The authentication is done using the user&#39;s US3 LIMS credentials and sending them with every request as header &#x60;Us-Email&#x60; and &#x60;Us-Password&#x60;. Alternatively Basic Auth can be used.
    """,  # noqa: E501
    package_data={"us3api": ["py.typed"]},
)
