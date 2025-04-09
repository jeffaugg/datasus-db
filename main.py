import logging
import datasus_db
import duckdb

def main():
    logging.getLogger().setLevel(logging.INFO)
    datasus_db.datasources.sim_do.import_sim_do()

    conn = duckdb.connect("datasus.db")

    # Verifique as tabelas disponíveis (isso pode variar de acordo com o datasource importado)
    tables = conn.execute("SHOW TABLES;").fetchall()
    print("Tabelas disponíveis:", tables)


if __name__ == "__main__":
    main()