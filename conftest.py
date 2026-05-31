import pytest

from utilities.logger import logger

pytest_plugins = [
    "fixtures.llm_fixture",
    "fixtures.rag_fixture",
    "fixtures.agent_fixture",
    "fixtures.api_fixture",
    "fixtures.browser_fixture",
]


def pytest_addoption(parser):
    parser.addoption(
        "--target-env",
        action="store",
        default="qa",
        help="Target environment for API and UI tests.",
    )
    parser.addoption(
        "--report-dir",
        action="store",
        default="reports",
        help="Directory where HTML reports are written.",
    )


@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--target-env")


@pytest.fixture(scope="session")
def report_dir(request):
    return request.config.getoption("--report-dir")


def pytest_configure(config):
    config.addinivalue_line("markers", "llm: mark test as LLM evaluation")
    config.addinivalue_line("markers", "rag: mark test as retrieval augmented generation")
    config.addinivalue_line("markers", "agent: mark test as agent reasoning")
    config.addinivalue_line("markers", "api: mark test as API validation")
    config.addinivalue_line("markers", "ui: mark test as UI validation")
    config.addinivalue_line("markers", "safety: mark test as safety validation")
    config.addinivalue_line("markers", "performance: mark test as performance validation")
    config.addinivalue_line("markers", "smoke: mark test as smoke suite")
    config.addinivalue_line("markers", "regression: mark test as regression suite")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        logger.error("Test failed", extra={"test_name": item.name})
        if "data" in item.funcargs:
            logger.error("Failed test data", extra={"data": item.funcargs["data"]})


def pytest_collection_modifyitems(config, items):
    if config.getoption("--collect-only"):
        return
    for item in items:
        if "smoke" in item.keywords:
            logger.debug(f"Smoke item selected: {item.name}")
