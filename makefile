# SMS Bot
# Author:  Daniel Nicolas Gisolfi

image=sms_bot
hub_image=dgisolfi/sms_bot
container=sms_bot
version=2.0

all: clean build run

dev: clean build dev_bot

push: clean build publish

intro:
	@echo "\n             SMS Bot v$(version)"

clean:
	-docker kill $(container)_dev
	-docker kill $(container)_prod
	-docker rmi $(image)
	-docker rmi $(hub_image)


# rebuild image
build: intro clean
	@docker build -t $(image) .

run:
	@docker run -it --rm --name $(container)_prod $(hub_image) bash

# build development enviorment
dev_bot: intro build
	@docker run -it --rm --name $(container)_dev -v ${PWD}:/DEV $(image) bash

publish:
	@echo "\n				pushing $(hub_image) to DockerHub"
	@docker tag ${image} ${hub_image}:latest
	@docker push ${hub_image}
