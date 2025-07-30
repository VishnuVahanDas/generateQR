import io
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
import qrcode
from .forms import QRForm
from .models import QR


@login_required
def create_qr(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            qr_obj = form.save(commit=False)
            qr_obj.user = request.user
            img = qrcode.make(qr_obj.url)
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            qr_obj.image.save('qr.png', ContentFile(buffer.getvalue()))
            qr_obj.save()
            return redirect('qr:detail', pk=qr_obj.pk)
    else:
        form = QRForm()
    return render(request, 'qr/create_qr.html', {'form': form})


@login_required
def qr_detail(request, pk):
    qr_obj = get_object_or_404(QR, pk=pk, user=request.user)
    return render(request, 'qr/qr_detail.html', {'qr': qr_obj})


@login_required
def user_qr_list(request):
    qrs = QR.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'qr/qr_list.html', {'qrs': qrs})
