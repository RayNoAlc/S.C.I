# -*- coding: utf-8 -*-
"""
inject_p3.py
Script to safely inject Prova 3 data and logic into index.html
Using string replacement or lambda functions so backslashes (\n) are preserved!
"""

import json
import re
import build_p3_dataset
import questions_p3_cat0
import questions_p3_cat1
import questions_p3_cat2
import p3_cards_and_hard

# 1. Combine questions
all_questions = (
    questions_p3_cat0.QUESTIONS_P3_CAT0 +
    questions_p3_cat1.QUESTIONS_P3_CAT1 +
    questions_p3_cat2.QUESTIONS_P3_CAT2
)

cat_names_js = f"const CAT_NAMES_P3 = {json.dumps(build_p3_dataset.CAT_NAMES_P3, ensure_ascii=False)};"
subtopics_js = f"const SUBTOPICS_P3 = {json.dumps(build_p3_dataset.SUBTOPICS_P3, ensure_ascii=False, indent=2)};"
questions_js = f"const QUESTIONS_P3 = {json.dumps(all_questions, ensure_ascii=False, indent=2)};"
hard_questions_js = f"const HARD_QUESTIONS_P3 = {json.dumps(p3_cards_and_hard.HARD_QUESTIONS_P3, ensure_ascii=False, indent=2)};"
study_cards_js = f"const STUDY_CARDS_P3 = {json.dumps(p3_cards_and_hard.STUDY_CARDS_P3, ensure_ascii=False, indent=2)};"
map_themes_js = f"const MAP_THEMES_P3 = {json.dumps(build_p3_dataset.MAP_THEMES_P3, ensure_ascii=False, indent=2)};"
map_concepts_js = f"const MAP_CONCEPTS_P3 = {json.dumps(build_p3_dataset.MAP_CONCEPTS_P3, ensure_ascii=False, indent=2)};"

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Verify existing constants aren't duplicated
if 'CAT_NAMES_P3' in content:
    print("Warning: CAT_NAMES_P3 already present in index.html, aborting to prevent duplication.")
    exit(1)

def insert_after(text, anchor, insertion):
    idx = text.find(anchor)
    if idx == -1:
        raise Exception(f"Anchor not found: {anchor[:50]}...")
    end_idx = idx + len(anchor)
    return text[:end_idx] + insertion + text[end_idx:]

# 2. Inject CAT_NAMES_P3 after CAT_NAMES_P2
m = re.search(r'const CAT_NAMES_P2 = \[.*?\];', content)
if not m: raise Exception("CAT_NAMES_P2 not found")
content = insert_after(content, m.group(0), '\n' + cat_names_js)

# 3. Inject SUBTOPICS_P3 after SUBTOPICS_P2
m = re.search(r'const SUBTOPICS_P2\s*=\s*\[[\s\S]*?\n\];', content)
if not m: raise Exception("SUBTOPICS_P2 not found")
content = insert_after(content, m.group(0), '\n\n' + subtopics_js)

# 4. Inject QUESTIONS_P3 after QUESTIONS_P2
m = re.search(r'const QUESTIONS_P2\s*=\s*\[[\s\S]*?\n\];', content)
if not m: raise Exception("QUESTIONS_P2 not found")
content = insert_after(content, m.group(0), '\n\n' + questions_js)

# 5. Inject HARD_QUESTIONS_P3 after HARD_QUESTIONS_P2
m = re.search(r'const HARD_QUESTIONS_P2\s*=\s*\[[\s\S]*?\n\];', content)
if not m: raise Exception("HARD_QUESTIONS_P2 not found")
content = insert_after(content, m.group(0), '\n\n' + hard_questions_js)

# 6. Inject STUDY_CARDS_P3 after STUDY_CARDS_P2
m = re.search(r'const STUDY_CARDS_P2\s*=\s*\[[\s\S]*?\n\];', content)
if not m: raise Exception("STUDY_CARDS_P2 not found")
content = insert_after(content, m.group(0), '\n\n' + study_cards_js)

# 7. Inject MAP_THEMES_P3 after MAP_THEMES_P2
m = re.search(r'const MAP_THEMES_P2\s*=\s*\[[\s\S]*?\n\];', content)
if not m: raise Exception("MAP_THEMES_P2 not found")
content = insert_after(content, m.group(0), '\n\n' + map_themes_js)

# 8. Inject MAP_CONCEPTS_P3 after MAP_CONCEPTS_P2
m = re.search(r'const MAP_CONCEPTS_P2\s*=\s*\[[\s\S]*?\n\];', content)
if not m: raise Exception("MAP_CONCEPTS_P2 not found")
content = insert_after(content, m.group(0), '\n\n' + map_concepts_js)

# 9. Register Prova 3 in PROVAS
p2_provas_anchor = "resumoUrl:'./resumo_prova2.html', pdfUrl:'./prova2sci.pdf'\n  }"
p3_entry = """,
  p3: {
    id:'p3', label:'Prova 3', shortLabel:'P3', icon:'<i class="ph ph-book-bookmark"></i>', ready:true,
    pillLabels:['Epidemiologia','Cárie & ICDNT','Fluorose & Periodontia'],
    catNames:CAT_NAMES_P3, subtopics:SUBTOPICS_P3, questions:QUESTIONS_P3, hardQuestions:HARD_QUESTIONS_P3,
    studyCards:STUDY_CARDS_P3, mapThemes:MAP_THEMES_P3, mapConcepts:MAP_CONCEPTS_P3,
    resumoUrl:'./resumo_prova3.html', pdfUrl:'./conteudos da prova 3/A Epidemiologia em saúde bucal - planejamento e organização 2023.pdf'
  }"""
content = insert_after(content, p2_provas_anchor, p3_entry)

# 10. Add mat-prova-3 in Materials screen
mat2_end_marker = '<!-- Viewer modal for slides/pdfs -->'
mat3_html = """<div class="material-prova" id="mat-prova-3">
        <div class="material-prova-hdr" onclick="_toggleMatProva(3)" role="button" aria-expanded="false">
          <span class="material-prova-icon"><i class="ph ph-clipboard-text"></i></span>
          <span class="material-prova-title">Prova 3</span>
          <span class="material-prova-badge" id="mat-badge-3">8 itens</span>
          <span class="material-prova-arrow" id="mat-arrow-3">›</span>
        </div>
        <div class="material-prova-body" id="mat-body-3" style="display:none">
          <div class="material-item" onclick="_openMaterial('resumo','./resumo_prova3.html','<i class=\\'ph ph-pencil-simple\\'></i> Resumo Completo — Prova 3')">
            <div class="material-item-icon"><i class="ph ph-pencil-simple"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">Resumo Completo — Prova 3</div>
              <div class="material-item-sub">Estudos Epidemiológicos · ICDNT · Índices Cárie/Dean/CPI · Macetes Prof. André</div>
            </div>
            <div class="material-item-type" style="color:#3dd68c">RESUMO</div>
          </div>
          <div class="material-item" onclick="_openMaterial('pdf','./conteudos da prova 3/A Epidemiologia em saúde bucal - planejamento e organização 2023.pdf','Slides — Planejamento e Organização')">
            <div class="material-item-icon"><i class="ph ph-chart-bar"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">Planejamento e Organização — Prof. André</div>
              <div class="material-item-sub">53 slides · Equipe OMS, instrumental, calibração, Kappa</div>
            </div>
            <div class="material-item-type" style="color:#f5a623">PDF</div>
          </div>
          <div class="material-item" onclick="_openMaterial('pdf','./conteudos da prova 3/TIPO DE ESTUDO EPIDEMIOLÓGICO E CRITÉRIOS PARA CLASSIFICAÇÃO - 2026.pdf','Slides — Tipos de Estudos')">
            <div class="material-item-icon"><i class="ph ph-chart-bar"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">Tipos de Estudos Epidemiológicos — Prof. André</div>
              <div class="material-item-sub">35 slides · Transversal, Coorte, Caso-Controle, Ecológico, RR/OR</div>
            </div>
            <div class="material-item-type" style="color:#f5a623">PDF</div>
          </div>
          <div class="material-item" onclick="_openMaterial('pdf','./conteudos da prova 3/cronologia de erupção para levantamentos epidemiológico 2024.pdf','Slides — Cronologia de Erupção')">
            <div class="material-item-icon"><i class="ph ph-chart-bar"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">Cronologia de Erupção — Prof. André</div>
              <div class="material-item-sub">34 slides · Notação FDI, erupção permanente/decídua, regras OMS</div>
            </div>
            <div class="material-item-type" style="color:#f5a623">PDF</div>
          </div>
          <div class="material-item" onclick="_openMaterial('pdf','./conteudos da prova 3/Epidemiologia da cárie - indices utilizados 2024 CPOD CEOD CPOS e ICDNT.pdf','Slides — Índices de Cárie')">
            <div class="material-item-icon"><i class="ph ph-chart-bar"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">Índices de Cárie (CPO-D, ceo-d, CPO-S, ICDAS)</div>
              <div class="material-item-sub">36 slides · 148 superfícies, escores ICDAS 0-6, evolução SB Brasil</div>
            </div>
            <div class="material-item-type" style="color:#f5a623">PDF</div>
          </div>
          <div class="material-item" onclick="_openMaterial('pdf','./conteudos da prova 3/levantamentos epidemiologico da cárie -ICDNT 2026.pdf','Slides — ICDNT')">
            <div class="material-item-icon"><i class="ph ph-chart-bar"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">ICDNT — Condição e Necessidade de Tratamento</div>
              <div class="material-item-sub">76 slides · Códigos 0-9 coroa/raiz, selante, HMI, restaurações</div>
            </div>
            <div class="material-item-type" style="color:#f5a623">PDF</div>
          </div>
          <div class="material-item" onclick="_openMaterial('pdf','./conteudos da prova 3/levantamento epidemiológico FLUOROSE 2026.pdf','Slides — Fluorose')">
            <div class="material-item-icon"><i class="ph ph-chart-bar"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">Fluorose Dentária — Prof. André</div>
              <div class="material-item-sub">79 slides · Índice de Dean 0-5, TF, dose de Burt, diagnóstico diferencial</div>
            </div>
            <div class="material-item-type" style="color:#f5a623">PDF</div>
          </div>
          <div class="material-item" onclick="_openMaterial('pdf','./conteudos da prova 3/levantamentos epidemiologico DOENÇA PERIODONTAL  2025.pdf','Slides — Doença Periodontal')">
            <div class="material-item-icon"><i class="ph ph-chart-bar"></i></div>
            <div class="material-item-body">
              <div class="material-item-title">Doença Periodontal (CPI e PIP) — Prof. André</div>
              <div class="material-item-sub">52 slides · Sonda Trinity 621, sextantes, dentes-índice, dados SB Brasil 2023</div>
            </div>
            <div class="material-item-type" style="color:#f5a623">PDF</div>
          </div>
        </div>
      </div>\n    </div>\n    """
content = content.replace("</div>\n    </div>\n    <!-- Viewer modal for slides/pdfs -->", mat3_html + "<!-- Viewer modal for slides/pdfs -->")

# 11. Update Tutor prompt
focus_p3_code = """  const focusP3=`- Estudos Epidemiológicos e Desenhos de Pesquisa: descritivos x analíticos, observacionais x experimentais, transversal (prevalência, foto instantânea), coorte (incidência, risco relativo, prospectivo), caso-controle (odds ratio, retrospectivo), ecológico (agregação, falácia ecológica), ensaios clínicos randomizados e comunitários.
- Planejamento e Organização de Levantamentos em Saúde Bucal: equipe tríade da OMS (examinador, anotador, monitor), regras e parâmetros (máx 4-5h/dia, ~30 exames/dia, mín 30 espelhos e 30 sondas periodontais Trinity), biossegurança (troca de luvas por paciente), calibração intra/interexaminador (4 etapas: teórica, clínica 6-8 crianças, calibração 15-20 pessoas) e estatística Kappa de Cohen (<0.20 pobre, 0.21-0.40 fraca, 0.41-0.60 moderada, 0.61-0.80 substancial, 0.81-1.00 quase perfeita).
- Cronologia de Erupção e Notação: FDI de dois dígitos (permanentes 1-4, decíduos 5-8), erupção decídua (início 6-8m com centrais inferiores, 20 dentes até 3 anos), 1º molar permanente erupciona aos 6-7 anos atrás dos decíduos sem esfoliação, canino inferior antes dos pré-molares inferiores e canino superior após os pré-molares superiores, meninas 5 meses mais precoces (Moyers). Dente irrompido = tocado pela ponta da sonda; permanente prevalece sobre decíduo no mesmo espaço; supranumerários ignorados.
- Epidemiologia da Cárie e Índices: CPO-D (OMS, permanente, 12 anos idade-chave global), ceo-d (decíduo aos 5 anos, não computa 'p' de perdidos), CPO-S (148 superfícies nos 32 dentes; 5 faces em posteriores perdidos e 4 em anteriores), ICDAS (escores 0 a 6, esmalte seco x úmido, microcavidade e cavidade evidente), metas e evolução SB Brasil (declínio CPO-D e polarização da cárie).
- ICDNT (Índice de Condição Dentária e Necessidade de Tratamento): coroa 0/A hígido a 9/- excluído (banda ortodôntica = 9; braquete = não excluído), raiz 0 hígida a 9 excluída, restauração temporária = cariado (1/B), necessidade de tratamento 0 a 9 (código 7 remineralização mancha branca ativa com flúor, código 8 selante preventivo com 3 critérios clínicos, código 9 dente excluído/sem necessidade).
- Fluorose Dentária: etiologia e fatores de risco, formação do esmalte (pré-eruptiva), dose limite de Burt (0,05-0,07 mg F/kg/dia), ingestão de dentifrício por crianças de 2-3 anos (~48% a 65%), tamanho de grão de arroz cru (0,1g) para <2-3 anos e grão de ervilha (0,3g) após 3 anos, índice de Dean (0 normal a 5 severo com pits, regra dos 2 dentes mais afetados pelo menor escore), índice TF (0 a 9, histopatológico após secagem), IFD comunitário (>0,6 tem relevância de saúde pública).
- Diagnóstico Diferencial do Esmalte: fluorose (bilateral, simétrica, cúspides/bordas, estrias horizontais difusas, mais resistente a ácido) vs mancha branca de cárie (assimétrica, cervical, biofilme, rugosa) vs HMI (molares e incisivos, opacidades demarcadas creme/castanhas, fratura pós-eruptiva) vs Turner (unilateral por abscesso decíduo) vs Tetraciclina (bandas horizontais fluorescentes sob UV) vs Amelogênese Imperfeita (genética generalizada em ambas as dentições).
- Epidemiologia da Doença Periodontal: índice CPI (0 hígido, 1 sangramento, 2 cálculo, 3 bolsa 4-5mm, 4 bolsa 6mm+, X excluído <2 dentes), 6 sextantes, bolsas NÃO registradas abaixo de 15 anos (pseudobolsas de erupção), sonda OMS Trinity 621 (ponta esférica 0,5mm, faixa preta 3,5-5,5mm, força 20g), índice PIP (perda de inserção da JCE à base da bolsa), SB Brasil 2023 (86% dos idosos de 65-74 anos têm sextantes excluídos).
(este é o conteúdo da Prova 3, atualmente selecionada pelo aluno)`;"""

tutor_target = "(este é o conteúdo da Prova 2, atualmente selecionada pelo aluno)`;"
content = insert_after(content, tutor_target, '\n' + focus_p3_code)

# Update return statement of getTutorSystemPrompt
content = content.replace(
    "return base+(currentProva==='p1'?focusP1:focusP2)+rules;",
    "return base+(currentProva==='p1'?focusP1:(currentProva==='p2'?focusP2:focusP3))+rules;"
)

# 12. Update _getTutorTopicMap
topic_p3 = """  if(currentProva==='p3'){
    return {
      'estudo|transversal|coorte|caso-controle|ecol|ecológico|falácia|risco relativo|odds ratio':'Estudos Epidemiológicos',
      'equipe|examinador|anotador|monitor|calibra|kappa|reprodutibilidade|bioética|parâmetros':'Levantamentos e Calibração',
      'erupção|cronologia|fdi|moyers|canino|molar permanente|supranumerário':'Cronologia de Erupção',
      'cpo-d|ceo-d|cpo-s|icdas|sb brasil|polarização':'Índices de Cárie',
      'icdnt|condição dental|hígido|cariado|restaurado|coroa|raiz':'ICDNT — Condição Dental',
      'necessidade de tratamento|selante|remineralização|hmi|faceta|endodontia':'ICDNT — Necessidade',
      'fluorose|burt|ingestão|dentifrício|dean|thylstrup|fejerskov|amelogênese':'Fluorose Dentária',
      'diagnóstico diferencial|mancha branca|turner|tetraciclina|amelogênese imperfeita':'Diagnóstico Diferencial do Esmalte',
      'cpi|pip|periodontal|bolsa|cálculo|sangramento|trinity|sextante':'Epidemiologia Periodontal',
    };
  }
  """
content = content.replace("function _getTutorTopicMap(){\n  if(currentProva==='p2'){", "function _getTutorTopicMap(){\n" + topic_p3 + "if(currentProva==='p2'){")

# 13. Update _encodeDuelId and _decodeDuelId
content = content.replace(
    "const provaBit   = config.prova==='p2'?1:0;",
    "const provaBits  = config.prova==='p3'?2:(config.prova==='p2'?1:0);"
)
content = content.replace(
    "| (provaBit                 << 15);",
    "| (provaBits                << 15);"
)
content = content.replace(
    "const prova     = isLegacy ? 'p1' : (((flags>>15)&1)?'p2':'p1');",
    "const provaVal   = isLegacy ? 0 : ((flags>>15)&3);\n  const prova     = provaVal===2 ? 'p3' : (provaVal===1 ? 'p2' : 'p1');"
)

# 14. Update _qaTestProvaRegistry
qa_registry_old = """    const ok = PROVAS && PROVAS.p1 && PROVAS.p2
      && Array.isArray(PROVAS.p1.questions) && PROVAS.p1.questions.length>0
      && Array.isArray(PROVAS.p2.questions) && PROVAS.p2.questions.length>0
      && PROVAS.p2.ready===true;
    if(ok){_qaPass('prova_registry');_qaLog(`<i class="ph ph-check-circle"></i> PROVAS OK — p1: ${PROVAS.p1.questions.length}q · p2: ${PROVAS.p2.questions.length}q`,'success');}
    else _qaFail('prova_registry','estrutura inesperada em PROVAS (verifique p1/p2/ready)');"""

qa_registry_new = """    const ok = PROVAS && PROVAS.p1 && PROVAS.p2 && PROVAS.p3
      && Array.isArray(PROVAS.p1.questions) && PROVAS.p1.questions.length>0
      && Array.isArray(PROVAS.p2.questions) && PROVAS.p2.questions.length>0
      && Array.isArray(PROVAS.p3.questions) && PROVAS.p3.questions.length>0
      && PROVAS.p2.ready===true && PROVAS.p3.ready===true;
    if(ok){_qaPass('prova_registry');_qaLog(`<i class="ph ph-check-circle"></i> PROVAS OK — p1: ${PROVAS.p1.questions.length}q · p2: ${PROVAS.p2.questions.length}q · p3: ${PROVAS.p3.questions.length}q`,'success');}
    else _qaFail('prova_registry','estrutura inesperada em PROVAS (verifique p1/p2/p3/ready)');"""

content = content.replace(qa_registry_old, qa_registry_new)

# Update line 11311
content = content.replace(
    "if(typeof PROVAS!=='undefined'&&PROVAS.p1&&PROVAS.p2&&PROVAS.p2.ready)_qaPass('prova_registry');",
    "if(typeof PROVAS!=='undefined'&&PROVAS.p1&&PROVAS.p2&&PROVAS.p3&&PROVAS.p2.ready&&PROVAS.p3.ready)_qaPass('prova_registry');"
)

# 15. Write back to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html updated successfully with Prova 3 content and logic!")
