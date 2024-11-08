import collections

def gale_shapley(pacientes, doadores):
    # Dicionário para manter o emparelhamento
    emparelhamento = {}
    pacientes_ordem = list(pacientes.keys())

    # Enquanto houver pacientes sem emparelhamento
    while pacientes_ordem:
        paciente_chave = pacientes_ordem.pop(0)
        paciente = pacientes[paciente_chave]

        # Verifica as preferências do paciente
        for prioridade in paciente:
            #Se a prioridade estiver livre, o emparelhamento é feito:
            if prioridade not in emparelhamento.values():
                emparelhamento[paciente_chave] = prioridade
                break
            
            elif prioridade in emparelhamento:
                emparelhado_atual = emparelhamento[prioridade].key()
                for i in doadores[prioridade]: 
                    #Se o emparelhado atual é mais prioritário que o paciente atual, nada acontece:
                    if doadores[prioridade.index(emparelhado_atual)] < doadores[prioridade.index(paciente_chave)]:
                        break
                    
                    #Se o o paciente atual e mais prioritário que o emparelhado atual, a troca é feita 
                    else:
                        emparelhamento[paciente_chave] = prioridade
                        pacientes_ordem.append(emparelhado_atual)
                        break
    return emparelhamento

preferencias_pacientes = {
    't1': ['K9', 'K14', 'K8', 'K18', 'K13', 'K7'],
    't2': ['K14', 'K8', 'K9', 'K13', 'K18', 'K7'],
    't3': ['K9', 'K8', 'K14', 'K18', 'K7', 'K13'],
    't4': ['K13', 'K18', 'K7', 'K8', 'K14', 'K9'],
    't5': ['K7', 'K18', 'K13', 'K9', 'K8', 'K14'],
    't6': ['K18', 'K7', 'K13', 'K14', 'K9', 'K8'],
    't7': ['K19', 'K20', 'K2', 'K16', 'K9', 'K14', 'K8', 'K18', 'K7', 'K13', 'K15', 'K1'],
    't8': ['K19', 'K2', 'K20', 'K16', 'K9', 'K14', 'K8', 'K7', 'K18', 'K13', 'K1', 'K15'],
    't9': ['K2', 'K19', 'K20', 'K9', 'K16', 'K14', 'K18', 'K8', 'K7', 'K13', 'K1', 'K15'],
    't10': ['K2', 'K20', 'K19', 'K9', 'K14', 'K16', 'K8', 'K18', 'K7', 'K13', 'K15', 'K1'],
    't11': ['K2', 'K19', 'K16', 'K20', 'K14', 'K9', 'K8', 'K18', 'K7', 'K13', 'K1', 'K15'],
    't12': ['K12', 'K17', 'K9', 'K14', 'K8', 'K18', 'K13', 'K7', 'K10', 'K3', 'K4', 'K11'],
    't13': ['K17', 'K12', 'K9', 'K14', 'K8', 'K18', 'K7', 'K13', 'K10', 'K4', 'K3', 'K11'],
    't14': ['K9', 'K12', 'K17', 'K8', 'K14', 'K7', 'K18', 'K10', 'K13', 'K11', 'K3', 'K4'],
    't15': ['K14', 'K9', 'K7', 'K12', 'K18', 'K17', 'K8', 'K13', 'K10', 'K4', 'K11', 'K3'],
    't16': ['K12', 'K7', 'K11', 'K9', 'K17', 'K14', 'K3', 'K8', 'K4', 'K10', 'K13', 'K18'],
    't17': ['K5', 'K6', 'K9', 'K20', 'K14', 'K8', 'K19', 'K18', 'K17', 'K13', 'K12', 'K2', 'K10', 'K11', 'K3', 'K7', 'K16', 'K15', 'K4', 'K1'],
    't18': ['K5', 'K6', 'K20', 'K9', 'K8', 'K14', 'K18', 'K19', 'K12', 'K13', 'K17', 'K2', 'K3', 'K10', 'K11', 'K16', 'K7', 'K15', 'K1', 'K4'],
    't19': ['K6', 'K5', 'K14', 'K8', 'K20', 'K9', 'K19', 'K18', 'K17', 'K13', 'K12', 'K11', 'K2', 'K10', 'K7', 'K3', 'K15', 'K16', 'K1', 'K4'],
    't20': ['K6', 'K5', 'K8', 'K9', 'K20', 'K14', 'K18', 'K19', 'K12', 'K17', 'K13', 'K11', 'K2', 'K10', 'K3', 'K7', 'K15', 'K16', 'K4', 'K1']
}

preferencias_doadores = {
    'K1': ['t11', 't8', 't10', 't19', 't18', 't20', 't9', 't12'],
    'K2': ['t8', 't10', 't11', 't9', 't12', 't19', 't20', 't18'],
    'K3': ['t16', 't13', 't14', 't15', 't17', 't19', 't20', 't18'],
    'K4': ['t16', 't15', 't13', 't14', 't17', 't18', 't20', 't19'],
    'K5': ['t18', 't19', 't20', 't12', 't15', 't14', 't17', 't16'],
    'K6': ['t19', 't18', 't20', 't5', 't12', 't13', 't16', 't17'],
    'K7': ['t4', 't3', 't5', 't2', 't7', 't1', 't11', 't9', 't10', 't8', 't14', 't13', 't16', 't19', 't20', 't15', 't17', 't18', 't6', 't12'],
    'K8': ['t4', 't2', 't3', 't5', 't1', 't7', 't9', 't11', 't8', 't10', 't14', 't13', 't16', 't20', 't19', 't15', 't17', 't18', 't6', 't12'],
    'K9': ['t3', 't4', 't5', 't2', 't7', 't1', 't11', 't9', 't10', 't8', 't14', 't13', 't16', 't19', 't20', 't15', 't17', 't18', 't6', 't12'],
    'K10': ['t16', 't13', 't14', 't15', 't17', 't20', 't19', 't18'],
    'K11': ['t13', 't16', 't15', 't14', 't17', 't19', 't20', 't18'],
    'K12': ['t16', 't13', 't15', 't14', 't17', 't20', 't19', 't18'],
    'K13': ['t4', 't2', 't5', 't3', 't7', 't1', 't9', 't11', 't8', 't10', 't14', 't13', 't16', 't20', 't19', 't15', 't17', 't18', 't6', 't12'],
    'K14': ['t3', 't4', 't5', 't7', 't2', 't11', 't1', 't9', 't10', 't8', 't14', 't13', 't20', 't19', 't16', 't17', 't15', 't18', 't12', 't6'],
    'K15': ['t8', 't11', 't10', 't19', 't18', 't20', 't9', 't12'],
    'K16': ['t10', 't8', 't11', 't18', 't19', 't20', 't12', 't9'],
    'K17': ['t14', 't16', 't13', 't15', 't19', 't17', 't20', 't18'],
    'K18': ['t5', 't4', 't3', 't2', 't7', 't10', 't9', 't11', 't1', 't14', 't8', 't13', 't20', 't16', 't19', 't15', 't17', 't18', 't6', 't12'],
    'K19': ['t10', 't8', 't11', 't19', 't18', 't20', 't9', 't12'],
    'K20': ['t11', 't8', 't10', 't18', 't19', 't20', 't9', 't12']
}

emparelhamento_final = gale_shapley(preferencias_pacientes, preferencias_doadores)

print("Emparelhamentos obtidos: ")
print(emparelhamento_final)

# Verificar valores repetidos no dicionário de emparelhamento final
valores_repetidos = [item for item, count in collections.Counter(emparelhamento_final.values()).items() if count > 1]

if valores_repetidos:
    print("Pacientes sem pares no emparelhamento final: ", valores_repetidos)
else:
    print("Não há pacientes sem pares no emparelhamento final.")