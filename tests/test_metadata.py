# third-party packages
import mao_45m_merge


# constants
AUTHOR: str = "Akio Taniguchi"
VERSION: str = "0.2.1"


# test functions
def test_author() -> None:
    assert mao_45m_merge.__author__ == AUTHOR


def test_version() -> None:
    assert mao_45m_merge.__version__ == VERSION
