import pytest


def test_get_report(client, report_uri, init_report_test_data):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith("200"))
    report = response.json
    for key in [
        "best_customers",
        "highest_revenue_by_month",
        "most_requested_ingredient",
    ]:
        pytest.assume(key in report)
