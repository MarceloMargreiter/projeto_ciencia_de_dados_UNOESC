import extract

if __name__ == "__main__": 
    #Define o caminho do arquivo CSV
    file_path = "data/amazon.csv"
    #Extrai os dados do arquivo CSV
    data = extract.extract_data(file_path)
    #realiza a exploração dos dados
    extract.data_exploration(data)


    #parei na hora 01:09