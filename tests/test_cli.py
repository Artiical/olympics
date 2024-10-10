from io import StringIO

from olympics import cli
from click.testing import CliRunner


def test_top_countries():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert "Top" in text
    assert "Country" in text
    assert "Gold" in text
    assert "Silver" in text
    assert "Bronze" in text
    assert "Total" in text


def test_top_collective():
    string = StringIO()
    cli.top_collective(file=string)
    text = string.getvalue()
    assert "Top" in text
    assert "Country" in text
    assert "Medals" in text


def test_top_individual():
    string = StringIO()
    cli.top_individual(file=string)
    text = string.getvalue()
    assert "Top" in text
    assert "Name" in text
    assert "Gender" in text
    assert "Country" in text
    assert "Medals" in text


def test_top_countries_with_custom_top():
    string = StringIO()
    cli.top_countries(top=5, file=string)
    text = string.getvalue()
    assert "Top 5 countries" in text


def test_top_collective_with_custom_top():
    string = StringIO()
    cli.top_collective(top=5, file=string)
    text = string.getvalue()
    assert "Top 5 collective events" in text


def test_top_individual_with_custom_top():
    string = StringIO()
    cli.top_individual(top=5, file=string)
    text = string.getvalue()
    assert "Top 5 individual events" in text


def test_search_countries_cli():
    runner = CliRunner()
    result = runner.invoke(cli.search_countries, ["uga"])
    assert result.exit_code == 0
    assert "Uganda" in result.output
    assert "Portugal" in result.output
