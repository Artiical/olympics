from olympics.__main__ import main
import argparse
import pytest


def test_countries():
    argv = ["countries"]
    main(argv)


def test_collective():
    argv = ["collective"]
    main(argv)


def test_individual():
    argv = ["individual"]
    main(argv)


def test_error():
    with pytest.raises(argparse.ArgumentTypeError):
        argv = ["individual", "--top", "-10"]
        main(argv)


def test_countries_with_top():
    argv = ["countries", "--top", "5"]
    main(argv)


def test_collective_with_top():
    argv = ["collective", "--top", "3"]
    main(argv)


def test_individual_with_top():
    argv = ["individual", "--top", "7"]
    main(argv)


def test_invalid_command():
    with pytest.raises(SystemExit):
        argv = ["invalid_command"]
        main(argv)


def test_missing_argument():
    with pytest.raises(SystemExit):
        argv = []
        main(argv)


# j'ai essayé d'aller plus loin pour les tests
