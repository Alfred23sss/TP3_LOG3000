"""Tests for expression parsing and Flask route behavior."""

import pytest

from app import app, calculate


def test_calculate_addition_expression():
    """`calculate` handles simple valid expressions with spaces."""
    assert calculate(" 2 + 3 ") == 5


def test_calculate_rejects_multiple_operators():
    """`calculate` rejects expressions containing more than one operator."""
    with pytest.raises(ValueError):
        calculate("2+3-1")


def test_calculate_rejects_non_numeric_operands():
    """`calculate` rejects non-numeric operands."""
    with pytest.raises(ValueError):
        calculate("a+3")


def test_post_index_renders_result():
    """POST `/` should render the computed result in the response HTML."""
    client = app.test_client()
    response = client.post("/", data={"display": "2+3"})
    assert response.status_code == 200
    assert b"5.0" in response.data


def test_template_shows_correct_button_labels():
    """Calculator page should expose expected button labels for operators/digits."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b">2<" in response.data
    assert b">8<" in response.data
    assert b">*<" in response.data
    assert b">/<" in response.data
