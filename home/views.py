from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class ProjetosView(TemplateView):
    template_name = 'projetos.html'

class OrcamentosView(TemplateView):
    template_name = 'orcamentos.html'

