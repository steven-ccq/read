from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import Http404
from django.shortcuts import render, redirect
from experiments.models import Book, Comment, Mark, User


def allbookpage(request, page):
    user = request.session.get('user')
    judge = User.objects.filter(name=user)
    if user is not None and judge.is_online == 0:
        judge.is_online = 1
        judge.save()
        request.session['user'] = None
        return redirect('/main')
    newest_books = Book.objects.all().order_by('publish_date')
    paginator = Paginator(newest_books, per_page=4)
    try:
        newest_books = paginator.page(page)
    except PageNotAnInteger:
        newest_books = paginator.page(1)
    except EmptyPage:
        newest_books = paginator.page(paginator.num_pages)
    except InvalidPage:
        raise Http404("您请求的页数不存在")
    context = {'newest_books': newest_books, 'paginator': paginator}
    return render(request, 'center.html', context)


def detail(request, id, page):
    user = request.session.get('user')
    judge = User.objects.filter(name=user)[0]
    if user is not None and judge.is_online == 0:
        judge.is_online = 1
        judge.save()
        request.session['user'] = None
        return redirect('/main')
    #user = 'sxy'
    book = Book.objects.filter(id=id).first()
    if request.method == 'POST':
        comment = Comment.objects.filter(book_id=id).order_by('time')
        reading_status = Mark.objects.filter(name=user, book_id=id)
        if not reading_status.exists():
            reading_status = '无'
        elif reading_status[0].mark == 1:
            reading_status = '在读'
        elif reading_status[0].mark == 2:
            reading_status = '读过'
        elif reading_status[0].mark == 0:
            reading_status = '想读'
        paginator = Paginator(comment, per_page=4)
        try:
            comment = paginator.page(page)
        except PageNotAnInteger:
            comment = paginator.page(1)
        except EmptyPage:
            comment = paginator.page(paginator.num_pages)
        except InvalidPage:
            raise Http404("您请求的页数不存在")
        if user is None:
            context = {'comment': comment, 'book': book, 'warning': '请先登录！',  'paginator':paginator, 'book_id': id, 'reading_status': reading_status}
            return render(request, 'detail.html', context)
        interest = request.POST.get('interest')
        if interest is not None:
            cover = Book.objects.filter(id=id)[0]
            b_cover = cover.cover
            if interest == '想读':
                mark = 0
            elif interest == '在读':
                mark = 1
            elif interest == '读过':
                mark = 2
            m = Mark.objects.filter(name=user, book_id=id).first()
            if m is not None:
                Mark.objects.update(name=user, book_id=id, cover=b_cover, mark=mark)
            else:
                m = Mark.objects.create(name=user, book_id=id, cover=b_cover, mark=mark)
        else:
            content = request.POST.get('content')
            score = request.POST.get('score')
            score = int(score)
            check = Comment.objects.filter(name=user, book_id=id)
            if check.exists():
                context = {'comment': comment, 'book': book, 'content': content, 'warning': '不能重复提交！', 'paginator':paginator, 'book_id': id, 'reading_status': reading_status}
                return render(request, 'detail.html', context)
            if content == '':
                context = {'comment': comment, 'book': book, 'content': content, 'warning': '评论不能为空！', 'paginator': paginator, 'book_id': id, 'reading_status': reading_status}
                return render(request, 'detail.html', context)
            review = Comment.objects.create(name=user, comment=content, book_id=id, grade=score)
            review.save()
            book.star = round((book.star+score)/2, 2)
            book.people += 1
            book.save()
    comment = Comment.objects.filter(book_id=id).order_by('time')
    paginator = Paginator(comment, per_page=4)
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    except InvalidPage:
        raise Http404("您请求的页数不存在")
    reading_status = Mark.objects.filter(name=user, book_id=id)
    if not reading_status.exists():
        reading_status = '无'
    elif reading_status[0].mark == 1:
        reading_status = '在读'
    elif reading_status[0].mark == 2:
        reading_status = '读过'
    elif reading_status[0].mark == 0:
        reading_status = '想读'
    context = {'comment': comment, 'book': book, 'paginator': paginator, 'book_id': id, 'reading_status': reading_status}
    return render(request, 'detail.html', context)





