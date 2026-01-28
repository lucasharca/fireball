# Project Fireball API

Projeto inicial de uma API para auxiliar jogos de RPG (começando por D&D), desenvolvida em **Python** usando **FastAPI**.

---

## 📦 Requisitos

* Python **3.10+**
* `pip`

---

## 🧪 Criando e ativando o ambiente virtual

Na raiz do projeto:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\activate
```

Quando ativo, o terminal mostrará algo como:

```text
(.venv) $
```

---

## 📥 Instalando dependências

Com o ambiente virtual ativo:

```bash
pip install fastapi uvicorn
```

(Opcional, mas recomendado)

```bash
pip freeze > requirements.txt
```

---

## ▶️ Executando a aplicação com Uvicorn

Na raiz do projeto, execute:

```bash
uvicorn app.main:app --reload
```

### O que esse comando faz:

* `app.main` → caminho do arquivo `main.py`
* `app` → instância do FastAPI criada no arquivo
* `--reload` → reinicia automaticamente ao salvar alterações (modo desenvolvimento)

Se tudo estiver correto, você verá algo como:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Acessando a API

### Endpoint de teste (Dice)

Abra no navegador:

```
http://127.0.0.1:8000/dice
```

Resposta esperada:

```json
{
  "message": "Hello Dice!"
}
```

---

## 📚 Documentação automática (Swagger)

FastAPI gera documentação automaticamente.

Acesse:

```
http://127.0.0.1:8000/docs
```

Ou a documentação alternativa:

```
http://127.0.0.1:8000/redoc
```

---

## 🗺️ Estrutura do projeto (atual)

```text
app/
 ├── main.py
 └── api/
      └── routes/
           └── dice.py
```

---

## 🚀 Próximos passos

* Implementar rolagem de dados real (ex: `1d20`, `2d6+3`)
* Adicionar validação de entrada
* Criar testes
* Persistência de histórico de rolagens

---

⚔️ *Projeto em estágio inicial — construído passo a passo.*
