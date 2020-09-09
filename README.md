ATS is automated system for test of gitlab-ce without docker.
Use REST API, Selenium, appium.

---- Python ----
Steps to install python3.8 ans pip
sudo apt update
sudo apt install python3.8 python3-pip

---- Ansible ----
Ref. : https://docs.ansible.com/ansible/latest/index.html

Steps to install ansible(Ubuntu)

sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

---- gitlab ----
cd deploy
ansible-playbook -i hosts.bak gitlab.yml

---- Selenium ----
sudo pip3 install selenium

wget -N https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

