import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--llm", action="store_true",
        help="Run tests that require LLM",
    )
    parser.addoption(
        "--reddit", action="store_true",
        help="Run tests that require Reddit",
    )


def pytest_runtest_setup(item):
    if 'llm' in item.keywords and not item.config.getoption("--llm"):
        pytest.skip("need --llm option to run this test")
