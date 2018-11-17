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
          	$('#dadosPC').html(data['html']);
          	$('#tituloModal').html(data['titulo']);
        }
    });
}

function atualizarDadosComputador(idComputador){
	var csrf = $('meta[name=csrf-token]').attr("content");
	var nome = $('[name="nome"]').val();
	var ip = $('[name="ip"]').val();
	var chave = $('[name="chave"]').val();
	$.ajax({
    	method: 'POST',
       	url: '/administracao/ajax/atualizarComputador',
       	dataType: 'json',
       	data: {
          	'idComputador': idComputador,
          	'csrfmiddlewaretoken': csrf,
          	'nome':nome,
          	'ip':ip,
          	'chave':chave,
        },
        success: function (data) {
          	$('#resposta').html(data);
          	buscarDadosComputador(idComputador);
        },
        error: function(jqXHR,error, errorThrown) {
        	$('#resposta').html(jqXHR);
        	console.log('===========ERRO============');
        	console.log(jqXHR);
        }
	});
}

function deletarComputador(idComputador){
	var csrf = $('meta[name=csrf-token]').attr("content");
	$.ajax({
    	method: 'POST',
       	url: '/administracao/ajax/deletarComputador',
       	dataType: 'json',
       	data: {
          	'idComputador': idComputador,
          	'csrfmiddlewaretoken': csrf,
        },
        success: function (data) {
          	$('#resposta').html(data);
          	setTimeout(function() {window.location.reload(false)}, 3000);
        },
        error: function(jqXHR,error, errorThrown) {
        	$('#resposta').html(jqXHR);
        	console.log('===========ERRO============');
        	console.log(jqXHR);
        }
	});
}