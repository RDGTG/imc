from django.shortcuts import render

def calculator_imc(request):
    if request.method == 'POST':
        try:
            # Captura os dados do formulário
            peso = float(request.POST.get('peso'))
            altura = float(request.POST.get('altura'))
            
            # Validação básica
            if altura <= 0 or peso <= 0:
                raise ValueError("Peso e altura devem ser valores positivos.")
            
            # Cálculo do IMC
            imc = peso / (altura ** 2)
            
            # Classificação
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif 18.5 <= imc < 25:
                classificacao = "Peso normal"
            elif 25 <= imc < 30:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obesidade"
            
            # Retorna o resultado
            return render(request, 'imc_app/resultado.html', {
                'imc': round(imc, 2),
                'classificacao': classificacao
            })
            
        except (ValueError, TypeError):
            # Se houver erro (ex.: usuário digita texto), mostra o formulário com mensagem de erro
            return render(request, 'imc_app/calculator_imc.html', {
                'erro': "Digite valores válidos (números positivos)."
            })
    
    # Se não for POST (ou seja, GET), mostra o formulário vazio
    return render(request, 'imc_app/calculator_imc.html')

