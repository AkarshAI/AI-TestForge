import pytest

from core.llm_client import LLMClient


@pytest.fixture
def llm_client():

    return LLMClient()




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call":

        if report.failed:

            print(
                f"\nFAILED TEST: {item.name}"
            )

            if "data" in item.funcargs:

                test_data = item.funcargs[
                    "data"
                ]

                print(
                    f"Question: "
                    f"{test_data['question']}"
                )