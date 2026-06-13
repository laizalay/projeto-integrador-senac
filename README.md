# 🔗 Nexus PI — Senac

> 🇧🇷 Plataforma web centralizada para submissão, acompanhamento e avaliação dos projetos integradores do Senac.
>
> 🇺🇸 Centralized web platform for submission, tracking and evaluation of Senac's integrative projects.

[![Licensa](https://img.shields.io/badge/license-MIT-green)](https://mit-license.org/)
[![Instituição](https://img.shields.io/badge/Institution-Senac-blue)](https://www.pe.senac.br/)
[![LGPD](https://img.shields.io/badge/Compliance-LGPD%20Ready-blueviolet)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
[![Django](https://img.shields.io/badge/Backend-Django%205-092E20)](https://www.djangoproject.com/)
[![Deploy](https://img.shields.io/badge/Deploy-Render-46E3B7)](https://render.com)

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

### Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
PYTHON_VERSION=3.11.0
```

> ⚠️ Nunca compartilhe o arquivo `.env` publicamente. Ele já está incluído no `.gitignore`.

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

**5. Crie os usuários iniciais**

Este comando cria automaticamente os usuários de demonstração e dois projetos de exemplo:
```bash
python manage.py criar_admin
```

### Credenciais de demonstração

| Papel | Usuário | Senha |
|---|---|---|
| Administrador | admin | admin123 |
| Coordenador | coordenador | coord123 |
| Professor | professor | prof123 |
| Aluno (Maria Silva) | aluno1 | aluno123 |
| Aluno (João Santos) | aluno2 | aluno123 |

> ⚠️ Altere as senhas após o primeiro acesso em ambiente de produção.

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
| **Administrador** | Acesso total. Cadastra, edita e remove usuários. Gerencia todos os projetos. Redefine senhas. |
| **Coordenador** | Visualiza todos os projetos. Acessa o Dashboard. Cadastra e edita usuários. |
| **Professor** | Visualiza projetos, filtra por turma e registra avaliações com rubrica. |
| **Aluno** | Submete e gerencia seus próprios projetos (CRUD completo). |

---

## 🌐 Páginas e Rotas do Sistema

| Método | Página / URL | Descrição | Acesso |
|---|---|---|---|
| GET | `/` | Página inicial com vitrine de projetos | Público |
| GET | `/portfolio/` | Portfólio público de projetos concluídos | Público (empresas) |
| GET/POST | `/login/` | Autenticação de usuários | Público |
| POST | `/logout/` | Encerramento de sessão | Autenticado |
| GET | `/painel/` | Painel principal com lista de projetos | Autenticado |
| GET | `/dashboard/` | Dashboard com estatísticas gerais | Admin/Coord |
| GET/POST | `/projeto/novo/` | Submissão de novo projeto | Aluno |
| GET | `/projeto/<id>/` | Visualização de detalhes do projeto | Autenticado |
| GET/POST | `/projeto/<id>/editar/` | Edição de projeto | Aluno (dono) |
| POST | `/projeto/<id>/excluir/` | Exclusão de projeto | Aluno/Admin |
| GET/POST | `/projeto/<id>/avaliar/` | Avaliação com rubrica | Professor |
| GET | `/usuarios/` | Lista de usuários cadastrados | Admin/Coord |
| GET/POST | `/usuarios/novo/` | Cadastro de novo usuário | Admin/Coord |
| GET/POST | `/usuarios/<id>/editar/` | Edição de dados do usuário | Admin/Coord |
| GET/POST | `/usuarios/<id>/senha/` | Redefinição de senha | Admin |
| GET | `/admin/` | Painel administrativo Django | Superusuário |

---

## 🔒 LGPD — Lei Geral de Proteção de Dados

O **Nexus PI** foi desenvolvido com atenção aos princípios da **Lei nº 13.709/2018 (LGPD)**:

- **Senhas criptografadas** — todas as senhas são armazenadas com hash seguro pelo Django (PBKDF2 + SHA256). Nenhuma senha é salva em texto puro.
- **Acesso por autenticação** — o sistema exige login para acessar dados de alunos e projetos. Apenas usuários autorizados visualizam informações de outros usuários.
- **Controle de permissões** — cada papel de usuário acessa apenas os dados necessários para sua função (princípio da minimização).
- **Proteção contra CSRF** — todos os formulários utilizam token CSRF nativo do Django, prevenindo ataques de falsificação de requisição.
- **Portfólio com consentimento** — apenas projetos com status "Concluído" ou "Avaliado" aparecem no portfólio público, respeitando o controle do aluno sobre seus dados.
- **Dados institucionais** — o sistema coleta apenas as informações necessárias: nome, e-mail institucional, papel e turma do usuário.

> ⚠️ Para uso em produção com dados reais, recomenda-se implementar uma política de privacidade formal e obter o consentimento explícito dos usuários.

---

## 📅 Fases do Projeto

- [x] **Fase 1** — Painel do Aluno (CRUD + Autenticação)
- [x] **Fase 2** — Painel do Professor (Avaliações + Rubrica) + Dashboard + Portfólio Público
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

| Nome | GitHub |
|---|---|
| Arthur Andrey — Front-End | [@thurzzinho](https://github.com/thurzzinho) |
| Gabriel Tenório — Back-End | [@gaahtenorio](https://github.com/gaahtenorio) |
| Laiza Maria — Full-Stack | [@laizalay](https://github.com/laizalay) |
| Luis Bezerra — Front-End | [@luissbezerra](https://github.com/luissbezerra) |
| Renata Oliveira — Desenvolvimento | [@srenataoliveira](https://github.com/srenataoliveira) |

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

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
PYTHON_VERSION=3.11.0
```

> ⚠️ Never share your `.env` file publicly. It is already included in `.gitignore`.

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

**5. Create the initial users**

This command automatically creates demo users and two sample projects:
```bash
python manage.py criar_admin
```

### Demo credentials

| Role | Username | Password |
|---|---|---|
| Administrator | admin | admin123 |
| Coordinator | coordenador | coord123 |
| Teacher | professor | prof123 |
| Student (Maria Silva) | aluno1 | aluno123 |
| Student (João Santos) | aluno2 | aluno123 |

> ⚠️ Change passwords after first access in a production environment.

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
| **Administrator** | Full access. Manages users and all projects. Resets passwords. |
| **Coordinator** | Views all projects. Accesses Dashboard. Registers and edits users. |
| **Teacher** | Views and evaluates projects. Filters by class. Registers evaluations with rubric. |
| **Student** | Submits and manages their own projects (full CRUD). |

---

## 🌐 System Pages and Routes

| Method | Page / URL | Description | Access |
|---|---|---|---|
| GET | `/` | Home page with project showcase | Public |
| GET | `/portfolio/` | Public portfolio of completed projects | Public (companies) |
| GET/POST | `/login/` | User authentication | Public |
| POST | `/logout/` | Session termination | Authenticated |
| GET | `/painel/` | Main dashboard with project list | Authenticated |
| GET | `/dashboard/` | Statistics overview dashboard | Admin/Coord |
| GET/POST | `/projeto/novo/` | Submit new project | Student |
| GET | `/projeto/<id>/` | Project detail view | Authenticated |
| GET/POST | `/projeto/<id>/editar/` | Edit project | Student (owner) |
| POST | `/projeto/<id>/excluir/` | Delete project | Student/Admin |
| GET/POST | `/projeto/<id>/avaliar/` | Evaluate with rubric | Teacher |
| GET | `/usuarios/` | List of registered users | Admin/Coord |
| GET/POST | `/usuarios/novo/` | Register new user | Admin/Coord |
| GET/POST | `/usuarios/<id>/editar/` | Edit user data | Admin/Coord |
| GET/POST | `/usuarios/<id>/senha/` | Reset user password | Admin |
| GET | `/admin/` | Django admin panel | Superuser |

---

## 🔒 Data Protection — LGPD (Brazilian GDPR)

**Nexus PI** was developed following the principles of **Brazilian Law No. 13.709/2018 (LGPD)**:

- **Encrypted passwords** — all passwords are stored with secure hash by Django (PBKDF2 + SHA256). No password is saved as plain text.
- **Authentication-based access** — the system requires login to access student and project data.
- **Permission control** — each user role only accesses the data necessary for their function (data minimization principle).
- **CSRF protection** — all forms use Django's native CSRF token, preventing cross-site request forgery attacks.
- **Portfolio with consent** — only projects with "Completed" or "Evaluated" status appear in the public portfolio.
- **Institutional data only** — the system collects only the necessary information: name, institutional email, role and class.

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

| Curricular Unit | Contribution to the Project | Instructor |
|---|---|---|
| Coding — Languages and Techniques | Feature implementation in Python/Django | Prof. Guibson Santana |
| Database | Modeling and CRUD in the system | Prof. Heuryk Wylk |
| Requirements Engineering | Requirements gathering and SRS documentation (IEEE 830) | Prof. Paulo Pimentel |
| Creativity | Interface prototyping and design | Prof. Paulo Pimentel |
| Research, Technology and Society | Problem definition and feasibility | Prof. Guibson Santana |
| Legislation | Data protection (LGPD) and developer responsibility | Prof. Renata Cristina |
| Extension Unit | Integration between disciplines | Prof. Arnott Ramos |
| Tech English | Bilingual README (PT/EN) | Prof. Leonardo Trevas |

**Advisor Teacher:** Prof. Guibson Santana.

---

## 🌐 Live Demo

The system is published at: **[https://projeto-integrador-senac-ng9t.onrender.com](https://projeto-integrador-senac-ng9t.onrender.com)**

Hosted on [Render.com](https://render.com) with automatic deployment on every GitHub push.

---

## 👨‍💻 Team

| Name | GitHub |
|---|---|
| Arthur Andrey — Front-End | [@thurzzinho](https://github.com/thurzzinho) |
| Gabriel Tenório — Back-End | [@gaahtenorio](https://github.com/gaahtenorio) |
| Laiza Maria — Full-Stack | [@laizalay](https://github.com/laizalay) |
| Luis Bezerra — Front-End | [@luissbezerra](https://github.com/luissbezerra) |
| Renata Oliveira — Development | [@srenataoliveira](https://github.com/srenataoliveira) |

---

## 🏫 Institution

Developed as an Integrative Project for the **Analysis and Systems Development** program — **Senac**, 2026.
