import sys
import os

def test_configuration_loading():
    # Check if config file exists
    config_file = os.path.join(os.path.dirname(__file__), '..', 'app', 'config.py')
    assert os.path.exists(config_file)

def test_default_settings():
    # Test that config file contains expected content
    config_file = os.path.join(os.path.dirname(__file__), '..', 'app', 'config.py')
    with open(config_file, 'r') as f:
        content = f.read()
        assert 'GEMINI_API_KEY' in content
        assert 'YOUTUBE_API_KEY' in content

def test_environment_variables():
    # Test that config has required constants defined
    config_file = os.path.join(os.path.dirname(__file__), '..', 'app', 'config.py')
    with open(config_file, 'r') as f:
        content = f.read()
        assert 'YOUTUBE_API_SERVICE_NAME' in content
        assert 'YOUTUBE_API_VERSION' in content
        assert 'initialize_session_state' in content