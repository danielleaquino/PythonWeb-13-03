CREATE TABLE IF NOT EXISTS posts(
    id integer primary key autoincrement,
    titulo string not null,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
)