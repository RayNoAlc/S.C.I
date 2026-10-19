# -*- coding: utf-8 -*-
"""
STUDY_CARDS_P3 and HARD_QUESTIONS_P3 for Prova 3 in S.C.I.
"""

STUDY_CARDS_P3 = [
    # Tema 0: Estudos Epidemiológicos e Levantamentos
    {"cat": 0, "theme": "Estudos Epidemiológicos", "themeKey": "epi", "q": "Qual é a diferença fundamental entre o método clínico e o método epidemiológico?", "a": "O método clínico tem como objeto o indivíduo (paciente), raciocínio fisiopatológico e visa cura/alívio de sintomas. O método epidemiológico tem como objeto a população (coletividade), raciocínio bioestatístico e visa prevenção, controle e políticas de saúde pública."},
    {"cat": 0, "theme": "Estudos Epidemiológicos", "themeKey": "epi", "q": "O que diferenciam estudos epidemiológicos descritivos de estudos analíticos?", "a": "Estudos descritivos respondem quem, onde e quando a doença ocorre, gerando hipóteses epidemiológicas. Estudos analíticos testam hipóteses causais investigando a associação entre fatores de risco e desfechos usando grupos controle."},
    {"cat": 0, "theme": "Desenhos de Pesquisa", "themeKey": "epi", "q": "O que caracteriza um estudo transversal e qual métrica ele avalia?", "a": "Avalia simultaneamente a exposição e o desfecho em um único ponto no tempo ('fotografia'). Mede a prevalência da doença. É rápido e econômico, mas não estabelece causalidade temporal direta."},
    {"cat": 0, "theme": "Desenhos de Pesquisa", "themeKey": "epi", "q": "Como funciona um estudo de coorte e qual é sua principal medida de associação?", "a": "Acompanha indivíduos livres da doença classificados pela exposição (expostos vs não expostos) ao longo do tempo. Mede a incidência de novos casos e calcula o Risco Relativo (RR). É imune ao viés de memória, mas tem alto custo."},
    {"cat": 0, "theme": "Desenhos de Pesquisa", "themeKey": "epi", "q": "Quando o estudo caso-controle é a escolha ideal e qual seu risco de viés?", "a": "É ideal para investigar doenças raras ou de longo período de latência. Parte de doentes (casos) e não doentes (controles) e busca a exposição passada (Odds Ratio). Está sujeito ao viés de memória (recordatório) e de seleção."},
    {"cat": 0, "theme": "Desenhos de Pesquisa", "themeKey": "epi", "q": "O que é um estudo ecológico e o que significa a falácia ecológica?", "a": "É um estudo correlacional onde a unidade de análise é a população/coletividade (países, cidades), e não indivíduos. A falácia ecológica é o erro de inferir associações no nível individual a partir de dados médios agregados da população."},
    {"cat": 0, "theme": "Desenhos de Pesquisa", "themeKey": "epi", "q": "Qual a diferença entre ensaios clínicos, ensaios de campo e ensaios de comunidade?", "a": "Ensaios clínicos testam intervenções em pacientes com a doença; ensaios de campo testam prevenção primária em pessoas sadias sob risco; ensaios de comunidade têm a coletividade inteira como unidade de intervenção (ex: fluoretação das águas)."},
    {"cat": 0, "theme": "Levantamentos em Saúde Bucal", "themeKey": "epi", "q": "Quais são as funções dos 3 membros da equipe de campo de um levantamento epidemiológico?", "a": "Examinador (CD): faz os exames com EPI completo e dita os códigos (proibido pegar lápis/prancheta). Anotador: preenche dados, registra os códigos e nunca deixa caselas vazias. Monitor: organiza o fluxo, apoia a logística e supervisiona a escovação prévia."},
    {"cat": 0, "theme": "Levantamentos em Saúde Bucal", "themeKey": "epi", "q": "Quais os parâmetros de trabalho e instrumentais da OMS para levantamentos epidemiológicos?", "a": "Máximo de 4 horas de exame por dia, cerca de 30 exames/dia por examinador e teto de 300 exames totais ao longo do estudo. Fornecer no mínimo 30 espelhos bucais planos e 30 sondas periodontais OMS (Trinity) por examinador para rotatividade de esterilização."},
    {"cat": 0, "theme": "Calibração e Concordância", "themeKey": "epi", "q": "Quais são as 4 etapas do processo de calibração de examinadores?", "a": "1) Fase Teórica (leitura do manual e códigos); 2) Exercício Clínico-Epidemiológico (6 a 8 crianças com ampla variabilidade clínica); 3) Calibração Propriamente Dita (15 a 20 indivíduos por grupo etário sem debate entre examinadores); 4) Discussão Final e cálculo de concordância."},
    {"cat": 0, "theme": "Calibração e Concordância", "themeKey": "epi", "q": "Como se interpreta o coeficiente Kappa na calibração de examinadores?", "a": "<0.20 pobre; 0.21-0.40 fraca; 0.41-0.60 moderada; 0.61-0.80 substancial (padrão aceito em levantamentos oficiais); 0.81-1.00 quase perfeita. Valores discrepantes exigem repetição ou descarte do examinador."},

    # Tema 1: Epidemiologia da Cárie, Erupção e ICDNT
    {"cat": 1, "theme": "Cronologia de Erupção", "themeKey": "carie", "q": "Como funciona o sistema de notação dentária da FDI / OMS de dois dígitos?", "a": "O primeiro dígito indica o quadrante (1 a 4 para dentes permanentes; 5 a 8 para dentes decíduos). O segundo dígito indica o dente a partir da linha média para distal (1 a 8 para permanentes; 1 a 5 para decíduos)."},
    {"cat": 1, "theme": "Cronologia de Erupção", "themeKey": "carie", "q": "Qual é a idade média de erupção dos primeiros molares permanentes e dos incisivos centrais?", "a": "Primeiros molares permanentes: 6 a 7 anos (superiores e inferiores, irrompem atrás dos decíduos sem esfoliação). Incisivos centrais inferiores: 6 a 7 anos; incisivos centrais superiores: 7 a 8 anos."},
    {"cat": 1, "theme": "Cronologia de Erupção", "themeKey": "carie", "q": "Qual elemento permanente apresenta maior diferença no tempo de erupção entre arco superior e inferior?", "a": "O canino permanente: o canino inferior erupciona por volta dos 9 a 10 anos, enquanto o canino superior erupciona apenas aos 11 a 12 anos."},
    {"cat": 1, "theme": "Índices de Cárie", "themeKey": "carie", "q": "O que significa o índice CPO-D e qual a idade internacional de comparação?", "a": "CPO-D = Dentes Cariados + Perdidos por cárie + Obturados na dentição permanente. A idade-índice adotada mundialmente pela OMS para comparação internacional é aos 12 anos."},
    {"cat": 1, "theme": "Índices de Cárie", "themeKey": "carie", "q": "Por que o índice ceo-d não computa o componente dente 'perdido' (P)?", "a": "Porque na dentição decídua (avaliada aos 5 anos) é impossível ter certeza clínica se o dente ausente foi extraído por cárie ou se sofreu esfoliação fisiológica natural. Em seu lugar usa-se o componente 'e' (extração indicada)."},
    {"cat": 1, "theme": "Índices de Cárie", "themeKey": "carie", "q": "Quantas superfícies são consideradas no índice CPO-S e como é avaliado o dente perdido?", "a": "São avaliadas 148 superfícies nos 32 dentes permanentes (5 superfícies por molar/pré-molar e 4 por incisivo/canino). No dente perdido por cárie, computam-se todas as superfícies como perdidas: 5 nos posteriores e 4 nos anteriores."},
    {"cat": 1, "theme": "Sistema ICDAS", "themeKey": "carie", "q": "O que representam os códigos 0, 1 e 2 do sistema ICDAS?", "a": "Código 0: Dente hígido após 5s de secagem com ar. Código 1: Primeira alteração visual no esmalte visível apenas após secagem prolongada ou em fissuras. Código 2: Mancha branca/marrom visível mesmo com o dente úmido."},
    {"cat": 1, "theme": "ICDNT — Condição Dental", "themeKey": "carie", "q": "Quais são os códigos do ICDNT para dente hígido, cariado, restaurado com cárie e restaurado sem cárie?", "a": "Permanente/Decíduo: 0/A = Hígido; 1/B = Cariado; 2/C = Restaurado com cárie; 3/D = Restaurado sem cárie."},
    {"cat": 1, "theme": "ICDNT — Condição Dental", "themeKey": "carie", "q": "Como são codificados no ICDNT o dente não erupcionado e o dente com banda ortodôntica?", "a": "Dente não erupcionado = código 8 (apenas coroa permanente). Dente com banda ortodôntica = código 9 (dente excluído da avaliação). Dentes com braquetes colados NÃO são excluídos."},
    {"cat": 1, "theme": "ICDNT — Tratamento", "themeKey": "carie", "q": "Quais os códigos de necessidade de tratamento do ICDNT para mancha branca ativa e aplicação de selante?", "a": "Código 7 = Remineralização de mancha branca ativa com flúor tópico. Código 8 = Aplicação de selante (exige os 3 critérios: dente presente há < 2 anos, homólogo cariado e histórico de cárie)."},
    {"cat": 1, "theme": "Regras de Exame OMS", "themeKey": "carie", "q": "Por que a OMS proíbe o uso de sonda exploradora pontiaguda no diagnóstico de cárie?", "a": "A sonda pontiaguda pode causar dano iatrogênico fraturando a camada superficial de esmalte desmineralizado (que poderia ser remineralizada). Além disso, a retenção mecânica depende da força do examinador e da anatomia da fissura, gerando falsos-positivos."},

    # Tema 2: Fluorose Dentária e Doença Periodontal
    {"cat": 2, "theme": "Fluorose Dentária", "themeKey": "fluorperio", "q": "Qual é a etiologia e o mecanismo biológico da fluorose dentária?", "a": "Ingestão crônica excessiva de flúor durante a amelogênese (especialmente na fase de maturação). O flúor inibe proteases, retardando a degradação e remoção das proteínas da matriz adamantina, resultando em esmalte hipomineralizado e poroso abaixo da superfície aprismática."},
    {"cat": 2, "theme": "Fluorose Dentária", "themeKey": "fluorperio", "q": "Qual é o limite seguro de ingestão diária de flúor proposto por Burt (1992)?", "a": "0,05 a 0,07 mg de fluoreto por quilograma de peso corporal ao dia. Crianças de 2 a 3 anos (peso médio 15 kg) ingerem em média 48% do dentifrício na escovação, podendo ultrapassar o limite com uso incorreto de pasta convencional."},
    {"cat": 2, "theme": "Índice de Dean", "themeKey": "fluorperio", "q": "Quais são os 6 graus do Índice de Dean para fluorose dentária?", "a": "0 = Normal; 1 = Questionável; 2 = Muito Leve (< 25% da superfície com opacidades ou picos nevados); 3 = Leve (25% a < 50%); 4 = Moderada (todo o esmalte afetado, desgaste e manchas castanhas); 5 = Severa/Grave (pits/depressões, morfologia alterada e corrosão)."},
    {"cat": 2, "theme": "Índice de Dean", "themeKey": "fluorperio", "q": "Qual é a regra de registro do Índice de Dean quando os dentes homólogos têm graus diferentes?", "a": "A codificação baseia-se nos dois dentes mais severamente afetados. Se eles não apresentarem o mesmo grau de severidade, registra-se o escore do MENOS afetado entre os dois."},
    {"cat": 2, "theme": "Diagnóstico Diferencial", "themeKey": "fluorperio", "q": "Como diferenciar clinicamente a fluorose dentária da mancha branca de cárie?", "a": "A fluorose é bilateral e simétrica em dentes homólogos, localizada em cúspides e bordas incisais, com esmalte liso e resistente. A mancha branca de cárie é assimétrica, localizada em áreas de retenção de biofilme (cervical e fossas) e apresenta aspecto rugoso quando ativa."},
    {"cat": 2, "theme": "Diagnóstico Diferencial", "themeKey": "fluorperio", "q": "O que diferencia hipoplasia de hipomineralização do esmalte?", "a": "Hipoplasia é um defeito quantitativo na deposição da matriz proteica durante a secreção (falta de espessura/estrutura). Hipomineralização é um defeito qualitativo na mineralização da matriz durante a maturação (esmalte poroso com opacidades e manchas, espessura normal)."},
    {"cat": 2, "theme": "Diagnóstico Diferencial", "themeKey": "fluorperio", "q": "O que caracteriza a Hipomineralização Molar-Incisivo (HMI) e o Dente de Turner?", "a": "HMI: afeta de 1 a 4 primeiros molares permanentes, frequentemente associada a incisivos, com manchas demarcadas e esmalte friável. Dente de Turner: hipoplasia localizada unilateral em permanente causada por trauma ou infecção periapical crônica do dente decíduo antecessor."},
    {"cat": 2, "theme": "Índice Periodontal (CPI)", "themeKey": "fluorperio", "q": "Quais são as características da sonda periodontal OMS / Trinity utilizada no CPI?", "a": "Possui ponta esférica de 0,5 mm de diâmetro (evita traumatismo no sulco), faixa preta milimetrada entre 3,5 mm e 5,5 mm, e linhas adicionais em 8,5 mm e 11,5 mm. A força aplicada no exame não deve exceder 20 gramas."},
    {"cat": 2, "theme": "Índice Periodontal (CPI)", "themeKey": "fluorperio", "q": "Quais são os códigos do Índice Periodontal Comunitário (CPI)?", "a": "0 = Sextante hígido; 1 = Sangramento à sondagem; 2 = Cálculo dentário (faixa preta totalmente visível); 3 = Bolsa rasa de 4 a 5 mm (margem na faixa preta); 4 = Bolsa profunda de 6 mm ou mais (faixa preta submersa); X = Sextante excluído (< 2 dentes funcionais)."},
    {"cat": 2, "theme": "Índice de Perda de Inserção (PIP)", "themeKey": "fluorperio", "q": "O que avalia o índice PIP e quais são suas referências milimétricas?", "a": "Avalia a perda de inserção clínica da Junção Cemento-Esmalte (JCE) até o fundo do sulco/bolsa: 0 = 0-3 mm; 1 = 4-5 mm (JCE na faixa preta); 2 = 6-8 mm (JCE entre faixa preta e 8,5 mm); 3 = 9-11 mm (JCE entre 8,5 e 11,5 mm); 4 = 12 mm ou mais; X = sextante excluído."},
    {"cat": 2, "theme": "Epidemiologia Periodontal", "themeKey": "fluorperio", "q": "Por que bolsas periodontais não são registradas pelo CPI em menores de 15 anos?", "a": "Porque adolescentes menores de 15 anos passam por erupção dental ativa e maturação gengival, apresentando pseudo-bolsas inflamatórias sem perda real de inserção conjuntiva. Registram-se apenas sangramento e cálculo."}
]

HARD_QUESTIONS_P3 = [
    # Categoria 0: Estudos Epidemiológicos e Levantamentos (7 questões)
    {
        "cat": 0, "sub": "desenhos_pesquisa", "pool": "ranked",
        "text": "Analise as afirmativas sobre os desenhos de estudos epidemiológicos:\nI. O estudo de coorte parte da exposição em indivíduos sadios e acompanha a incidência de novos casos no tempo, sendo a melhor opção observacional para estabelecer causalidade.\nII. O estudo transversal mede a prevalência em um único instante, permitindo comprovar a relação temporal inequívoca entre exposição e desfecho.\nIII. Os estudos caso-controle partem de doentes e não doentes, calculam Odds Ratio e são ideais para investigar doenças de baixa prevalência ou longo período de latência.\nIV. Nos estudos ecológicos, a unidade de observação é o indivíduo, eliminando o risco da falácia ecológica.\nEstão CORRETAS apenas:",
        "options": ["I e III.", "I, II e III.", "II e IV.", "I, III e IV."],
        "answer": 0, "target": "estudo_coorte",
        "hint": "O estudo transversal NÃO comprova causalidade temporal (causalidade reversa), e o estudo ecológico analisa populações agregadas, não indivíduos.",
        "explanation": "I e III estão corretas. II está incorreta: o estudo transversal não comprova relação temporal direta de causa e efeito. IV está incorreta: o estudo ecológico tem como unidade a população/comunidade, estando sujeito à falácia ecológica.",
        "wrongReasons": [None, "II está incorreta — o estudo transversal não comprova causalidade temporal.", "Ambas estão incorretas.", "IV está incorreta — a unidade é agregada/populacional, não individual."]
    },
    {
        "cat": 0, "sub": "desenhos_pesquisa", "pool": "ranked",
        "text": "Em um estudo sobre tabagismo e doença periodontal, foram examinados 100 indivíduos:\n- 60 fumantes: 40 desenvolveram periodontite e 20 permaneceram hígidos.\n- 40 não fumantes: 10 desenvolveram periodontite e 30 permaneceram hígidos.\nCom base nos dados, o Risco Relativo (RR) e sua interpretação clínica são:",
        "options": [
            "RR = 2,64, indicando que o tabagismo atua como fator de risco de intensidade moderada para doença periodontal.",
            "RR = 1,00, demonstrando ausência de associação estatística entre fumo e periodontite.",
            "RR = 0,38, evidenciando que o tabagismo atuou como fator de proteção periodontal.",
            "RR = 4,00, configurando associação causal perfeita sem necessidade de controle de confundimento."
        ],
        "answer": 0, "target": "estudo_coorte",
        "hint": "Incidência nos expostos = 40/60 (0,66). Incidência nos não expostos = 10/40 (0,25). RR = 0,66 / 0,25.",
        "explanation": "O risco nos expostos é 40/60 = 0,66; nos não expostos é 10/40 = 0,25. O RR é 0,66 / 0,25 = 2,64. Como RR > 1 e próximo de 2, trata-se de um fator de risco com intensidade moderada (conforme os slides do Prof. André).",
        "wrongReasons": [None, "Incorreto: RR é 2,64, não 1,00.", "Incorreto: RR < 1 representaria proteção; aqui o RR é 2,64.", "Incorreto: o valor calculado é 2,64."]
    },
    {
        "cat": 0, "sub": "planejamento_levantamentos", "pool": "ranked",
        "text": "Sobre o planejamento e organização da equipe de campo em levantamentos epidemiológicos (OMS / SB Brasil), analise:\nI. O examinador deve trabalhar sentado, com a criança à sua frente, sendo expressamente vedado manipular fichas, pranchetas ou lápis durante o exame.\nII. Recomenda-se uma jornada de até 4 horas diárias de exames clínicos, com média de 30 exames por observador ao dia, até o teto de 300 exames totais por examinador.\nIII. Cada examinador deve dispor de no mínimo 30 espelhos planos e 30 sondas periodontais OMS para garantir rotatividade de esterilização em autoclave.\nIV. O monitor da equipe é responsável por registrar os códigos na ficha enquanto o anotador supervisiona a escovação das crianças.\nEstão CORRETAS apenas:",
        "options": ["I, II e III.", "I e IV.", "II, III e IV.", "Todas estão corretas."],
        "answer": 0, "target": "equipe_levantamento",
        "hint": "As atribuições do monitor e do anotador foram invertidas no item IV: o anotador preenche a ficha e o monitor cuida da escovação prévia e do fluxo.",
        "explanation": "I, II e III estão corretas. IV está incorreta: quem anota os códigos na ficha é o ANOTADOR; o MONITOR é quem organiza as buscas, o fluxo e supervisiona a escovação prévia das crianças.",
        "wrongReasons": [None, "IV está incorreta — funções de anotador e monitor invertidas.", "I também está correta e deve constar.", "IV está incorreta, logo nem todas estão corretas."]
    },
    {
        "cat": 0, "sub": "calibracao_concordancia", "pool": "ranked",
        "text": "Sobre o processo de calibração de examinadores e a estatística Kappa, analise as afirmativas:\nI. A calibração intra-examinador avalia a reprodutibilidade do examinador consigo mesmo, enquanto a inter-examinador avalia a concordância entre os diferentes examinadores da equipe.\nII. O exercício clínico-epidemiológico prévio deve contar com 6 a 8 crianças que exibam ampla variabilidade clínica para discussão diagnóstica conjunta.\nIII. Na calibração propriamente dita, examinam-se de 15 a 20 indivíduos por faixa etária, sendo proibido o debate entre os membros da equipe durante o exame.\nIV. Valores de Kappa entre 0,41 e 0,60 são classificados como concordância substancial, sendo o padrão mínimo exigido para levantamentos oficiais da OMS.\nEstão CORRETAS apenas:",
        "options": ["I, II e III.", "I, II, III e IV.", "II e IV.", "Apenas I e III."],
        "answer": 0, "target": "calibracao_kappa",
        "hint": "Kappa de 0,41 a 0,60 é MODERADA. A concordância SUBSTANCIAL corresponde à faixa de 0,61 a 0,80.",
        "explanation": "I, II e III estão corretas. IV está incorreta: 0,41 a 0,60 é concordância moderada; substancial é de 0,61 a 0,80 (Landis & Koch, citado pelo Prof. André).",
        "wrongReasons": [None, "IV está incorreta — 0,41-0,60 é moderada, não substancial.", "IV está incorreta.", "II também está correta."]
    },
    {
        "cat": 0, "sub": "tipos_estudos", "pool": "ranked",
        "text": "Considere as características de estudos experimentais em saúde bucal:\nI. No Ensaio Clínico Randomizado, a alocação aleatória visa garantir que os grupos intervenção e controle tenham características basais semelhantes.\nII. No Ensaio de Campo, os participantes são indivíduos clinicamente doentes atendidos em ambiente hospitalar especializado.\nIII. No Ensaio de Comunidade, a unidade de intervenção e análise é a coletividade inteira (ex: fluoretação da água de abastecimento público de um município comparado a outro).\nIV. Em um estudo experimental sobre bochecho com clorexidina e placa bacteriana, o tipo de bochecho é a variável independente e o índice de placa é a variável dependente.\nEstão CORRETAS apenas:",
        "options": ["I, III e IV.", "I e II.", "II, III e IV.", "Todas estão corretas."],
        "answer": 0, "target": "estudos_experimentais",
        "hint": "Ensaios de campo envolvem indivíduos SAUDÁVEIS sob risco na comunidade (prevenção primária), não pacientes hospitalizados com doença instalada.",
        "explanation": "I, III e IV estão corretas. II está incorreta: no ensaio de campo, os participantes são livres da doença (saudáveis sob risco na comunidade); ensaios em pacientes doentes são ensaios clínicos.",
        "wrongReasons": [None, "II está incorreta — ensaio de campo é em pessoas saudáveis.", "II está incorreta.", "II está incorreta, portanto nem todas estão corretas."]
    },
    {
        "cat": 0, "sub": "tipos_estudos", "pool": "ranked",
        "text": "Em relação às diferenças entre o diagnóstico clínico individual e o diagnóstico epidemiológico coletivo, é INCORRETO afirmar que:",
        "options": [
            "O método epidemiológico busca o diagnóstico etiológico individual para prescrição de conduta medicamentosa personalizada.",
            "O raciocínio epidemiológico fundamenta-se na bioestatística e na análise de indicadores populacionais como morbidade e mortalidade.",
            "O método clínico utiliza anamnese e exames complementares visando primariamente à cura e ao alívio do sofrimento do paciente.",
            "As condutas decorrentes do diagnóstico epidemiológico materializam-se em programas de saúde pública, políticas e intervenções populacionais."
        ],
        "answer": 0, "target": "estudos_epidemiologicos",
        "hint": "Diagnóstico etiológico individual para prescrição medicamentosa personalizada é a essência do método CLÍNICO, não epidemiológico.",
        "explanation": "A afirmativa A descreve o método clínico. O diagnóstico epidemiológico avalia a coletividade por indicadores populacionais para subsidiar programas e políticas de prevenção e controle coletivo.",
        "wrongReasons": [None, "Correta descrição do método epidemiológico.", "Correta descrição do método clínico.", "Correta descrição dos desdobramentos epidemiológicos."]
    },
    {
        "cat": 0, "sub": "desenhos_pesquisa", "pool": "ranked",
        "text": "Um pesquisador coletou dados secundários do IDH de 250 municípios brasileiros e comparou com o percentual de escolares de 12 anos que perderam ao menos um molar permanente nesses municípios, encontrando correlação inversa. Esse desenho de estudo e sua principal limitação são:",
        "options": [
            "Estudo ecológico; está sujeito à falácia ecológica, pois associações observadas em nível agregado municipal podem não se reproduzir no nível individual.",
            "Estudo de coorte prospectivo; está sujeito a elevado viés de memória dos escolares avaliados.",
            "Ensaio clínico de comunidade; não possui grupo controle para mensuração de eficácia terapêutica.",
            "Estudo caso-controle; possui alto custo financeiro devido ao longo tempo de acompanhamento dos participantes."
        ],
        "answer": 0, "target": "estudo_ecologico",
        "hint": "Dados agregados de municípios (IDH e médias populacionais) = estudo ecológico. Principal risco = falácia ecológica.",
        "explanation": "Trata-se de um estudo ecológico (unidade populacional/municipal). Sua clássica limitação metodológica é a falácia ecológica (inferir relações individuais a partir de médias populacionais).",
        "wrongReasons": [None, "Não é coorte (não acompanhou indivíduos no tempo) nem tem viés de memória.", "Não é ensaio de intervenção comunitária.", "Não é caso-controle (não selecionou casos e controles individuais)."]
    },

    # Categoria 1: Epidemiologia da Cárie, Erupção e ICDNT (7 questões)
    {
        "cat": 1, "sub": "cronologia_erupcao", "pool": "ranked",
        "text": "Analise as afirmativas sobre a cronologia e a sequência de erupção dos dentes permanentes:\nI. O primeiro molar permanente erupciona aos 6-7 anos atrás dos molares decíduos, sem necessidade de esfoliação de nenhum dente decíduo antecessor.\nII. Os caninos inferiores erupcionam aos 9-10 anos, antes dos caninos superiores, que erupcionam por volta dos 11-12 anos.\nIII. Segundo Moyers, as meninas apresentam emergência dental cerca de 5 meses mais precoce que os meninos.\nIV. Na notação FDI, os dentes decíduos do quadrante inferior direito são numerados de 81 a 85.\nEstão CORRETAS:",
        "options": ["I, II, III e IV.", "I, II e III apenas.", "II e IV apenas.", "I e IV apenas."],
        "answer": 0, "target": "cronologia_erupcao_node",
        "hint": "Todas as 4 afirmativas refletem dados e tabelas exatas apresentadas nos slides do Prof. André.",
        "explanation": "Todas as afirmativas estão corretas. O 1º molar irrompe aos 6-7 anos sem esfoliação; caninos inferiores precedem os superiores em ~2 anos; meninas são ~5 meses mais precoces; e o quadrante inferior direito decíduo é o 8 (dentes 81 a 85).",
        "wrongReasons": [None, "A IV também está correta (quadrante 8 decíduo).", "I e III também estão corretas.", "II e III também estão corretas."]
    },
    {
        "cat": 1, "sub": "indices_carie", "pool": "ranked",
        "text": "Sobre os índices de cárie dentária CPO-D, ceo-d e CPO-S, analise:\nI. O índice CPO-D tem como idade-índice de referência internacional da OMS os 12 anos de idade.\nII. No índice ceo-d (para dentes decíduos), o componente 'P' não é utilizado, adotando-se a letra 'e' para dentes com extração indicada.\nIII. O CPO-S avalia 148 superfícies nos 32 dentes permanentes, atribuindo 5 superfícies para dentes posteriores perdidos e 4 para anteriores perdidos.\nIV. Um valor de CPO-D elevado com predomínio do componente 'O' indica alta necessidade de tratamento cirúrgico mutilador não atendida.\nEstão CORRETAS apenas:",
        "options": ["I, II e III.", "I, II, III e IV.", "II e IV.", "Apenas I e IV."],
        "answer": 0, "target": "indice_cpod",
        "hint": "Predomínio de 'O' (obturado/restaurado) indica ACESSO a serviços restauradores de saúde bucal, não necessidade de cirurgia mutiladora.",
        "explanation": "I, II e III estão corretas. IV está incorreta: predomínio do componente O (obturado) indica que a população teve acesso a serviços odontológicos curativos/restauradores; quem indica sequela mutiladora é o P (perdido) e necessidade de tratamento é o C (cariado).",
        "wrongReasons": [None, "IV está incorreta — predomínio de O indica acesso a restaurações.", "I também está correta.", "IV está incorreta."]
    },
    {
        "cat": 1, "sub": "icdnt_condicao", "pool": "ranked",
        "text": "Durante um levantamento epidemiológico pelo ICDNT (OMS), um examinador avaliou os seguintes dentes permanentes de um escolar de 12 anos:\n- Dente 16: presença de restauração em resina oclusal íntegra, sem cárie.\n- Dente 11: presença de cárie ativa cavitada envolvendo esmalte e dentina.\n- Dente 26: dente com coroa destruída por cárie e restauração de amálgama fraturada com cárie ativa marginal.\n- Dente 36: extraído precocemente aos 9 anos devido a complicação de cárie.\nOs códigos corretos de condição dental da coroa atribuídos a esses dentes são, respectivamente:",
        "options": [
            "16 = código 3; 11 = código 1; 26 = código 2; 36 = código 4.",
            "16 = código 0; 11 = código 1; 26 = código 1; 36 = código 5.",
            "16 = código 3; 11 = código B; 26 = código C; 36 = código E.",
            "16 = código 6; 11 = código 2; 26 = código 3; 36 = código 4."
        ],
        "answer": 0, "target": "icdnt_coroa",
        "hint": "Lembre dos códigos ICDNT permanentes: 0 hígido, 1 cariado, 2 restaurado c/ cárie, 3 restaurado s/ cárie, 4 perdido p/ cárie.",
        "explanation": "16 = 3 (restaurado sem cárie); 11 = 1 (cariado); 26 = 2 (restaurado com cárie); 36 = 4 (perdido devido à cárie). As letras (B, C, E) aplicam-se à dentição decídua, não permanente.",
        "wrongReasons": [None, "Incorreto: 16 é restaurado (3), 26 tem restauração com cárie (2).", "Incorreto: letras são para dentes decíduos.", "Incorreto: 16 não é selante (6) e 26 não é restaurado sem cárie (3)."]
    },
    {
        "cat": 1, "sub": "icdnt_necessidade", "pool": "ranked",
        "text": "Segundo os critérios do Projeto SB Brasil / OMS para registro da Necessidade de Tratamento no ICDNT, analise:\nI. Código 1 é indicado para restauração de uma superfície dentária e Código 2 para restauração de duas ou mais superfícies.\nII. Código 7 é atribuído quando o dente apresenta mancha branca ativa com necessidade de remineralização à base de flúor.\nIII. Código 8 (selante) exige a presença simultânea de 3 critérios: dente presente há menos de 2 anos, homólogo com cárie e histórico de cárie na dentição decídua.\nIV. Quando a condição da coroa for código 8 (não erupcionado) ou código 4 (perdido), a necessidade de tratamento deve ser anotada obrigatoriamente como código 9 (sem informação / não se aplica).\nEstão CORRETAS:",
        "options": ["I, II, III e IV.", "I e III apenas.", "II, III e IV apenas.", "I, II e IV apenas."],
        "answer": 0, "target": "icdnt_tratamento",
        "hint": "Todas as 4 afirmativas descrevem exatamente as regras de preenchimento do manual do examinador do SB Brasil.",
        "explanation": "Todas estão corretas. Código 1 (1 face) e 2 (2+ faces); Código 7 (remineralização de mancha branca); Código 8 (selante com os 3 critérios); e se o dente for não erupcionado (8) ou ausente (4/5), anota-se código 9 no tratamento.",
        "wrongReasons": [None, "II e IV também estão corretas.", "I também está correta.", "III também está correta (regra dos 3 critérios do selante)."]
    },
    {
        "cat": 1, "sub": "icdnt_condicao", "pool": "ranked",
        "text": "Sobre as regras especiais de exame e decisão diagnóstica estabelecidas pela OMS e SB Brasil, analise as afirmativas:\nI. Um dente permanente é considerado irrompido e examinável quando já puder ser tocado com a ponta da sonda periodontal.\nII. Dentes supranumerários encontrados no arco devem ser registrados normalmente em caselas adicionais da ficha.\nIII. Se um dente decíduo e um permanente ocuparem o mesmo espaço interdental, o examinador deve registrar o dente permanente.\nIV. Em caso de dúvida entre superfície hígida e cariada, considera-se hígida; em dúvida entre restaurada com cárie e restaurada sem cárie, considera-se restaurada sem cárie.\nEstão CORRETAS apenas:",
        "options": ["I, III e IV.", "I, II e III.", "II, III e IV.", "Todas estão corretas."],
        "answer": 0, "target": "regras_exame_oms",
        "hint": "Dentes supranumerários NÃO são computados nem registrados em levantamentos epidemiológicos da OMS.",
        "explanation": "I, III e IV estão corretas. II está incorreta: dentes supranumerários NÃO são considerados nem registrados em levantamentos da OMS/SB Brasil.",
        "wrongReasons": [None, "II está incorreta — supranumerários não são considerados.", "II está incorreta.", "II está incorreta, portanto nem todas estão corretas."]
    },
    {
        "cat": 1, "sub": "indices_carie", "pool": "ranked",
        "text": "O Sistema Internacional de Detecção e Avaliação de Cáries (ICDAS) propõe uma escala de 0 a 6. Sobre seus critérios, associe:\nI. Código 0 → Dente hígido após 5 segundos de secagem com ar.\nII. Código 2 → Mancha branca ou marrom visível mesmo com o dente úmido.\nIII. Código 3 → Microcavitação inicial em esmalte (< 0,5 mm) sem exposição de dentina.\nIV. Código 6 → Sombra escura subjacente de dentina sem perda de continuidade de esmalte.\nEstão CORRETAS apenas:",
        "options": ["I, II e III.", "I, II, III e IV.", "II e IV.", "Apenas III e IV."],
        "answer": 0, "target": "sistema_icdas",
        "hint": "Sombra escura subjacente de dentina é o Código 4 do ICDAS. O Código 6 é cavitação extensa com dentina exposta em mais de 50% da superfície.",
        "explanation": "I, II e III estão corretas. IV está incorreta: sombra subjacente de dentina é o código 4; o código 6 representa cavitação extensa com dentina visível em mais da metade da superfície.",
        "wrongReasons": [None, "IV está incorreta — código 6 é cavidade extensa (>50%).", "I e III também estão corretas.", "IV está incorreta."]
    },
    {
        "cat": 1, "sub": "icdnt_condicao", "pool": "ranked",
        "text": "Por que o manual de levantamentos da OMS e o SB Brasil recomendam enfaticamente o NÃO uso da sonda exploradora pontiaguda no exame de cárie dentária?",
        "options": [
            "Porque a pressão da ponta afiada pode fraturar o esmalte desmineralizado incipiente (lesão reversível), tornando a cavidade irreversível, além de a retenção mecânica depender da força do examinador e da anatomia da fissura.",
            "Porque a sonda exploradora pontiaguda acelera a transmissão do vírus da hepatite B entre dentes do mesmo indivíduo.",
            "Porque a sonda pontiaguda é incapaz de diagnosticar restaurações estéticas de resina composta.",
            "Porque a OMS aboliu qualquer tipo de instrumental metálico, exigindo apenas espátulas plásticas descartáveis."
        ],
        "answer": 0, "target": "regras_exame_oms",
        "hint": "A sonda pontiaguda causa iatrogenia (fratura do esmalte que poderia ser remineralizado) e retenção mecânica não significa necessariamente cárie ativa.",
        "explanation": "A sonda exploradora pontiaguda pode provocar iatrogenia fraturando esmalte superficial desmineralizado e convertendo lesões remineralizáveis em cavidades francas. Além disso, a retenção mecânica depende da força do examinador e da morfologia anatômica da fossa.",
        "wrongReasons": [None, "Incorreto: a razão primária é a iatrogenia no esmalte e imprecisão diagnóstica.", "Incorreto: o foco é a detecção de cárie, não identificação de resinas.", "Incorreto: a sonda periodontal OMS Trinity continua sendo preconizada."]
    },

    # Categoria 2: Fluorose Dentária e Doença Periodontal (7 questões)
    {
        "cat": 2, "sub": "indices_fluorose", "pool": "ranked",
        "text": "Em um levantamento de fluorose dentária pelo Índice de Dean, o examinador encontrou no paciente:\n- Dente 11: Grau 3 (Leve — opacidades cobrindo entre 25% e 50% da superfície).\n- Dente 21: Grau 4 (Moderado — todo o esmalte afetado com desgaste acentuado).\n- Demais dentes: graus 1 ou 2.\nSegundo as regras de codificação do Índice de Dean estabelecidas pela OMS, o escore registrado para esse indivíduo deve ser:",
        "options": [
            "Grau 3 (Leve), pois quando os dois dentes mais severamente afetados não apresentam o mesmo grau, atribui-se o escore do MENOS afetado entre os dois.",
            "Grau 4 (Moderado), pois deve prevalecer sempre o grau de maior gravidade encontrado na cavidade bucal.",
            "Grau 3,5, correspondente à média aritmética exata dos dois elementos mais afetados.",
            "Grau 1 (Questionável), devido à presença de dúvida entre os dois incisivos centrais superiores."
        ],
        "answer": 0, "target": "indice_dean",
        "hint": "Regra áurea de Dean: o registro é feito com base nos dois dentes mais afetados; se discordantes, prevalece o MENOR escore entre eles.",
        "explanation": "Pela regra de Dean: codifica-se com base nos dois dentes mais severamente afetados (11 e 21). Como não estão igualmente afetados (grau 3 e grau 4), o escore registrado deve ser o do MENOS afetado entre os dois, ou seja, Grau 3 (Leve).",
        "wrongReasons": [None, "Incorreto: não prevalece o maior, mas sim o menos afetado dos dois.", "Incorreto: o índice de Dean não possui graus fracionados.", "Incorreto: não há dúvida para rebaixar para questionável; a regra define o escore 3."]
    },
    {
        "cat": 2, "sub": "diagnostico_diferencial", "pool": "ranked",
        "text": "Analise as afirmativas sobre o diagnóstico diferencial entre defeitos de esmalte e cárie dentária:\nI. A fluorose dentária apresenta caráter sistêmico com distribuição bilateral e simétrica em dentes homólogos, atingindo principalmente bordas incisais e cúspides.\nII. A mancha branca de cárie é assimétrica, localiza-se em sítios de estagnação de biofilme (região cervical e cicatrículas) e apresenta aspecto rugoso quando ativa.\nIII. A Hipomineralização Molar-Incisivo (HMI) é um defeito qualitativo que afeta de um a quatro primeiros molares permanentes, frequentemente associada aos incisivos.\nIV. O Dente de Turner é uma alteração sistêmica bilateral causada pelo uso crônico de antibióticos da classe das tetraciclinas durante o primeiro ano de vida.\nEstão CORRETAS apenas:",
        "options": ["I, II e III.", "I, II, III e IV.", "II e IV.", "Apenas I e IV."],
        "answer": 0, "target": "diag_diferencial_esmalte",
        "hint": "O Dente de Turner é um defeito LOCAL e UNILATERAL decorrente de trauma ou abscesso do decíduo antecessor. Tetraciclina causa mancha intrínseca generalizada.",
        "explanation": "I, II e III estão corretas. IV está incorreta: o Dente de Turner é uma hipoplasia focal local e unilateral causada por trauma mecânico ou abscesso periapical do dente decíduo antecessor; o uso de tetraciclina gera manchas intrínsecas acinzentadas em bandas, sem relação com Turner.",
        "wrongReasons": [None, "IV está incorreta — Turner é local/unilateral por trauma ou abscesso de decíduo.", "I e III também estão corretas.", "IV está incorreta."]
    },
    {
        "cat": 2, "sub": "fluorose_clinica", "pool": "ranked",
        "text": "Sobre os aspectos etiológicos e os fatores de risco da fluorose dentária, analise:\nI. Ocorre pela ingestão crônica de fluoreto durante a fase de desenvolvimento dental (amelogênese), principalmente no período de maturação do esmalte.\nII. O limite máximo de ingestão diária de risco proposto por Burt (1992) é de 0,05 a 0,07 mg F/kg de peso corporal.\nIII. Crianças de 2 a 3 anos chegam a ingerir cerca de 48% do dentifrício utilizado na escovação dentária.\nIV. Aplicações tópicas profissionais de flúor realizadas aos 15 anos de idade aumentam significativamente o risco de desenvolvimento de fluorose em dentes permanentes.\nEstão CORRETAS apenas:",
        "options": ["I, II e III.", "I, II, III e IV.", "II e IV.", "Apenas I e IV."],
        "answer": 0, "target": "fluorose_biologia",
        "hint": "Aos 15 anos, as coroas dos permanentes já estão completamente formadas e mineralizadas — NÃO há mais qualquer risco de fluorose!",
        "explanation": "I, II e III estão corretas. IV está incorreta: aos 15 anos a amelogênese de todos os dentes permanentes (exceto 3º molares) já se encerrou; aplicações tópicas nessa idade não causam fluorose.",
        "wrongReasons": [None, "IV está incorreta — após a formação da coroa não há risco de fluorose.", "I e III também estão corretas.", "IV está incorreta."]
    },
    {
        "cat": 2, "sub": "epidemiologia_periodontal", "pool": "ranked",
        "text": "Sobre o Índice Periodontal Comunitário (CPI / CPITN) preconizado pela OMS, analise as afirmativas:\nI. A sonda utilizada possui ponta esférica de 0,5 mm, faixa preta entre 3,5 mm e 5,5 mm, com força de inserção não superior a 20 gramas.\nII. Em adultos, o exame é realizado em 10 dentes-índice distribuídos em 6 sextantes: 17/16, 11, 26/27, 47/46, 31, 36/37.\nIII. Código 3 indica bolsa rasa de 4 a 5 mm (margem gengival cobrindo parte da faixa preta) e Código 4 indica bolsa de 6 mm ou mais (faixa preta totalmente submersa).\nIV. Em participantes menores de 15 anos de idade, todas as bolsas periodontais rasas e profundas devem ser registradas obrigatoriamente para cálculo do índice.\nEstão CORRETAS apenas:",
        "options": ["I, II e III.", "I, II, III e IV.", "II e IV.", "Apenas I e IV."],
        "answer": 0, "target": "indice_cpi",
        "hint": "Bolsas periodontais NÃO são registradas em menores de 15 anos de idade (devido à erupção dental ativa e pseudo-bolsas).",
        "explanation": "I, II e III estão corretas. IV está incorreta: em menores de 15 anos, bolsas periodontais NÃO são registradas (registra-se apenas higidez, sangramento e cálculo) para evitar pseudo-bolsas de erupção.",
        "wrongReasons": [None, "IV está incorreta — bolsas não são avaliadas em < 15 anos.", "I e III também estão corretas.", "IV está incorreta."]
    },
    {
        "cat": 2, "sub": "epidemiologia_periodontal", "pool": "ranked",
        "text": "Sobre os critérios do exame periodontal (CPI e PIP) e os dados epidemiológicos do SB Brasil 2023, analise:\nI. Um sextante com apenas 1 dente funcional presente deve ser codificado como 'X' (sextante excluído).\nII. O índice PIP mede a distância da Junção Cemento-Esmalte (JCE) até o fundo do sulco/bolsa, onde o código 1 indica perda de 4 a 5 mm (JCE na faixa preta).\nIII. No SB Brasil 2023, o agravo periodontal mais prevalente em adultos de 35 a 44 anos foi o cálculo dentário (38,7%), seguido por sangramento (32,4%).\nIV. Em idosos de 65 a 74 anos no SB Brasil 2023, 86% dos indivíduos apresentaram sextantes excluídos (código X), reflexo da alta prevalência de edentulismo.\nEstão CORRETAS:",
        "options": ["I, II, III e IV.", "I e III apenas.", "II, III e IV apenas.", "I, II e IV apenas."],
        "answer": 0, "target": "indice_pip",
        "hint": "Todas as 4 afirmativas descrevem com exatidão as regras do CPI/PIP e os dados epidemiológicos oficiais do SB Brasil 2023 apresentados nos slides.",
        "explanation": "Todas estão corretas. Sextante com 1 dente = X; PIP código 1 = 4-5 mm; SB Brasil 2023: cálculo (38,7%) e sangramento (32,4%) lideram em adultos; e 86% de idosos têm sextantes excluídos por edentulismo.",
        "wrongReasons": [None, "II e IV também estão corretas.", "I também está correta.", "III também está correta."]
    },
    {
        "cat": 2, "sub": "indices_fluorose", "pool": "ranked",
        "text": "O Índice de Fluorose Dentária Comunitário (IFD), proposto por Dean para avaliar o impacto em saúde pública, é calculado pela somatória do produto da frequência de cada grau pelo respectivo peso, dividida pelo total de examinados. Um valor de IFD igual a 0,35 significa que:",
        "options": [
            "A situação epidemiológica é classificada como Negativa, indicando que a fluorose não constitui problema de saúde pública na comunidade, mantendo alto valor preventivo contra cárie.",
            "A comunidade encontra-se em situação Muito Grave, exigindo interrupção emergencial da fluoretação da água.",
            "Existe uma epidemia de fluorose de grau moderado a severo na localidade.",
            "O índice é inconclusivo e a pesquisa precisa ser repetida em um prazo de 30 dias."
        ],
        "answer": 0, "target": "indice_dean",
        "hint": "Escala de IFD da comunidade: 0,0 a 0,4 é considerado 'Negativo' (sem impacto na saúde pública, benefício anticárie preservado).",
        "explanation": "IFD entre 0,0 e 0,4 é classificado como 'Negativo' do ponto de vista de saúde pública: a fluorose presente é leve/muito leve e não representa agravo sanitário, demonstrando balanço ideal na prevenção da cárie.",
        "wrongReasons": [None, "Incorreto: situação muito grave corresponderia a IFD entre 3,0 e 4,0.", "Incorreto: IFD de 0,35 indica prevalência desprezível de formas graves.", "Incorreto: o índice é plenamente conclusivo e dentro da faixa ideal."]
    },
    {
        "cat": 2, "sub": "indices_fluorose", "pool": "ranked",
        "text": "Sobre o Índice TF (Thylstrup & Fejerskov, 1978) e sua relação com as alterações histológicas do esmalte fluorótico, é CORRETO afirmar que:",
        "options": [
            "Classifica a fluorose em 10 escores (0 a 9) com base na porosidade biológica do esmalte após secagem com ar, onde os escores 5 a 9 indicam perda focal externa de esmalte (depressões/pits e perda anatômica).",
            "Foi desenvolvido exclusivamente para avaliar manchas por tetraciclina e cárie oculta em molares decíduos.",
            "Substitui completamente o uso de sondas e espelhos bucais por testes radiográficos panorâmicos obrigatórios.",
            "Classifica os dentes em apenas 3 categorias: ausente, questionável e restaurado."
        ],
        "answer": 0, "target": "indice_tf",
        "hint": "Índice TF avalia de 0 a 9 baseado na porosidade do esmalte após secagem de ar, com pits a partir do escore 5.",
        "explanation": "O Índice TF (1978) classifica as alterações fluoróticas em 10 categorias (0 a 9). Os escores 1 a 3 correspondem a linhas e opacidades; o escore 4 a branco-giz completo; e de 5 a 9 há perda focal de esmalte superficial (pits e desgaste de contorno).",
        "wrongReasons": [None, "Incorreto: o índice TF é específico para fluorose dentária.", "Incorreto: o exame é visual clínico pós-secagem prolongada de ar.", "Incorreto: o TF possui 10 graus (0 a 9), não 3 categorias."]
    }
]

print(f"STUDY_CARDS_P3 count: {len(STUDY_CARDS_P3)}")
print(f"HARD_QUESTIONS_P3 count: {len(HARD_QUESTIONS_P3)}")
