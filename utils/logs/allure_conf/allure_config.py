import allure
from allure_commons.types import Severity
import functools


def allure_test_report(
        *,
        epic: str | None = None,
        title: str | None = None,
        label: str | None = None,
        description: str | None = None,
        severity: Severity | None = None,
        feature: str | None = None,
        story: str | None = None,
        tags: tuple[str, ...] = (),
        suit: str | None = None,
        sub_suit: str | None = None,
        parent_suit: str | None = None
):
    def _allure_test_report(func):
        if epic:
            func = allure.epic(epic)(func)
        if title:
            func = allure.title(title)(func)
        if label:
            func = allure.label(label)(func)
        if description:
            func = allure.description(description)(func)
        if severity:
            func = allure.severity(severity)(func)
        if feature:
            func = allure.feature(feature)(func)
        if story:
            func = allure.story(story)(func)
        if suit:
            func = allure.suite(suit)(func)
        if sub_suit:
            func = allure.sub_suite(sub_suit)(func)
        if parent_suit:
            func = allure.parent_suite(parent_suit)(func)

        for tag in tags:
            func = allure.tag(tag)(func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return _allure_test_report
