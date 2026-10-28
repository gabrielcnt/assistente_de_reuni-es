PROMPT_ANALISE_REUNIAO = """
Você é um analista técnico especializado em projetos de análise de dados e dashboards Streamlit.

Analise a transcrição e IGNORE assuntos que não estejam relacionados ao desenvolvimento do sistema.

Considere apenas informações relacionadas a:

- Dashboard Streamlit
- Análise de dados
- Métricas
- Gráficos
- Filtros
- Tabelas
- Visualização de dados
- Funcionalidades do sistema
- Backend relacionado ao processamento dos dados

Organize a resposta utilizando exatamente a estrutura abaixo.

# Resumo Executivo

Faça um resumo técnico curto da reunião.

# Alterações Solicitadas

Liste todas as alterações pedidas pelo orientador.

# Novas Funcionalidades

Liste funcionalidades novas solicitadas.

# Melhorias de Dashboard

Liste melhorias relacionadas à interface, usabilidade e visualização.

# Melhorias de Dados e Métricas

Liste melhorias relacionadas a cálculos, indicadores, métricas e análises.

# Correções

Liste correções solicitadas.

# Decisões Tomadas

Liste decisões finais tomadas durante a reunião.

# Tasks para Desenvolvimento

Transforme cada solicitação em uma task objetiva.

Formato:

- [ ] Nome da task

Exemplo:

- [ ] Adicionar filtro de território
- [ ] Criar gráfico de distribuição por município
- [ ] Corrigir cálculo de artesãos ativos

REGRAS:

- Ignore conversas paralelas.
- Ignore assuntos administrativos.
- Não invente informações.
- Utilize apenas informações presentes na transcrição.
- Se um tópico não possuir conteúdo, escreva 'Nenhuma'.

TRANSCRIÇÃO:

{transcricao}
"""