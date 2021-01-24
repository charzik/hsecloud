# hsecloud

sudo apt update && sudo apt upgrade

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt update && apt-cache policy docker-ce

sudo apt install -y docker-ce

git clone https://github.com/charzik/hsecloud

cd hsecloud

sudo docker image build --network=host -t service_status:1.0 -f service_status/Dockerfile .

sudo docker run -d -p 8080:8080 service_status:1.0
