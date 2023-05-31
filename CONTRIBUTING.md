# Contributing to this project

Currently this document mainly involves a short form deveoper documentation.

First, obtain code by doing a git clone:

    git clone <repository url>

Then, you can either follow these commands or just execute all targets in Makefile.

First, you need to set up a virtual environment. Of course, this is not mandatory, but pretty handy.

I like to place my virtual env in hidden directory called `.venv`.

    python -m venv .venv

or:

    make venv

Then activate your virtual environment:

    .venv/bin/activate

After this, you might like to do pip install. You need optional-dependency called *test* in order to run tests.

    pip install ".[test]"

or:

    make install

After this you can run tests:

    pytest

or:

    make test
