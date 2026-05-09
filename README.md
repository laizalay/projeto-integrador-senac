# 🔭 Observatório de Projetos Integradores — Senac

> 🇧🇷 Sistema web para submissão, acompanhamento e avaliação dos projetos integradores da instituição.
>
> 🇺🇸 Web system for submission, tracking and evaluation of the institution's integrative projects.

---

## 🌐 Language / Idioma

- [🇧🇷 Português](#-português)
- [🇺🇸 English](#-english)

---

<br>

# 🇧🇷 Português

## 📋 Sobre o Projeto

O **Observatório de Projetos Integradores** é uma plataforma desenvolvida para centralizar e organizar os projetos integradores dos alunos do Senac. A plataforma permite que alunos submetam seus projetos, coordenadores acompanhem as entregas e gerem relatórios, professores realizem avaliações e empresas identifiquem novos talentos — tudo dentro de um único sistema.

### Funcionalidades da Fase 1

- ✅ Página inicial (Home) com estatísticas do sistema
- ✅ Sistema de autenticação com login seguro
- ✅ Cadastro de usuários realizado apenas pelo Administrador/Coordenador
- ✅ Painel do Aluno com CRUD completo de projetos
  - **Create** — Submeter um novo projeto
  - **Read** — Visualizar projetos e detalhes
  - **Update** — Editar informações e status
  - **Delete** — Excluir projeto

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python 3 | Linguagem principal |
| Flask | Framework web (backend) |
| SQLAlchemy | ORM — comunicação da linguagem Python com o banco de dados |
| SQLite | Banco de dados local |
| Jinja2 | Templates HTML (incluso no Flask) |
| HTML5 + CSS3 | Frontend |
| JavaScript | Interatividade no frontend |

---

## 🗂️ Estrutura do Projeto

```
observatorio/
├── app.py                    # Arquivo principal: rotas, modelos e lógica
├── requirements.txt          # Dependências Python
├── Procfile                  # Configuração para deploy (Render)
├── instance/
│   └── observatorio.db       # Banco de dados SQLite (gerado automaticamente)
├── static/
│   ├── css/
│   │   └── style.css         # Estilos do sistema
│   └── js/
│       └── main.js           # JavaScript
└── templates/
    ├── base.html             # Template base (navbar + footer)
    ├── home.html             # Página inicial
    ├── login.html            # Tela de login
    ├── painel.html           # Painel do aluno
    ├── projeto_form.html     # Formulário criar/editar projeto
    ├── projeto_detalhe.html  # Detalhes do projeto
    ├── usuarios.html         # Lista de usuários (admin/coord)
    └── usuario_form.html     # Cadastro de usuário
```

---

## ⚙️ Como Rodar Localmente

### Pré-requisitos
- [Python 3.10+](https://www.python.org/downloads/)
- pip (gerenciador de pacotes, já vem com Python)

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/laizalay/projeto-integrador-senac.git

# 2. Entre na pasta
cd observatorio

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode o sistema
python app.py
```

Acesse no navegador: **http://localhost:5000**

### Credenciais iniciais

| Papel | E-mail | Senha |
|---|---|---|
| Administrador | admin@senac.br | admin123 |

> ⚠️ Altere a senha do administrador após o primeiro acesso.

---

## 👥 Papéis de Usuário

| Papel | Permissões |
|---|---|
| **Administrador** | Acesso total, cadastra usuários |
| **Coordenador** | Acessa todos os projetos, cadastra usuários |
| **Aluno** | Gerencia apenas seus próprios projetos |

---

## 🌐 Deploy

O sistema está publicado em: **https://projeto-integrador-senac-ng9t.onrender.com**

Hospedado via [Render.com](https://render.com).

---

## 📅 Fases do Projeto

- [x] **Fase 1** — Painel do Aluno (CRUD + Autenticação)
- [ ] **Fase 2** — Painel do Professor (Avaliações)
- [ ] **Fase 3** — Painel do Coordenador (Visão geral)
- [ ] **Fase 4** — Portfólio público + Consulta por empresas

---

## 👨‍💻 Equipe

| Nome | Função |
|---|---|
| [Arthur Andrey] https://github.com/thurzzinho | Front-End |
| [Gabriel Tenório] https://github.com/gaahtenorio | Desenvolvimento |
| [Laiza Maria] https://github.com/laizalay | Back-End | 
| [Luis Bezerra] https://github.com/luissbezerra | Desenvolvimento |
| [Renata Oliveira] https://github.com/srenataoliveira | Desenvolvimento |

---

## 🏫 Instituição

Desenvolvido como Projeto Integrador do curso de **Análise e Desenvolvimento de Sistemas** — **Faculdade Senac**, 2026.

---

<br>

---

<br>

# 🇺🇸 English

## 📋 About the Project

The **Integrative Projects Observatory** is a platform developed to centralize and organize integrative projects from Senac students. The platform allows students to submit their projects, coordinators to track deliverables and generate reports, teachers to conduct evaluations, and companies to identify new talents — all within a single system.

### Phase 1 Features

- ✅ Home page with system statistics
- ✅ Secure login authentication system
- ✅ User registration restricted to Administrator/Coordinator only
- ✅ Student Dashboard with full project CRUD
  - **Create** — Submit a new project
  - **Read** — View projects and details
  - **Update** — Edit information and status
  - **Delete** — Remove a project

---

## 🚀 Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Flask | Web framework (backend) |
| SQLAlchemy | ORM — database communication |
| SQLite | Local database |
| Jinja2 | HTML templates (included with Flask) |
| HTML5 + CSS3 | Frontend |
| JavaScript | Frontend interactivity |

---

## 🗂️ Project Structure

```
observatorio/
├── app.py                    # Main file: routes, models and logic
├── requirements.txt          # Python dependencies
├── Procfile                  # Deploy configuration (Render)
├── instance/
│   └── observatorio.db       # SQLite database (auto-generated)
├── static/
│   ├── css/
│   │   └── style.css         # System styles
│   └── js/
│       └── main.js           # JavaScript
└── templates/
    ├── base.html             # Base template (navbar + footer)
    ├── home.html             # Home page
    ├── login.html            # Login screen
    ├── painel.html           # Student dashboard
    ├── projeto_form.html     # Create/edit project form
    ├── projeto_detalhe.html  # Project details
    ├── usuarios.html         # User list (admin/coord)
    └── usuario_form.html     # User registration
```

---

## ⚙️ How to Run Locally

### Requirements
- [Python 3.10+](https://www.python.org/downloads/)
- pip (package manager, bundled with Python)

### Step by step

```bash
# 1. Clone the repository
git clone https://github.com/laizalay/projeto-integrador-senac.git

# 2. Enter the folder
cd observatorio

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the system
python app.py
```

Open in your browser: **http://localhost:5000**

### Default credentials

| Role | E-mail | Password |
|---|---|---|
| Administrator | admin@senac.br | admin123 |

> ⚠️ Change the administrator password after first access.

---

## 👥 User Roles

| Role | Permissions |
|---|---|
| **Administrator** | Full access, manages users |
| **Coordinator** | Views all projects, manages users |
| **Student** | Manages their own projects only |

---

## 🌐 Live Demo

The system is published at: **https://projeto-integrador-senac-ng9t.onrender.com**

Hosted on [Render.com](https://render.com).

---

## 📅 Project Phases

- [x] **Phase 1** — Student Dashboard (CRUD + Authentication)
- [ ] **Phase 2** — Teacher Dashboard (Evaluations)
- [ ] **Phase 3** — Coordinator Dashboard (Overview)
- [ ] **Phase 4** — Public Portfolio + Partner Company Access

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| [Arthur Andrey] | Front-End |
| [Gabriel Tenório] | Development |
| [Laiza Maria] | Back-End |
| [Luis Bezerra] | Development |
| [Renata Oliveira] | Development |

---

## 🏫 Institution

Developed as an Integrative Project for the **Analysis and Systems Development** program — **Senac College**, 2026.
