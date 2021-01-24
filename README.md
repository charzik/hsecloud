# hsecloud
sudo docker image build -t service_status:1.0 -f service_status/Dockerfile .
sudo docker run -d -p 8080:8080 service_status:1.0
