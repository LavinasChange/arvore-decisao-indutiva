tabela = [
    {"dia": "D1", "perspectiva": "Ensolarado", "temperatura": "Quente", "umidade": "Alta", "vento": "Fraco",
     "jogar_tenis": "Não"},
    {"dia": "D2", "perspectiva": "Ensolarado", "temperatura": "Quente", "umidade": "Alta", "vento": "Forte",
     "jogar_tenis": "Não"},
    {"dia": "D3", "perspectiva": "Nublado", "temperatura": "Quente", "umidade": "Alta", "vento": "Fraco",
     "jogar_tenis": "Sim"},
    {"dia": "D4", "perspectiva": "Chuvoso", "temperatura": "Moderada", "umidade": "Alta", "vento": "Fraco",
     "jogar_tenis": "Sim"},
    {"dia": "D5", "perspectiva": "Chuvoso", "temperatura": "Fresca", "umidade": "Normal", "vento": "Fraco",
     "jogar_tenis": "Sim"},
    {"dia": "D6", "perspectiva": "Chuvoso", "temperatura": "Fresca", "umidade": "Normal", "vento": "Forte",
     "jogar_tenis": "Não"},
    {"dia": "D7", "perspectiva": "Nublado", "temperatura": "Fresca", "umidade": "Normal", "vento": "Forte",
     "jogar_tenis": "Sim"},
    {"dia": "D8", "perspectiva": "Ensolarado", "temperatura": "Moderada", "umidade": "Alta", "vento": "Fraco",
     "jogar_tenis": "Não"},
    {"dia": "D9", "perspectiva": "Ensolarado", "temperatura": "Fresca", "umidade": "Normal", "vento": "Fraco",
     "jogar_tenis": "Sim"},
    {"dia": "D10", "perspectiva": "Chuvoso", "temperatura": "Moderada", "umidade": "Normal", "vento": "Fraco",
     "jogar_tenis": "Sim"},
    {"dia": "D11", "perspectiva": "Ensolarado", "temperatura": "Moderada", "umidade": "Normal", "vento": "Forte",
     "jogar_tenis": "Sim"},
    {"dia": "D12", "perspectiva": "Nublado", "temperatura": "Moderada", "umidade": "Alta", "vento": "Forte",
     "jogar_tenis": "Sim"},
    {"dia": "D13", "perspectiva": "Nublado", "temperatura": "Quente", "umidade": "Normal", "vento": "Fraco",
     "jogar_tenis": "Sim"},
    {"dia": "D14", "perspectiva": "Chuvoso", "temperatura": "Moderada", "umidade": "Alta", "vento": "Frote",
     "jogar_tenis": "Não"}
]
a = []
for item in tabela:
    a.append(item['vento'])
print(a)
