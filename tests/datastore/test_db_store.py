from src.datastore.db_store import get_session


def test_get_session_returns_same_object() -> None:
    assert get_session() is get_session()
