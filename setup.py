import sys

from setuptools import find_packages, setup

MINIMAL_PY_VERSION = (3, 8)
if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError(
        "pyrogram_patch works only with Python {}+".format(
            ".".join(map(str, MINIMAL_PY_VERSION))
        )
    )


setup(
    name="pyrogram_patch",
    version="1.4.0",
    license="MIT",
    author="kotttee",
    python_requires=">=3.8",
    description="This package will add middlewares, routers and fsm for pyrogram",
    url="https://github.com/kotttee/pyrogram_patch/",
    install_requires=["pyrogram>=2.0.0", "redis~=4.5.4"],
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
)
