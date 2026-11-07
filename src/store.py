from __future__ import annotations

class FeatureStore:
    def __init__(self):
        self._data: dict[tuple[str, str], dict] = {}
    def put(self, entity: str, key: str, features: dict) -> None:
        self._data[(entity, key)] = dict(features)
    def get(self, entity: str, key: str) -> dict | None:
        return self._data.get((entity, key))
