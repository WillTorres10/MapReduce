function buscarDadosComputador(idComputador){
	var csrf = $('meta[name=csrf-token]').attr("content");
	 $.ajax({
        method: 'POST',
        url: '/administracao/ajax/dadosComputador',
        dataType: 'json',
        data: {
          	'idComputador': idComputador,
          	'csrfmiddlewaretoken': csrf,
        },
        success: function (data) {
        	console.log("entrou");
          	$('#dadosPC').html(data['html']);
          	$('#tituloModal').html(data['titulo']);
        },
        error: function(jqXHR,error, errorThrown) {
        	console.log('===========ERRO============');
        	console.log(jqXHR);
        }
      });
}