from django.shortcuts import render, get_object_or_404, redirect
from .models import Chapter, Comment, Interaction
from django.template import Template, Context

# Create your views here.

def home(request):
    return render(request, 'home.html')

def guiapje_completo_old(request):
    return render(request, 'guiapje_completo.html')

def guiapje_completo(request, page_number=None):
    if page_number is None:
        page_number = 1
    # Processar de acordo com o número da página
    context = {
        'page_number': page_number
    }
    return render(request, 'guiapje_completo.html', context)

def chapter_list(request):
    chapters = Chapter.objects.all()
    #return render(request, 'app_guiapje/chapter_list.html', {'chapters': chapters})
    return render(request, 'app_guiapje/home.html', {'chapters': chapters})

def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    return render(request, 'app_guiapje/chapter_detail.html', {'chapter': chapter})

def add_comment(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        Comment.objects.create(chapter=chapter, user=request.user, text=comment_text)
    return redirect('chapter_detail', pk=chapter.chapter.id)

def like_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    interaction, created = Interaction.objects.get_or_create(chapter=chapter, user=request.user)
    interaction.liked = not interaction.liked
    interaction.disliked = False if interaction.liked else interaction.disliked
    interaction.save()
    return redirect('chapter_detail', pk=chapter.chapter.id)

def dislike_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    interaction, created = Interaction.objects.get_or_create(chapter=chapter, user=request.user)
    interaction.disliked = not interaction.disliked
    interaction.liked = False if interaction.disliked else interaction.liked
    interaction.save()
    return redirect('chapter_detail', pk=chapter.chapter.id)