from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Board, Comment
from .forms import BoardForm, BoardCommentForm

# 메인화면 커뮤니티창

def home(request):
    return render(request,'home.html')

def bhome(request):
    boardList = Board.objects.order_by('-id')
    q = request.GET.get('q', '')
    if q: # q가 있으면
        boardList = boardList.filter(subject__icontains=q) 
    page = request.GET.get('page', 1)
    paginator = Paginator(boardList, 10)
    try:
        boards= paginator.page(page)
    except PageNotAnInteger:
        boards = paginator.page(1)
    except EmptyPage:
        boards = paginator.page(paginator.num_pages)
    
    return render(request,'bhome.html',{'boards':boards, 'q':q})


#글쓰기
def bwrite(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.created_date=timezone.now()
            board.name=request.user
            board.hits=0
            board.save()
            return redirect('/board/bdetail/'+str(board.id))
    
    else:
        form = BoardForm()
        return render(request,'bwrite.html',{'form':form})

#자세한 글
def bdetail(request,board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    comments = Comment.objects.filter(board_id=board_id)

    if request.method == 'POST':
        comment_form = BoardCommentForm(request.POST)

        if comment_form.is_valid():
            content = comment_form.cleaned_data['comment_textfield']
            com = comment_form.save(commit=False)
            com.board_id=board_id
            com.comment_user=request.user
            com.comment_date=timezone.now()
            com.save()
            comment_form = BoardCommentForm()
            context = {
                'board': board_detail,
                'comments': comments,
                'comment_form': comment_form
             }
            return render(request, 'bdetail.html',context)
        else:
            return render(request, 'bdetail.html',context)
    
    else:
        comment_form = BoardCommentForm()

    context = {
        'board': board_detail,
        'comments': comments,
        'comment_form': comment_form
    }
 
    return render(request, 'bdetail.html', context)
    #return render(request,'bdetail.html', {'board':board_detail})

#글 클릭시 조회수 up 
def bhits(request,board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    Board.objects.filter(id=board_detail.pk).update(hits = board_detail.hits + 1)
    return redirect('/board/bdetail/'+str(board_detail.id))

#글 수정
def bupdate(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit = False)
            board.created_date=timezone.now()
            board.name=request.user
            board.hits=0
            board.save()
            return redirect('/board/bdetail/'+str(board.id))
    else:
        form = BoardForm(instance=board)
        return render(request, 'bupdate.html',{'form':form})

def bdelete(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    return redirect('bhome')
