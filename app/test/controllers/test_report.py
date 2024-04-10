import pytest

from app.controllers import ReportController


def test_get_report(app, init_report_test_data):
    report, error = ReportController.get_report()
    pytest.assume(error is None)
    pytest.assume("best_customers" in report)
    pytest.assume("highest_revenue_by_month" in report)
    pytest.assume("most_requested_ingredient" in report)


def test_best_customers(app, init_report_test_data):
    best_customers = ReportController.get_best_customers()
    for customer in best_customers:
        pytest.assume("client_name" in customer)
        pytest.assume("orders_count" in customer)
        pytest.assume("total_spent" in customer)


def test_highest_revenue_by_month(app, init_report_test_data):
    highest_revenue = ReportController.get_highest_revenue_by_month()
    pytest.assume("month" in highest_revenue)
    pytest.assume("revenue" in highest_revenue)


def test_most_requested_ingredient(app, init_report_test_data):
    ingredient = ReportController.get_most_requested_ingredient()
    pytest.assume(ingredient is not None)
    pytest.assume("name" in ingredient)
    pytest.assume("price" in ingredient)
