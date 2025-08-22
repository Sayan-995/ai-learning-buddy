import sys
import os

def test_utils_module_exists():
    # Check if utils file exists
    utils_file = os.path.join(os.path.dirname(__file__), '..', 'app', 'utils.py')
    assert os.path.exists(utils_file)

def test_youtube_functions():
    # Test that YouTube functions exist
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
    from utils import get_youtube_links, get_youtube_solution_link
    assert callable(get_youtube_links)
    assert callable(get_youtube_solution_link)

def test_solution_search():
    # Test solution search function exists
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
    from utils import get_solution_link
    assert callable(get_solution_link)