# Nibelung
========

Nibelung is a Linux safety testing tool with GUI interface, which is writing in python.

With nibelung, you can:
* Detect security vulnerabilities
* Audit (Logs)
* Authentication

It's based on sqlalchemy(ORM) & pyqt(GUI), and can be packaged by pyinstaller.

Install
--------

```bash
git clone git://github.com/bbtfr/nibelung.git
cd nibelung

apt-get install python-qt4
pip install sqlalchemy

./main.py
```

Package
--------

```bash
cd nibelung
pyinstaller -F app/app.py
```
