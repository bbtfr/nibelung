PyInstaller='../pyinstaller-2.0/pyinstaller.py'
python $PyInstaller -F app/app.py
rm -rf dist/plugins
cp -r plugins dist
cp app/lib/plugin.py dist/plugins
python app/db_seed.py
rm -rf dist/db
cp -r db dist