import pandas as pd

# Agrupar motivo da Instauração da TCE por região /OK
# N° total de TCE's em municipios alinhados e não alinhados (coluna alinhamento_tce)

def agregar_motivos_tce(motivo: str) -> str:
    
    motivo_lower = motivo.lower()

    lista_omissao = [
        'omissão no dever de prestar contas',
        'Não encaminhamento da documentação exigida para a prestação de contas',
        'Não encaminhamento de documentação exigida para a prestação de contas'
    ]

    if any(palavra in motivo_lower for palavra in lista_omissao):
        return 'Omissão'

    return 'Outra irregularidade'

url = './database/clean/tces_clean.parquet'
tces_dataframe = pd.read_parquet(url)

tces_dataframe['motivo_instauracao_tce'] = tces_dataframe['motivo_instauracao_tce'].apply(agregar_motivos_tce)

tces_motivo = pd.crosstab(index=[tces_dataframe['ano_referencia'], tces_dataframe['ministerio']],
                          columns=[tces_dataframe['motivo_instauracao_tce'], tces_dataframe['regiao']])

tces_motivo.columns = [
    f'qntd_motivo_instauracao_{m.upper().replace("Ã", "A").replace("Ç", "C").replace(" ", "_")}_{r.lower()}'
    for m, r in tces_motivo.columns
]

tces_alinhamento = pd.crosstab(index=[tces_dataframe['ano_referencia'], tces_dataframe['ministerio']],
                               columns=[tces_dataframe['alinhamento_tce']])

alinhamento = {0: 'NAO_ALINHADO', 1: 'ALINHADO'}
tces_alinhamento.columns = [f'qntd_tces_{alinhamento.get(col, col)}' for col in tces_alinhamento.columns]