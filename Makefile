all: build infra

infra-services:
	@kubectl apply -f infra/services/location
	@kubectl apply -f infra/services/payment
	@kubectl apply -f infra/services/trip

infra-gateway:
	@kubectl create configmap krakend-config --from-file=infra/gateway/krakend.json --dry-run=client -o yaml | kubectl apply -f -
	@kubectl apply -f infra/gateway/krakend.yaml
	@kubectl rollout restart deployment.apps/krakend-deployment

infra: infra-services infra-gateway

build-trip:
	@docker build -t trip-service ./services/trip-service -f ./services/trip-service/Dockerfile

build-location:
	@docker build -t location-service ./services/location-service -f ./services/location-service/Dockerfile

build-payment:
	@docker build -t payment-service ./services/payment-service -f ./services/payment-service/Dockerfile

build: build-trip build-location build-payment
