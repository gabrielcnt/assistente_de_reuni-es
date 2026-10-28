# Assistente de Transcrições

Aplicação CLI desenvolvida em Python que transforma gravações de reuniões em **transcrições, resumos técnicos e documentos PDF**, utilizando a API da OpenAI.

O projeto automatiza a análise de reuniões para identificar decisões, solicitações de alterações, novas funcionalidades e tarefas de desenvolvimento. O prompt de análise é direcionado principalmente a reuniões sobre dashboards em Streamlit, análise de dados, métricas, gráficos, filtros, tabelas e funcionalidades de sistemas.

## Funcionalidades

- **Transcrição de áudio:** converte arquivos MP3 em texto utilizando a API de transcrição da OpenAI.
- **Análise de reuniões com IA:** gera resumos estruturados a partir das transcrições.
- **Identificação de tarefas:** organiza as ações de desenvolvimento identificadas durante a reunião em uma lista de tarefas com caixas de seleção Markdown.
- **Geração de relatórios:** salva os resumos em Markdown e PDF.
- **Processamento de áudios segmentados:** combina as transcrições de diferentes partes de uma mesma gravação.
- **Organização automática dos resultados:** gera arquivos com nomes baseados na data e no horário de execução.
- **Verificação de acesso à API:** disponibiliza um script para verificar o carregamento da chave e o acesso à API da OpenAI.

## Como funciona

O fluxo de execução é dividido em etapas:

1. **Verificação de transcrições existentes:** o programa procura arquivos `.txt` no diretório `transcricoes/`. Se encontrar algum, utiliza a transcrição mais recente segundo o nome do arquivo e não realiza uma nova transcrição de áudio naquela execução.
2. **Transcrição de áudio:** se não houver uma transcrição existente, o programa procura arquivos MP3 em `audio/partes/` e envia cada parte à API de transcrição.
3. **Consolidação:** os textos das partes são combinados e salvos em um único arquivo de transcrição.
4. **Análise com IA:** a transcrição é enviada à API da OpenAI para produzir um resumo técnico estruturado conforme as instruções definidas em `prompt.py`.
5. **Geração dos resultados:** o resumo é salvo em Markdown e convertido em PDF.

> **Importante:** o projeto não divide gravações de áudio automaticamente. Os arquivos MP3 precisam estar previamente segmentados e organizados no diretório de entrada.

## Estrutura do resumo

A análise gerada pela IA segue uma estrutura definida em `prompt.py`:

- **Resumo Executivo:** visão geral dos principais assuntos e resultados da reunião.
- **Alterações Solicitadas:** modificações solicitadas durante a reunião.
- **Novas Funcionalidades:** funcionalidades propostas ou discutidas.
- **Melhorias de Dashboard:** melhorias relacionadas à visualização e interação com dashboards.
- **Melhorias de Dados e Métricas:** ajustes em dados, indicadores e métricas.
- **Correções:** problemas identificados que precisam ser corrigidos.
- **Decisões Tomadas:** decisões registradas durante a reunião.
- **Tasks para Desenvolvimento:** tarefas identificadas, organizadas em uma lista de itens com caixas de seleção Markdown.

O prompt orienta a análise para os assuntos relevantes ao desenvolvimento de sistemas, evitando dar destaque a conversas sem relação com esse objetivo.

## Tecnologias e requisitos

- **Python 3.10 ou superior**
- **API da OpenAI**
  - `gpt-4o-mini-transcribe` para transcrição de áudio.
  - `gpt-4.1-mini` para análise e elaboração dos resumos.
- **Conexão com a internet**
- **Chave de API válida**, com acesso aos modelos utilizados pelo projeto.

O uso da API pode gerar custos, dependendo do volume de áudio processado e das solicitações realizadas.

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/gabrielcnt/assistente_de_reuni-es.git
cd assistente_de_reuni-es
```

### 2. Crie e ative um ambiente virtual

**Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

### 4. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto:

```dotenv
OPENAI_API_KEY=sua_chave_da_openai
```

Substitua `sua_chave_da_openai` pela sua chave de API válida.

**Segurança:** não compartilhe sua chave de API nem envie o arquivo `.env` para o repositório. O arquivo está incluído no `.gitignore` para evitar o versionamento acidental das credenciais.

## Preparação dos áudios

Coloque os arquivos MP3 previamente segmentados no diretório `audio/partes/`.

Exemplo:

```text
audio/
└── partes/
    ├── parte_000.mp3
    ├── parte_001.mp3
    └── parte_002.mp3
```

Os arquivos são processados em ordem alfabética. Por isso, recomenda-se utilizar nomes com numeração preenchida com zeros, como `parte_001.mp3` e `parte_010.mp3`, para preservar a ordem esperada.

O diretório `audio/partes/` precisa existir antes da execução.

## Executando o projeto

Na raiz do projeto, com o ambiente virtual ativado e a chave da API configurada, execute:

```bash
python main.py
```

O programa seguirá o fluxo de transcrição, análise e geração dos arquivos, conforme a disponibilidade de transcrições existentes e de arquivos de áudio.

### Processar uma nova reunião

Se o diretório `transcricoes/` já contiver um arquivo `.txt`, o programa utilizará a transcrição mais recente segundo o nome do arquivo, sem processar os novos áudios naquela execução.

Para processar uma nova reunião, mova ou arquive a transcrição anterior para fora de `transcricoes/` antes de executar o programa novamente.

## Arquivos gerados

Os resultados são organizados em três diretórios:

```text
transcricoes/
└── transcricao_AAAAMMDD_HHMMSS.txt

resumos/
└── resumo_AAAAMMDD_HHMMSS.md

pdfs/
└── resumo_AAAAMMDD_HHMMSS.pdf
```

Os nomes incluem a data e o horário de execução para facilitar a identificação dos resultados.

Os diretórios de saída são criados automaticamente quando necessário.

### Transcrição `.txt`

Contém o texto consolidado a partir dos arquivos de áudio processados.

### Resumo `.md`

Contém a análise estruturada da reunião, seguindo as seções definidas em `prompt.py`. O formato Markdown facilita a leitura, a edição e o acompanhamento das tarefas identificadas.

### Relatório `.pdf`

Contém uma versão em PDF do resumo gerado, facilitando o compartilhamento e a consulta do documento.

**Observação:** a data exibida no cabeçalho do resumo corresponde à data de execução do programa, e não necessariamente à data em que a reunião aconteceu.

## Estrutura do projeto

```text
.
├── config.py          # Carrega a chave da API a partir do .env
├── main.py            # Orquestra o processamento e a geração dos resultados
├── pdf_generator.py   # Converte o resumo em Markdown para PDF
├── prompt.py          # Define o formato e o escopo da análise
├── requirements.txt   # Dependências Python
├── test_api.py        # Verificação manual de acesso à API
├── audio/
│   └── partes/        # Partes MP3 de entrada
├── transcricoes/      # Transcrições geradas
├── resumos/           # Resumos em Markdown
└── pdfs/              # Resumos em PDF
```

## Verificação da API

O projeto inclui o script `test_api.py`, que permite verificar o carregamento da chave e o acesso à API da OpenAI.

Execute:

```bash
python test_api.py
```

O script realiza uma verificação manual de acesso e lista os modelos disponíveis conforme o acesso da conta.

Essa verificação **não substitui uma suíte de testes automatizados** nem garante, por si só, que todas as etapas do processamento funcionarão corretamente.

## Limitações conhecidas

- A aplicação é executada pela linha de comando (CLI).
- Os arquivos de áudio precisam estar previamente segmentados em partes MP3.
- Quando já existe uma transcrição `.txt` em `transcricoes/`, o programa reutiliza a mais recente pelo nome do arquivo, em vez de transcrever novos áudios.
- A qualidade dos resumos depende da clareza da gravação, da transcrição obtida e do conteúdo discutido na reunião.
- O processamento depende da disponibilidade da API da OpenAI, de uma conexão com a internet e de uma chave válida com acesso aos modelos utilizados.
- A data registrada no cabeçalho do resumo é a data de execução do programa, não uma data extraída do conteúdo da reunião.

## Possíveis evoluções

Algumas melhorias que podem ser consideradas em versões futuras:

- Automatizar a divisão de gravações longas em partes menores.
- Permitir selecionar explicitamente os arquivos de áudio que serão processados.
- Adicionar testes automatizados para as principais etapas do processamento.
- Melhorar o tratamento de erros e o acompanhamento do progresso da execução.
- Permitir configurar o escopo e o formato dos resumos sem alterar diretamente o prompt.

---