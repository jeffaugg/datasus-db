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
        
    # Exemplo de consulta para dados hospitalares SIH
    sih_data = conn.execute("SELECT * FROM sih_rd LIMIT 10;").fetchall()
    print("Algumas linhas da tabela SIH_RD:")
    for row in sih_data:
        print(row)
        
    # Converter para DataFrame antes de exportar para CSV
    sih_df = conn.execute("SELECT * FROM sih_rd LIMIT 10;").df()
    sih_df.to_csv("sih_data.csv", index=False)
    print("Dados exportados para 'sih_data.csv'.")


if __name__ == "__main__":
    main()
