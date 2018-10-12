from math import log2


def entropia(positivo, total):
    diferenca = total - positivo
    if diferenca == 0 or diferenca == total:
        return 0

    a = positivo / total
    b = diferenca / total
    return - a * log2(a) - b * log2(b)


def ganho(geral, total_itens, lista_entropia):
    soma = 0
    for entropia_item in lista_entropia:
        soma += entropia_item[0] * entropia_item[1] / total_itens
    return geral - soma


entropia_geral = entropia(9, 14)

entropia_p_ensolarado = entropia(2, 5)
entropia_p_nublado = entropia(4, 4)
entropia_p_chuvoso = entropia(3, 5)

entropia_t_quente = entropia(2, 4)
entropia_t_moderada = entropia(4, 6)
entropia_t_fresca = entropia(3, 4)

entropia_u_alta = entropia(3, 7)
entropia_u_normal = entropia(6, 7)

entropia_v_forte = entropia(3, 6)
entropia_v_fraco = entropia(6, 8)

ganho_p = ganho(entropia_geral, 14, [(entropia_p_ensolarado, 5), (entropia_p_nublado, 4), (entropia_p_chuvoso, 5)])
ganho_t = ganho(entropia_geral, 14, [(entropia_p_ensolarado, 5), (entropia_p_nublado, 4), (entropia_p_chuvoso, 5)])
ganho_u = ganho(entropia_geral, 14, [(entropia_p_ensolarado, 5), (entropia_p_nublado, 4), (entropia_p_chuvoso, 5)])
ganho_v = ganho(entropia_geral, 14, [(entropia_p_ensolarado, 5), (entropia_p_nublado, 4), (entropia_p_chuvoso, 5)])

max(ganho_p, ganho_t, ganho_v, ganho_u)
