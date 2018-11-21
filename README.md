<h1>MapReduce</h1>

<p>Esse foi o trabalho final apresentado na disciplina de Sistemas Distribuídos do curso de Sistemas de Informação da Universidade Federal do Piauí.</p>

<p>
<b>Professor:</b> Francisco Airton Pereira da Silva <br>
<b>Alunos:</b>
    <ul>
        <li>Hericlys Borges Sousa</li>
        <li>Igor de Carvalho Gonçalves</li>
        <li>William de Oliveira TOrres</li>
    </ul>
</p>

<h2>Funcionamento</h2>

<p style="text-align: justify">O suposto sistema trata-se de uma rede de <i>clusters</i>, desenvolvida por um cliente (interface gráfica), por um <i>master</i>, e os <i>clusters</i>. A interface gráfica foi utilizada para realizar o gerenciamento dos usuários e dos <i>clusters</i>. O master é responsável por lidar com as conexões dos <i>clusters</i> e a divisão de tarefas entre eles, além de conter o servidor web da interface gráfica. Por fim, os <i>clusters</i> apenas recebem, realizam e retornar a resposta da tarefa passada para eles.<p>

<p>
    O servidor web foi feito em utilizando <i>Django</i>, <i>JavaScript</i>, <i>Boostrap 4</i>, <i>Jquery</i>, <i>Ajax</i> e <i>Json</i> e <i>Mysql</i> como SGBD. Ele realiza o gerenciamento das entidades trabalhadas no sistema, além de exibir a interface e lidar como consultas.
</p>
<p>O servidor <i>master</i> foi desenvolvido em python utilizando comunicação por meio do <i>sockets</i>. Ele possui dois trabalhos, o primeiro é lidar com as conexões com os <i>clusters</i> e a outra é lidar com as tarefas que devem ser executadas pelos <i>clusters</i>. Quando ele está lidando com as conexões, o seu trabalho é aceitar a conexão e em seguida autenticar o <i>cluster</i> no sistema, se o <i>cluster</i> que se conectou for cadastrado no sistema, ele liberará funcionalidades, caso contrário, a conexão será fechada. Já na parte de lidar com as tarefas, ele fica “perguntando” ao servidor web se há algum trabalho que ainda não foi realizado, se houver, ele analisará qual dos <i>clusters</i> conectados é a melhor opção para resolver o problema, e então ele envia a tarefa para o escravo selecionado.
</p>
<p>Por fim, os cluster realiza duas ações durante seu funcionamento. Após autenticar a conexão com o master, ele cria uma thread para esperar tarefas a ao mesmo tempo fica enviando status de uso do processador e da memória RAM para o master. A thread fica aguardando um comando do master, quando esse comando chega, ela cria uma terceira thread que irá lidar com a tarefa, após a tarefa ser concluída o resultado é retornado para o master.</p>
<p>Na função <i>MapReduce</i>, logo no início tratamos de eliminar todos os pontos, vírgulas, dois pontos, e outras pontuações para que no retorno da função só contenha a  palavra desejada, e a quantidade de vezes que ela se repete. </p>
<p>Depois criamos duas listas: existentes e contar. A lista existentes irá armazenar as palavras sem repetí-las. A lista contar servirá para armazenar a quantidade de vezes que determinada palavra se repete no texto no índice da palavra na lista existente.</p>
<p>A lista ordenado serve para ordenar cada palavra na lista existentes a sua devida quantidade de repetições na lista contar.</p>
<p>Para mostrar o resultado a função <i>MapReduce</i> chama a função verificaPalavras, que irá verificar se a palavra existe na lista ordenado. Se ela existir, a função retorna a palavra e a quantidade de vezes que ela se repete no texto.</p>