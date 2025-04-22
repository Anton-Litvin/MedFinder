import sqlite3
import json
import os

class CacheManager:
    def __init__(self, db_path: str = "cache.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    func_name TEXT NOT NULL,
                    input_value TEXT NOT NULL,
                    result TEXT NOT NULL,
                    UNIQUE(func_name, input_value)
                )
            """)

    def get_cached(self, func_name: str, input_value: str):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT result FROM cache WHERE func_name = ? AND input_value = ?",
            (func_name, input_value)
        )
        row = cursor.fetchone()
        if row:
            try:
                return json.loads(row[0])
            except json.JSONDecodeError:
                return None
        return None

    def save_to_cache(self, func_name: str, input_value: str, result: dict):
        with self.connection:
            self.connection.execute(
                "INSERT OR REPLACE INTO cache (func_name, input_value, result) VALUES (?, ?, ?)",
                (func_name, input_value, json.dumps(result))
            )
