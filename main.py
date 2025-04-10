import logging
import datasus_db
import duckdb

def main():
    logging.getLogger().setLevel(logging.INFO)

    # Importa os dados hospitalares (SIH_RD)
    datasus_db.datasources.sih_rd.import_sih_rd()

    # Importa os dados ambulatoriais (SIA_PA)
    datasus_db.datasources.sia_pa.import_sia_pa()

    conn = duckdb.connect("datasus.db")

    # Lista as tabelas criadas – isso pode variar, dependendo dos dados importados
    tables = conn.execute("SHOW TABLES;").fetchall()
    print("Tabelas disponíveis:", tables)
    
   

if __name__ == "__main__":
    main()
