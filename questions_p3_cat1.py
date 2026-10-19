# -*- coding: utf-8 -*-
"""
questions_p3_cat1.py
Banco de 35 questões da Categoria 1 da Prova 3:
"Epidemiologia da Cárie, Erupção e ICDNT"
Subtópicos:
  - cronologia_erupcao (9 questões)
  - indices_carie (9 questões)
  - icdnt_condicao (9 questões)
  - icdnt_necessidade (8 questões)
"""

QUESTIONS_P3_CAT1 = [
    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 1: cronologia_erupcao (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "No sistema de notação dentária preconizado pela Federação Dentária Internacional (FDI) e adotado pela Organização Mundial da Saúde (OMS), o dente decíduo segundo molar inferior esquerdo é identificado pelo código numérico de dois dígitos:",
        "options": [
            "37",
            "75",
            "85",
            "25"
        ],
        "answer": 1,
        "target": "notacao_fdi",
        "hint": "Quadrantes decíduos: 5 (superior direito), 6 (superior esquerdo), 7 (inferior esquerdo), 8 (inferior direito). O segundo molar é o dente número 5.",
        "explanation": "No sistema de dois dígitos da FDI, o primeiro dígito indica o quadrante (1 a 4 para dentição permanente; 5 a 8 para dentição decídua). O quadrante inferior esquerdo decíduo é o 7. O segundo dígito indica o dente a partir da linha média (segundo molar decíduo = 5). Logo, o código é 75.",
        "wrongReasons": [
            "37 é o segundo molar permanente inferior esquerdo.",
            None,
            "85 é o segundo molar decíduo inferior DIREITO (quadrante 8).",
            "25 é o segundo pré-molar permanente superior esquerdo."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "Sobre a cronologia de erupção da dentição permanente, o primeiro dente permanente a emergir na cavidade bucal humana é habitualmente o:",
        "options": [
            "Incisivo lateral superior aos 8 anos de idade.",
            "Primeiro molar permanente (inferior ou superior) por volta dos 6 a 7 anos, irrompendo posteriormente ao segundo molar decíduo sem esfoliação prévia.",
            "Canino superior aos 5 anos de idade esfoliando o canino de leite.",
            "Terceiro molar aos 12 anos de idade marcando o fim da dentição mista."
        ],
        "answer": 1,
        "target": "cronologia_erupcao_node",
        "hint": "Conhecido como 'dente dos 6 anos', ele não substitui nenhum de leite: nasce diretamente atrás dos decíduos.",
        "explanation": "O primeiro molar permanente irrompe por volta dos 6 aos 7 anos de idade diretamente no espaço retromolar atrás do segundo molar decíduo, sem a perda de nenhum dente decíduo precedente. Por essa razão, pais frequentemente não percebem que se trata de um dente permanente, predispondo-o à cárie.",
        "wrongReasons": [
            "Incisivos laterais superiores irrompem por volta dos 8 a 9 anos, após os incisivos centrais e primeiros molares.",
            None,
            "Caninos superiores permanentes erupcionam aos 11-12 anos, e não aos 5 anos.",
            "Terceiros molares erupcionam tipicamente após os 17-18 anos; aos 12 anos irrompe o segundo molar permanente."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "Em relação à sequência cronológica de erupção entre os arcos superior e inferior na dentição permanente, destaca-se uma importante diferença anatômica quanto ao dente canino:",
        "options": [
            "O canino superior erupciona precocemente aos 7 anos, antes dos incisivos centrais.",
            "No arco inferior, o canino (9-10 anos) erupciona ANTES dos pré-molares; enquanto no arco superior, o canino (11-12 anos) erupciona tipicamente DEPOIS dos pré-molares.",
            "Os caninos superiores e inferiores sempre erupcionam no mesmo dia e na mesma hora.",
            "Os caninos inferiores nunca erupcionam em indivíduos do sexo masculino."
        ],
        "answer": 1,
        "target": "cronologia_erupcao_node",
        "hint": "Lembre-se da sequência clássica: no arco inferior o canino vem antes dos pré-molares (3 antes de 4 e 5); no arco superior os pré-molares vêm antes do canino (4 e 5 antes de 3).",
        "explanation": "No arco mandibular (inferior), a sequência habitual de erupção é: 1º molar, incisivo central, incisivo lateral, CANINO, 1º pré-molar, 2º pré-molar e 2º molar. Já no arco maxilar (superior), a sequência é: 1º molar, incisivo central, incisivo lateral, 1º pré-molar, 2º pré-molar, CANINO e 2º molar. Ou seja, o canino inferior precede os pré-molares, enquanto o superior é posterior a eles.",
        "wrongReasons": [
            "O canino superior permanente erupciona tardiamente (11 a 12 anos), após incisivos e pré-molares.",
            None,
            "Não existe sincronia simultânea absoluta no mesmo dia entre caninos superiores e inferiores.",
            "Caninos inferiores erupcionam normalmente em ambos os sexos."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "Segundo os estudos de Moyers sobre a cronologia de desenvolvimento da dentição, qual é a diferença observada no ritmo de erupção entre os sexos feminino e masculino?",
        "options": [
            "Meninos erupcionam todos os dentes permanentes 2 anos antes das meninas.",
            "Meninas apresentam, em média, uma precocidade eruptiva de cerca de 5 meses em relação aos meninos.",
            "Não existe nenhuma variação biológica entre meninos e meninas na emergência dentária.",
            "Meninas não possuem dentes pré-molares permanentes em virtude do cariótipo XX."
        ],
        "answer": 1,
        "target": "cronologia_erupcao_node",
        "hint": "As meninas amadurecem esqueleticamente e dentalmente antes dos meninos em cerca de meio ano (5 meses).",
        "explanation": "Conforme documentado por Moyers e reiterado nos slides do Prof. André, as meninas apresentam maior precocidade esquelética e dental, erupcionando os dentes permanentes em média cerca de 5 meses antes dos meninos.",
        "wrongReasons": [
            "Meninos não são mais precoces; na verdade, apresentam erupção ligeiramente mais tardia que as meninas.",
            None,
            "Existe sim diferença estatisticamente documentada e clinicamente relevante entre os sexos.",
            "Ambos os sexos possuem a mesma fórmula dental de 32 dentes permanentes com 8 pré-molares."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "De acordo com os critérios padronizados da OMS para levantamentos epidemiológicos de saúde bucal, quando um dente é considerado formalmente 'IRROMPIDO'?",
        "options": [
            "Apenas quando toda a sua coroa clínica tiver atingido a linha de oclusão com o antagonista.",
            "Quando qualquer porção da sua superfície coronária tiver rompido a mucosa gengival e puder ser tocada pela ponta da sonda.",
            "Quando o exame radiográfico periapical demonstrar 100% de formação do ápice radicular.",
            "Quando o paciente relatar dor de dente há mais de 30 dias consecutivos."
        ],
        "answer": 1,
        "target": "regras_exame_oms",
        "hint": "Critério da ponta da sonda: rompeu a gengiva e a sonda encostou na coroa, já é considerado irrompido e deve ser examinado.",
        "explanation": "Para a OMS, um dente é registrado como presente/irrompido assim que qualquer cúspide ou borda incisal tiver perfurado a mucosa bucal e puder ser palpada/tocada pela ponta da sonda periodontal, independentemente de ter ou não atingido o plano oclusal.",
        "wrongReasons": [
            "Não se exige que atinja a oclusão; basta perfurar a gengiva e ser tocado pela sonda para entrar no exame.",
            None,
            "Não se utilizam radiografias de rotina em levantamentos de campo da OMS para aferir ápice radicular.",
            "Presença de dor é sintoma subjetivo que não define erupção anatômica."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "Em um exame de levantamento epidemiológico escolar, o examinador observa que o dente permanente 11 está erupcionando lingualizado, enquanto o incisivo central decíduo 51 ainda permanece retido no mesmo espaço anatômico. Segundo a regra da OMS, qual dente deve ser avaliado e anotado na ficha?",
        "options": [
            "Apenas o dente decíduo 51, ignorando o dente permanente.",
            "Apenas o dente PERMANENTE 11, pois na ocorrência concomitante no mesmo espaço o permanente tem precedência sobre o decíduo.",
            "Ambos os dentes devem ser anotados no mesmo quadradinho, somando suas notas.",
            "O examinador deve extrair o dente decíduo imediatamente na cadeira da escola antes de anotar."
        ],
        "answer": 1,
        "target": "regras_exame_oms",
        "hint": "Regra da OMS: quando o dente permanente e seu antecessor decíduo dividem o mesmo espaço, o dente PERMANENTE prevalece e é o único anotado.",
        "explanation": "De acordo com as normas da OMS, quando um dente decíduo e o seu sucessor permanente estão presentes simultaneamente no mesmo espaço interdental, o examinador deve registrar exclusivamente a condição do dente PERMANENTE. O dente decíduo é desconsiderado no registro.",
        "wrongReasons": [
            "O decíduo é ignorado para priorizar o status do dente definitivo permanente.",
            None,
            "Não é permitido somar códigos de dois dentes em uma mesma quadrícula de notação.",
            "Levantamentos epidemiológicos são estritamente observacionais; é terminantemente vedado realizar procedimentos cirúrgicos mutiladores durante o inquérito de campo."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "Durante o exame de um adolescente de 12 anos, o cirurgião-dentista constata a presença de um dente supranumerário conoide erupcionado na linha média entre os incisivos centrais superiores (mesiodens). Conforme as normas da OMS, esse dente deve ser:",
        "options": [
            "Incluído no CPO-D no componente 'C' atribuindo nota 99.",
            "Totalmente IGNORADO no exame epidemiológico, não sendo registrado nas quadrículas do CPO-D ou ICDNT.",
            "Registrado substituindo o dente 11, enquanto o 11 é excluído.",
            "Codificado como pilar de prótese total removível."
        ],
        "answer": 1,
        "target": "regras_exame_oms",
        "hint": "Dentes supranumerários não fazem parte da fórmula dental humana padrão de 28/32 dentes da OMS, portanto são ignorados.",
        "explanation": "A regra da OMS estabelece que dentes supranumerários não devem ser computados nem registrados nos índices de cárie (CPO-D, ICDNT). O examinador deve examinar apenas a série normal dos dentes habituais da fórmula dentária humana.",
        "wrongReasons": [
            "Não se inclui supranumerário no CPO-D nem existe código 99 no índice.",
            None,
            "O mesiodens não substitui o dente central normal anatômico 11.",
            "Não tem nenhuma relação com pilar protético."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "A dentição decídua completa é composta por um total de 20 dentes. Sua erupção tem início habitual com os incisivos centrais inferiores por volta dos:",
        "options": [
            "1 a 2 meses de vida intrauterina.",
            "6 a 8 meses de idade após o nascimento.",
            "2 anos e meio a 3 anos de idade.",
            "6 anos completos junto com o primeiro molar."
        ],
        "answer": 1,
        "target": "cronologia_erupcao_node",
        "hint": "Os primeiros dentinhos de leite a nascer são os centrais inferiores, por volta de meio ano de vida (6 a 8 meses).",
        "explanation": "A erupção dos dentes decíduos inicia-se habitualmente entre os 6 e 8 meses de idade com a emergência dos incisivos centrais decíduos inferiores (71 e 81), completando-se por volta dos 2,5 a 3 anos com a chegada dos segundos molares decíduos.",
        "wrongReasons": [
            "A erupção não ocorre no período intrauterino na esmagadora maioria dos nascimentos.",
            None,
            "Aos 2,5 a 3 anos a dentição decídua se completa, e não se inicia.",
            "Aos 6 anos inicia-se a dentição permanente com os primeiros molares e incisivos centrais inferiores."
        ]
    },
    {
        "cat": 1,
        "sub": "cronologia_erupcao",
        "pool": "all",
        "text": "Se em um adolescente de 15 anos um pré-molar permanente não se encontra na cavidade bucal e não há histórico de extração ou agenesia confirmada, e radiograficamente o dente ainda não rompeu a mucosa, no índice ICDNT da OMS para a coroa ele deve receber o código:",
        "options": [
            "0 (Hígido)",
            "4 (Perdido por cárie)",
            "8 (Dente não irrompido)",
            "9 (Dente excluído)"
        ],
        "answer": 2,
        "target": "icdnt_coroa",
        "hint": "Dente presente intraósseo ou na gengiva que ainda não erupcionou recebe o código 8.",
        "explanation": "No ICDNT da OMS, o código 8 para a coroa identifica o dente permanente NÃO IRROMPIDO (retido na mucosa ou tecido ósseo sem ter rompido a gengiva). O código 0 é hígido já erupcionado, 4 é perdido por cárie e 9 é excluído.",
        "wrongReasons": [
            "0 é hígido completamente irrompido e visível no arco.",
            "4 é atribuído a dentes comprovadamente extraídos em decorrência de cárie.",
            None,
            "9 é dente com banda ortodôntica ou impossível de inspecionar."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 2: indices_carie (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "O índice CPO-D, proposto por Klein e Palmer e padronizado pela OMS para mensurar o ataque de cárie em dentes permanentes, é composto pelo somatório de:",
        "options": [
            "Dentes com Cálculo + Periodontite + Oclusão defeituosa.",
            "Dentes Cariados (C) + Dentes Perdidos por cárie (P) + Dentes Obturados/restaurados sem cárie (O).",
            "Dentes Clareados + Polidos + Ortodônticos.",
            "Cistos periapicais + Pulpopatias + Osteomielite."
        ],
        "answer": 1,
        "target": "indice_cpod",
        "hint": "C-P-O: Cariados, Perdidos (por cárie) e Obturados (restaurados). O 'D' significa que a unidade de medida é o dente.",
        "explanation": "O CPO-D expressa a média de dentes permanentes que sofreram ataque de cárie no passado ou presente: C (cariados com cavidade ativa), P (perdidos ou extraídos exclusivamente por cárie) e O (obturados/restaurados sem cárie recorrente).",
        "wrongReasons": [
            "CPO-D não avalia cálculo, periodontite ou oclusão; para periodontia usa-se o CPI.",
            None,
            "Clareamento e polimento são procedimentos estéticos cosméticos alheios ao índice CPO-D.",
            "Cistos e osteomielite são patologias cirúrgicas hospitalares não quantificadas no CPO-D."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "Qual é a idade-índice internacional recomendada pela OMS como parâmetro global de comparação epidemiológica do ataque de cárie dentária (CPO-D) entre países?",
        "options": [
            "5 anos de idade.",
            "12 anos de idade.",
            "35 a 44 anos de idade.",
            "65 a 74 anos de idade."
        ],
        "answer": 1,
        "target": "indice_cpod",
        "hint": "Aos 12 anos praticamente todos os dentes permanentes (exceto terceiros molares) já erupcionaram e estão expostos ao meio bucal há alguns anos.",
        "explanation": "A idade de 12 anos é a idade-chave internacional de referência da OMS para a cárie dentária na dentição permanente, pois quase todos os dentes permanentes já irromperam e permite a comparação direta das tendências epidemiológicas mundiais.",
        "wrongReasons": [
            "5 anos é a idade-índice da OMS para a dentição decídua (índice ceo-d).",
            None,
            "35 a 44 anos é a faixa-etária padrão da OMS para adultos e doença periodontal.",
            "65 a 74 anos é a faixa-etária de idosos para avaliação de edentulismo e perda de inserção."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "Em relação ao índice ceo-d, utilizado na dentição decídua (especialmente aos 5 anos de idade), assinale a afirmativa CORRETA:",
        "options": [
            "O componente 'e' representa dentes com 'extração indicada por cárie', e o componente 'p' de dentes perdidos é omitido para não confundir com a esfoliação fisiológica.",
            "O ceo-d avalia 32 dentes decíduos em adultos jovens.",
            "Dentes que caíram naturalmente por esfoliação da raiz devem ser obrigatoriamente computados como 'perdidos por cárie'.",
            "O ceo-d é medido exclusivamente através de tomografias cone-beam tridimensionais."
        ],
        "answer": 0,
        "target": "indice_ceod",
        "hint": "Em crianças de 5 anos é difícil saber se um incisivo ausente caiu sozinho (esfoliou) ou foi extraído por cárie; por isso o 'p' é excluído e usa-se 'e' (extração indicada).",
        "explanation": "No ceo-d: c = cariado; e = extração indicada por cárie; o = obturado. O componente de dentes perdidos (p) não é utilizado na rotina da dentição decídua aos 5 anos porque não é possível distinguir com segurança dentes perdidos precocemente por cárie de dentes que sofreram esfoliação fisiológica natural.",
        "wrongReasons": [
            None,
            "Dentição decídua possui no máximo 20 dentes, e não 32.",
            "Dentes esfoliados fisiologicamente não podem ser computados como perda por cárie.",
            "O exame do ceo-d é estritamente clínico visual sob luz natural com espelho e sonda da OMS."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "Enquanto o CPO-D avalia a condição do dente como um todo, o índice CPO-S mede o ataque de cárie em SUPERFÍCIES dentárias. Considerando uma dentição permanente completa de 32 dentes, o número total de superfícies anatômicas avaliadas no CPO-S é de:",
        "options": [
            "32 superfícies.",
            "148 superfícies (ou 128 superfícies excluindo os terceiros molares).",
            "500 superfícies oclusais.",
            "20 superfícies proximais."
        ],
        "answer": 1,
        "target": "indice_cpos",
        "hint": "Dentes posteriores (molares e pré-molares) têm 5 superfícies; dentes anteriores (caninos e incisivos) têm 4 superfícies.",
        "explanation": "No CPO-S: 16 dentes posteriores (8 molares + 8 pré-molares) têm 5 superfícies cada (16 x 5 = 80). 4 terceiros molares têm 5 faces (4 x 5 = 20). 12 dentes anteriores (incisivos e caninos) têm 4 superfícies cada (12 x 4 = 48). Total = 80 + 20 + 48 = 148 superfícies (ou 128 sem os terceiros molares).",
        "wrongReasons": [
            "32 é o número total de dentes, não de superfícies anatômicas.",
            None,
            "500 superfícies ultrapassa absurdamente a anatomia da dentição humana.",
            "20 superfícies corresponde apenas a 4 dentes posteriores."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "No cálculo do índice CPO-S, quando um dente posterior (ex: dente 16) foi extraído em decorrência de cárie, quantas superfícies são computadas como perdidas (P-S)?",
        "options": [
            "1 superfície.",
            "5 superfícies.",
            "4 superfícies.",
            "Zero superfícies, pois o dente não está mais na boca."
        ],
        "answer": 1,
        "target": "indice_cpos",
        "hint": "Como o molar tinha 5 faces anatômicas antes da extração, todas as suas 5 faces entram na contagem de perdidas.",
        "explanation": "Pela regra do CPO-S, dentes ausentes extraídos por cárie recebem a pontuação correspondente ao número total de faces anatômicas que possuíam: 5 superfícies para dentes posteriores (molares e pré-molares) e 4 superfícies para dentes anteriores (incisivos e caninos).",
        "wrongReasons": [
            "1 superfície seria uma restauração simples em dente presente.",
            None,
            "4 superfícies é a pontuação atribuída a dentes ANTERIORES perdidos por cárie.",
            "Dentes perdidos por cárie DEVEM ser computados, caso contrário a severidade passada da cárie seria subestimada."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "O Sistema Internacional de Detecção e Avaliação de Cárie (ICDAS) utiliza critérios visuais refinados com escores de 0 a 6. O escore 1 do ICDAS caracteriza-se por:",
        "options": [
            "Superfície dentária perfeitamente hígida sem desmineralização.",
            "Primeira alteração visual detectável no esmalte (opacidade ou descoloração), visível APENAS após secagem prolongada com ar.",
            "Cavidade extensa com dentina amolecida visível envolvendo mais da metade da coroa.",
            "Presença de coroa protética metálica fundida total."
        ],
        "answer": 1,
        "target": "sistema_icdas",
        "hint": "Escore 1: só aparece quando seca com jato de ar; enquanto está úmido de saliva parece normal.",
        "explanation": "No ICDAS: Escore 0 é dente hígido; Escore 1 é a alteração visual inicial visível apenas após secagem prolongada (mancha branca subclínica incipiente); Escore 2 é a alteração visual nítida já perceptível no esmalte ainda úmido.",
        "wrongReasons": [
            "Superfície hígida corresponde ao Escore 0 do ICDAS.",
            None,
            "Cavidade extensa com mais de 50% de dentina envolvida corresponde ao Escore 6 do ICDAS.",
            "Coroas protéticas são avaliadas por códigos específicos de restauração/prótese, não pelo escore 1."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "Qual é a principal distinção clínica entre o escore 2 e o escore 3 no sistema ICDAS?",
        "options": [
            "O escore 2 necessita de anestesia geral e o escore 3 de bochecho com flúor.",
            "No escore 2 há alteração visual em esmalte úmido sem perda de integridade de superfície; no escore 3 há microcavitação focal (microfratura) do esmalte sem dentina visível na base.",
            "No escore 2 o dente foi extraído e no escore 3 o dente está saudável.",
            "Não há nenhuma distinção, sendo termos absolutamente idênticos."
        ],
        "answer": 1,
        "target": "sistema_icdas",
        "hint": "O escore 3 marca a quebra (microcavidade) do esmalte superficial, mas a dentina ainda não está exposta.",
        "explanation": "O Escore 2 exibe mancha branca ou pigmentada visível tanto em dente úmido quanto seco, porém a superfície do esmalte permanece intacta (não cavitada). O Escore 3 caracteriza-se pela ruptura localizada do esmalte (microcavidade localizada) sem dentina clinicamente visível nas paredes ou base da lesão.",
        "wrongReasons": [
            "ICDAS é um índice diagnóstico observacional, não uma prescrição de anestesia geral.",
            None,
            "Dentes extraídos recebem outros registros; no ICDAS analisam-se lesões em superfícies dentárias existentes.",
            "Os escores 2 e 3 representam estágios biológicos e patológicos claramente distintos da evolução da cárie."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "Ao analisar a evolução epidemiológica da cárie no Brasil através dos inquéritos nacionais (SB Brasil 2003, SB Brasil 2010 e SB Brasil 2023), observa-se aos 12 anos de idade:",
        "options": [
            "Um aumento explosivo no número de dentes perdidos, superando um CPO-D de 15 dentes por criança.",
            "Uma expressiva tendência de queda no CPO-D (de 2,78 em 2003 para cerca de 2,07 em 2010 e abaixo de 2,0 no SB Brasil 2023), consolidando o Brasil na faixa de baixa prevalência de cárie da OMS.",
            "A eliminação 100% total e absoluta da bactéria Streptococcus mutans da população brasileira.",
            "Que todas as crianças brasileiras de todas as classes sociais possuem exatamente o mesmo índice de cárie sem desigualdades."
        ],
        "answer": 1,
        "target": "indice_cpod",
        "hint": "A fluoretação das águas, dentifrícios fluoretados e a expansão do Brasil Sorridente reduziram o CPO-D para o patamar de baixa prevalência da OMS (< 3,0).",
        "explanation": "Os inquéritos SB Brasil demonstraram um declínio consistente do CPO-D aos 12 anos: de 2,78 (2003) para 2,07 (2010) e mantendo-se em níveis baixos no SB Brasil 2023. Esse resultado colocou o Brasil no grupo de países com baixa prevalência de cárie segundo os parâmetros internacionais da OMS.",
        "wrongReasons": [
            "O índice de cárie caiu substancialmente, jamais atingindo valores catastróficos de 15 dentes aos 12 anos.",
            None,
            "A cárie não foi erradicada nem as bactérias da microbiota bucal foram extintas.",
            "Permanece uma profunda desigualdade e polarização da cárie entre regiões e estratos socioeconômicos."
        ]
    },
    {
        "cat": 1,
        "sub": "indices_carie",
        "pool": "all",
        "text": "O fenômeno epidemiológico contemporâneo da 'POLARIZAÇÃO DA CÁRIE DENTÁRIA' descreve a situação na qual:",
        "options": [
            "A cárie dentária passou a ocorrer apenas nas calotas polares do Ártico.",
            "A maior carga da doença concentra-se em uma minoria da população vivendo sob piores condições socioeconômicas e vulnerabilidade, enquanto a maioria tem baixo ou nenhum ataque de cárie.",
            "Todos os dentes anteriores ficam cariados e todos os dentes posteriores ficam imunes.",
            "A doença cárie afeta igualmente todas as camadas sociais sem nenhuma relação com renda ou escolaridade."
        ],
        "answer": 1,
        "target": "indice_cpod",
        "hint": "Com a queda na média geral, a doença não sumiu por igual: concentrou-se fortemente nos bolsões de maior pobreza e vulnerabilidade.",
        "explanation": "A polarização da cárie é o fenômeno em que, apesar do declínio das médias nacionais do CPO-D, o agravo passa a se concentrar em grupos específicos mais vulneráveis (menor renda, menor escolaridade materna e falta de saneamento/água fluoretada), que acumulam grande parte das lesões não tratadas.",
        "wrongReasons": [
            "Polarização é um termo epidemiológico sobre distribuição desigual de doenças em grupos humanos, nada tendo a ver com regiões polares do globo.",
            None,
            "Não se refere a dentes anteriores x posteriores na boca.",
            "A cárie tem relação direta e profunda com determinantes sociais de saúde, renda e acesso a serviços."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 3: icdnt_condicao (9 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "No Índice de Condição Dentária e Necessidade de Tratamento (ICDNT) padronizado pela OMS, qual é o código atribuído a uma coroa dentária PERMANENTE que se apresenta totalmente HÍGIDA (sem cárie clínica evidente e sem restauração)?",
        "options": [
            "0",
            "1",
            "A",
            "9"
        ],
        "answer": 0,
        "target": "icdnt_coroa",
        "hint": "Para dentes permanentes os códigos de condição coronária são numéricos (0 a 9); dente hígido permanente é o primeiro código.",
        "explanation": "No ICDNT, a coroa permanente hígida recebe o código 0. Se fosse um dente decíduo hígido, receberia a letra 'A'. O código 1 é permanente cariado e o 9 é excluído.",
        "wrongReasons": [
            None,
            "1 é o código de dente permanente CARIADO.",
            "A é o código para dente DECÍDUO hígido.",
            "9 é o código para dente permanente EXCLUÍDO (ex: com banda ortodôntica)."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "Em relação aos códigos do ICDNT para dentes DECÍDUOS, assinale a correspondência CORRETA entre letra e condição coronária:",
        "options": [
            "A = Perdido por cárie; B = Hígido; C = Não irrompido.",
            "A = Hígido; B = Cariado; C = Restaurado com cárie; D = Restaurado sem cárie; E = Perdido por cárie.",
            "A = Selante de fissuras; B = Banda ortodôntica; C = Raiz residual.",
            "Dentição decídua não pode ser examinada pelo ICDNT segundo normas da OMS."
        ],
        "answer": 1,
        "target": "icdnt_coroa",
        "hint": "As letras decíduas acompanham os números permanentes: A=0 (hígido), B=1 (cariado), C=2 (restaurado com cárie), D=3 (restaurado sem cárie), E=4 (perdido por cárie).",
        "explanation": "Na notação da OMS/ICDNT: Dentes permanentes utilizam números (0 a 9) e decíduos utilizam letras equivalentes (A=hígido, B=cariado, C=restaurado com cárie, D=restaurado sem cárie, E=perdido por cárie, F=selante, G=prótese/coroa, -=excluído).",
        "wrongReasons": [
            "A correspondência foi distorcida: A é hígido e B é cariado.",
            None,
            "Selante na dentição decídua é código F, não A.",
            "O ICDNT foi concebido especificamente para abranger tanto a dentição permanente quanto a decídua simultaneamente."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "Um estudante de odontologia examina um primeiro molar permanente (dente 46) que possui uma restauração oclusal de amálgama íntegra, porém na face vestibular adjacente à margem gengival apresenta uma cavidade ativa de cárie com base amolecida. Qual é o código correto de condição da coroa no ICDNT?",
        "options": [
            "0 (Hígido)",
            "2 (Restaurado com cárie)",
            "3 (Restaurado sem cárie)",
            "6 (Selante de fóssulas)"
        ],
        "answer": 1,
        "target": "icdnt_coroa",
        "hint": "O dente tem restauração prévia E TAMBÉM tem cárie ativa (seja recidiva marginal ou lesão primária em outra face).",
        "explanation": "No ICDNT, o código 2 (ou 'C' em decíduos) é atribuído quando o dente apresenta uma ou mais restaurações definitivas E simultaneamente apresenta uma ou mais lesões de cárie ativas (independentemente de estarem em contato com a restauração ou em outra face da mesma coroa).",
        "wrongReasons": [
            "O dente não é hígido, pois possui restauração e cavidade cariosa ativa.",
            None,
            "O código 3 é exclusivo para dentes restaurados que NÃO possuem nenhuma cárie ativa.",
            "Amálgama e cavidade cariosa não se classificam como selante preventivo (código 6)."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "Se um dente permanente apresentar uma restauração provisória à base de óxido de zinco e eugenol (IRM) ou material restaurador temporário (Cavit) colocada em serviço de urgência, no ICDNT da OMS sua coroa deve ser registrada como:",
        "options": [
            "Código 3 (Restaurado sem cárie)",
            "Código 1 (Cariado)",
            "Código 0 (Hígido)",
            "Código 7 (Prótese fixa definitiva)"
        ],
        "answer": 1,
        "target": "icdnt_coroa",
        "hint": "Restaurações provisórias são consideradas dentes doentes não finalizados; no levantamento contam como cariados.",
        "explanation": "Conforme o manual da OMS, qualquer dente contendo material restaurador provisório/temporário deve ser registrado como CARIADO (código 1 em permanentes ou B em decíduos), uma vez que a patologia cariosa não foi definitivamente sanada.",
        "wrongReasons": [
            "Código 3 é reservado para materiais restauradores DEFINITIVOS (resina composta, amálgama, ionômero definitivo).",
            None,
            "O dente sofreu destruição cariosa e intervenção temporária, não podendo ser considerado hígido.",
            "Materiais provisórios não são próteses definitivas fixas nem coroas protéticas (código 7)."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "Qual é a regra da OMS no ICDNT para dentes com aparelhos ortodônticos fixos em relação à exclusão (código 9)?",
        "options": [
            "Qualquer paciente com aparelho ortodôntico deve ter todos os 32 dentes excluídos.",
            "Dentes com braquetes colados NÃO são excluídos (devem ser examinados normalmente); mas dentes com BANDAS metálicas circunferenciais devem ser EXCLUÍDOS (código 9).",
            "Dentes com braquetes são excluídos e dentes com bandas são considerados hígidos.",
            "Aparelho ortodôntico transforma todos os dentes automaticamente no código 4 (perdido por cárie)."
        ],
        "answer": 1,
        "target": "icdnt_coroa",
        "hint": "O braquete permite enxergar e sondar quase toda a coroa; a banda metálica abraça o dente e esconde as superfícies (logo, o dente com banda é excluído = 9).",
        "explanation": "Dentes com braquetes ortodônticos colados devem ser examinados normalmente em todas as suas faces visíveis. No entanto, dentes que sustentam bandas metálicas cimentadas que cobrem as paredes do dente impossibilitando a visualização direta devem ser codificados como EXCLUÍDOS (código 9 em permanentes ou '-' em decíduos).",
        "wrongReasons": [
            "Não se exclui a boca inteira; dentes sem bandas são examinados normalmente.",
            None,
            "A regra inverteu os dispositivos: o braquete não exclui, enquanto a banda metálica circundante exclui.",
            "Aparelho ortodôntico não significa perda dentária por cárie (código 4)."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "No ICDNT, a perda dentária na dentição permanente é dividida em dois códigos fundamentais: código 4 e código 5. Assinale a diferença entre eles:",
        "options": [
            "Código 4 é dente perdido por cárie; Código 5 é dente perdido por qualquer outra razão (ortodontia, periodontia, trauma ou agenesia).",
            "Código 4 é dente decíduo e Código 5 é dente permanente.",
            "Código 4 é dente superior e Código 5 é dente inferior.",
            "Código 4 é dente com mancha branca e Código 5 é dente com fluorose severa."
        ],
        "answer": 0,
        "target": "icdnt_coroa",
        "hint": "O código 4 entra no componente 'P' do CPO-D; o código 5 é exclusão por outros motivos (orto, trauma) e NÃO entra no CPO-D.",
        "explanation": "O código 4 identifica dentes permanentes extraídos ou perdidos exclusivamente em decorrência de cárie dentária (e compõe o componente 'P' do CPO-D). O código 5 identifica dentes ausentes perdidos por trauma, extração ortodôntica, doença periodontal ou agenesia congênita (não entrando no CPO-D tradicional).",
        "wrongReasons": [
            None,
            "Ambos os códigos 4 e 5 são aplicados à dentição permanente no ICDNT.",
            "Os códigos aplicam-se a todos os quadrantes, superiores e inferiores.",
            "Mancha branca e fluorose são alterações de esmalte em dentes presentes, não ausências dentárias."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "Em relação à avaliação da RAIZ no ICDNT, dentes com recessão gengival que apresentam a superfície radicular exposta sem nenhuma lesão de cárie ou restauração recebem o código:",
        "options": [
            "0 (Raiz hígida)",
            "1 (Raiz cariada)",
            "8 (Raiz não exposta)",
            "9 (Raiz excluída)"
        ],
        "answer": 0,
        "target": "icdnt_coroa",
        "hint": "Raiz visível (exposta) e sadia recebe o mesmo código básico de hígido: zero.",
        "explanation": "Na avaliação radicular do ICDNT: Código 0 = raiz exposta hígida; Código 1 = raiz exposta com cárie; Código 2 = raiz restaurada com cárie; Código 3 = raiz restaurada sem cárie; Código 8 = raiz não exposta (coberta por gengiva); Código 9 = excluída.",
        "wrongReasons": [
            None,
            "Código 1 é para raiz com lesão ativa de cárie radicular.",
            "Código 8 é atribuído quando a raiz NÃO está exposta (ou seja, quando o periodonto recobre totalmente a junção cemento-esmalte).",
            "Código 9 é reservado para dentes excluídos do exame."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "Segundo a 'Regra da Dúvida Diagnóstica' da OMS, quando o examinador se depara com um caso limítrofe no qual hesita entre considerar o dente hígido ou cariado em estágio inicial, a diretriz expressa é:",
        "options": [
            "Registrar imediatamente como cariado para pecar pelo excesso de cuidado.",
            "Registrar o escore de menor severidade (no caso, registrar HÍGIDO código 0).",
            "Aplicar anestesia infiltrativa e realizar curetagem exploratória com broca esférica.",
            "Chamar a polícia sanitária para interditar o colégio."
        ],
        "answer": 1,
        "target": "regras_exame_oms",
        "hint": "A OMS é estritamente conservadora: na dúvida, opte pela condição mais saudável (menor escore).",
        "explanation": "A diretriz oficial da OMS para levantamentos epidemiológicos preconiza que, havendo dúvida razoável entre dois códigos diagnósticos, o examinador deve invariavelmente atribuir o código de menor gravidade (ex: entre hígido e cariado, registrar HÍGIDO; entre restaurado sem cárie e restaurado com cárie, registrar RESTAURADO SEM CÁRIE).",
        "wrongReasons": [
            "Registrar cárie na dúvida superestimaria artificialmente a prevalência de doença, violando as regras da OMS.",
            None,
            "Intervenção operatória invasiva é proibida e antiética em inquéritos epidemiológicos de campo.",
            "A dúvida diagnóstica é uma questão técnica metodológica, não uma infração policial."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_condicao",
        "pool": "all",
        "text": "Um dente permanente que apresenta uma coroa protética total metalocerâmica colocada em função de um histórico de restaurações extensas, sem cárie nas margens cervicais, deve ser codificado na coroa do ICDNT como:",
        "options": [
            "Código 0 (Hígido)",
            "Código 3 (Restaurado sem cárie)",
            "Código 7 (Pilar de ponte, coroa especial ou faceta)",
            "Código 9 (Excluído)"
        ],
        "answer": 2,
        "target": "icdnt_coroa",
        "hint": "Coroas totais, próteses fixas e facetas estéticas têm um código próprio: código 7 (ou 'G' em decíduos).",
        "explanation": "No ICDNT, o código 7 (ou letra 'G' para decíduos) é destinado especificamente a dentes que sustentam coroas totais (metálicas, metalocerâmicas, jaquetas), dentes pilares de prótese fixa ou facetas protéticas.",
        "wrongReasons": [
            "Não é hígido, pois a coroa natural foi substituída por material protético artificial.",
            "Código 3 é para restaurações diretas convencionais parciais (amálgama, resina, CIV), não coroas totais.",
            None,
            "Coroas protéticas examináveis não são excluídas; recebem código 7."
        ]
    },

    # ─────────────────────────────────────────────────────────────
    # SUBTÓPICO 4: icdnt_necessidade (8 questões)
    # ─────────────────────────────────────────────────────────────
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "No ICDNT, a avaliação da 'Necessidade de Tratamento' gera códigos específicos de intervenção para cada elemento dentário. O código 0 de necessidade indica que:",
        "options": [
            "O dente necessita de extração imediata com urgência.",
            "Nenhum tratamento curativo ou restaurador é necessário naquele elemento dentário.",
            "O paciente precisa de prótese total dupla.",
            "O dente possui indicação de implante osseointegrado imediato."
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Código 0 de necessidade = dente que não necessita de nenhuma intervenção odontológica.",
        "explanation": "O código 0 na coluna de necessidade de tratamento indica ausência de necessidade interventiva (dente hígido ou adequadamente tratado que não demanda procedimentos restauradores, cirúrgicos ou endodônticos).",
        "wrongReasons": [
            "Extração indicada é classificada sob o código 6 de necessidade de tratamento.",
            None,
            "Próteses totais são avaliadas na seção de prótese, não no código de dente individual.",
            "Implante osseointegrado não é código 0 do ICDNT."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "Qual é a distinção no ICDNT entre a necessidade de tratamento código 1 e código 2?",
        "options": [
            "Código 1 é clareamento dental; Código 2 é faceta de porcelana.",
            "Código 1 indica restauração de 1 superfície; Código 2 indica restauração de 2 ou mais superfícies.",
            "Código 1 é para dentes decíduos e Código 2 é exclusivo para dentes permanentes.",
            "Código 1 é aplicação tópica de bochecho e Código 2 é raspagem subgengival."
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Trata-se da extensão da restauração requerida: 1 face (ex: apenas oclusal) vs 2 ou mais faces (ex: ocluso-proximal).",
        "explanation": "No ICDNT: Código 1 = Restauração de 1 superfície (lesões de cárie restritas a uma face, ex: oclusal simples); Código 2 = Restauração de 2 ou mais superfícies (lesões envolvendo múltiplas faces, ex: mesio-ocluso-distal).",
        "wrongReasons": [
            "Clareamento cosmético não integra os códigos de necessidade curativa do ICDNT.",
            None,
            "Ambos os códigos 1 e 2 aplicam-se indistintamente a dentes decíduos e permanentes.",
            "Raspagem periodontal é avaliada pelo índice CPI, não na necessidade dentária do ICDNT."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "Um dente permanente que apresenta lesão de cárie cavitada profunda com exposição pulpar visível, sintomatologia de dor espontânea e fístula na mucosa alveolar tem como código de necessidade de tratamento no ICDNT:",
        "options": [
            "Código 1 (Restauração simples de 1 face)",
            "Código 5 (Tratamento endodôntico / pulpotomia)",
            "Código 8 (Aplicação de selante de cicatrículas)",
            "Código 0 (Nenhum tratamento)"
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Envolvimento pulpar e fístula exigem intervenção no canal radicular (endodontia).",
        "explanation": "O código 5 na necessidade de tratamento do ICDNT é reservado para elementos que necessitam de intervenção na polpa dentária (tratamento de canal endodôntico ou pulpotomia) em decorrência de exposição pulpar por cárie ou trauma, desde que o dente seja restaurável.",
        "wrongReasons": [
            "Restauração simples não soluciona necrose pulpar e fístula infecciosa.",
            None,
            "Selante de cicatrículas é preventivo em dentes hígidos, contraindicado em polpa exposta.",
            "O elemento necessita de tratamento urgente para debelar foco infeccioso."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "O código 6 na coluna de necessidade de tratamento do ICDNT indica indicação de EXTRAÇÃO. Em qual das seguintes situações esse código deve ser prescrito?",
        "options": [
            "Dente hígido com pequeno acúmulo de placa bacteriana supragengival removível com gaze.",
            "Raiz residual irrecuperável por destruição cariosa maciça que impede qualquer reabilitação protética coronal.",
            "Dente com mancha branca ativa em esmalte passível de remineralização com flúor.",
            "Dente restaurado com compósito apresentando leve manchamento estético superficial por café."
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Extração é o desfecho cirúrgico final quando a destruição é tão extensa que restauração e canal são inviáveis.",
        "explanation": "O código 6 (Extração) é assinalado quando a destruição da coroa por cárie é tão avançada que o dente não pode ser restaurado por nenhuma técnica, restando apenas raízes residuais infectadas, ou quando há perda óssea periodontal extrema com mobilidade grau 3.",
        "wrongReasons": [
            "Placa bacteriana exige orientação de higiene, jamais extração mutiladora.",
            None,
            "Mancha branca ativa requer remineralização fluoretada (código 7), sendo erro gravíssimo extrair o dente.",
            "Manchamento extrínseco por café é resolvido com polimento coronário."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "No ICDNT, a necessidade de tratamento código 7 corresponde a:",
        "options": [
            "Exodontia cirúrgica sob narcose.",
            "Remineralização de mancha branca ativa de cárie (aplicação de flúor tópico profissional/verniz).",
            "Biópsia excisional de lesão tumoral maligna.",
            "Instalação de aparelho ortodôntico invisível com alinhadores plásticos."
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Código 7 é a medida conservadora não invasiva para lesões iniciais reversíveis de desmineralização em esmalte.",
        "explanation": "O código 7 do ICDNT indica intervenção preventiva remineralizante: aplicação de verniz ou gel fluoretado para promover a remineralização de lesões de mancha branca ativas não cavitadas.",
        "wrongReasons": [
            "Exodontia cirúrgica é código 6.",
            None,
            "Biópsias não fazem parte da grade numérica de tratamento do ICDNT.",
            "Ortodontia corretiva com alinhadores não é contemplada no índice de necessidade da OMS."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "Segundo os critérios clínicos estabelecidos pelo Prof. André e pela OMS, para que um examinador assinale o código 8 (SELANTE de fóssulas e fissuras) na necessidade de tratamento do ICDNT, quais condições devem ser simultaneamente preenchidas?",
        "options": [
            "O dente deve ter uma cavidade aberta em dentina amolecida de mais de 5 mm de profundidade.",
            "O dente deve possuir fóssulas e fissuras anatomicamente profundas, estar em indivíduo com histórico/risco de cárie e encontrar-se suficientemente irrompido para garantir isolamento contra contaminação salivar.",
            "O dente deve estar completamente coberto por mucosa óssea e ser invisível na boca.",
            "O dente deve ser uma prótese total de resina acrílica montada em articulador."
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Três critérios: 1) anatomia profunda retentiva; 2) risco de cárie no paciente; 3) erupção suficiente para isolar sem saliva.",
        "explanation": "A prescrição de selante (código 8 no ICDNT) requer: 1) Morfologia de cicatrículas e fissuras profundas e retentivas com suspeita de desmineralização inicial; 2) Paciente apresentando risco ou histórico de atividade de cárie; e 3) Erupção adequada da coroa que permita o isolamento do campo para adesão do material selante.",
        "wrongReasons": [
            "Cavidade aberta em dentina contraindica selante e exige restauração com código 1 ou 2.",
            None,
            "Dentes não irrompidos não podem receber selante na clínica.",
            "Próteses totais não possuem cicatrículas naturais de esmalte e não recebem selante preventivo."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "Em qual situação o código 9 (Não registrado / Sem informação) deve ser OBRIGATORIAMENTE atribuído na coluna de Necessidade de Tratamento do ICDNT?",
        "options": [
            "Apenas se o paciente tiver 100 anos de idade.",
            "Quando a condição da coroa foi registrada como 9 (excluído), 8 (dente não irrompido) ou 4/5 (dente ausente/perdido).",
            "Quando o dente for um incisivo lateral perfeitamente hígido.",
            "Sempre que o exame for realizado em uma segunda-feira pela manhã."
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Se o dente não pôde ser visto (excluído), se ainda não nasceu (não irrompido) ou já foi extraído (perdido), não há como prescrever tratamento dentário na ficha.",
        "explanation": "No ICDNT, se a coroa foi classificada como 8 (não irrompida), 9 (excluída por banda metálica), 4 (perdida por cárie) ou 5 (perdida por outra razão), é compulsório assinalar código 9 (sem informação / não registrado) na necessidade de tratamento, pois não há elemento dental presente a ser tratado.",
        "wrongReasons": [
            "Idade do paciente não obriga o preenchimento de código 9 em dentes examináveis presentes.",
            None,
            "Dente hígido recebe código 0 de necessidade (nenhum tratamento), e não código 9.",
            "O dia da semana e o turno não influenciam os critérios do manual da OMS."
        ]
    },
    {
        "cat": 1,
        "sub": "icdnt_necessidade",
        "pool": "all",
        "text": "Um primeiro molar permanente jovem apresenta severo comprometimento estrutural por Hipomineralização Molar-Incisivo (HMI) com fratura de esmalte pós-eruptiva extensa e perda de duas cúspides, sem condições de retenção para restauração direta simples de compósito. O código de necessidade de tratamento mais adequado no ICDNT é:",
        "options": [
            "Código 0 (Nenhum tratamento)",
            "Código 3 (Coroa por qualquer motivo / restauração indireta complexa)",
            "Código 7 (Remineralização de mancha branca)",
            "Código 8 (Selante preventivo de fissura)"
        ],
        "answer": 1,
        "target": "icdnt_tratamento",
        "hint": "Grande perda estrutural que não suporta restauração direta requer reabilitação com coroa total/recoberta (código 3).",
        "explanation": "O código 3 na necessidade de tratamento do ICDNT engloba a confecção de coroa protética ou cobertura cuspídea completa (seja por cárie extensa, traumatismo ou defeitos severos de desenvolvimento do esmalte como a HMI com perda extensa de cúspides que impossibilita restaurações diretas).",
        "wrongReasons": [
            "O elemento necessita de tratamento reabilitador complexo, não podendo receber código 0.",
            None,
            "Remineralização simples é ineficaz para dentes que já sofreram perda volumétrica de cúspides inteiras.",
            "Selante só tem indicação em fissuras intactas, não em dentes com fratura coronária estrutural extensa."
        ]
    }
]

if __name__ == '__main__':
    print("QUESTIONS_P3_CAT1 count:", len(QUESTIONS_P3_CAT1))
    for i, q in enumerate(QUESTIONS_P3_CAT1):
        assert len(q['options']) == 4, f"Q{i} does not have 4 options"
        assert 0 <= q['answer'] <= 3, f"Q{i} answer out of bounds"
        assert len(q['wrongReasons']) == 4, f"Q{i} wrongReasons length != 4"
        assert q['wrongReasons'][q['answer']] is None, f"Q{i} wrongReasons at answer is not None"
        for idx, wr in enumerate(q['wrongReasons']):
            if idx != q['answer']:
                assert isinstance(wr, str) and len(wr) > 0, f"Q{i} option {idx} wrongReason missing"
    print("All 35 questions in CAT1 validated successfully!")
