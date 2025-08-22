import pytest
import sys
import os

# Add app folder to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

@pytest.fixture
def sample_fixture():
    return "Hello, World!"

@pytest.fixture
def sample_quiz_data():
    return {
        "question": "What is 2+2?",
        "answers": ["3", "4", "5", "6"],
        "correctAnswer": 1
    }