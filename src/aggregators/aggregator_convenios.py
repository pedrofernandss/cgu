import pandas as pd

def ler_dados(url: str) -> pd.DataFrame:
    tces_dataframe = pd.read_parquet(url)

    return tces_dataframe

def agrupar_qntd_convenios_ministerio(dataframe: pd.DataFrame) -> pd.DataFrame:
    contagem_convenios_por_ministerio = dataframe.groupby(
    ['ministerio', 'ano_referencia']).size().reset_index(name='quantidade_convenios')

    return contagem_convenios_por_ministerio

