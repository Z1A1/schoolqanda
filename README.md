"# schoolqanda" 
install docker
2train: docker run -it -v ${pwd}:/app rasa/rasa:2.8.7-full train
3run the bot: docker run -it -v ${pwd}:/app rasa/rasa:2.8.7-full shell
