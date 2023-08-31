from django.shortcuts import render
from word_counter.word_count.word_counter import WordCounter

word_counter = WordCounter()

def index(request):
    if request.method == 'POST':
        if 'load' in request.POST:
            filename = request.POST['filename']
            word_counter.load(filename)
        elif 'wordcount' in request.POST:
            word = request.POST['word']
            word_counter_result = word_counter.wordcount(word)
        elif 'clear_memory' in request.POST:
            word_counter.clear_memory()

    context = {
        'word_counter_result': word_counter_result,
    }
    return render(request, 'word_count/index.html', context)