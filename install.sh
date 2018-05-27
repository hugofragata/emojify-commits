wget https://raw.githubusercontent.com/hugofragata/emojify-commits/master/emojify.py
wget https://raw.githubusercontent.com/hugofragata/emojify-commits/master/emoji.json
cp emoji.json ./.git/hooks/
cp emojify.py ./.git/hooks/prepare-commit-msg
chmod +x ./.git/hooks/prepare-commit-msg
rm emoji.json emojify.py
