"""
test code for the Report class(es)
"""
import pytest

from report import Row, Report

@pytest.fixture
def example_report():
    """
    utility function to provide a fresh report to test with
    """
    report = Report(limit=4)

    populate_report(report)
    return report


def populate_report(report):
    """
    utility function to populate an existing Report with
    some additional data

    :param report: the report object to populate

    The Report will be populated in place
    """
    report.add_row(Row("Natasha", "Smith", "WA"))
    report.add_row(Row("Devin", "Lei", "WA"))
    report.add_row(Row("Bob", "Li", "CA"))
    report.add_row(Row("Tracy", "Jones", "OR"))
    report.add_row(Row("Johnny", "Jakes", "WA"))
    report.add_row(Row("Derek", "Wright", "WA"))
    report.add_row(Row("Jordan", "Cooper", "WA"))
    report.add_row(Row("Mike", "Wong", "WA"))


def test_row_init():
    """
    test that a new row has the proper attributes initialized
    """
    row1 = Row("Joe", "Camel", "WA")

    assert row1.fname == "Joe"
    assert row1.lname == "Camel"
    assert row1.state == "WA"


def test_row_id_unique():
    """ two Rows should have unique IDs """
    row1 = Row("Joe", "Camel", "WA")
    row2 = Row("Bob", "Camel", "WA")

    assert row1.id != row2.id


def test_report_length(example_report):
    """
    test report size method
    """
    # the test data has 8 rows
    assert example_report.size() == 8


def test_number_of_pages(example_report):
    """
    check that the number of pages is correct
    """
    assert example_report.get_number_of_pages() == 2


def test_row_str(mocker):
    mocker.patch("report.uuid4", return_value="Cane")
    row1 = Row("Joe", "Camel", "WA")
    assert str(row1) == "ID = Cane, First Name = Joe, Last Name = Camel, State = WA"


def test_add_row():
    rep = Report(5)
    row1 = Row("Alessandro", "Varisco", "IT")
    rep.add_row(row1)
    assert len(rep.rows) == 1
    assert rep.rows[-1] == row1

def test_remove_row(example_report):
    row1 = example_report.rows[3]
    example_report.remove_row(row1.id)
    assert example_report.size() == 7
    assert row1 not in example_report.rows



