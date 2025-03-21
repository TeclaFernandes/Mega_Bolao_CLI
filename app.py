import pandas as pd

def verificar_jogos(planilha, numeros_sorteados):
    try:
        print(f"Lendo a planilha: {planilha}")
        df = pd.read_excel(planilha)
        
        if 'Nome' not in df.columns or 'Jogo' not in df.columns:
            print("Erro: A planilha deve conter as colunas 'Nome' e 'Jogo'.")
            return None
        
        print("Convertendo os jogos para listas de números...")
        df['Jogo'] = df['Jogo'].apply(lambda x: list(map(int, str(x).split('-'))))
        
        print("Calculando acertos para cada participante...")
        df['Acertos'] = df['Jogo'].apply(lambda jogo: len(set(jogo) & set(numeros_sorteados)))
        
        df = df.sort_values(by='Acertos', ascending=False)
        
        return df
    except Exception as e:
        print(f"Erro ao processar a planilha: {e}")
        return None

def main():
    planilha = 'jogos.xlsx'
    
    try:
        entrada = input("Digite os números sorteados separados por vírgula: ")
        numeros_sorteados = list(map(int, entrada.split(',')))
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números separados por vírgula.")
        return
    
    resultado = verificar_jogos(planilha, numeros_sorteados)
    
    if resultado is not None:
        print("\nResultados:")
        print(resultado[['Nome', 'Acertos']])
        
        resultado.to_excel('resultado_bolao.xlsx', index=False)
        print("\nResultados salvos em 'resultado_bolao.xlsx'.")
    else:
        print("Não foi possível processar os jogos. Verifique os dados e tente novamente.")

if __name__ == "__main__":
    main()