import logging
import datasus_db
import duckdb
import pandas as pd

def main():
    logging.getLogger().setLevel(logging.INFO)
    
    # Conecta ao banco de dados
    conn = duckdb.connect("datasus.db")
    
    # Verifica as tabelas disponíveis
    tables = conn.execute("SHOW TABLES;").fetchall()
    print("Tabelas disponíveis:", tables)
    
    # Carrega os dados em um DataFrame
    df = conn.execute("SELECT * FROM sim_do").fetchdf()
    
    # Exporta o DataFrame para CSV (sem o índice)
    df.to_csv("sim_do_data.csv", index=False)
    print("Dados exportados para 'sim_do_data.csv'.")

if __name__ == "__main__":
    main()
