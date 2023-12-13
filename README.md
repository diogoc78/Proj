Relatório do Trabalho prático
Sistemas Distribuídos

Função no Servidor 
inv_trignometria(x,y)


Aluno:
Diogo Cardoso
1707239
diogoc78 dcardoso7891@gmail.com


Indice
1. Descrição do Trabalo...........................................3
2. Implementação do Trabalho................................3
3. Funcionamento do trabalho.................................3
4. Conclusão..............................................................3
5. Bibliografia.............................................................3

1.	Descrição do Trabalho

Para implementar a função inv_trignometria no servidor e permitir que o cliente envie solicitações para calcular os valores das funções arccos, arcsin e arctg, você precisará de uma arquitetura cliente-servidor que permita a comunicação entre eles. Vou fornecer uma visão geral da arquitetura e um exemplo de implementação em Python usando sockets para a comunicação.



2.	Implementação do Trabalho	
O desenvolvimento de uma função no servidor para calcular os valores das funções trigonométricas inversas, como arccos(y), arcsin(y) e arctg(y), é um processo fundamental na implementação de sistemas distribuídos. Nesse contexto, o servidor atua como uma entidade centralizada capaz de processar solicitações provenientes de clientes. A função "inv_trigonometria" proposta permite que o cliente envie uma função trigonométrica desejada juntamente com um argumento, e o servidor retorna o resultado correspondente.

Objetivo:
O principal objetivo dessa implementação é fornecer uma solução eficiente e flexível para o cálculo de funções trigonométricas inversas em um ambiente distribuído. Isso permite a separação de preocupações, com o servidor especializado em executar cálculos trigonométricos e o cliente encarregado de enviar solicitações e processar os resultados obtidos.


3.	Funcionamento do trabalho	

Passo 1: Configuração do Ambiente
pip install Flask requests


Passo 2: Implementação do Servidor (ProjMath.py.py)
	Este código define um servidor Flask com uma rota /inv_trigonometria que aceita solicitações POST contendo dados JSON. Ele implementa as funções trigonométricas inversas e retorna os resultados.


Passo 3: Execução do Servidor (ProjMath.py)


“python ProjMath.py” usando este comando , o servidor agora está aguardando solicitações em http://localhost:5000/inv_trigonometria.

![1](https://github.com/diogoc78/Proj/assets/145680518/ad4758db-34e4-4220-b636-28009b3abe80)


Passo 4: Implementação do Cliente
	Este código define uma função calcular_trigonometria que envia uma solicitação para o servidor. O exemplo de uso no final chama a função para calcular arccos(0.5).

Passo 5: : Execução do Cliente (ProjCliente.py)

“python ProjCliente.py” usando este comando , verá a resposta do servidor, indicando o resultado da função trigonométrica inversa. 

![2](https://github.com/diogoc78/Proj/assets/145680518/60380940-9984-4d9f-aa04-9ae4a511df44)


Passo 6 : Em prática 

Aqui a ligação foi estabelefica entre o Cliente e o Servidor.

![3](https://github.com/diogoc78/Proj/assets/145680518/0f9082c9-fd69-4b13-994a-7e3193182ca0)


Quando existir uma ligação o cliente terá a possiblidade de escolher que tipo de função deseja (arccos, arcsin, arctg) e poderá escolher o valor desejado.

 
![4](https://github.com/diogoc78/Proj/assets/145680518/f9673cdc-625c-48e1-abe4-5c7b5a09c95a)


Como resultado final terá o resultado apresentado , tem a oportunidade de voltar a escolher outra função das oferecidas ou fechar o menu (escrevendo “sair”).


![6](https://github.com/diogoc78/Proj/assets/145680518/07064974-da5a-4df9-a437-04da62a61896)


Aqui ,estão as logs do servidor e pudemos ver , o servidor a receber a mensagem do cliente e a reastabelecer a ligação com o cliente á espera de mais dados da parte do cliente .

![7](https://github.com/diogoc78/Proj/assets/145680518/55d0dbfe-b067-451f-b330-44774eea8b26)

 
4.	Conclusão
Neste projeto, implementamos um sistema distribuído que permite o cálculo de funções trigonométricas inversas de forma centralizada em um servidor remoto. A função inv_trigonometria foi projetada para aceitar solicitações contendo a função trigonométrica desejada e o argumento, retornando os resultados correspondentes ao cliente.

O que foi feito:

Servidor Flask:
Implementamos um servidor Flask capaz de receber solicitações POST em uma rota específica (/inv_trigonometria).
Desenvolvemos a lógica para processar as solicitações, calcular as funções trigonométricas inversas (arccos, arcsin, arctg) e retornar os resultados aos clientes.

Cliente Simples:
Criamos um cliente básico em Python que envia solicitações para o servidor com exemplos de funções e argumentos.

O que faltou fazer:

Segurança e Validação:
A implementação atual não lida adequadamente com preocupações de segurança e validação. Em um ambiente de produção, seria essencial validar e filtrar cuidadosamente os dados recebidos do cliente para evitar potenciais vulnerabilidades.

Bibliografia
https://chat.openai.com/
https://cienciaprogramada.com.br/2021/12/funcoes-trigonometricas-com-python/
https://www.youtube.com/
https://www.scribd.com/document/270511052/Python
https://acervolima.com/diferenciacao-de-funcoes-trigonometricas-inversas/
