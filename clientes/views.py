from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, RegistroFrom
from .models import Cliente
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q

# Create your views here.
@login_required
def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html',{'form': form})
    
def cliente_list(request):
    query = request.GET.get("q")
    if query:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) |  Q(apellido__icontains=query)          
        )
    else:
        clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes':clientes})


@login_required
def update_cliente (request, pk):
    cliente=get_object_or_404(Cliente, pk=pk)
    if request.method =='POST':
        form=ClienteForm(request.POST,request.FILES ,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form=ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form':  form, 'cliente': cliente})

@login_required
def delete_cliente(request, pk):
    cliente=get_object_or_404(Cliente, pk=pk)
    if request.method =='POST':
        cliente.delete()
        return redirect('cliente_list')
    else:
        form=ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente':cliente})

def generar_pdf_cliente(request):
    response= HttpResponse(content_type = 'application/pdf')
    #abrir =inline, descargar = attachment
    response ['Content-Disposition'] = 'inline; filename="clientes.pdf'
    pdf=canvas.Canvas(response,pagesize=letter,)
    pdf.setTitle("Reporte de Clientes")
    width,height =letter
    
    img= 'clientes/clientes.jpg'  
    pdf.drawImage(img, 45, height - 60, width=70, height=40)

    fecha_elaborada=datetime.datetime.today().strftime("%Y-%m-%d")
    pagina_num = 1
    
    def agregar_pie_pag(pdf, pagina_num):
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(30,20, f"Fecha de Elaboraccion: {fecha_elaborada}")
        pdf.drawString(width-100, 20, f"Pagina_Num: {pagina_num}")

    #CONTENIDO DEL PDF
    pdf.setFont("Helvetica-Bold", 25)
    texto = "Lista de Clientes"
    ancho_texto = pdf.stringWidth(texto)
    x = (width - ancho_texto)/2
    pdf.drawString(x,height - 35, texto)
    
    pdf.setFont("Helvetica-Bold", 15)
    encabezados = ["Nombre" , "Apellidos" , "Fecha Nac", "Edad", "Lugar",]
    x_inicial = 35
    y = height -80
    
    for i, encabezado in enumerate(encabezados):
        pdf.drawString(x_inicial + i * 100 , y , encabezado)
        
    y-=10
    pdf.line(40, y, width-40, y)
    
    y-=20
    pdf.setFont("Times-Roman", 14)
    
    query = request.GET.get("q")
    if query:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) |  Q(apellido__icontains=query)
        )
    else:
        clientes =Cliente.objects.all()
    for cliente in clientes:
        pdf.drawString(40, y, cliente.nombre)
        pdf.drawString(140, y, cliente.apellido)
        pdf.drawString(240, y, cliente.fecha_nac.strftime("%Y-%m-%d"))
        pdf.drawString(340, y, str(cliente.edad))
        pdf.drawString(440, y, cliente.lugar)
        y-=25

    agregar_pie_pag(pdf, pagina_num)
    
    pdf.showPage()
    pdf.save()
    return response

def register(request):
    if request.method == 'POST':
        form = RegistroFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFrom()
        return render(request, 'registration/register.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login')