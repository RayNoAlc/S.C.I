# -*- coding: utf-8 -*-
"""
questions_p3_cat0.py
Banco de 35 questões da Categoria 0 da Prova 3:
"Estudos Epidemiológicos e Levantamentos em Saúde Bucal"
Subtópicos:
  - tipos_estudos (9 questões)
  - desenhos_pesquisa (9 questões)
  - planejamento_levantamentos (9 questões)
  - calibracao_concordancia (8 questões)
"""

QUESTIONS_P3_CAT0 = [
    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 1: tipos_estudos (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "A epidemiologia em saúde bucal difere da abordagem clínica individual principalmente pelo seu foco de análise. Enquanto a clínica odontológica visa o diagnóstico e cura do indivíduo, a epidemiologia tem como propósito central:",
        "options": [
            "Realizar procedimentos cirúrgicos curativos imediatos em escala ambulatorial.",
            "Investigar a distribuição e os determinantes dos agravos à saúde em populações para orientar o planejamento e as políticas públicas.",
            "Eliminar a necessidade de fichas e prontuários por meio de prontuários estritamente individuais.",
            "Substituir o método científico experimental por observações subjetivas dos profissionais de saúde."
        ],
        "answer": 1,
        "target": "estudos_epidemiologicos",
        "hint": "Pense no objetivo coletivo da saúde pública: entender padrões populacionais para formular ações e alocar recursos.",
        "explanation": "A epidemiologia investiga a frequência, a distribuição espacial e temporal, bem como os determinantes e condicionantes de saúde-doença na coletividade humana, fornecendo a base científica para o planejamento, organização e avaliação das ações e serviços de saúde.",
        "wrongReasons": [
            "Procedimentos curativos individuais são atribuição da clínica assistencial, não do objeto de estudo da ciência epidemiológica.",
            None,
            "A epidemiologia depende rigorosamente de fichas padronizadas, bancos de dados coletivos e prontuários para consolidar estatísticas.",
            "A epidemiologia é estritamente fundamentada no método científico, bioestatística e critérios diagnósticos padronizados."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "Quanto à classificação dos estudos epidemiológicos em relação à postura do pesquisador diante da variável de exposição, os estudos são classificados como:",
        "options": [
            "Qualitativos ou quantitativos, dependendo do software estatístico empregado.",
            "Observacionais, quando o pesquisador apenas testemunha a exposição natural; e Experimentais, quando ele aloca ativamente a intervenção.",
            "Longitudinais, quando há apenas uma medição no tempo; e Transversais, quando há seguimento por muitos anos.",
            "Descritivos exclusivos, pois na odontologia em saúde coletiva não se admite a realização de experimentos."
        ],
        "answer": 1,
        "target": "estudos_descritivos_analiticos",
        "hint": "O critério é a manipulação: o pesquisador interfere e aplica algo ativamente, ou apenas mede o que já ocorre espontaneamente?",
        "explanation": "Nos estudos observacionais, o pesquisador não interfere na alocação do fator de exposição (apenas observa e quantifica a realidade). Nos estudos experimentais (ensaios), o pesquisador manipula ativamente a intervenção (ex: testa uma nova pasta dental ou um selante).",
        "wrongReasons": [
            "Qualitativo e quantitativo são abordagens metodológicas gerais, não a classificação pela intervenção do pesquisador.",
            None,
            "A alternativa inverteu os conceitos: estudos transversais realizam uma única medição temporal, enquanto longitudinais acompanham indivíduos no tempo.",
            "A odontologia realiza inúmeros ensaios experimentais clínicos e comunitários (como testes de eficácia de dentifrícios e fluoretação)."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "Os estudos epidemiológicos podem ter finalidade descritiva ou analítica. Assinale a alternativa que caracteriza com precisão um estudo DESCRITIVO:",
        "options": [
            "Tem como propósito essencial testar relações causais entre um fator de risco e o surgimento de uma patologia bucal.",
            "Descreve a distribuição de um agravo segundo as variáveis de pessoa, tempo e lugar, gerando hipóteses epidemiológicas sem grupo controle.",
            "Manipula a dosagem de medicamentos em cobaias em ambiente laboratorial controlado.",
            "Sempre exige o cálculo prévio de Risco Relativo (RR) e Odds Ratio (OR) para comprovar associação etiológica."
        ],
        "answer": 1,
        "target": "estudos_descritivos_analiticos",
        "hint": "Estudos descritivos respondem: 'Quem adoece? Onde? Quando?' — sem comparar grupos controle para provar causa e efeito.",
        "explanation": "Estudos descritivos limitam-se a quantificar a distribuição de doenças e características de saúde em termos de 'quem' (características dos indivíduos), 'onde' (distribuição espacial) e 'quando' (tendência temporal). Servem para conhecer o perfil epidemiológico e gerar hipóteses, as quais serão posteriormente testadas por estudos analíticos.",
        "wrongReasons": [
            "Testar relações causais com grupos controle é a definição de estudos analíticos.",
            None,
            "Manipulação em laboratório com cobaias refere-se a ensaios pré-clínicos biomédicos, não a estudos epidemiológicos descritivos populacionais.",
            "Cálculo de RR e OR é específico de estudos analíticos (coorte e caso-controle), inexistindo em descritivos puros."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "Em relação às fontes de dados utilizadas na epidemiologia em saúde bucal, dados SECUNDÁRIOS são aqueles:",
        "options": [
            "Coletados diretamente pelo pesquisador por meio de exames clínicos intraorais de campo.",
            "Provenientes de registros de rotina preexistentes em sistemas de informação em saúde, censos ou certidões de óbito.",
            "Considerados de segunda categoria por não possuírem relevância estatística ou científica.",
            "Exclusivos de pesquisas laboratoriais in vitro em dentes humanos doados a bancos de dentes."
        ],
        "answer": 1,
        "target": "fontes_dados",
        "hint": "Dados secundários já foram coletados previamente para outra finalidade administrativa ou sanitária (ex: SIM, SINASC, SISAB, IBGE).",
        "explanation": "Dados secundários são informações já coletadas e registradas previamente por terceiros ou sistemas oficiais (como SISAB/e-SUS APS, SIM, SINASC, prontuários hospitalares e censos do IBGE). Dados primários, por outro lado, são aqueles coletados diretamente pelos pesquisadores para o objetivo específico do inquérito.",
        "wrongReasons": [
            "Coleta direta no campo por meio de exames clínicos gera dados PRIMÁRIOS, não secundários.",
            None,
            "Dados secundários são de altíssimo valor epidemiológico e subsidiam a vigilância em saúde bucal e séries temporais nacionais.",
            "Bancos de dentes in vitro pertencem à pesquisa experimental básica laboratorial, não a fontes secundárias epidemiológicas de base populacional."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "Na comparação entre o método clínico odontológico e o método epidemiológico realizada pelo Prof. André, assinale a correlação CORRETA:",
        "options": [
            "No método epidemiológico o foco é o paciente doente, enquanto no método clínico o foco é a comunidade saudável.",
            "O método clínico utiliza inquéritos e taxas populacionais, enquanto a epidemiologia emprega prontuário e anamnese individual.",
            "No método clínico o objetivo é o diagnóstico individual para cura ou reabilitação; no método epidemiológico o objetivo é conhecer a frequência e determinantes populacionais para prevenção e planejamento.",
            "O método epidemiológico prescinde totalmente de critérios diagnósticos objetivos, apoiando-se em intuição diagnóstica."
        ],
        "answer": 2,
        "target": "estudos_epidemiologicos",
        "hint": "Lembre-se do quadro comparativo dos slides: Objeto, Investigação, Diagnóstico e Tratamento.",
        "explanation": "No método clínico, o objeto é o indivíduo, a investigação é a anamnese/exame físico individual, o diagnóstico é a enfermidade individual e o tratamento visa a cura/alívio. No método epidemiológico, o objeto é a população, a investigação são inquéritos/levantamentos, o diagnóstico é a situação de saúde/índices e o tratamento é o plano de saúde pública/medidas preventivas.",
        "wrongReasons": [
            "A alternativa inverteu: no método clínico o foco é o indivíduo; no epidemiológico o foco é a população/comunidade.",
            "Inquéritos e taxas pertencem à epidemiologia; anamnese e prontuário individual pertencem à clínica odontológica.",
            None,
            "A epidemiologia exige critérios diagnósticos padronizados e reprodutíveis (OMS, ICDNT, Dean), muito mais rígidos que a subjetividade clínica."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "Um estudo comunitário que avalia o impacto da adição de flúor às águas de abastecimento público de um município, comparando-o com um município vizinho sem água fluoretada, caracteriza-se como um:",
        "options": [
            "Ensaio clínico individualizado duplo-cego em ambulatório.",
            "Ensaio comunitário (ou quase-experimento de intervenção comunitária).",
            "Estudo de série de casos puramente descritivo de consultório privado.",
            "Estudo retrospectivo de caso-controle baseado em prontuários clínicos privados."
        ],
        "answer": 1,
        "target": "estudos_experimentais",
        "hint": "A unidade de intervenção não é o indivíduo isolado, mas a comunidade como um todo atendida pela rede de abastecimento.",
        "explanation": "Ensaios comunitários são estudos de intervenção em que a manipulação do fator de exposição (neste caso, a fluoretação da água) é aplicada a grupos populacionais inteiros ou comunidades geográficas, e não alocada individualmente a cada paciente.",
        "wrongReasons": [
            "Não é um ensaio individual duplo-cego, pois a intervenção é feita na infraestrutura urbana de água para toda a cidade.",
            None,
            "Série de casos é um estudo descritivo observacional de poucos pacientes, totalmente incompatível com a avaliação de uma política municipal de fluoretação.",
            "Não é um caso-controle retrospectivo, mas sim uma intervenção de saúde pública acompanhada no tempo."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "Nos estudos analíticos em saúde bucal, as variáveis sob investigação dividem-se fundamentalmente em dependentes e independentes. A variável DEPENDENTE é aquela que:",
        "options": [
            "Representa a intervenção administrada ativamente pelo pesquisador.",
            "Representa o desfecho ou a doença cujo comportamento se busca explicar (ex: presença de cárie ou bolsa periodontal).",
            "É sempre uma característica imutável do pesquisador responsável pelo levantamento.",
            "Representa exclusivamente o custo financeiro do exame epidemiológico por sextante."
        ],
        "answer": 1,
        "target": "estudos_descritivos_analiticos",
        "hint": "A variável dependente 'depende' dos fatores de exposição; ela é o resultado biológico/clínico em estudo.",
        "explanation": "A variável dependente (ou variável de desfecho / resposta) é a condição patológica, agravo ou evento clínico que está sendo estudado (ex: prevalência de fluorose, perda dentária). A variável independente é a suposta causa ou fator de exposição (ex: consumo de açúcar, tabagismo, renda familiar).",
        "wrongReasons": [
            "A intervenção administrada ou o fator causal presumido é a variável independente de exposição.",
            None,
            "Características do pesquisador não são as variáveis dependentes biológicas do estudo.",
            "O custo orçamentário é uma métrica de gestão logística, não a variável biológica dependente de saúde-doença."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "Qual das seguintes afirmações sobre o Ensaios Clínicos Randomizados (ECR) em odontologia está CORRETA?",
        "options": [
            "A alocação dos participantes aos grupos teste e controle é decidida pela preferência pessoal do paciente.",
            "A randomização assegura que fatores de confusão conhecidos e desconhecidos sejam distribuídos de maneira homogênea entre os grupos comparados.",
            "Ensaios clínicos randomizados nunca podem ser cegados, sendo obrigatório que o examinador saiba quem recebeu placebo.",
            "São estudos de baixo custo, fáceis de conduzir e sem nenhuma implicação de comitês de ética em pesquisa."
        ],
        "answer": 1,
        "target": "estudos_experimentais",
        "hint": "O que a alocação aleatória (sorteio) traz de mais valioso para a validade interna do estudo?",
        "explanation": "A grande força do Ensaio Clínico Randomizado reside na alocação aleatória (randomização), que neutraliza vieses de seleção e distribui homogeneamente variáveis de confusão (como idade, higiene e dieta) entre o grupo que recebe o tratamento e o grupo controle.",
        "wrongReasons": [
            "A alocação não é livre escolha do paciente; se o paciente escolhesse, haveria grave viés de seleção.",
            None,
            "O mascaramento (cegamento simples, duplo ou triplo) é altamente desejável e frequentemente implementado em ECRs.",
            "ECRs são estudos complexos, onerosos, demorados e que exigem rigorosa aprovação ética (CEP/CONEP) com termo de consentimento livre e esclarecido."
        ]
    },
    {
        "cat": 0,
        "sub": "tipos_estudos",
        "pool": "all",
        "text": "A vigilância em saúde bucal apoia-se em estudos epidemiológicos sistemáticos para cumprir seu papel sanitário. A esse respeito, é INCORRETO afirmar:",
        "options": [
            "A vigilância em saúde bucal restringe-se a registrar óbitos decorrentes de câncer bucal em hospitais terciários.",
            "Permite o acompanhamento contínuo da ocorrência de cárie, doença periodontal e fluorose na população.",
            "Subsidia o planejamento de ações preventivas e a distribuição de recursos humanos e materiais na atenção primária.",
            "Utiliza dados de inquéritos nacionais periódicos (como o SB Brasil) e dados contínuos dos sistemas de informação (SISAB)."
        ],
        "answer": 0,
        "target": "estudos_epidemiologicos",
        "hint": "Atenção ao termo restritivo: a vigilância em saúde bucal abrange uma vasta gama de condições clínicas e preventivas na APS, não apenas óbitos hospitalares.",
        "explanation": "A vigilância em saúde bucal vai muito além de óbitos: monitora cárie, fluorose, perda dentária, periodontopatias, traumatismos e maloclusões em todas as faixas etárias para alimentar políticas públicas de prevenção e atenção integral.",
        "wrongReasons": [
            None,
            "Esta afirmação é verdadeira: o monitoramento continuado desses agravos é o cerne da vigilância em saúde bucal.",
            "Esta afirmação é verdadeira: dados epidemiológicos fundamentam o planejamento na APS.",
            "Esta afirmação é verdadeira: inquéritos populacionais e sistemas contínuos integram a vigilância."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 2: desenhos_pesquisa (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "Um pesquisador deseja conhecer a prevalência de cárie dentária e a necessidade de prótese total em idosos de 65 a 74 anos de uma determinada cidade em um dado momento temporal. O desenho epidemiológico mais indicado para este fim é:",
        "options": [
            "Estudo de Coorte prospectivo de 30 anos.",
            "Estudo Transversal (ou Seccional / de Prevalência).",
            "Ensaio Clínico Randomizado cruzado com placebo.",
            "Estudo Experimental in vitro com cortes histológicos."
        ],
        "answer": 1,
        "target": "estudo_transversal",
        "hint": "O objetivo é medir a prevalência atual (foto instantânea da população) em um ponto fixo no tempo.",
        "explanation": "O estudo transversal (corte transversal ou inquérito de prevalência) avalia a presença da exposição e da doença simultaneamente em um determinado ponto no tempo. É o modelo padrão-ouro para diagnósticos de situação de saúde bucal populacional e planejamento de serviços.",
        "wrongReasons": [
            "O estudo de coorte mede incidência e novos casos ao longo do tempo, sendo excessivamente longo e custoso para uma estimativa de prevalência pontual.",
            None,
            "Ensaio clínico testa tratamentos sob intervenção experimental, não servindo para diagnosticar o panorama epidemiológico populacional da cidade.",
            "Estudo in vitro é laboratorial básico, incapaz de medir prevalência de cárie ou edentulismo na sociedade."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "A principal limitação metodológica inerente aos estudos transversais em relação à determinação de causalidade reside na:",
        "options": [
            "Impossibilidade de utilizar questionários socioeconômicos.",
            "Dificuldade de estabelecer a precedência temporal entre a exposição e o desfecho (viés de causalidade reversa).",
            "Exigência compulsória de acompanhar os participantes até o final da vida.",
            "Incapacidade absoluta de calcular frequências relativas ou porcentagens amostrais."
        ],
        "answer": 1,
        "target": "estudo_transversal",
        "hint": "Se você fotografa a pessoa no mesmo momento com a exposição e a doença, como saber quem veio antes: o ovo ou a galinha?",
        "explanation": "Como a exposição e o desfecho são aferidos no mesmo instante ('fotografia instantânea'), os estudos transversais têm dificuldade em comprovar que a exposição precedeu a doença no tempo, podendo incorrer no viés da causalidade reversa.",
        "wrongReasons": [
            "Estudos transversais utilizam rotineiramente questionários sociodemográficos e comportamentais amplos.",
            None,
            "Estudos transversais não realizam seguimento temporal; quem acompanha indivíduos no tempo é o estudo de coorte.",
            "Estudos transversais calculam perfeitamente taxas de prevalência, frequências relativas e porcentagens."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "Em um estudo de COORTE, a seleção dos grupos de participantes parte de:",
        "options": [
            "Indivíduos doentes (casos) e sadios (controles), investigando o passado para buscar exposições.",
            "Indivíduos livres da doença sob investigação, classificados segundo o seu status de exposição a um fator de risco, acompanhados ao longo do tempo.",
            "Registros agregados de países inteiros comparando consumo de açúcar per capita sem contato com as pessoas.",
            "Apenas pacientes internados em Unidades de Terapia Intensiva com patologias terminais."
        ],
        "answer": 1,
        "target": "estudo_coorte",
        "hint": "Coorte parte da EXPOSIÇÃO para o DESFECHO: seleciona quem fuma e quem não fuma (ambos sem periodontite) e acompanha no tempo.",
        "explanation": "No estudo de coorte, os participantes são selecionados com base na sua exposição ou não ao fator de risco presumido, devendo estar inicialmente livres do desfecho (doença). Eles são seguidos prospectivamente ao longo do tempo para aferir a incidência de novos casos da doença.",
        "wrongReasons": [
            "Partir de doentes (casos) e não doentes (controles) investigando o passado é o desenho de Caso-Controle.",
            None,
            "Análise de dados médios agregados de países inteiros caracteriza o Estudo Ecológico.",
            "Estudos de coorte geralmente avaliam populações gerais ou grupos ocupacionais saudáveis no início do acompanhamento."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "A medida de associação epidemiológica típica calculada em estudos de COORTE, obtida pela razão entre a incidência nos expostos e a incidência nos não-expostos, denomina-se:",
        "options": [
            "Odds Ratio (Razão de Chances).",
            "Risco Relativo (RR).",
            "Índice CPO-D médio corrigido.",
            "Coeficiente Kappa de concordância interexaminador."
        ],
        "answer": 1,
        "target": "estudo_coorte",
        "hint": "Como o coorte mede diretamente a INCIDÊNCIA nos dois grupos, calcula-se a razão de riscos.",
        "explanation": "O Risco Relativo (RR) é calculado como: Incidência nos Expostos (Ie) / Incidência nos Não-Expostos (Io). Por medir diretamente a incidência no tempo, o estudo de coorte é o delineamento observacional por excelência para o cálculo do RR.",
        "wrongReasons": [
            "O Odds Ratio (OR) é a medida típica de estudos Caso-Controle, onde não é possível calcular a incidência real da população.",
            None,
            "CPO-D é um índice de ataque de cárie dentária, não uma medida bioestatística de associação de risco relativo.",
            "O coeficiente Kappa mede a concordância diagnóstica entre examinadores, nada tendo a ver com risco epidemiológico."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "Pesquisadores investigaram a associação entre tabagismo pesado e carcinoma espinocelular de boca. Selecionaram 150 pacientes com câncer bucal e 150 pacientes sem câncer bucal emparelhados por idade e sexo, investigando retrospectivamente o histórico de tabagismo nos últimos 20 anos. Esse delineamento é:",
        "options": [
            "Estudo de Coorte prospectivo.",
            "Estudo Caso-Controle.",
            "Ensaio de Campo comunitário com intervenção direta.",
            "Inquérito Transversal de base escolar."
        ],
        "answer": 1,
        "target": "estudo_caso_controle",
        "hint": "Começou pelo desfecho (150 doentes = casos, 150 sadios = controles) e olhou para trás no tempo.",
        "explanation": "O estudo Caso-Controle parte da identificação de indivíduos com a doença (casos) e sem a doença (controles) e analisa retrospectivamente a frequência de exposição prévia aos fatores de risco. É o método ideal e mais eficiente para estudar doenças raras ou de longo período de indução.",
        "wrongReasons": [
            "O coorte começaria com fumantes e não fumantes livres de câncer e os seguiria para o futuro.",
            None,
            "Não houve nenhuma intervenção comunitária ou aplicação experimental de produtos.",
            "Não é um inquérito transversal escolar, pois selecionou grupos clínicos hospitalares com base na presença/ausência de neoplasia maligna."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "A medida de associação primária empregada nos estudos Caso-Controle para estimar a força da associação entre a exposição e a doença é o:",
        "options": [
            "Coeficiente de mortalidade infantil por mil nascidos vivos.",
            "Odds Ratio (OR ou Razão de Chances).",
            "Índice de Dean ponderado pela idade biológica.",
            "Grau de inserção periodontal (PIP) em milímetros."
        ],
        "answer": 1,
        "target": "estudo_caso_controle",
        "hint": "Como o tamanho da população sob risco não é conhecido no caso-controle, não se mede incidência; compara-se a chance de exposição entre casos e controles.",
        "explanation": "No estudo Caso-Controle, os pesquisadores determinam o número de casos e controles, não sendo possível calcular taxas de incidência da doença na população. Utiliza-se, portanto, o Odds Ratio (Razão de Chances ou Razão de Produtos Cruzados) para estimar a associação.",
        "wrongReasons": [
            "Mortalidade infantil é um indicador demográfico de saúde pública geral.",
            None,
            "Índice de Dean mede a severidade de fluorose dentária.",
            "O PIP mede perda de inserção clínica periodontal em levantamentos clínicos, não associação bioestatística."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "Um estudo correlacionou o consumo médio per capita de açúcar vendido nos supermercados de 20 estados brasileiros com o índice CPO-D médio estadual obtido no SB Brasil, concluindo que o consumo de sacarose está associado à cárie. A unidade de observação desse estudo é:",
        "options": [
            "O indivíduo isolado com suas fichas clínicas de acompanhamento.",
            "O agregado populacional (estados brasileiros), caracterizando um Estudo Ecológico.",
            "Células bacterianas de Streptococcus mutans em cultura de laboratório.",
            "Famílias nucleares acompanhadas em visitas domiciliares na ESF."
        ],
        "answer": 1,
        "target": "estudo_ecologico",
        "hint": "A unidade de análise não é a pessoa (João ou Maria), mas o conjunto coletivo territorial (o estado, a cidade).",
        "explanation": "Em estudos ecológicos (ou correlacionais), a unidade de observação e análise é um grupo de indivíduos ou uma população agregada (municípios, estados, países), e não a pessoa individual. Compara-se a média de exposição com a taxa global do desfecho naquela coletividade.",
        "wrongReasons": [
            "Nos estudos ecológicos não há dados individualizados de cada pessoa.",
            None,
            "Culturas bacterianas são objeto de microbiologia laboratorial, não de epidemiologia ecológica.",
            "Famílias individuais não foram a unidade de mensuração agregada neste exemplo estadual."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "A 'Falácia Ecológica' (ou viés de agregação) ocorre quando o pesquisador:",
        "options": [
            "Usa materiais de moldagem odontológica não biodegradáveis que poluem o meio ambiente.",
            "Comete o erro de inferir que uma associação observada no nível agregado/populacional necessariamente se aplica a cada indivíduo daquela população.",
            "Coleta amostras de água de abastecimento fora dos frascos estéreis padronizados pela ABNT.",
            "Esquece de preencher o cabeçalho sociodemográfico da ficha clínica do exame periodontal."
        ],
        "answer": 1,
        "target": "estudo_ecologico",
        "hint": "É o salto indevido do coletivo para o individual: 'o estado tem alto consumo de açúcar e alta cárie, logo aquele paciente específico cárie porque ele come muito açúcar'.",
        "explanation": "A falácia ecológica consiste em atribuir aos indivíduos de uma população características ou associações estatísticas observadas exclusivamente no nível agregado (macrogrupos). Nem todo indivíduo residente no estado com alto consumo médio de açúcar foi quem consumiu o açúcar ou desenvolveu cárie.",
        "wrongReasons": [
            "A falácia ecológica é um conceito bioestatístico e metodológico, nada tendo a ver com sustentabilidade ambiental de resíduos odontológicos.",
            None,
            "Contaminação de frascos de água é um erro operacional de amostragem bromatológica, não falácia ecológica.",
            "Esquecer de preencher dados na ficha é falha de anotação de campo."
        ]
    },
    {
        "cat": 0,
        "sub": "desenhos_pesquisa",
        "pool": "all",
        "text": "Considere que um estudo de coorte em saúde bucal encontrou um Risco Relativo (RR) de 3,4 para a associação entre tabagismo e perda óssea alveolar severa, com intervalo de confiança de 95% variando de 2,1 a 5,2. Esse achado indica que:",
        "options": [
            "O tabagismo é um fator protetor que reduz o risco de perda óssea alveolar.",
            "Os indivíduos tabagistas apresentaram risco 3,4 vezes maior de desenvolver perda óssea severa em comparação aos não-tabagistas, sendo a associação estatisticamente significante.",
            "O estudo deve ser anulado, pois qualquer valor de RR diferente de zero indica erro amostral.",
            "Exatamente 3,4% de todos os participantes do estudo desenvolveram câncer de boca."
        ],
        "answer": 1,
        "target": "estudo_coorte",
        "hint": "RR > 1 indica fator de risco; como o IC95% (2,1 a 5,2) não inclui o valor nulo 1, a associação é significante.",
        "explanation": "Um Risco Relativo de 3,4 significa que a incidência da doença no grupo exposto é 3,4 vezes maior que no grupo não-exposto. Como o intervalo de confiança de 95% não inclui a unidade (1,0), a associação observada é estatisticamente significante, confirmando o tabagismo como fator de risco para periodontite severa.",
        "wrongReasons": [
            "Fator protetor apresentaria RR menor do que 1,0 (ex: RR = 0,4).",
            None,
            "O valor nulo de ausência de efeito para RR e OR é 1,0, e não zero.",
            "RR não representa percentual absoluto de doentes, mas sim uma razão entre duas taxas de incidência."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 3: planejamento_levantamentos (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Segundo as recomendações da Organização Mundial da Saúde (OMS) e as diretrizes do SB Brasil, a equipe mínima de campo para realização de exames epidemiológicos bucais é formada por uma 'tríade':",
        "options": [
            "Um cirurgião-dentista clínico geral, um radiologista e um bioquímico.",
            "Examinador (cirurgião-dentista), Anotador (geralmente TSB/ASB ou estudante treinado) e Monitor (organizador do fluxo e biossegurança).",
            "Apenas o cirurgião-dentista, que deve simultaneamente ditar, examinar e preencher a ficha.",
            "Um médico de família, um enfermeiro sanitarista e o diretor da unidade de saúde."
        ],
        "answer": 1,
        "target": "equipe_levantamento",
        "hint": "Quem dita os códigos? Quem anota com atenção? Quem organiza as crianças e a biossegurança?",
        "explanation": "A tríade operacional padrão estabelecida pela OMS e pelo Ministério da Saúde é composta pelo Examinador (responsável pelo exame visual/tátil padronizado), pelo Anotador (responsável pelo preenchimento fidedigno da ficha de campo) e pelo Monitor (responsável pelo fluxo, acolhimento, biossegurança e escovação supervisionada prévia).",
        "wrongReasons": [
            "Não há radiologista nem bioquímico em levantamentos epidemiológicos bucais de campo padrão.",
            None,
            "O examinador nunca deve anotar simultaneamente, pois isso quebra a cadeia asséptica, reduz o ritmo e aumenta dramaticamente o erro diagnóstico.",
            "A equipe de exame bucal é composta primordialmente por pessoal treinado em odontologia e saúde bucal."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Durante o exame epidemiológico no campo, qual é a conduta correta do ANOTADOR para assegurar a fidelidade dos dados registrados?",
        "options": [
            "Anotar em silêncio absoluto para não desconcentrar o examinador e inventar códigos quando não escutar direito.",
            "Repetir em voz alta o código que ouviu do examinador, aguardar confirmação tácita e certificar-se de não deixar quadrículas em branco na ficha.",
            "Corrigir o diagnóstico do cirurgião-dentista sempre que discordar da presença de cárie.",
            "Interromper o exame para orientar a escovação dentária individual de cada voluntário."
        ],
        "answer": 1,
        "target": "equipe_levantamento",
        "hint": "A técnica da repetição em voz alta (eco) garante que o código falado seja exatamente o código transcrito.",
        "explanation": "O anotador deve repetir em voz alta cada código ditado pelo examinador para que eventuais falhas de audição ou lapsos sejam imediatamente corrigidos. Além disso, antes de liberar o participante, deve verificar minuciosamente se todos os campos da ficha foram preenchidos.",
        "wrongReasons": [
            "O anotador nunca deve adivinhar códigos nem ficar em silêncio; ele deve confirmar repetindo em voz alta.",
            None,
            "O anotador não pode alterar o diagnóstico do examinador calibrado.",
            "A orientação de escovação é função prévia do monitor/educador, não do anotador durante o registro."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Qual das seguintes atribuições compete precipuamente ao MONITOR da equipe de levantamento epidemiológico?",
        "options": [
            "Diagnosticar se as bolsas periodontais ultrapassam 5,5 mm na sonda Trinity.",
            "Organizar o fluxo e chamada dos voluntários, conferir o consentimento (TCLE/TALE), coordenar a escovação prévia e zelar pela biossegurança de campo.",
            "Decidir sozinho a alíquota de fluoreto adicionada à rede de abastecimento municipal.",
            "Fazer o cálculo final do coeficiente Kappa após o encerramento do inquérito."
        ],
        "answer": 1,
        "target": "equipe_levantamento",
        "hint": "O monitor é o guardião da logística externa ao ato do exame: fluxo, preparação e acolhimento.",
        "explanation": "O monitor acolhe os participantes, organiza a fila e conferência de autorizações (TCLE/TALE), coordena a higiene bucal prévia (remoção de biofilme e restos com escovação supervisionada) e auxilia na reposição de instrumentais estéreis e biossegurança do ambiente.",
        "wrongReasons": [
            "Diagnóstico periodontal com sonda Trinity é atribuição clínica exclusiva do examinador cirurgião-dentista.",
            None,
            "Fluoretação da água é responsabilidade de companhias de saneamento ambiental sob vigilância sanitária.",
            "O cálculo estatístico de Kappa é executado pelo coordenador epidemiológico / bioestatístico da pesquisa."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "A OMS recomenda parâmetros de carga horária e produtividade para evitar a fadiga visual e física do examinador em levantamentos de saúde bucal. A recomendação padrão é de:",
        "options": [
            "Trabalho ininterrupto de 12 horas diárias examinando cerca de 120 pessoas por turno.",
            "No máximo 4 a 5 horas diárias de exames clínicos, examinando aproximadamente 30 a 35 voluntários por dia por examinador.",
            "Exames apenas no período noturno utilizando lanternas individuais de smartphone.",
            "Um teto ilimitado de exames, pois quanto mais cansado o examinador, mais rápido ele diagnostica."
        ],
        "answer": 1,
        "target": "equipe_levantamento",
        "hint": "A fadiga do examinador é um dos maiores fatores de erro diagnóstico. O limite diário de exames é de cerca de 30 a 35 pessoas.",
        "explanation": "Para preservar a acurácia diagnóstica e evitar o cansaço visual e postural do examinador, a OMS preconiza turnos diários de no máximo 4 a 5 horas de exame clínico, totalizando em média 30 a 35 pessoas por dia por examinador (com teto sugerido de 300 a 400 exames totais por profissional no inquérito).",
        "wrongReasons": [
            "12 horas ininterruptas causariam estafa extrema, destruindo a confiabilidade diagnóstica dos dados.",
            None,
            "Exames devem ser realizados sob luz natural indireta favorável ou iluminação artificial adequada durante o dia.",
            "O cansaço aumenta drasticamente os falsos-positivos e falsos-negativos, sendo proibido ultrapassar limites saudáveis."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Para viabilizar a rotina de esterilização e manter a continuidade dos exames de campo, a quantidade mínima recomendada de instrumentais (espelhos bucais planos e sondas periodontais OMS) por examinador é de:",
        "options": [
            "Apenas 1 espelho e 1 sonda, lavados na torneira com detergente entre os pacientes.",
            "Pelo menos 30 a 35 conjuntos de espelhos planos e sondas OMS por examinador para permitir rotatividade e autoclave diária.",
            "500 kits cirúrgicos completos com boticões e alavancas para cada examinador.",
            "Nenhum instrumental metálico, sendo obrigatório o uso de espátulas de madeira de sorvete."
        ],
        "answer": 1,
        "target": "equipe_levantamento",
        "hint": "Se o examinador avalia cerca de 30 pessoas por dia, quantos kits estéreis ele precisa ter disponíveis?",
        "explanation": "Recomenda-se um estoque de pelo menos 30 a 35 jogos de espelho plano e sonda OMS para cada examinador. Isso permite realizar os exames do turno sem interrupção e enviar os conjuntos para esterilização (autoclave) em pacotes selados para o dia seguinte.",
        "wrongReasons": [
            "Lavar na torneira entre pacientes viola gravemente as normas de biossegurança e causa contaminação cruzada.",
            None,
            "Não se utilizam boticões e instrumentos cirúrgicos mutiladores em inquéritos epidemiológicos observacionais.",
            "Espátulas de madeira não substituem o espelho bucal plano e a sonda periodontal milimetrada da OMS."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Sobre as condições de iluminação e posicionamento para os exames clínicos no campo em levantamentos epidemiológicos, é CORRETO afirmar:",
        "options": [
            "O participante deve ficar sob sol direto do meio-dia para garantir máxima incidência de raios ultravioleta.",
            "Deve-se buscar iluminação natural indireta de boa qualidade, sentando o participante de costas para a janela/abertura de luz e o examinador de frente para a boca e a fonte luminosa.",
            "É expressamente proibido o uso de lanternas de LED frontais mesmo em salas escuras sem janela.",
            "O examinador deve ficar em pé e o participante deitado no chão de concreto sem encosto."
        ],
        "answer": 1,
        "target": "regras_exame_oms",
        "hint": "Como posicionar o paciente e a luz? A luz natural indireta deve iluminar a cavidade bucal sem ofuscar o examinador.",
        "explanation": "A iluminação de campo deve ser natural indireta (evitando sol direto que gera reflexos e ofuscamento) ou com luz artificial portátil padronizada. O participante deve estar sentado em cadeira de espaldar alto com a luz incidindo sobre sua face/boca, enquanto o examinador se posiciona comodamente para visualização direta e indireta.",
        "wrongReasons": [
            "Sol direto causa desconforto térmico ao voluntário, ressecamento tecidual e ofuscamento visual ao examinador.",
            None,
            "Lanternas de LED frontais com luz branca padronizada são aceitas e recomendadas quando a luz natural for insuficiente.",
            "Examinador e participante devem estar adequadamente acomodados (cadeira anatômica ou mesa com encosto) preservando a ergonomia."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Em relação às normas de biossegurança estipuladas pela OMS para levantamentos epidemiológicos em odontologia, qual conduta é OBRIGATÓRIA?",
        "options": [
            "Uso de luvas de procedimento cirúrgico, sendo mandatória a troca de par de luvas a cada novo participante examinado.",
            "Reutilização da mesma luva de procedimento durante todo o turno matutino, higienizando-a apenas com álcool gel sobre as mãos enluvadas.",
            "Dispensa total do uso de máscara e óculos de proteção pelo examinador em dias de calor intenso.",
            "Desinfecção dos espelhos clínicos bucais em água sanitária por 1 minuto sem autoclave."
        ],
        "answer": 0,
        "target": "equipe_levantamento",
        "hint": "A troca de luvas entre pacientes é regra inviolável de biossegurança: novo participante = novo par de luvas descartáveis.",
        "explanation": "O examinador e a equipe devem utilizar EPI completo (avental/jaleco, gorro, máscara cirúrgica ou N95 e óculos de proteção). É absolutamente obrigatória a troca das luvas de procedimento descartáveis a cada participante examinado para evitar transmissão cruzada de patógenos.",
        "wrongReasons": [
            None,
            "Passar álcool sobre luvas degrada o látex e nitrila gerando microporosidades, além de não eliminar o risco biológico cruzado.",
            "Máscaras e óculos de proteção são indispensáveis contra respingos de saliva e aerossóis, independente do clima.",
            "Instrumentais semicríticos com risco de contato sanguíneo ou mucoso exigem esterilização completa por autoclave."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Antes do início do exame clínico intraoral em crianças e escolares, qual procedimento prévio de higiene deve ser executado sob coordenação do monitor?",
        "options": [
            "Aplicação tópica de flúor gel a 1,23% e bochecho com peróxido de hidrogênio a 10%.",
            "Escovação dentária supervisionada com pasta e escova descartável para remoção do biofilme visível e restos alimentares.",
            "Profilaxia mecânica com taça de borracha, pedra-pomes e motor de alta rotação sem refrigeração.",
            "Bochecho obrigatório com anestésico tópico para eliminar a sensibilidade à sonda."
        ],
        "answer": 1,
        "target": "regras_exame_oms",
        "hint": "Para enxergar as superfícies dentárias com clareza, os dentes devem estar limpos de placa bacteriana e restos de comida.",
        "explanation": "A remoção mecânica do biofilme e restos de alimentos através da escovação supervisionada prévia é etapa essencial, pois permite ao examinador inspecionar visualmente fossas, fissuras, cicatrículas e a margem gengival sem interferência de resíduos alimentares.",
        "wrongReasons": [
            "Não se aplica flúor gel concentrado antes do exame, pois isso alteraria a condição superficial e os critérios de mancha branca.",
            None,
            "Não há uso de motores de alta rotação nem profilaxia profissional agressiva no campo de levantamentos comunitários.",
            "Não se utiliza anestésico tópico na cavidade oral para exames epidemiológicos observacionais da OMS."
        ]
    },
    {
        "cat": 0,
        "sub": "planejamento_levantamentos",
        "pool": "all",
        "text": "Durante o exame, caso restos alimentares ou saliva espessa cubram uma fossa oclusal de um molar, a conduta correta do examinador segundo a OMS é:",
        "options": [
            "Inserir com força a ponta pontiaguda de uma sonda exploradora afiada número 5 até ouvir um estalo de retenção mecânica.",
            "Remover cuidadosamente os restos com uma mecha de gaze esterilizada ou rolete de algodão antes de inspecionar com a sonda da OMS.",
            "Atribuir automaticamente o código de dente cariado sem remover a sujeira.",
            "Excluir o dente imediatamente do inquérito atribuindo o código 9."
        ],
        "answer": 1,
        "target": "regras_exame_oms",
        "hint": "A OMS proíbe sondas exploradoras pontiagudas e orienta limpar suavemente com algodão/gaze para visualização clara.",
        "explanation": "Se houver resíduos ou saliva cobrindo as estruturas anatômicas, o examinador deve limpar a área utilizando gaze ou rolete de algodão estéril. A OMS proíbe terminantemente o uso de sondas afiadas com pressão em fossas e fissuras pelo alto risco de cavitação iatrogênica em lesões iniciais.",
        "wrongReasons": [
            "Pressionar sonda exploradora pontiaguda causa iatrogenia (fratura do esmalte hipomineralizado) e é proibido pela OMS.",
            None,
            "O examinador não pode chutar ou presumir cárie sem limpar e visualizar nitidamente o esmalte subjacente.",
            "O código 9 (excluído) é reservado para dentes com bandas ortodônticas, dentes pilares de prótese fixa ou impossíveis de examinar."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 4: calibracao_concordancia (8 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "O processo de calibração em epidemiologia de saúde bucal tem como objetivo fundamental:",
        "options": [
            "Aumentar o número de dentes cariados encontrados para justificar mais verbas governamentais.",
            "Uniformizar e padronizar os critérios diagnósticos entre os examinadores, reduzindo os erros sistemáticos e garantindo a reprodutibilidade dos dados.",
            "Calibrar os autoclaves da universidade quanto à pressão de vapor e temperatura manométrica.",
            "Definir a nota dos alunos na disciplina de acordo com a velocidade do exame intraoral."
        ],
        "answer": 1,
        "target": "calibracao_kappa",
        "hint": "Calibrar os examinadores significa garantir que todos vejam e classifiquem a mesma lesão com o mesmo critério e código.",
        "explanation": "A calibração dos examinadores visa padronizar a aplicação dos critérios diagnósticos da OMS, reduzindo a variabilidade intra e interexaminador e minimizando vieses de medição, assegurando que os dados coletados sejam fidedignos, válidos e internacionalmente comparáveis.",
        "wrongReasons": [
            "A calibração busca a verdade epidemiológica e a reprodutibilidade, jamais inflar artificialmente índices de doença.",
            None,
            "A calibração em epidemiologia refere-se à padronização dos examinadores humanos, não à manutenção física do autoclave.",
            "A velocidade do exame não é critério de qualidade; o fundamental é o rigor e a consistência diagnóstica."
        ]
    },
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "A concordância INTRA-examinador e a concordância INTER-examinador avaliam, respectivamente:",
        "options": [
            "A concordância de um examinador consigo mesmo ao examinar os mesmos pacientes em momentos distintos; e a concordância entre diferentes examinadores (ou com um examinador padrão-ouro).",
            "O índice de placa bacteriana intraoral; e a presença de tártaro interdental.",
            "A velocidade de digitação do anotador; e a paciência do monitor com os voluntários.",
            "A precisão da balança antropométrica; e a altura do voluntário no estadiômetro."
        ],
        "answer": 0,
        "target": "calibracao_kappa",
        "hint": "'Intra' = dentro de si mesmo (consistência interna); 'Inter' = entre indivíduos diferentes (comparação mútua).",
        "explanation": "A concordância intra-examinador verifica se o mesmo examinador mantém o mesmo critério diagnóstico quando reexamina os mesmos indivíduos após certo intervalo. A concordância inter-examinador mede a consonância diagnóstica entre examinadores diferentes ou em relação a um padrão-ouro de referência.",
        "wrongReasons": [
            None,
            "Não se refere a localização de placa ou tártaro, mas à métrica estatística de consistência diagnóstica humana.",
            "Refere-se ao exame clínico do cirurgião-dentista examinador, não à digitação do anotador.",
            "Mede a concordância nos códigos bucais (CPO-D, ICDNT, Dean, CPI), não medidas antropométricas corporais."
        ]
    },
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "De acordo com o protocolo da OMS e os slides do Prof. André, o processo clássico de calibração divide-se em etapas consecutivas. Na etapa de 'treinamento clínico prévio', recomenda-se que:",
        "options": [
            "Os examinadores viajem para Genebra para uma prova escrita dissertativa.",
            "Examinem em conjunto um grupo de cerca de 6 a 8 voluntários com ampla variedade de condições bucais, discutindo amplamente cada divergência diagnóstica.",
            "Realizem exames em 1.000 voluntários sem nenhuma discussão prévia sobre os códigos.",
            "Cada examinador escolha seus próprios códigos e critérios de acordo com livros antigos."
        ],
        "answer": 1,
        "target": "calibracao_kappa",
        "hint": "No treinamento clínico preliminar, um pequeno grupo (6 a 8 crianças/voluntários com lesões diversas) é examinado e cada divergência é discutida à beira da cadeira.",
        "explanation": "Após a etapa teórica em sala de aula, o treinamento clínico preliminar reúne 6 a 8 indivíduos portadores de variadas condições (dentes hígidos, cáries ativas/inativas, restaurações, fluorose). Todos os examinadores avaliam esses pacientes em conjunto, discutindo abertamente os critérios para unificar a percepção clínica.",
        "wrongReasons": [
            "A calibração é conduzida localmente pela coordenação do inquérito e professores calibradores credenciados.",
            None,
            "Treinar em 1.000 pessoas sem discutir geraria erro maciço sem qualquer aprendizado corretivo.",
            "O objetivo da calibração é exatamente eliminar critérios individuais próprios, adotando rigidamente as diretrizes da OMS."
        ]
    },
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "Na etapa formal de calibração e cálculo de concordância diagnóstica que precede a ida ao campo, a recomendação da OMS é que cada examinador examine:",
        "options": [
            "Apenas uma foto impressa de dentes extraídos.",
            "Cerca de 15 a 20 indivíduos, reexaminando-os após um intervalo de tempo para o cálculo do coeficiente de concordância estatística.",
            "500 pacientes consecutivos no hospital de urgência odontológica.",
            "Somente manequins de plástico com dentes pré-furados por brocas."
        ],
        "answer": 1,
        "target": "calibracao_kappa",
        "hint": "O grupo de calibração estatística consiste em cerca de 15 a 20 pessoas examinadas e reexaminadas.",
        "explanation": "Na etapa de calibração formal, seleciona-se um grupo de 15 a 20 voluntários que são examinados pelo padrão-ouro e por todos os examinadores, sendo reexaminados em dias distintos para possibilitar o cálculo do índice Kappa intra e interexaminador.",
        "wrongReasons": [
            "A calibração em fotografias ou dentes extraídos é meramente ilustrativa e teórica, não substituindo o exame clínico in vivo.",
            None,
            "500 pacientes é o tamanho de uma amostra de inquérito completa, inviável e desnecessário para a fase de calibração preliminar.",
            "Manequins artificiais não reproduzem a textura, umidade, biofilme e reflexos da cavidade bucal humana real."
        ]
    },
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "Por que a porcentagem simples de concordância (concordância bruta) NÃO é considerada suficiente pelos bioestatísticos para validar a calibração de examinadores?",
        "options": [
            "Porque porcentagens são muito difíceis de calcular sem computadores quânticos.",
            "Porque a porcentagem bruta inclui a concordância que ocorreria pelo mero acaso (sorte), superestimando a verdadeira confiabilidade diagnóstica.",
            "Porque a OMS proíbe o uso de números percentuais em qualquer relatório oficial de saúde pública.",
            "Porque a concordância bruta mede apenas a velocidade do exame em segundos."
        ],
        "answer": 1,
        "target": "calibracao_kappa",
        "hint": "Se uma doença é muito rara ou muito comum, dois examinadores concordarão muito só no 'chute'. Como descontar a sorte?",
        "explanation": "A concordância percentual simples sofre grande viés da prevalência da doença e não desconta o acordo esperado pelo mero acaso. A estatística Kappa de Cohen foi desenvolvida justamente para subtrair a concordância devida ao acaso, mensurando a concordância líquida real.",
        "wrongReasons": [
            "Porcentagens brutas são simples frações matemáticas elementares.",
            None,
            "A OMS utiliza porcentagens rotineiramente, mas exige índices específicos (como Kappa) para concordância diagnóstica.",
            "Concordância percentual mede a proporção de acordos diagnósticos, não tempo em segundos."
        ]
    },
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "Segundo a consagrada classificação de Landis & Koch para o coeficiente de concordância Kappa de Cohen, um valor de Kappa compreendido entre 0,61 e 0,80 é classificado como:",
        "options": [
            "Pobre (inaceitável para qualquer levantamento).",
            "Substancial (ou boa concordância).",
            "Perfeita (100% de precisão absoluta).",
            "Fraca (necessitando anulação imediata da pesquisa)."
        ],
        "answer": 1,
        "target": "calibracao_kappa",
        "hint": "Escala de Landis & Koch: <0.20 pobre; 0.21-0.40 fraca; 0.41-0.60 moderada; 0.61-0.80 substancial; 0.81-1.00 quase perfeita.",
        "explanation": "Na classificação de Landis & Koch: <0.20 (pobre); 0.21 a 0.40 (fraca/razoável); 0.41 a 0.60 (moderada); 0.61 a 0.80 (substancial/boa); e 0.81 a 1.00 (quase perfeita). O valor mínimo aceitável em levantamentos nacionais da OMS gira em torno de 0.65 a 0.70.",
        "wrongReasons": [
            "Pobre corresponde a valores abaixo de 0.20.",
            None,
            "Perfeita exigiria valor de 1,00 absoluto, o que raramente ocorre na prática biológica.",
            "Fraca corresponde a valores entre 0.21 e 0.40."
        ]
    },
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "Durante o levantamento epidemiológico propriamente dito em campo, qual procedimento é recomendado pela OMS para monitorar a manutenção da consistência dos examinadores ao longo das semanas de trabalho?",
        "options": [
            "Trocar todos os examinadores da equipe a cada segunda-feira.",
            "Reexaminar aleatoriamente cerca de 5% a 10% da amostra examinada, calculando a concordância intraexaminador continuada.",
            "Interromper o inquérito e aplicar uma prova teórica escrita aos examinadores no meio da rua.",
            "Examinar apenas familiares e parentes dos examinadores para garantir 100% de aprovação."
        ],
        "answer": 1,
        "target": "calibracao_kappa",
        "hint": "Para certificar que os examinadores não mudaram seus critérios ('deriva diagnóstica'), reexamina-se uma fração de 5% a 10% da amostra durante o próprio inquérito.",
        "explanation": "A OMS recomenda que durante todo o inquérito sejam realizados reexames em 5% a 10% dos participantes (selecionados de modo aleatório ou sistemático) para monitorar e reportar a consistência intraexaminador ao longo de toda a coleta de dados de campo.",
        "wrongReasons": [
            "Trocar os examinadores toda semana inviabilizaria a logística e exigiria novas calibrações dispendiosas.",
            None,
            "Provas escritas teóricas não medem a consistência visual-tátil de campo na prática clínica.",
            "Amostragem de conveniência com parentes violaria todos os preceitos éticos e metodológicos de representatividade populacional."
        ]
    },
    {
        "cat": 0,
        "sub": "calibracao_concordancia",
        "pool": "all",
        "text": "Se ao final da calibração um examinador obtiver um coeficiente Kappa de 0,35 em relação ao padrão-ouro para o diagnóstico de cárie pelo ICDNT, a conduta correta da coordenação do inquérito é:",
        "options": [
            "Liberá-lo imediatamente para iniciar os exames em escolas porque 0,35 é considerado excelente.",
            "Não liberá-lo para o campo, submetendo-o a nova discussão de critérios e novo ciclo de treinamento prático até atingir no mínimo concordância substancial (Kappa ≥ 0,65-0,70).",
            "Eliminar todas as crianças cariadas da amostra populacional para facilitar o trabalho dele.",
            "Substituir o ICDNT por intuição pessoal sem anotação em fichas."
        ],
        "answer": 1,
        "target": "calibracao_kappa",
        "hint": "Kappa de 0,35 é classificado como fraco (insuficiente). Um examinador não calibrado distorcerá os dados da pesquisa.",
        "explanation": "Examinadores com Kappa inferior ao limite de corte aceitável (habitualmente 0,65 a 0,70) não podem ir a campo para coletar dados oficiais. Eles devem passar por novo ciclo de discussão teórica, treinamento clínico e nova rodada de calibração para corrigir suas discrepâncias.",
        "wrongReasons": [
            "Kappa de 0,35 é fraco/baixo e jamais habilitaria um examinador para coletar dados epidemiológicos oficiais.",
            None,
            "Não se pode manipular a amostra populacional de campo para mascarar deficiências diagnósticas do examinador.",
            "Abandonar o índice epidemiológico padronizado destruiria a validade científica do levantamento."
        ]
    }
]

if __name__ == '__main__':
    print("QUESTIONS_P3_CAT0 count:", len(QUESTIONS_P3_CAT0))
    for i, q in enumerate(QUESTIONS_P3_CAT0):
        assert len(q['options']) == 4, f"Q{i} does not have 4 options"
        assert 0 <= q['answer'] <= 3, f"Q{i} answer out of bounds"
        assert len(q['wrongReasons']) == 4, f"Q{i} wrongReasons length != 4"
        assert q['wrongReasons'][q['answer']] is None, f"Q{i} wrongReasons at answer is not None"
        for idx, wr in enumerate(q['wrongReasons']):
            if idx != q['answer']:
                assert isinstance(wr, str) and len(wr) > 0, f"Q{i} option {idx} wrongReason missing"
    print("All 35 questions in CAT0 validated successfully!")
