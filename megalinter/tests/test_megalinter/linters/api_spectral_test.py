# !/usr/bin/env python3
"""
Unit tests for API linter spectral
This class has been automatically @generated by .automation/build.py, please don't update it manually
"""

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class api_spectral_test(TestCase, LinterTestRoot):
    descriptor_id = "API"
    linter_name = "spectral"
