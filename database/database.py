import sqlite3
import json
import time
import os

class CacheManager:
    def __init__(self, db_path: str = "cache.db", ttl_seconds: int = 3600):
        self.db_path = db_path
        self.ttl = ttl_seconds  # Время жизни записи в секундах (по умолчанию 1 час)
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
                    timestamp INTEGER NOT NULL,
                    UNIQUE(func_name, input_value)
                )
            """)

    def get_cached(self, func_name: str, input_value: str):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT result, timestamp FROM cache WHERE func_name = ? AND input_value = ?",
            (func_name, input_value)
        )
        row = cursor.fetchone()
        if row:
            result_str, saved_time = row
            current_time = int(time.time())
            if current_time - saved_time < self.ttl:
                try:
                    return json.loads(result_str)
                except json.JSONDecodeError:
                    return None
            else:
                # Истёк TTL — удаляем запись и возвращаем None
                self._delete_entry(func_name, input_value)
                return None
        return None

    def save_to_cache(self, func_name: str, input_value: str, result: dict):
        timestamp = int(time.time())
        with self.connection:
            self.connection.execute(
                "INSERT OR REPLACE INTO cache (func_name, input_value, result, timestamp) VALUES (?, ?, ?, ?)",
                (func_name, input_value, json.dumps(result), timestamp)
            )

    def clear_expired(self):
        """Удаляет устаревшие записи из кэша"""
        threshold = int(time.time()) - self.ttl
        with self.connection:
            self.connection.execute(
                "DELETE FROM cache WHERE timestamp < ?",
                (threshold,)
            )

    def _delete_entry(self, func_name: str, input_value: str):
        with self.connection:
            self.connection.execute(
                "DELETE FROM cache WHERE func_name = ? AND input_value = ?",
                (func_name, input_value)
            )
