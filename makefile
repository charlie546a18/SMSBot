# Erin SMS Bot
# Author:  Daniel Nicolas Gisolfi

image=sms_bot
hub_image=dgisolfi/sms_bot
container=sms_bot_prod
version=2.0

all: clean build os_latest

dev: clean build dev_os

intro:
	@echo "\n             SMS Bot v$(version)"

clean:
	-docker kill $(container)_dev
	-docker kill $(container)_prod
	-docker rmi $(image)
	-docker rmi $(hub_image)


#rebuild image
build: intro
	@docker build -t $(image) .

# build development enviorment
dev_os: intro build
	@docker run -it --rm --name $(container)_dev -v ${PWD}:/DEV $(image) bash