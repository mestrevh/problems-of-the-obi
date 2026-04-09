from pikepdf import Pdf, PdfImage
from pathlib import Path

data = Path("data")
imgs = Path("imgs")
imgs.mkdir(exist_ok=True)

for question in data.glob("*.pdf"):
    print(question)
    arquivo = Pdf.open(question)
    
    for pagina in arquivo.pages:
        i = 1
        for nome, imagem in pagina.images.items():
            imagem_salvar = PdfImage(imagem)
            imagem_salvar.extract_to(fileprefix=f"imgs/{nome}_{question.name}_{i}.png")
            i += 1
            