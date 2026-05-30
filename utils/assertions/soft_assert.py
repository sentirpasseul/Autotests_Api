import pytest


class SoftAssert:
    def __init__(self):
        self._errors = []

    def check(self, condition: bool, message: str = ""):
        if not condition:
            self._errors.append(message or "Condition failed")

    def assert_all(self):
        if self._errors:
            formatted = "\n".join(f"  [{i + 1}] {e}" for i, e in enumerate(self._errors))
            raise AssertionError(f"Soft assert failures:\n{formatted}")
