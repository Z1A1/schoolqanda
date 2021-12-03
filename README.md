"# schoolqanda" 
install docker
train: docker run -it -v ${pwd}:/app rasa/rasa:2.8.7-full train
run the bot: docker run -it -v ${pwd}:/app rasa/rasa:2.8.7-full shell
