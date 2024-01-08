# Contributing to this project

Currently this document mainly involves a short form developer documentation.

## Requirements:

 * Python 3
 * pip
 * make
 * git

And for packaging

 * shiv
 * fpm

In Debian-based systems you can install these by issuing

    sudo apt install python3 python3-venv python3-pip make git

## Set up a development environment

First, obtain code by doing a git clone:

    git clone <repository url>

Then, you can either follow these commands manually or just execute all targets in Makefile.

First, you need to set up a virtual environment. This is mandatory on all systems which wish to follow [PEP 668](https://peps.python.org/pep-0668/) which prevents system-wide installs not handled by the system's package manager.

I like to place my virtual env in hidden directory called `.venv`.

    python3 -m venv .venv

or:

    make venv

Then activate your virtual environment:

    .venv/bin/activate

All commands from now on should be executed in this virtual environment.

Now, you might like to do pip install to install all dependencies. You need optional-dependency called *test* in order to run tests.

    pip install ".[test]"

or:

    make dev-environment

After this you can run tests:

    pytest

or:

    make test
    make integration-test

Makefile has tests divided to two parts: both integration and unit tests. Integration test is something that creates files to disk or does something else that will cause side-effects.

## Developing

All features *MUST* be developed with a test driven development style. I will not accept any contributions containing non-tested code. And testing means automatic testing here.

## Packaging

To make a deb package from this program one can do

    make build

A self-containing Python bundle (made with Shiv) can be created with

    make bundle

and

    make viewer
