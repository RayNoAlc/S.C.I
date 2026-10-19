# -*- coding: utf-8 -*-
"""
Script to build the complete Prova 3 dataset for S.C.I:
- CAT_NAMES_P3
- SUBTOPICS_P3
- QUESTIONS_P3 (105 questions, 35 per category)
- HARD_QUESTIONS_P3 (21 complex ranked questions, 7 per category)
- STUDY_CARDS_P3 (32 flashcards)
- MAP_THEMES_P3 (3 map themes)
- MAP_CONCEPTS_P3 (24 concept nodes)
- Integrates into PROVAS in index.html
"""
import json, re

CAT_NAMES_P3 = [
    "Estudos Epidemiológicos e Levantamentos em Saúde Bucal",
    "Epidemiologia da Cárie, Erupção e ICDNT",
    "Fluorose Dentária e Doença Periodontal"
]

SUBTOPICS_P3 = [
    {"cat": 0, "key": "tipos_estudos", "label": "Tipos de Estudos Epidemiológicos", "desc": "Descritivos x Analíticos, Observacionais x Experimentais"},
    {"cat": 0, "key": "desenhos_pesquisa", "label": "Desenhos de Pesquisa", "desc": "Transversal, Coorte, Caso-Controle, Ecológico, RR e OR"},
    {"cat": 0, "key": "planejamento_levantamentos", "label": "Planejamento de Levantamentos", "desc": "Equipe (examinador, anotador, monitor), regras OMS, biossegurança"},
    {"cat": 0, "key": "calibracao_concordancia", "label": "Calibração e Concordância", "desc": "Intra/Interexaminador, etapas, coeficiente Kappa"},
    {"cat": 1, "key": "cronologia_erupcao", "label": "Cronologia de Erupção e Notação", "desc": "Nomenclatura FDI, cronologia permanente/decídua, Moyers"},
    {"cat": 1, "key": "indices_carie", "label": "Índices de Cárie (CPO-D, ceo-d, ICDAS)", "desc": "CPO-D, ceo-d, CPO-S 148 faces, ICDAS 0-6, SB Brasil"},
    {"cat": 1, "key": "icdnt_condicao", "label": "ICDNT — Condição Dental", "desc": "Códigos 0/A a 9/-, coroa e raiz, regras de exame OMS"},
    {"cat": 1, "key": "icdnt_necessidade", "label": "ICDNT — Necessidade de Tratamento", "desc": "Códigos 0 a 9, restaurações, HMI, selante e regras"},
    {"cat": 2, "key": "fluorose_clinica", "label": "Fluorose Dentária e Fatores de Risco", "desc": "Etiologia, amelogênese, dose de Burt, ingestão de dentifrício"},
    {"cat": 2, "key": "indices_fluorose", "label": "Índices de Fluorose (Dean e TF)", "desc": "Índice de Dean 0-5, regra dos 2 dentes, Índice TF, IFD"},
    {"cat": 2, "key": "diagnostico_diferencial", "label": "Diagnóstico Diferencial do Esmalte", "desc": "Fluorose x Mancha branca cárie, HMI, Turner, Tetraciclina"},
    {"cat": 2, "key": "epidemiologia_periodontal", "label": "Epidemiologia Periodontal (CPI e PIP)", "desc": "CPI 0-4/X, PIP, sonda OMS Trinity, sextantes, SB Brasil"}
]

MAP_THEMES_P3 = [
    {"key": "epi", "icon": "<i class=\"ph ph-chart-line-up\"></i>", "name": "Estudos Epidemiológicos e Levantamentos", "fill": "#7c3aed", "bg": "rgba(124,58,237,0.14)", "border": "rgba(167,139,250,0.35)", "tc": "#c4b5fd", "catIdx": 0},
    {"key": "carie", "icon": "<i class=\"ph ph-tooth\"></i>", "name": "Epidemiologia da Cárie, Erupção e ICDNT", "fill": "#059669", "bg": "rgba(5,150,105,0.14)", "border": "rgba(52,211,153,0.35)", "tc": "#6ee7b7", "catIdx": 1},
    {"key": "fluorperio", "icon": "<i class=\"ph ph-shield-check\"></i>", "name": "Fluorose Dentária e Doença Periodontal", "fill": "#0284c7", "bg": "rgba(2,132,199,0.14)", "border": "rgba(56,189,248,0.35)", "tc": "#7dd3fc", "catIdx": 2}
]

MAP_CONCEPTS_P3 = [
    {"id": "estudos_epidemiologicos", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Estudos Epidemiológicos", "desc": "A epidemiologia investiga a distribuição e determinantes das doenças na população para subsidiar intervenções de saúde pública. Difere do método clínico pelo foco coletivo, raciocínio bioestatístico e ênfase preventiva.", "connects": ["estudos_descritivos_analiticos", "estudo_transversal"], "crossConnects": []},
    {"id": "estudos_descritivos_analiticos", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Descritivos x Analíticos", "desc": "Descritivos respondem quem, onde e quando, gerando hipóteses epidemiológicas. Analíticos testam hipóteses causais investigando a relação entre fatores de exposição e desfechos com grupos controle.", "connects": ["estudos_epidemiologicos", "estudo_transversal", "fontes_dados"], "crossConnects": []},
    {"id": "fontes_dados", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Fontes de Dados", "desc": "Dados secundários provêm de sistemas rotineiros oficiais (SIM, SINASC, SISAB, IBGE); dados primários são levantamentos locais e inquéritos nacionais coletados diretamente para a pesquisa (ex: SB Brasil).", "connects": ["estudos_descritivos_analiticos", "estudo_ecologico"], "crossConnects": []},
    {"id": "estudo_transversal", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Estudo Transversal", "desc": "Estudo observacional seccional que avalia simultaneamente exposição e doença em um único momento. Mede a prevalência populacional, ideal para diagnóstico de base e planejamento de serviços de saúde.", "connects": ["estudos_descritivos_analiticos", "estudo_coorte"], "crossConnects": ["indice_cpod"]},
    {"id": "estudo_coorte", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Estudo de Coorte", "desc": "Estudo longitudinal prospectivo ou retrospectivo que acompanha indivíduos expostos e não expostos livres da doença no tempo. Mede a incidência e calcula o Risco Relativo (RR), sendo imune ao viés de memória.", "connects": ["estudo_transversal", "estudo_caso_controle"], "crossConnects": []},
    {"id": "estudo_caso_controle", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Estudo Caso-Controle", "desc": "Estudo analítico retrospectivo que parte de indivíduos doentes (casos) e sadios (controles), investigando o passado para quantificar a exposição pregressa (Odds Ratio). Ideal para doenças raras.", "connects": ["estudo_coorte", "estudo_ecologico"], "crossConnects": []},
    {"id": "estudo_ecologico", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Estudo Ecológico e Falácia", "desc": "Estudo correlacional em que a unidade de observação é a população como um todo (cidades, países). Sujeito à falácia ecológica (inferir relações individuais a partir de médias agregadas).", "connects": ["estudo_caso_controle", "estudos_experimentais"], "crossConnects": []},
    {"id": "estudos_experimentais", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Ensaios Experimentais", "desc": "Estudos em que o pesquisador manipula ativamente a exposição (variável independente). Divide-se em Ensaios Clínicos Randomizados (pacientes), Ensaios de Campo (saudáveis) e de Comunidade.", "connects": ["estudo_ecologico", "equipe_levantamento"], "crossConnects": ["calibracao_kappa"]},
    {"id": "equipe_levantamento", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Equipe do Levantamento", "desc": "Tríade da OMS: Examinador (cirurgião-dentista clínico, EPI completo, troca de luvas a cada mucosa), Anotador (preenche fichas, não deixa vazios) e Monitor (fluxo e escovação supervisionada).", "connects": ["calibracao_kappa"], "crossConnects": []},
    {"id": "calibracao_kappa", "resumoUrl": "./resumo_prova3.html", "th": "epi", "name": "Calibração e Estatística Kappa", "desc": "Padronização diagnóstica intra e interexaminador em 4 etapas (teórica, clínica 6-8 crianças, calibração 15-20 pessoas e discussão). O índice Kappa varia de <0.20 (pobre) a 0.81-1.00 (quase perfeita).", "connects": ["equipe_levantamento", "estudos_experimentais"], "crossConnects": ["regras_exame_oms"]},
    {"id": "cronologia_erupcao_node", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "Cronologia de Erupção", "desc": "Sequência cronológica da emergência dental. Meninas são 5 meses mais precoces que meninos. O primeiro molar permanente erupciona aos 6-7 anos atrás dos decíduos sem esfoliação.", "connects": ["notacao_fdi", "regras_exame_oms"], "crossConnects": []},
    {"id": "notacao_fdi", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "Notação FDI / OMS", "desc": "Sistema de dois dígitos: 1º dígito indica o quadrante (1-4 permanente, 5-8 decíduo); 2º dígito indica o dente a partir da linha média (1-8 permanente, 1-5 decíduo).", "connects": ["cronologia_erupcao_node", "indice_cpod"], "crossConnects": []},
    {"id": "indice_cpod", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "Índice CPO-D e SB Brasil", "desc": "Mede ataque de cárie em dentes permanentes (Cariados + Perdidos por cárie + Obturados). Idade-índice global OMS de 12 anos. O SB Brasil registrou 2,78 em 2003 e expressiva queda nas últimas décadas.", "connects": ["indice_ceod", "indice_cpos"], "crossConnects": ["icdnt_coroa"]},
    {"id": "indice_ceod", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "Índice ceo-d (Decíduos)", "desc": "Adaptação para dentes decíduos na idade-chave de 5 anos: cariados (c) + indicação de extração (e) + obturados (o). Não computa dentes perdidos (P) para evitar confusão com esfoliação fisiológica.", "connects": ["indice_cpod"], "crossConnects": []},
    {"id": "indice_cpos", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "Índice CPO-S (Superfícies)", "desc": "Avaliação detalhada por superfícies dentárias (148 faces nos 32 dentes). Dentes posteriores têm 5 superfícies e anteriores 4 superfícies. Dentes perdidos por cárie computam 5 faces posteriores e 4 anteriores.", "connects": ["indice_cpod", "sistema_icdas"], "crossConnects": []},
    {"id": "sistema_icdas", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "Sistema ICDAS", "desc": "Sistema clínico de detecção de cárie com escores de 0 (hígido) a 6 (cavidade extensa >50% em dentina), permitindo avaliar desde lesões iniciais subsuperficiais até destruições coronárias francas.", "connects": ["indice_cpos", "icdnt_coroa"], "crossConnects": []},
    {"id": "icdnt_coroa", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "ICDNT — Condição Dental", "desc": "Índice da OMS que codifica a coroa (0/A hígido a 9/- excluído) e avalia cárie radicular separadamente. Incorpora o dente restaurado com cárie (código 2/C) e perdido por outra razão (código 5).", "connects": ["icdnt_tratamento", "regras_exame_oms"], "crossConnects": ["indice_cpod"]},
    {"id": "icdnt_tratamento", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "ICDNT — Tratamento", "desc": "Coleta necessidades de intervenção: 0 nenhum, 1 rest 1 face, 2 rest 2+ faces, 3 coroa/HMI posterior, 4 faceta/HMI anterior, 5 endodontia, 6 extração, 7 flúor remineralizante, 8 selante e 9 sem informação.", "connects": ["icdnt_coroa", "regras_exame_oms"], "crossConnects": []},
    {"id": "regras_exame_oms", "resumoUrl": "./resumo_prova3.html", "th": "carie", "name": "Regras Especiais da OMS", "desc": "Dente irrompido = tocado pela sonda; supranumerários ignorados; permanente sobrepõe decíduo; na dúvida atribuir hígido ou restaurado sem cárie. Proibido usar sonda exploradora pontiaguda.", "connects": ["icdnt_tratamento", "cronologia_erupcao_node"], "crossConnects": ["calibracao_kappa"]},
    {"id": "fluorose_biologia", "resumoUrl": "./resumo_prova3.html", "th": "fluorperio", "name": "Fluorose: Fatores de Risco", "desc": "Ingestão crônica excessiva de flúor durante a maturação do esmalte. O limite seguro de Burt é 0,05-0,07 mg F/kg/dia. Crianças de 2 a 3 anos ingerem cerca de 48% do creme dental durante a escovação.", "connects": ["indice_dean", "diag_diferencial_esmalte"], "crossConnects": []},
    {"id": "indice_dean", "resumoUrl": "./resumo_prova3.html", "th": "fluorperio", "name": "Índice de Dean e IFD", "desc": "Classifica a fluorose em 0 Normal, 1 Questionável, 2 Muito Leve (<25%), 3 Leve (25-50%), 4 Moderada (desgaste) e 5 Severa (pits). Registro pelos dois dentes mais afetados pelo menor escore.", "connects": ["fluorose_biologia", "indice_tf"], "crossConnects": []},
    {"id": "indice_tf", "resumoUrl": "./resumo_prova3.html", "th": "fluorperio", "name": "Índice TF (0 a 9)", "desc": "Índice de Thylstrup & Fejerskov fundamentado na porosidade biológica do esmalte após secagem prolongada. Classifica em 10 graus (0 a 9), sendo sensível para detectar perdas estruturais focais de esmalte.", "connects": ["indice_dean", "diag_diferencial_esmalte"], "crossConnects": []},
    {"id": "diag_diferencial_esmalte", "resumoUrl": "./resumo_prova3.html", "th": "fluorperio", "name": "Diagnóstico Diferencial do Esmalte", "desc": "Diferencia fluorose (simétrica em cúspides/bordas) de mancha branca de cárie (assimétrica cervical), HMI (molares e incisivos), Dente de Turner (unilateral por trauma/abscesso) e mancha por tetraciclina.", "connects": ["indice_dean", "indice_cpi"], "crossConnects": ["sistema_icdas"]},
    {"id": "indice_cpi", "resumoUrl": "./resumo_prova3.html", "th": "fluorperio", "name": "Índice Periodontal (CPI)", "desc": "Mede condições periodontais por sextantes em dentes-índice: 0 hígido, 1 sangramento, 2 cálculo, 3 bolsa 4-5mm, 4 bolsa 6mm+ e X excluído. Bolsas não são registradas em menores de 15 anos.", "connects": ["indice_pip", "sonda_oms_trinity"], "crossConnects": []},
    {"id": "indice_pip", "resumoUrl": "./resumo_prova3.html", "th": "fluorperio", "name": "Perda de Inserção (PIP)", "desc": "Avalia perda de inserção periodontal mensurada da JCE até a base do sulco/bolsa na sonda CPI: código 0 (0-3mm), 1 (4-5mm), 2 (6-8mm), 3 (9-11mm), 4 (12mm+) e X (sextante excluído).", "connects": ["indice_cpi", "sonda_oms_trinity"], "crossConnects": []},
    {"id": "sonda_oms_trinity", "resumoUrl": "./resumo_prova3.html", "th": "fluorperio", "name": "Sonda Periodontal da OMS", "desc": "Instrumental padrão com ponta esférica de 0,5 mm (evita laceração sulcular), faixa preta de 3,5 a 5,5 mm e linhas em 8,5 e 11,5 mm. Força padronizada de 20 gramas.", "connects": ["indice_cpi", "indice_pip"], "crossConnects": ["equipe_levantamento"]}
]

print(f"Categories: {len(CAT_NAMES_P3)}")
print(f"Subtopics: {len(SUBTOPICS_P3)}")
print(f"Map Themes: {len(MAP_THEMES_P3)}")
print(f"Map Concepts: {len(MAP_CONCEPTS_P3)}")
