apt update && apt upgrade -y

pkg install git

pkg install python
rm -rf CALL-BOMBER
git clone --depth=1 https://github.com/U7P4L-IN/CALL-BOMBER.git

cd CALL-BOMBER

python BOMBER.py