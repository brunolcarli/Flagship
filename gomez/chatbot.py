from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from gomez.train_conversations import conversations

wernicke = ChatBot('Gomez')
trainer = ListTrainer(wernicke)
for conversation in conversations:
    trainer.train(conversation)
