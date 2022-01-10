# Tutorial MDN Django

O objetivo é desenvolver um sistema web para o gerenciamento de uma biblioteca.

## Requerimentos

- Python 3 ou superior

## Para utilizar o projeto

Utilize os códigos abaixo na linha de comando adaptando para seu sistema:

```
git clone https://github.com/Acacio-coding/tutotrialMDNDjango.git
```

```
cd mdn
```

```
python3 -m venv <nome da sua venv>
```

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

```
python3 manage.py collectstatic
```

```
python3 manage.py migrate
```

Obs.: Não esqueça de configurar o settings.py gerado dentro de "<b>locallibrary</b>" para atender aos seus requisitos.

## Para iniciar o servidor local

```
python3 manage.py runserver
```
