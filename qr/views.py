import io
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import qrcode
from .forms import QRForm
from .models import QR


def create_qr(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            qr_obj = form.save(commit=False)
            img = qrcode.make(qr_obj.url)
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            qr_obj.image.save('qr.png', ContentFile(buffer.getvalue()))
            qr_obj.save()
            return redirect('qr:detail', pk=qr_obj.pk)
    else:
        form = QRForm()
    return render(request, 'qr/create_qr.html', {'form': form})


def qr_detail(request, pk):
    qr_obj = QR.objects.get(pk=pk)
    return render(request, 'qr/qr_detail.html', {'qr': qr_obj})
