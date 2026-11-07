from src.store import FeatureStore
def test_roundtrip():
    s = FeatureStore()
    s.put("user", "u1", {"recency": 3, "freq": 12})
    assert s.get("user", "u1")["freq"] == 12
    assert s.get("user", "missing") is None
