from django.shortcuts import render, redirect
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot(
    "chatbot",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            #     "default_response": "Sorry, I don't know what that means",
            #     "maximum_similarity_threshold": 0.90,
        }
    ],
)

list_to_train = [
    "hi",
    "hi, there",
    "What's your name?",
    "I'm just a chatbot",
    "What is your favorable food?",
    "I like cheese",
    "what's your fav sport?",
    "swimming",
    "do you have children",
    "no",
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train("chatterbot.corpus.english")

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)


def index(request):
    return render(request, "blog/index.html")


def specific(request):
    return HttpResponse("list1")


def getResponse(request):
    userMessage = request.GET.get("userMessage")
    chatResponse = bot.get_response(userMessage)
    return HttpResponse(chatResponse)
