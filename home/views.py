from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Reservation
from datetime import datetime



@login_required(login_url='index')
def index(request):
	req =[]
	if request.method == 'POST':
		kategori = request.POST.get('kategori')
		search  = request.POST.get('search')
		sdate  = request.POST.get('sdate')
		edate  = request.POST.get('edate')

		if kategori == 'status':
			data = Reservation.objects.filter(status__icontains=search).order_by('-bookingTime')
		elif kategori == 'podName':
			data = Reservation.objects.filter(podName__icontains=search).order_by('-bookingTime')
		elif kategori == 'date':
			data = Reservation.objects.filter(bookingTime__gte=sdate, bookingTime__lte=edate).order_by('-bookingTime')

		req = {
			'kat' : kategori,
			'search' : search,
			'sdate' : sdate,
			'edate' : edate,
		}

	else:
		data = Reservation.objects.all().order_by('-bookingTime')

	paginator = Paginator(data, 5)
	page_num = request.GET.get('page', 1)

	try:
		page = paginator.page(page_num)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		page = paginator.page(1)

	currentpage = int((5 * page.number) - 4)

	tonumber = currentpage + 4


	context = {
		'title': 'Home',
		'page_obj' : page,
		'pagin' : paginator,
		'number' : currentpage,
		'tonumber' : tonumber,
		'req' : req,
	}

	return render(request,'index.html',context)


def detail(request,*args,**kwargs):
	detailid = kwargs.get('pk')

	data = Reservation.objects.filter(pk=detailid)

	context = {
		'title': 'Detail Reservation',
		'details' : data,
	}
	return render(request, 'detail.html', context)