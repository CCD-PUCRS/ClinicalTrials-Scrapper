# ClinicalTrials-Scrapper
**Scrapper para obter informações do Clinical Trials e outros sites através de LLM**

Scrapper para coletar informações de sites, como o Clinical Trials, e através da [roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) (LLM para perguntas-repostas) executado localmente obter os requisitos de estudos clínicos e informações a partir de dados não-estruturados em texto livre.

Em um primeiro momento a ferramenta solicita uma fonte de dados.
Atualmente é capaz de acessar os requerimentos do Clinical Trials, textos da Wikipedia sobre um termo, e sites sem uma estrutura específica.
Em um segundo momento esses dados são lidos pelo LLM que é capaz de responder perguntas sobre o estudo.
No futuro é esperado que um conjunto de perguntas seja usado para obter dados estruturados a partir das respostas do LLM, acessando diversos estudos ou fontes de dados online automaticamente.

Dados do Clinical Trials são obtidos pela [API](https://classic.clinicaltrials.gov/api/gui) em JSON, dados da Wikipedia pela biblioteca [wikipedia](https://pypi.org/project/wikipedia/), e dados em de links em HTML são processados pelo biblioteca [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).

O comando para execução do scrapper/LLM é:
```Sh
python scrapper_llm.py
```
