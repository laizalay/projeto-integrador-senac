# 🔗 Nexus PI — Senac

> 🇧🇷 Plataforma web centralizada para submissão, acompanhamento e avaliação dos projetos integradores do Senac.
>
> 🇺🇸 Centralized web platform for submission, tracking and evaluation of Senac's integrative projects.

---

## 🌐 Language / Idioma

- [🇧🇷 Português](#-português)
- [🇺🇸 English](#-english)

---

<br>

# 🇧🇷 Português

## 📋 Sobre o Projeto

O **Nexus PI** é uma plataforma desenvolvida para centralizar e organizar os projetos integradores dos alunos do Senac. O nome *Nexus* representa a conexão entre todos os envolvidos — alunos, professores, coordenadores e empresas parceiras — em um único sistema.

A plataforma substitui o processo atual de envio por e-mail e Teams, eliminando problemas de organização, perda de documentos e dificuldade no controle de versões.

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python 3 | Linguagem principal |
| Django 5 | Framework web (backend) |
| SQLite | Banco de dados local |
| HTML5 + CSS3 + JS | Frontend |
| GitHub | Versionamento de código |
| Render | Hospedagem e deploy automático |

---

## 🗂️ Estrutura do Projeto

```
nexuspi/
├── manage.py                        # Comando principal do Django
├── requirements.txt                 # Dependências Python
├── Procfile                         # Configuração de deploy (Render)
├── build.sh                         # Script de build automático
├── nexuspi/
│   ├── settings.py                  # Configurações do projeto
│   ├── urls.py                      # Rotas globais
│   └── wsgi.py                      # Interface de produção
├── core/
│   ├── models.py                    # Modelos: Usuario, Projeto, Avaliacao
│   ├── views.py                     # Lógica das páginas
│   ├── urls.py                      # Rotas do app
│   ├── forms.py                     # Formulários
│   └── templates/
├── templates/
│   ├── base.html                    # Template base (navbar + footer)
│   ├── home.html                    # Página inicial
│   ├── login.html                   # Tela de login
│   ├── painel.html                  # Painel principal
│   ├── dashboard.html               # Dashboard do coordenador
│   ├── portfolio.html               # Portfólio público (empresas)
│   ├── projeto_form.html            # Criar/editar projeto
│   ├── projeto_detalhe.html         # Detalhes do projeto
│   ├── projeto_avaliar.html         # Avaliação com rubrica
│   ├── usuarios.html                # Lista de usuários
│   ├── usuario_form.html            # Cadastro de usuário
│   ├── usuario_editar.html          # Editar usuário
│   └── usuario_senha.html           # Redefinir senha
└── static/
    └── css/style.css                # Estilos do sistema
```

---

## ⚙️ Como Rodar Localmente

### Pré-requisitos
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/about) — para clonar o repositório
- pip (gerenciador de pacotes, já vem com Python)

### Passo a passo

**1. Clone o repositório**

Abra o terminal na pasta onde deseja salvar o projeto e execute:
```bash
git clone https://github.com/laizalay/projeto-integrador-senac.git
```

**2. Entre na pasta do projeto**
```bash
cd projeto-integrador-senac
```

**3. Instale as dependências**

As dependências são as bibliotecas que o projeto precisa para funcionar:
```bash
pip install -r requirements.txt
```

**4. Execute as migrações do banco de dados**
```bash
python manage.py migrate
```

**5. Crie o administrador inicial**
```bash
python manage.py criar_admin
```

**6. Rode o sistema**
```bash
python manage.py runserver
```

**7. Acesse no navegador:**
```
http://localhost:8000
```

---

## 👥 Papéis de Usuário

| Papel | Permissões |
|---|---|
| **Administrador** | Acesso total. Cadastra, edita e remove usuários. Gerencia todos os projetos. |
| **Coordenador** | Visualiza todos os projetos. Acessa o Dashboard. Cadastra usuários. |
| **Professor** | Visualiza e avalia projetos. Filtra por turma. Registra avaliações com rubrica. |
| **Aluno** | Submete e gerencia seus próprios projetos (CRUD completo). |

---

## 🌐 Páginas do Sistema

| Página | URL | Acesso |
|---|---|---|
| Home | `/` | Público |
| Portfólio | `/portfolio/` | Público (empresas) |
| Login | `/login/` | Público |
| Painel | `/painel/` | Autenticado |
| Dashboard | `/dashboard/` | Admin/Coord |
| Novo Projeto | `/projeto/novo/` | Aluno |
| Avaliar Projeto | `/projeto/<id>/avaliar/` | Professor |
| Usuários | `/usuarios/` | Admin/Coord |
| Admin Django | `/admin/` | Superusuário |

---

## 🔒 LGPD — Lei Geral de Proteção de Dados

O **Nexus PI** foi desenvolvido com atenção aos princípios da **Lei nº 13.709/2018 (LGPD)**:

- **Senhas criptografadas** — todas as senhas são armazenadas com hash seguro pelo Django (PBKDF2 + SHA256). Nenhuma senha é salva em texto puro.
- **Acesso por autenticação** — o sistema exige login para acessar dados de alunos e projetos. Apenas usuários autorizados visualizam informações de outros usuários.
- **Controle de permissões** — cada papel de usuário acessa apenas os dados necessários para sua função (princípio da minimização).
- **Proteção contra CSRF** — todos os formulários utilizam token CSRF nativo do Django, prevenindo ataques de falsificação de requisição.
- **Portfólio com consentimento** — apenas projetos com status "Concluído" ou "Avaliado" aparecem no portfólio público, respeitando o controle do aluno sobre seus dados.
- **Dados institucionais** — o sistema coleta apenas as informações necessárias: nome, e-mail institucional e papel do usuário.

> ⚠️ Para uso em produção com dados reais, recomenda-se implementar uma política de privacidade formal e obter o consentimento explícito dos usuários.

---

## 📅 Fases do Projeto

- [x] **Fase 1** — Painel do Aluno (CRUD + Autenticação)
- [x] **Fase 2** — Painel do Professor (Avaliações + Rubrica) + Dashboard + Portfólio
- [ ] **Fase 3** — Relatórios e exportação de dados
- [ ] **Fase 4** — Perfil do aluno com foto e links
- [ ] **Fase 5** — Notificações e melhorias de UX

---

## 🔮 Próximas Atualizações

- [ ] Upload de arquivos e documentos do projeto
- [ ] Geração de relatórios em PDF para coordenadores
- [ ] Página de perfil com foto, link do GitHub e Curriculum Lattes
- [ ] Filtro avançado no portfólio público
- [ ] Sistema de notificações por e-mail
- [ ] Migração do banco de dados para PostgreSQL
- [ ] Modo escuro na interface

---

## 🏫 Unidades Curriculares e Professor Orientador

| UC | Contribuição para o Projeto | Professor Responsável |
|---|---|---|
| Coding — Linguagens e Técnicas | Implementação das funcionalidades em Python/Django | Prof. Guibson Santana |
| Banco de Dados | Modelagem e CRUD no sistema | Prof. Heuryk Wylk |
| Engenharia de Requisitos | Levantamento de requisitos e documentação SRS (IEEE 830) | Prof. Paulo Pimentel |
| Criatividade | Prototipação e design da interface | Prof. Paulo Pimentel |
| Pesquisa, Tecnologia e Sociedade | Definição do problema e viabilidade | Prof. Guibson Santana |
| Legislação | Proteção de dados (LGPD) e responsabilidade do desenvolvedor | Profª. Renata Cristina |
| Unidade de Extensão | Integração entre disciplinas | Prof. Arnott Ramos |
| Tech English | README bilíngue (PT/EN) | Prof. Leonardo Trevas |

**Professor Orientador:** Prof. Guibson Santana.

---

## 🌐 Deploy

O sistema está publicado em: **[https://projeto-integrador-senac-ng9t.onrender.com](https://projeto-integrador-senac-ng9t.onrender.com)**

Hospedado via [Render.com](https://render.com) com deploy automático a cada push no GitHub.

---

## 👨‍💻 Equipe

| Nome | Função |
|---|---|
| [Arthur Andrey](https://github.com/thurzzinho) | Front-End |
| [Gabriel Tenório](https://github.com/gaahtenorio) | Back-End |
| [Laiza Maria](https://github.com/laizalay) | Full-stack |
| [Luis Bezerra](https://github.com/luissbezerra) | Front-End |
| [Renata Oliveira](https://github.com/srenataoliveira) | Desenvolvimento |

---

## 🏫 Instituição

Desenvolvido como Projeto Integrador do curso de **Análise e Desenvolvimento de Sistemas** — **Senac**, 2026.

---

<br>

---

<br>

# 🇺🇸 English

## 📋 About the Project

**Nexus PI** is a platform developed to centralize and organize integrative projects from Senac students. The name *Nexus* represents the connection between everyone involved — students, teachers, coordinators and partner companies — in a single system.

The platform replaces the current process of submission by email and Teams, eliminating organization problems, document loss and version control difficulties.

---

## 🚀 Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Django 5 | Web framework (backend) |
| SQLite | Local database |
| HTML5 + CSS3 + JS | Frontend |
| GitHub | Version control |
| Render | Hosting and automatic deployment |

---

## 🗂️ Project Structure

```
nexuspi/
├── manage.py                        # Django main command
├── requirements.txt                 # Python dependencies
├── Procfile                         # Deploy configuration (Render)
├── build.sh                         # Automatic build script
├── nexuspi/
│   ├── settings.py                  # Project settings
│   ├── urls.py                      # Global routes
│   └── wsgi.py                      # Production interface
├── core/
│   ├── models.py                    # Models: Usuario, Projeto, Avaliacao
│   ├── views.py                     # Page logic
│   ├── urls.py                      # App routes
│   └── forms.py                     # Forms
└── templates/                       # HTML templates
```

---

## ⚙️ How to Run Locally

### Requirements
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/about) — to clone the repository
- pip (package manager, bundled with Python)

### Step by step

**1. Clone the repository**

Open the terminal in the folder where you want to save the project and run:
```bash
git clone https://github.com/laizalay/projeto-integrador-senac.git
```

**2. Enter the project folder**
```bash
cd projeto-integrador-senac
```

**3. Install the dependencies**

Dependencies are the libraries the project needs to work:
```bash
pip install -r requirements.txt
```

**4. Run the database migrations**
```bash
python manage.py migrate
```

**5. Create the initial administrator**
```bash
python manage.py criar_admin
```

**6. Run the system**
```bash
python manage.py runserver
```

**7. Open in your browser:**
```
http://localhost:8000
```

---

## 👥 User Roles

| Role | Permissions |
|---|---|
| **Administrator** | Full access. Manages users and all projects. |
| **Coordinator** | Views all projects. Accesses Dashboard. Registers users. |
| **Teacher** | Views and evaluates projects. Filters by class. Registers evaluations with rubric. |
| **Student** | Submits and manages their own projects (full CRUD). |

---

## 🔒 Data Protection — LGPD (Brazilian GDPR)

**Nexus PI** was developed following the principles of **Brazilian Law No. 13.709/2018 (LGPD)**:

- **Encrypted passwords** — all passwords are stored with secure hash by Django (PBKDF2 + SHA256). No password is saved as plain text.
- **Authentication-based access** — the system requires login to access student and project data.
- **Permission control** — each user role only accesses the data necessary for their function (data minimization principle).
- **CSRF protection** — all forms use Django's native CSRF token, preventing cross-site request forgery attacks.
- **Portfolio with consent** — only projects with "Completed" or "Evaluated" status appear in the public portfolio.
- **Institutional data only** — the system collects only the necessary information: name, institutional email and user role.

---

## 📅 Project Phases

- [x] **Phase 1** — Student Dashboard (CRUD + Authentication)
- [x] **Phase 2** — Teacher Dashboard (Evaluations + Rubric) + Dashboard + Portfolio
- [ ] **Phase 3** — Reports and data export
- [ ] **Phase 4** — Student profile with photo and links
- [ ] **Phase 5** — Notifications and UX improvements

---

## 🔮 Upcoming Features

- [ ] File and document upload for projects
- [ ] PDF report generation for coordinators
- [ ] Profile page with photo, GitHub link and Lattes Curriculum
- [ ] Advanced filter in public portfolio
- [ ] Email notification system
- [ ] Database migration to PostgreSQL
- [ ] Dark mode interface

---

## 🏫 Curricular Units and Advisor

| Curricular Unit | Contribution to the Project | Advisor Teacher |
|---|---|---|
| Coding — Languages and Techniques | Feature implementation in Python/Django | Teacher Guibson Santana |
| Database | Modeling and CRUD in the system | Teacher Heuryk Wylk |
| Requirements Engineering | Requirements gathering and SRS documentation (IEEE 830) | Teacher Paulo Pimentel |
| Creativity | Interface prototyping and design | Teacher Paulo Pimentel |
| Research, Technology and Society | Problem definition and feasibility | Teacher Guibson Santana |
| Legislation | Data protection (LGPD) and developer responsibility | Teacher Renata Cristina |
| Extension Unit | Integration between disciplines | Teacher Arnott Ramos |
| Tech English | Bilingual README (PT/EN) | Teacher Leonardo Trevas |

**Advisor Teacher:** Teacher Guibson Santana.

---

## 🌐 Live Demo

The system is published at: **[https://projeto-integrador-senac-ng9t.onrender.com](https://projeto-integrador-senac-ng9t.onrender.com)**

Hosted on [Render.com](https://render.com) with automatic deployment on every GitHub push.

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| [Arthur Andrey](https://github.com/thurzzinho) | Front-End |
| [Gabriel Tenório](https://github.com/gaahtenorio) | Back-End |
| [Laiza Maria](https://github.com/laizalay) | Full-Stack |
| [Luis Bezerra](https://github.com/luissbezerra) | Front-End |
| [Renata Oliveira](https://github.com/srenataoliveira) | Development |

---

## 🏫 Institution

Developed as an Integrative Project for the **Analysis and Systems Development** program — **Senac**, 2026.
