from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from weasyprint import HTML
import os


def home(request):
    return render(request, 'app/home.html')


def gerar_relatorio_pdf(request):
    # Renderiza o template
    template = get_template('app/tabela.html')
    html_content = template.render()

    # Configuração do PDF usando weasyprint e estilos externos
    views_dir = os.path.dirname(os.path.abspath(__file__))
    stylesheets = [os.path.join(views_dir, 'static/app/css/styles.css')]
    pdf_files = HTML(string=html_content).write_pdf(stylesheets=stylesheets, page_size=('A4', 'landscape'))

    # Resposta HTTP com o PDF gerado
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="relatorio.pdf"'
    response.write(pdf_files)

    return response
    