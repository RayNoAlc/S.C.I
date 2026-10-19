# -*- coding: utf-8 -*-
"""
questions_p3_cat2.py
Banco de 35 questões da Categoria 2 da Prova 3:
"Fluorose Dentária e Doença Periodontal"
Subtópicos:
  - fluorose_clinica (9 questões)
  - indices_fluorose (9 questões)
  - diagnostico_diferencial (9 questões)
  - epidemiologia_periodontal (8 questões)
"""

QUESTIONS_P3_CAT2 = [
    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 1: fluorose_clinica (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "A fluorose dentária é uma anomalia de desenvolvimento do esmalte de caráter sistêmico. Sobre sua etiologia e período de ocorrência, é CORRETO afirmar:",
        "options": [
            "Ocorre pela aplicação tópica excessiva de flúor gel em dentes permanentes de adultos de 40 anos.",
            "Decorre da ingestão crônica e excessiva de fluoreto exclusivamente durante a fase de amelogênese (formação e maturação pré-eruptiva do esmalte). Dentes completamente formados e irrompidos não desenvolvem fluorose.",
            "É causada por infecção bacteriana direta nas glândulas salivares parótidas durante a adolescência.",
            "Pode se desenvolver em qualquer fase da vida adulta através do consumo de sal de cozinha iodado."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "A fluorose afeta a formação do esmalte (amelogênese) antes de o dente nascer na boca.",
        "explanation": "A fluorose dentária é causada pela ingestão crônica de fluoreto durante a amelogênese (especialmente nas fases de transição e maturação do esmalte). Uma vez que a mineralização coronária está finalizada e o dente irrompeu na cavidade bucal, não há possibilidade biológica de desenvolvimento de fluorose.",
        "wrongReasons": [
            "Aplicação tópica em adultos não causa fluorose, pois o esmalte já está maduro e completamente formado.",
            None,
            "Não tem origem bacteriana nem acomete as glândulas salivares; é uma alteração metabólica dos ameloblastos.",
            "O iodo do sal não provoca fluorose dentária e adultos não desenvolvem o agravo."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "Qual é a janela temporal mais crítica de susceptibilidade biológica para o desenvolvimento de fluorose com repercussão estética nos incisivos permanentes superiores?",
        "options": [
            "Entre os 15 e os 25 anos de idade durante a graduação universitária.",
            "Do nascimento até aproximadamente os 3 anos de idade, com período de maior vulnerabilidade entre os 15 e os 30 meses de vida.",
            "Exclusivamente durante a velhice após os 65 anos.",
            "No nono mês de gestação apenas para os terceiros molares."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "As coroas dos incisivos centrais e laterais superiores permanentes formam-se e mineralizam-se nos primeiros 3 anos de vida pós-natal.",
        "explanation": "O período crítico de risco estético para fluorose nos incisivos permanentes situa-se do nascimento até os 3 anos de idade (período de maturação do esmalte coronário), especialmente entre os 15 e 30 meses de vida, quando ocorre a calcificação e maturação dos incisivos centrais superiores.",
        "wrongReasons": [
            "Aos 15 a 25 anos todos os incisivos já estão erupcionados há muitos anos no arco.",
            None,
            "Idosos não sofrem fluorose de desenvolvimento no esmalte.",
            "Terceiros molares formam-se na infância tardia (7 a 10 anos), e não no período gestacional."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "Segundo a clássica revisão de Burt (1992), amplamente citada na epidemiologia de saúde bucal e nas aulas do Prof. André, a dose limite diária de segurança para ingestão de flúor a fim de prevenir a fluorose clinicamente inaceitável é de:",
        "options": [
            "10 a 15 mg F / kg de peso corporal / dia.",
            "0,05 a 0,07 mg F / kg de peso corporal / dia.",
            "Zero absoluto, pois qualquer molécula de flúor destrói o esmalte.",
            "100 mg F / kg de peso corporal / dia."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "A faixa de segurança de Burt é muito estreita: cinco a sete centésimos de miligrama por quilo ao dia (0,05 a 0,07 mg F/kg/dia).",
        "explanation": "Burt (1992) estabeleceu que a ingestão diária entre 0,05 e 0,07 mg de fluoreto por quilograma de peso corporal por dia constitui o limiar de equilíbrio ideal entre a máxima prevenção de cárie dentária e o risco mínimo de fluorose dentária esteticamente indesejável.",
        "wrongReasons": [
            "10 a 15 mg F/kg/dia ultrapassa em mais de 100 vezes o limite seguro, causando toxicidade crônica severa.",
            None,
            "O flúor na dose ótima (água fluoretada e dentifrício) é o principal fator preventivo da cárie sem causar danos.",
            "100 mg F/kg/dia seria uma dose letal aguda de toxicidade sistêmica gravíssima."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "Estudos epidemiológicos evidenciam que crianças de 2 a 3 anos de idade deglutem involuntariamente uma fração expressiva do creme dental durante a escovação. Essa porcentagem estimada de ingestão involuntária é de aproximadamente:",
        "options": [
            "Zero %, pois bebês sempre cospem todo o produto perfeitamente.",
            "Cerca de 48% a 65% da quantidade de dentifrício colocada na escova.",
            "Exatamente 99,9% em todas as crianças até os 18 anos.",
            "Apenas 1% se o creme dental tiver sabor de menta forte."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "Crianças pequenas ainda não possuem o reflexo de cuspir desenvolvido, engolindo cerca de metade do creme dental colocado na escova.",
        "explanation": "Devido à imaturidade do reflexo de deglutição e do controle neuromuscular em crianças com menos de 3 a 4 anos, estudos clássicos apontam que cerca de 48% a 65% do creme dental colocado na escova é involuntariamente deglutido pela criança, constituindo o principal fator de risco para fluorose em áreas fluoretadas.",
        "wrongReasons": [
            "Bebês de 2 a 3 anos não dominam a habilidade motora de expectorar totalmente a espuma do dentifrício.",
            None,
            "Aos 18 anos o reflexo de cuspir está plenamente estabelecido e a ingestão é residual mínima.",
            "Sabores artificiais adocicados até estimulam a deglutição, mas o percentual médio ingerido por crianças gira em torno de 50%."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "Qual é a recomendação oficial do Ministério da Saúde e da Sociedade Brasileira de Odontopediatria quanto à QUANTIDADE de creme dental fluoretado (1.100 ppm F) para a escovação de bebês e crianças de até 2 a 3 anos de idade?",
        "options": [
            "Preencher todas as cerdas da escova até transbordar (cerca de 2 a 3 gramas).",
            "Uma quantidade mínima equivalente a um 'grão de arroz cru' (aproximadamente 0,1 g).",
            "Não escovar os dentes até a criança completar 7 anos de idade.",
            "Dissolver meio tubo de pasta em uma jarra de refrigerante de cola."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "Para bebês: 'grão de arroz cru' (0,1 g). Para crianças que já sabem cuspir: 'grão de ervilha' (0,3 g).",
        "explanation": "Para aliar o benefício anticárie da concentração padrão (1.100 ppm F) com a segurança contra a fluorose em crianças pequenas que deglutem o produto, preconiza-se a quantidade estritamente controlada equivalente a um 'grão de arroz cru' (0,1 g) para crianças de 0 a 2/3 anos, evoluindo para um 'grão de ervilha' (0,3 g) para crianças maiores.",
        "wrongReasons": [
            "Cobrir as cerdas inteiras expõe a criança a uma superdosagem diária maciça de flúor, induzindo fluorose.",
            None,
            "A higiene bucal deve iniciar-se assim que o primeiro dente irromper na boca.",
            "A orientação de misturar pasta com refrigerante é absurda e antiodontológica."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "A respeito do mecanismo biológico pelo qual o excesso de flúor afeta a formação do esmalte dentário na amelogênese, assinale a afirmativa CORRETA:",
        "options": [
            "O flúor destrói mecanicamente os dentes com brocas microscópicas.",
            "O excesso de fluoreto retarda a degradação e remoção das proteínas da matriz do esmalte (amelogeninas) durante a fase de maturação, resultando em retenção proteica e esmalte subsuperficial poroso e hipomineralizado.",
            "O flúor impede a formação da raiz dentária, fazendo o dente nascer sem polpa.",
            "O flúor transforma a hidroxiapatita em sacarose pura altamente cariogênica."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "Na maturação, as proteínas (amelogeninas) deveriam ser digeridas para dar lugar aos cristais de mineral. O excesso de flúor inibe essa remoção proteica.",
        "explanation": "Durante a fase de maturação da amelogênese, as proteases do esmalte (como a calicreína-4) clivam as amelogeninas para que a água e as proteínas saiam e os cristais de hidroxiapatita cresçam. O excesso crônico de fluoreto inibe essa degradação proteica, causando retenção anormal de proteínas e resultando em um esmalte poroso (hipomineralizado) abaixo da superfície.",
        "wrongReasons": [
            "Não há ação mecânica física de brocas na amelogênese.",
            None,
            "A raiz dentária forma-se pela bainha de Hertwig posteriormente, não sendo a estrutura afetada pela fluorose clínica de esmalte.",
            "O flúor forma fluorapatita, e jamais sacarose."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "A concentração mínima de fluoreto recomendada e legalmente estabelecida para dentifrícios no Brasil para garantir eficácia comprovada no controle da cárie dentária é de:",
        "options": [
            "Zero ppm F (cremes dentais sem flúor são os mais eficazes contra a cárie).",
            "1.000 a 1.100 ppm F (partes por milhão de flúor solúvel).",
            "50.000 ppm F para uso diário três vezes ao dia.",
            "1 ppm F apenas em dias de feriado municipal."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "Cremes dentais com menos de 1.000 ppm F não demonstram superioridade em relação a placebo na redução de cárie.",
        "explanation": "A literatura científica e os consensos internacionais (como OMS e Associação Brasileira de Odontopediatria) estabelecem que dentifrícios devem conter no mínimo 1.000 a 1.100 ppm de flúor quimicamente solúvel para exercerem efeito anticárie clinicamente relevante. Pastas sem flúor ou com concentrações subótimas (ex: 500 ppm) não protegem contra cárie.",
        "wrongReasons": [
            "Pastas sem flúor não têm efeito protetor anticárie clinicamente demonstrado em ensaios randomizados.",
            None,
            "50.000 ppm F causaria toxicidade química imediata na mucosa; a concentração de uso diário é de cerca de 1.100 ppm.",
            "1 ppm F é uma concentração irrisória ineficaz em cremes dentais tópicos."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "Em relação aos efeitos sistêmico e tópico do fluoreto, assinale a correlação preconizada pela cariologia contemporânea:",
        "options": [
            "O efeito do flúor contra a cárie é estritamente sistêmico (pré-eruptivo), sendo inútil escovar os dentes com pasta após a erupção.",
            "O principal efeito preventivo contra a cárie é TÓPICO local (pós-eruptivo na cavidade bucal), enquanto o risco de fluorose decorre da ação SISTÊMICA (pré-eruptiva durante a formação do esmalte).",
            "A fluorose é causada exclusivamente pelo ar respirado em praias oceânicas.",
            "Engolir flúor na fase adulta protege as restaurações antigas contra fraturas mecânicas."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "Efeito anticárie = tópico local permanente na saliva/placa. Risco de fluorose = sistêmico infantil pré-eruptivo.",
        "explanation": "A compreensão moderna da ação do flúor demonstrou que o efeito benéfico anticárie é predominantemente local/tópico no biofilme e saliva em contato com os dentes já erupcionados (promovendo remineralização e inibindo desmineralização). Por outro lado, a fluorose decorre exclusivamente da ingestão sistêmica durante a odontogênese pré-eruptiva.",
        "wrongReasons": [
            "O paradigma antigo pré-eruptivo foi superado; o flúor atua localmente nos dentes erupcionados por toda a vida.",
            None,
            "O ar marinho não causa fluorose; o agravo decorre da ingestão de água, suplementos ou dentifrícios deglutidos.",
            "A ingestão na fase adulta não fortalece nem altera quimicamente a coroa de dentes já maduros."
        ]
    },
    {
        "cat": 2,
        "sub": "fluorose_clinica",
        "pool": "all",
        "text": "Entre os fatores que aumentam o risco de fluorose dentária em populações infantis residentes em municípios com água de abastecimento otimamente fluoretada, destaca-se:",
        "options": [
            "A prescrição desnecessária e concomitante de suplementos medicamentosos fluoretados (gotas ou comprimidos de flúor).",
            "O consumo de água mineral totalmente destilada sem sais minerais.",
            "A escovação dentária realizada exclusivamente com água pura sem nenhuma pasta.",
            "O aleitamento materno exclusivo até os 6 meses de vida."
        ],
        "answer": 0,
        "target": "fluorose_biologia",
        "hint": "Somar duas fontes sistêmicas de flúor (água fluoretada + comprimido/gota de flúor) ultrapassa a dose segura de Burt.",
        "explanation": "Em localidades que já contam com água de abastecimento público com teor ótimo de fluoreto, a suplementação sistêmica com comprimidos, gotas ou vitaminas contendo flúor é formalmente contraindicada, pois soma fontes sistêmicas elevando a dose muito acima do limiar seguro (0,07 mg F/kg/dia).",
        "wrongReasons": [
            None,
            "Água destilada sem sais não contém flúor e não oferece risco de fluorose.",
            "Escovar sem pasta não introduz flúor sistêmico.",
            "O leite materno possui teores muito baixos de flúor (menos de 0,01 ppm), sendo totalmente seguro e protetor."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 2: indices_fluorose (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "O Índice de Fluorose Dentária preconizado pela OMS e amplamente utilizado em levantamentos nacionais e internacionais foi desenvolvido por:",
        "options": [
            "H. Trendley Dean.",
            "G. V. Black.",
            "Paul Leavell & Hugh Clark.",
            "Marc Lalonde."
        ],
        "answer": 0,
        "target": "indice_dean",
        "hint": "Pioneiro da epidemiologia da fluorose nos EUA nas décadas de 1930 e 1940: H. Trendley Dean.",
        "explanation": "H. Trendley Dean desenvolveu na década de 1930 o clássico índice de fluorose (Índice de Dean), adotado pela OMS e pelo Ministério da Saúde em levantamentos como o SB Brasil para categorizar o agravo em escores ordinais de 0 a 5.",
        "wrongReasons": [
            None,
            "Black foi o sistematizador do preparo cavitário operatório e classificação de cavidades em odontologia restauradora.",
            "Leavell & Clark criaram a teoria da História Natural da Doença e os níveis de prevenção.",
            "Marc Lalonde foi Ministro da Saúde do Canadá e autor do Informe Lalonde de determinantes de saúde."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "De acordo com as definições do Índice de Dean, o escore 2 é denominado 'MUITO LEVE' e caracteriza-se por:",
        "options": [
            "Esmalte perfeitamente liso, translúcido e sem nenhuma mancha.",
            "Pequenas áreas brancas e opacas espalhadas irregularmente pela coroa, envolvendo MENOS DE 25% da superfície dentária vestibular.",
            "Opacidades confluentes cobrindo mais de 75% da coroa com cavidades e perda de substância.",
            "Dente totalmente destruído por cárie com fístula purulenta."
        ],
        "answer": 1,
        "target": "indice_dean",
        "hint": "Escore 2 (Muito Leve): opacidade cobrindo menos de 25% da superfície. Escore 3 (Leve): cobrindo de 25% a 50%.",
        "explanation": "No índice de Dean: Escore 0 = Normal; Escore 1 = Questionável; Escore 2 = Muito Leve (pequenas opacidades brancas cobrindo menos de 25% da superfície do dente); Escore 3 = Leve (25% a menos de 50%); Escore 4 = Moderado (desgaste e pigmentação marrom); Escore 5 = Severo (fossas e corrosão).",
        "wrongReasons": [
            "Esmalte totalmente normal translúcido corresponde ao escore 0 (Normal).",
            None,
            "Opacidades extensas com confluência e desmoronamento correspondem aos escores 4 ou 5.",
            "Cárie e fístula infecciosa são diagnosticadas pelo CPO-D/ICDNT, não pelo índice de Dean."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "No Índice de Dean, o escore 3 é denominado 'LEVE' e define-se quando as manchas brancas e opacas de fluorose cobrem:",
        "options": [
            "Menos de 5% da superfície do dente.",
            "Entre 25% e menos de 50% da superfície dentária examinada.",
            "Exatamente 100% de todos os dentes incluindo a mucosa jugal.",
            "Apenas raízes expostas em pacientes edêntulos."
        ],
        "answer": 1,
        "target": "indice_dean",
        "hint": "Lembre-se dos cortes percentuais de Dean: < 25% é Muito Leve (2); de 25% a < 50% é Leve (3).",
        "explanation": "No escore 3 (Leve) de Dean, a opacidade branca do esmalte é mais extensa e nítida do que no grau muito leve, cobrindo entre 25% e menos de 50% da superfície anatômica do dente examinado.",
        "wrongReasons": [
            "Menos de 5% se enquadraria no escore 1 (Questionável) ou 2 (Muito Leve).",
            None,
            "100% do dente com desgaste ou pits corresponde a Moderado (4) ou Severo (5).",
            "O índice de Dean avalia exclusivamente esmalte coronário de dentes presentes."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "A forma mais grave no Índice de Dean é o escore 5 ('SEVERA'). O sinal clínico patognomônico que diferencia a fluorose severa das formas brandas e moderadas é:",
        "options": [
            "Translucidez cristalina idêntica a dente de leite de recém-nascido.",
            "Presença de confluência de fossas, depressões ('pits') e aspecto corroído do esmalte dentário com hipoplasia generalizada e grande fragilidade.",
            "Crescimento de dentes adicionais na bochecha.",
            "Aparecimento de cárie rampante em todos os molares decíduos."
        ],
        "answer": 1,
        "target": "indice_dean",
        "hint": "O grau 5 (severo) tem 'pits' (fossetas cavitadas de desmoronamento do esmalte poroso subsuperficial) e aparência corroída.",
        "explanation": "O escore 5 (Severa) de Dean caracteriza-se pela hipoplasia acentuada de todas as superfícies de esmalte, com presença marcante de depressões puntiformes ('pits'), áreas de confluência corroída e ampla perda de substância decorrente da fragilidade mecânica do esmalte intensamente poroso.",
        "wrongReasons": [
            "Translucidez límpida é a característica do dente sadio normal (escore 0).",
            None,
            "Fluorose não causa dentes ectópicos em tecidos moles.",
            "A fluorose é uma anomalia estrutural do esmalte, não uma cárie bacteriana aguda."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "Para determinar o diagnóstico de fluorose de um INDIVÍDUO no Índice de Dean, a OMS preconiza uma regra diagnóstica fundamental. Essa regra estabelece que o escore do indivíduo é definido:",
        "options": [
            "Pelo dente mais sadio da boca inteira.",
            "Pelos DOIS dentes mais severamente afetados; caso eles apresentem escores diferentes, prevalece o escore do MENOR entre eles.",
            "Somando os escores de todos os dentes e multiplicando pela idade do paciente.",
            "Apenas pelo dente canino inferior esquerdo."
        ],
        "answer": 1,
        "target": "indice_dean",
        "hint": "Regra dos dois dentes mais afetados pelo menor escore: se o mais grave é 4 e o segundo mais grave é 3, o paciente recebe nota 3.",
        "explanation": "A clássica regra de Dean determina que o escore do indivíduo deve ser estabelecido com base nos dois dentes mais afetados da boca. Caso não sejam idênticos em gravidade, atribui-se o código do menos severo dos dois (ex: dente A com escore 4 e dente B com escore 3 -> o diagnóstico final do paciente é escore 3).",
        "wrongReasons": [
            "Avaliar o mais sadio ignoraria a presença da doença no indivíduo.",
            None,
            "Não se somam nem se multiplicam escores pela idade no índice individual de Dean.",
            "O exame envolve todos os dentes da cavidade bucal, não apenas um canino isolado."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "Um adolescente apresenta o dente 11 com fluorose escore 3 (Leve) e o dente 21 com escore 3 (Leve). Todos os demais dentes da boca apresentam escores 0 ou 1. Qual é o escore final de Dean atribuído a esse indivíduo?",
        "options": [
            "Escore 0 (Normal)",
            "Escore 1 (Questionável)",
            "Escore 3 (Leve)",
            "Escore 6 (Soma dos dois)"
        ],
        "answer": 2,
        "target": "indice_dean",
        "hint": "Os dois dentes mais afetados são 11 (escore 3) e 21 (escore 3). O menor entre 3 e 3 é 3.",
        "explanation": "Aplicando a regra de Dean: os dois dentes mais gravemente acometidos são o 11 e o 21, ambos com escore 3. O menor entre eles é 3, logo o diagnóstico do indivíduo no levantamento é escore 3 (Leve).",
        "wrongReasons": [
            "0 ignoraria os dois incisivos centrais afetados pelo grau leve.",
            "1 é questionável, abaixo da severidade nítida dos dois incisivos.",
            None,
            "Não existe escore 6 no índice de Dean nem se somam notas."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "O Índice de Thylstrup & Fejerskov (Índice TF) foi proposto como uma alternativa mais sensível e detalhada ao Índice de Dean. A principal característica metodológica e biológica do Índice TF é:",
        "options": [
            "Avaliar dentes exclusivamente sem secagem, cheios de saliva e biofilme espesso.",
            "Fundamentar-se na correlação direta entre os graus clínicos observados após secagem prolongada e a profundidade histológica da porosidade do esmalte, variando de 0 a 9 escores.",
            "Ser restrito apenas a animais de zoológico.",
            "Calcular o volume de saliva produzido por minuto."
        ],
        "answer": 1,
        "target": "indice_tf",
        "hint": "O índice TF tem 10 escores (0 a 9), exige secagem rigorosa e foi desenhado com base em cortes histológicos da porosidade do esmalte.",
        "explanation": "O índice TF (Thylstrup & Fejerskov, 1978) fundamenta-se nos aspectos histopatológicos da fluorose, classificando o esmalte em 10 graus (0 a 9). Requer limpeza e secagem meticulosa com ar comprimido para evidenciar as linhas opacas iniciais e gradua com alta precisão desde tênues estrias até perdas focais de esmalte.",
        "wrongReasons": [
            "O índice TF exige rigorosa limpeza e secagem com ar comprimido antes do exame.",
            None,
            "O índice TF foi desenvolvido e validado em dentes humanos em inquéritos populacionais.",
            "Não é um teste de fluxo salivar, mas uma métrica clínica de integridade de esmalte."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "No Índice Comunitário de Fluorose (CFI / IFD) de Dean, que resume a prevalência e gravidade da fluorose em uma comunidade, quando o valor numérico calculado ultrapassa 0,6, considera-se que a fluorose na população:",
        "options": [
            "É totalmente inexistente na cidade.",
            "Passa a constituir um problema com relevância para a saúde pública, demandando vigilância e monitoramento dos teores de flúor.",
            "Obriga a interrupção imediata de todo o atendimento odontológico nas UBS.",
            "Indica que 100% dos cidadãos perderam todos os dentes da boca."
        ],
        "answer": 1,
        "target": "indice_dean",
        "hint": "Conforme estipulado por Dean, um CFI > 0,6 sinaliza que a fluorose começa a ter significado de saúde pública para a gestão municipal.",
        "explanation": "Dean estabeleceu faixas de significância para o Índice Comunitário de Fluorose (IFD): valores entre 0,0 e 0,4 são negativos/sem significado; entre 0,4 e 0,6 são limítrofes; e acima de 0,6 o agravo passa a ter relevância para a saúde pública, exigindo ações de controle e monitoramento dos sistemas de fluoretação.",
        "wrongReasons": [
            "Inexistente seria um índice de valor zero absoluto.",
            None,
            "Não se interrompe o atendimento das UBS; pelo contrário, reforçam-se a vigilância sanitária e a orientação populacional.",
            "CFI mede fluorose em esmalte, não taxa de edentulismo populacional."
        ]
    },
    {
        "cat": 2,
        "sub": "indices_fluorose",
        "pool": "all",
        "text": "Em levantamentos epidemiológicos de base populacional no Brasil (como o SB Brasil), qual é o perfil epidemiológico predominante da fluorose dentária encontrado aos 12 anos de idade?",
        "options": [
            "Prevalência nula, nunca tendo sido encontrado nenhum caso de fluorose no território brasileiro.",
            "A grande maioria dos casos diagnosticados concentra-se nas formas muito leves e leves (escores 1, 2 e 3 de Dean), com frequência extremamente baixa ou nula das formas moderadas e severas.",
            "Mais de 90% da população brasileira apresenta a forma severa com perda total da coroa.",
            "A fluorose atinge exclusivamente indivíduos com mais de 80 anos."
        ],
        "answer": 1,
        "target": "indice_dean",
        "hint": "A quase totalidade da fluorose no Brasil é esteticamente branda (graus muito leve e leve), compatível com águas fluoretadas no padrão ótimo.",
        "explanation": "Os inquéritos SB Brasil comprovam que, onde há fluorose, ela ocorre predominantemente nos graus questionável, muito leve e leve (escores 1 a 3 de Dean), os quais não causam prejuízo funcional e têm impacto estético desprezível. As formas severas (escore 5) são virtualmente raras no país.",
        "wrongReasons": [
            "Casos leves de fluorose existem e são monitorados rotineiramente no SB Brasil.",
            None,
            "Formas severas com destruição de coroa são raríssimas na epidemiologia nacional.",
            "Aos 12 anos é exatamente a idade de monitoramento da fluorose em dentes permanentes jovens."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 3: diagnostico_diferencial (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "O diagnóstico diferencial entre a fluorose dentária leve e a mancha branca ativa de cárie é fundamental na clínica e na epidemiologia. Assinale a característica que aponta especificamente para o diagnóstico de FLUOROSE DENTÁRIA:",
        "options": [
            "Lesão estritamente assimétrica e unilateral localizada no fundo do sulco gengival cervical de um único molar.",
            "Apresentação bilateral e simétrica em dentes homólogos, afetando preferencialmente cúspides e bordas incisais, com estrias opacas acompanhando as periquimáceas.",
            "Superfície extremamente rugosa, cavitada e amolecida ao toque leve com a sonda.",
            "Localização restrita apenas a locais com acúmulo patológico de biofilme espesso e gengivite sangrante."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "Fluorose é sistêmica: se afetou o 11, afeta o 21 no mesmo lugar e com o mesmo padrão horizontal.",
        "explanation": "Como a fluorose tem etiologia sistêmica durante a formação do dente, ela manifesta-se de modo bilateral e simétrico em dentes homólogos formados na mesma época, acometendo áreas de esmalte limpo e resistente (bordas incisais e cúspides). A cárie, sendo biofilme-dependente, é localizada, assimétrica e acomete nichos de estagnação de placa (cervical e proximal).",
        "wrongReasons": [
            "Lesão unilateral e cervical com biofilme é a apresentação clássica da mancha branca ativa de cárie.",
            None,
            "Fluorose leve apresenta superfície intacta, lisa e brilhante; superfície rugosa amolecida é cárie ativa.",
            "Fluorose ocorre independentemente de biofilme, afetando áreas limpas sujeitas à autoclise."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "A Hipomineralização Molar-Incisivo (HMI) é uma condição clínica prevalente que demanda diagnóstico diferencial com a fluorose. Qual é a característica típica da HMI?",
        "options": [
            "Manchas difusas e simétricas em todos os 32 dentes da boca sem fragilidade estrutural.",
            "Opacidades demarcadas com limites nítidos e bordas claras (coloração variando de branco-creme a amarelo-castanho), acometendo de 1 a 4 primeiros molares permanentes, frequentemente com incisivos associados e alta fragilidade com fraturas pós-eruptivas.",
            "Causada exclusivamente pela ingestão de salmão cru contaminado por mercúrio.",
            "Dentes imunes a qualquer sensibilidade dolorosa."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "HMI: opacidades demarcadas (com limites nítidos, amarelas/castanhas) em primeiros molares e incisivos permanentes, com quebra fácil do esmalte após erupção.",
        "explanation": "A HMI caracteriza-se por opacidades demarcadas (de bordas bem definidas, de cor creme a castanho-escuro) que afetam obrigatoriamente de 1 a 4 primeiros molares permanentes, podendo envolver incisivos permanentes. O esmalte é estruturalmente frágil e frequentemente sofre colapso mecânico pós-eruptivo à mastigação.",
        "wrongReasons": [
            "Fluorose apresenta manchas difusas sem limite nítido; a HMI apresenta opacidades demarcadas e assimétricas.",
            None,
            "HMI não decorre de ingestão de salmão, mas de distúrbios sistêmicos precoces nos primeiros anos de vida.",
            "Dentes com HMI apresentam severa hipersensibilidade dentinária ao ar, frio e escovação."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "Um adolescente de 13 anos apresenta hipoplasia localizada de esmalte com defeito circunscrito e coloração amarelada em uma área da face vestibular do primeiro pré-molar inferior direito (dente 44). Todos os demais 27 dentes presentes na boca apresentam esmalte hígido e uniforme. O paciente relata histórico de abscesso dentário grave no dente de leite predecessor aos 4 anos de idade. Esse quadro é diagnóstico de:",
        "options": [
            "Fluorose severa grau 5 de Dean.",
            "Dente de Turner (ou Hipoplasia de Turner).",
            "Manchamento sistêmico por tetraciclina na gestação.",
            "Amelogênese imperfeita autossômica dominante generalizada."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "Lesão em um ÚNICO dente permanente causada por infecção/trauma no dente de leite predecessor: Dente de Turner.",
        "explanation": "O Dente de Turner (hipoplasia de Turner) decorre de agressão localizada (traumatismo ou infecção periapical crônica com abscesso) no dente decíduo predecessor que lesa mecanicamente ou toxicamente o gérmen do dente permanente subjacente. É estritamente localizado e unilateral, afetando tipicamente um único dente.",
        "wrongReasons": [
            "Fluorose é necessariamente sistêmica, bilateral e afeta dentes homólogos, jamais um único pré-molar isolado.",
            None,
            "Tetraciclina gera faixas horizontais bilaterais simétricas em todos os dentes que estavam em odontogênese.",
            "Amelogênese imperfeita é uma condição genética generalizada que atinge todos os dentes de ambas as dentições."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "O manchamento intrínseco de esmalte e dentina causado pelo uso de TETRACICLINA durante a fase de desenvolvimento dentário caracteriza-se semiologicamente por:",
        "options": [
            "Pits puntiformes no bordo incisal decorrentes de desmoronamento de hidroxiapatita.",
            "Bandas horizontais pigmentadas difusas (de tonalidade amarelada, acinzentada ou castanho-escura) que exibem fluorescência amarelo-brilhante quando iluminadas sob luz ultravioleta (Wood).",
            "Manchas brancas localizadas exclusivamente na face oclusal de dentes decíduos.",
            "Desaparecimento completo do canal radicular antes da erupção do dente."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "A tetraciclina se quela ao cálcio na dentina/esmalte e forma bandas horizontais que brilham (fluorescem) sob luz ultravioleta.",
        "explanation": "A tetraciclina liga-se aos íons cálcio da hidroxiapatita em formação (especialmente na dentina), gerando bandas horizontais simétricas bilaterais que correspondem ao período de uso do antibiótico. Ao exame sob luz ultravioleta (lâmpada de Wood), essas áreas emitem fluorescência amarelada característica.",
        "wrongReasons": [
            "Pits de desmoronamento em bordo incisal são característicos de fluorose severa grau 5 de Dean.",
            None,
            "O manchamento por tetraciclina é sistêmico em coroas permanentes e decíduas em formação, não restrito a oclusais decíduas.",
            "Não promove obliteração pré-eruptiva do canal radicular."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "A AMELOGÊNESE IMPERFEITA diferencia-se clinicamente e epidemiologicamente da fluorose dentária por:",
        "options": [
            "Ser uma afecção de base puramente alimentar decorrente do consumo de maçã ácida.",
            "Ser uma desordem genética hereditária que compromete absolutamente TODOS os dentes de ambas as dentições (decídua e permanente), frequentemente com história familiar de consanguinidade e histórico em várias gerações.",
            "Ser causada pela ingestão de água da chuva fervida em panela de ferro.",
            "Não apresentar nenhuma alteração na espessura ou mineralização do esmalte."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "Amelogênese imperfeita é genética: todos os dentes de leite e todos os dentes permanentes são afetados e há histórico na família.",
        "explanation": "A amelogênese imperfeita é um grupo de desordens genéticas hereditárias ligadas a mutações em genes como AMELX e ENAM. Afeta todos os dentes das duas dentições (decídua e permanente) de forma generalizada e homogênea, acompanhada de histórico familiar positivo, ao contrário da fluorose que poupa períodos sem ingestão excessiva.",
        "wrongReasons": [
            "Amelogênese imperfeita é de etiologia genética congênita, não alimentar ácida.",
            None,
            "Não tem relação causal com água da chuva ou panelas de ferro.",
            "Causa graves anomalias quantitativas (hipoplásica) ou qualitativas (hipocalcificada / hipomaturada) no esmalte."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "Qual das seguintes características semiológicas diferencia as linhas opacas da fluorose das linhas de hipoplasia de esmalte causadas por febre alta na infância?",
        "options": [
            "A fluorose causa dor excruciante na língua e a febre causa necrose pulpar imediata.",
            "As lesões de fluorose acompanham suavemente a arquitetura das periquimáceas com transição difusa para o esmalte sadio e resistência aumentada à cárie; enquanto hipoplasias pós-febris apresentam bordas abruptas em degrau e ranhuras focais bem demarcadas.",
            "Não existe nenhuma maneira científica de distinguir as duas condições.",
            "A fluorose nunca atinge dentes anteriores."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "Fluorose tem aspecto difuso e suave em periquimáceas; hipoplasias por febre/doença aguda geram linhas e degraus de borda nítida.",
        "explanation": "A fluorose caracteriza-se por estrias opacas horizontais difusas que se mesclam imperceptivelmente com o esmalte sadio subjacente (transição gradual). Já hipoplasias associadas a episódios febris agudos na infância (sarampo, pneumonia) geram interrupções abruptas focais em degrau na espessura do esmalte correspondentes ao período exato do estresse metabólico febril.",
        "wrongReasons": [
            "Fluorose não causa dor lingual nem a febre gera necrose pulpar direta.",
            None,
            "A semiologia odontológica estabelece critérios diagnósticos diferenciais muito claros e objetivos.",
            "Os incisivos anteriores permanentes são exatamente os dentes mais comumente examinados na fluorose estética."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "Durante exame epidemiológico de escolares de 12 anos, o examinador observa manchas brancas leitosas localizadas na região cervical vestibular dos dentes 16 e 26, recobertas por biofilme espesso associado a sangramento gengival marginal. Ao secar com gaze, a superfície apresenta-se opaca e rugosa. O diagnóstico mais provável é:",
        "options": [
            "Fluorose severa com desmoronamento.",
            "Lesão de cárie ativa em esmalte (mancha branca de cárie).",
            "Mancha por tetraciclina de uso adulto.",
            "Esmalte hígido normal sem nenhuma alteração."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "Cervical + biofilme retido + gengivite + esmalte rugoso ao secar = mancha branca ativa de cárie.",
        "explanation": "A localização cervical (nicho de acúmulo de placa), a presença de biofilme adjacente à gengivite e o aspecto fosco/rugoso após secagem são sinais clássicos da lesão inicial de cárie ativa em esmalte (mancha branca de cárie), e não fluorose.",
        "wrongReasons": [
            "Fluorose poupa áreas cervicais e não apresenta superfície rugosa associada a biofilme bacteriano estagnado.",
            None,
            "Tetraciclina produz faixas horizontais intrínsecas acinzentadas, não mancha branca rugosa cervical de placa.",
            "Há evidente desmineralização de esmalte e inflamação gengival, descartando esmalte normal."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "Por que o dente com fluorose dentária moderada ou leve exibe MAIOR RESISTÊNCIA à desmineralização por cárie em comparação a um dente com hipomineralização pós-eruptiva de outra etiologia?",
        "options": [
            "Porque os dentes fluoróticos contêm chumbo radioativo que esteriliza as bactérias.",
            "Porque a incorporação de fluoreto na rede cristalina do esmalte forma fluorapatita e hidroxiapatita fluorada, reduzindo substancialmente a solubilidade do mineral em meio ácido.",
            "Porque o esmalte fluorótico é composto por ouro maciço impermeável.",
            "Porque crianças com fluorose nunca ingerem carboidratos fermentáveis na dieta."
        ],
        "answer": 1,
        "target": "fluorose_biologia",
        "hint": "A presença de fluorapatita diminui o pH crítico de desmineralização do esmalte de 5,5 para cerca de 4,5.",
        "explanation": "O esmalte dentário com fluorose possui elevada concentração de íons fluoreto integrados à rede de hidroxiapatita, formando fluorapatita. Esse mineral é termodinamicamente muito mais estável e insolúvel frente aos ácidos produzidos pela fermentação bacteriana (o pH crítico cai de 5,5 para cerca de 4,5).",
        "wrongReasons": [
            "Fluorose não envolve chumbo radioativo.",
            None,
            "O dente é composto por tecidos biológicos mineralizados, e não ligas de ouro.",
            "A dieta dessas crianças contém carboidratos normalmente; a resistência reside na química do mineral dental."
        ]
    },
    {
        "cat": 2,
        "sub": "diagnostico_diferencial",
        "pool": "all",
        "text": "Em um paciente de 8 anos, os dentes 16 e 26 apresentam opacidades demarcadas de cor castanho-amarelada nas cúspides vestibulares com perda focal de esmalte por fratura pós-eruptiva. Já os dentes 11 e 21 apresentam opacidades demarcadas branco-cremosas bem delimitadas no terço incisal. Os demais dentes são completamente sadios. Esse conjunto de achados clínicos é típico de:",
        "options": [
            "Dente de Turner por traumatismo no queixo.",
            "Hipomineralização Molar-Incisivo (HMI).",
            "Fluorose generalizada grau 5 de Dean.",
            "Mancha extrínseca por bochecho de clorexidina."
        ],
        "answer": 1,
        "target": "diag_diferencial_esmalte",
        "hint": "Acometimento de primeiros molares permanentes associado a incisivos permanentes com opacidades demarcadas: HMI (Hipomineralização Molar-Incisivo).",
        "explanation": "O envolvimento simultâneo de primeiros molares permanentes (com opacidades demarcadas e fratura mecânica pós-eruptiva) e incisivos centrais superiores (com opacidades demarcadas branco-creme bem delimitadas), poupando os demais dentes, é o quadro padrão da Hipomineralização Molar-Incisivo (HMI).",
        "wrongReasons": [
            "Dente de Turner é tipicamente unilateral em um único dente, não afetando múltiplos molares e incisivos simultaneamente.",
            None,
            "Fluorose é difusa em periquimáceas, simétrica e acometeria outros elementos dentários em formação na época.",
            "Clorexidina gera pigmentação marrom superficial extrínseca removível com jato de bicarbonato, sem fratura estrutural."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 4: epidemiologia_periodontal (8 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "O Índice Periodontal Comunitário (CPI - Community Periodontal Index), preconizado pela OMS, avalia as condições periodontais por meio da divisão da boca em:",
        "options": [
            "32 quadrículas radiográficas isoladas.",
            "6 sextantes anatômicos.",
            "4 quadrantes apenas para dentes decíduos.",
            "2 metades: lado direito e lado esquerdo."
        ],
        "answer": 1,
        "target": "indice_cpi",
        "hint": "Sextantes: a boca é dividida em 6 partes (três superiores e três inferiores).",
        "explanation": "O CPI divide a dentição em 6 sextantes: superior direito (18 a 14), superior anterior (13 a 23), superior esquerdo (24 a 28), inferior esquerdo (38 a 34), inferior anterior (33 a 43) e inferior direito (44 a 48). Cada sextante recebe o escore da sua condição periodontal mais severa.",
        "wrongReasons": [
            "Não utiliza radiografias de campo nem divide em 32 quadrículas isoladas.",
            None,
            "CPI avalia primordialmente a dentição permanente e divide em sextantes, não 4 quadrantes decíduos.",
            "A divisão não é em metades direita/esquerda, mas em 6 sextantes (anteriores e posteriores)."
        ]
    },
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "No exame pelo CPI da OMS, cada sextante só pode ser incluído no levantamento se possuir no mínimo:",
        "options": [
            "Todos os 8 dentes presentes e intactos.",
            "Pelo menos 2 ou mais dentes presentes que não estejam indicados para extração.",
            "Apenas raízes residuais com supuração.",
            "Um implante de titânio osseointegrado funcional."
        ],
        "answer": 1,
        "target": "indice_cpi",
        "hint": "Regra dos dois dentes: sextante com menos de dois dentes funcionais é considerado EXCLUÍDO (código X).",
        "explanation": "Pelas regras da OMS para o CPI, um sextante só é examinado se contiver no mínimo 2 dentes funcionais presentes (não indicados para extração). Se houver apenas 1 dente ou nenhum dente presente no sextante, atribui-se o código 'X' (sextante excluído).",
        "wrongReasons": [
            "Não se exige todos os 8 dentes; bastam 2 dentes funcionais no sextante.",
            None,
            "Raízes residuais indicadas para extração não qualificam o sextante como examinável.",
            "Implantes não eram tradicionalmente pontuados como dentes naturais no protocolo clássico do CPI da OMS."
        ]
    },
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "Assinale a correspondência CORRETA entre o código numérico do CPI e a respectiva condição clínica periodontal:",
        "options": [
            "Código 0 = Periodontite destrutiva avançada com perda óssea total.",
            "Código 1 = Sangramento gengival à sondagem; Código 2 = Cálculo dentário supra ou subgengival detectado pela sonda; Código 3 = Bolsa periodontal rasa (4 a 5 mm); Código 4 = Bolsa periodontal profunda (6 mm ou mais).",
            "Código 3 = Esmalte hígido com fluorose moderada.",
            "Código 4 = Presença exclusiva de cárie em esmalte."
        ],
        "answer": 1,
        "target": "indice_cpi",
        "hint": "Escala progressiva do CPI: 0 hígido, 1 sangramento, 2 cálculo, 3 bolsa 4-5mm (faixa preta na margem), 4 bolsa 6mm+ (faixa preta some).",
        "explanation": "No CPI: Código 0 = Hígido (sem sangramento/cálculo/bolsa); Código 1 = Sangramento à sondagem; Código 2 = Cálculo dentário detectado (mas bolsa < 4 mm); Código 3 = Bolsa de 4 a 5 mm (margem gengival na faixa preta); Código 4 = Bolsa de 6 mm ou mais (faixa preta da sonda desaparece totalmente); Código X = Sextante excluído.",
        "wrongReasons": [
            "Código 0 é periodonto absolutamente hígido e saudável.",
            None,
            "CPI não avalia fluorose dentária; fluorose é avaliada pelo índice de Dean.",
            "Cárie dentária não é objeto do CPI; cárie é quantificada no CPO-D e ICDNT."
        ]
    },
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "A sonda periodontal padronizada pela OMS para o exame do CPI (conhecida no Brasil como sonda Trinity 621) possui características específicas de fabricação. Entre elas destaca-se:",
        "options": [
            "Ponta em agulha perfurante afiada sem nenhuma marcação milimétrica.",
            "Ponta esférica de 0,5 mm de diâmetro (que evita traumatismo tecidual), faixa preta calibrada entre 3,5 mm e 5,5 mm, e linhas adicionais em 8,5 mm e 11,5 mm.",
            "Lâmina bisturi curva com fio cortante de tungstênio.",
            "Tubo de sucção a vácuo para aspiração contínua de sangue."
        ],
        "answer": 1,
        "target": "sonda_oms_trinity",
        "hint": "Esferinha na ponta de 0,5 mm para não machucar o sulco + faixa preta entre 3,5 e 5,5 mm.",
        "explanation": "A sonda periodontal da OMS (Trinity 621) é desenhada especificamente para inquéritos epidemiológicos: sua extremidade possui uma ponta esférica de 0,5 mm (que facilita a detecção tátil de cálculo subgengival e impede a perfuração do epitélio juncional) e uma faixa preta que vai exatamente de 3,5 mm a 5,5 mm.",
        "wrongReasons": [
            "Pontas afiadas agudas laceram o periodonto inflamado e são proibidas no protocolo da OMS.",
            None,
            "Não possui lâmina cortante nem funciona como bisturi cirúrgico.",
            "A sonda é um instrumento clínico manual mecânico, sem tubos ou bombas de aspiração."
        ]
    },
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "A força de sondagem periodontal recomendada pela OMS durante o exame com a sonda Trinity não deve ultrapassar:",
        "options": [
            "500 gramas de força.",
            "Aproximadamente 20 gramas de força (equivalente à pressão suave suficiente para empurrar a sonda sob a unha do polegar sem provocar dor ou branqueamento acentuado).",
            "10 quilogramas de força com apoio dos dois braços.",
            "Zero gramas, pois a sonda nunca deve encostar nos tecidos bucais."
        ],
        "answer": 1,
        "target": "sonda_oms_trinity",
        "hint": "Pressão padronizada de 20 gramas: teste clássico da cutícula/unha sem dor.",
        "explanation": "A OMS padroniza a força de sondagem em no máximo 20 gramas. Essa pressão pode ser aferida clinicamente inserindo a ponta da sonda sob a unha do polegar até o limite em que a pressão seja suavemente percebida sem provocar dor ou branqueamento tecidual exagerado, evitando falsas bolsas por penetração traumática.",
        "wrongReasons": [
            "500 gramas perfuraria o assoalho da bolsa e causaria hemorragia grave.",
            None,
            "10 kg é uma força biomecânica absurda que fraturaria o osso alveolar.",
            "A sonda deve deslizar suavemente no sulco gengival para cumprir seu papel diagnóstico."
        ]
    },
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "Segundo as diretrizes internacionais da OMS para levantamentos epidemiológicos, em indivíduos com MENOS DE 15 ANOS de idade:",
        "options": [
            "Não se deve examinar a cavidade bucal em nenhuma hipótese.",
            "NÃO se registram bolsas periodontais (códigos 3 e 4 do CPI), avaliando-se exclusivamente sangramento gengival (código 1) e cálculo dentário (código 2).",
            "Todos os dentes devem ser classificados como portadores de bolsa profunda de 12 mm.",
            "É obrigatório realizar cirurgia a retalho com enxerto ósseo liofilizado na escola."
        ],
        "answer": 1,
        "target": "indice_cpi",
        "hint": "Em crianças e adolescentes até 14 anos ocorrem pseudobolsas devido à erupção ativa dos dentes. Por isso, bolsas (3 e 4) NÃO são registradas em menores de 15 anos.",
        "explanation": "Em indivíduos com idade inferior a 15 anos, a emergência contínua dos dentes no arco cria sulcos gengivais anatomicamente aprofundados (falsas bolsas ou pseudobolsas de erupção). Para evitar superestimar a prevalência de periodontite, a OMS determina que abaixo dos 15 anos registram-se apenas os códigos 0 (hígido), 1 (sangramento) e 2 (cálculo), ignorando códigos 3 e 4.",
        "wrongReasons": [
            "Crianças e adolescentes são examinados rotineiramente para cárie e gengivite.",
            None,
            "Atribuir código de bolsa profunda a crianças geraria falsos-positivos bizarros.",
            "Levantamentos de campo são estritamente observacionais diagnósticos, sem procedimentos cirúrgicos periodontais invasivos."
        ]
    },
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "O índice de Perda de Inserção Periodontal (PIP / LOA - Loss of Attachment) mede o dano cumulativo da doença periodontal ao longo da vida do indivíduo. Clinicamente, a perda de inserção é mensurada entre:",
        "options": [
            "A ponta da cúspide vestibular e a borda incisal do antagonista.",
            "A Junção Cemento-Esmalte (JCE) anatômica do dente e o fundo da bolsa periodontal ou sulco gengival.",
            "O ápice radicular radiográfico e a mandíbula contralateral.",
            "A cartilagem do nariz e o osso mentoniano do queixo."
        ],
        "answer": 1,
        "target": "indice_pip",
        "hint": "Inserção periodontal perdida = distância da JCE até a base da bolsa.",
        "explanation": "A perda de inserção periodontal (PIP) representa a destruição do ligamento periodontal e osso alveolar decorrente de periodontite ao longo da vida. É aferida medindo-se a distância em milímetros da Junção Cemento-Esmalte (JCE) anatômica até o ponto mais apical alcançado pela ponta da sonda periodontal no fundo do sulco/bolsa.",
        "wrongReasons": [
            "Cúspide a borda do antagonista mede a oclusão/trespasse vertical (overbite).",
            None,
            "Não se mede o ápice radicular ao vivo sem radiografias invasivas de campo.",
            "Nariz ao mento mede a Dimensão Vertical de Oclusão (DVO) da prótese, nada tendo a ver com PIP."
        ]
    },
    {
        "cat": 2,
        "sub": "epidemiologia_periodontal",
        "pool": "all",
        "text": "Os resultados do inquérito epidemiológico nacional SB Brasil 2023 revelaram um dado alarmante em relação à saúde periodontal da população IDOSA brasileira (65 a 74 anos de idade). Qual foi esse achado?",
        "options": [
            "100% dos idosos brasileiros possuem gengivas perfeitamente saudáveis sem nenhuma perda dental.",
            "Cerca de 86% dos idosos apresentaram sextantes periodontais EXCLUÍDOS (código X do CPI), refletindo o severo histórico de perdas dentárias precoces e edentulismo mutilador no país.",
            "Todos os idosos brasileiros utilizam aparelhos ortodônticos linguais estéticos.",
            "A doença periodontal foi completamente erradicada do território nacional graças à água de torneira."
        ],
        "answer": 1,
        "target": "indice_cpi",
        "hint": "Aproximadamente 86% dos idosos não têm dentes suficientes para serem examinados no CPI (sextantes com código X devido a extrações mutiladoras passadas).",
        "explanation": "O SB Brasil 2023 evidenciou a dramática herança do modelo odontológico mutilador do passado: aproximadamente 86% dos idosos de 65 a 74 anos apresentaram sextantes com código X (excluídos do CPI por terem menos de 2 dentes funcionais no sextante ou por edentulismo total), demonstrando que a perda dentária acumulada é o maior desafio na terceira idade.",
        "wrongReasons": [
            "A saúde periodontal dos idosos brasileiros é gravemente comprometida por perdas dentárias passadas.",
            None,
            "Idosos brasileiros na atenção primária do SUS sofrem com edentulismo, não com ortodontia lingual estética.",
            "A periodontite continua sendo uma das patologias bucais crônicas mais prevalentes do país."
        ]
    }
]

if __name__ == '__main__':
    print("QUESTIONS_P3_CAT2 count:", len(QUESTIONS_P3_CAT2))
    for i, q in enumerate(QUESTIONS_P3_CAT2):
        assert len(q['options']) == 4, f"Q{i} does not have 4 options"
        assert 0 <= q['answer'] <= 3, f"Q{i} answer out of bounds"
        assert len(q['wrongReasons']) == 4, f"Q{i} wrongReasons length != 4"
        assert q['wrongReasons'][q['answer']] is None, f"Q{i} wrongReasons at answer is not None"
        for idx, wr in enumerate(q['wrongReasons']):
            if idx != q['answer']:
                assert isinstance(wr, str) and len(wr) > 0, f"Q{i} option {idx} wrongReason missing"
    print("All 35 questions in CAT2 validated successfully!")
