var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [10,9,8,7,6,5,4,3,2,1],
    datasets: [{ 
        data: [50, 25.5, 82, 1, 1.5, 60],
        backgroundColor: [
                'rgba(62,149,205, 0.5)',
        ],
        label: "CPU",
        borderColor: "#3e95cd",
        fill: true
      }, { 
        data: [50, 4, 82, 6, 3.5, 100],
        backgroundColor: [
                'rgba(142,94,162, 0.5)',
        ],
        label: "RAM",
        borderColor: "#8e5ea2",
        fill: true
      },
    ]
  }
});

function addData(chart, data, datasetIndex) {
   chart.data.datasets[datasetIndex].data = data;
   chart.update();
}

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
            var cpu = data['cpu'].split(',').map(function(item) {
                return parseFloat(item, 10);
            });
            var ram = data['ram'].split(',').map(function(item) {
                return parseFloat(item, 10);
            });
            console.log(ram)
            addData(myChart, cpu, 0);
            addData(myChart, ram, 1);
            if (data['status'] == 0){
              $('#grafico').html('Computador inativo');
            }
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


function buscarDadosTarefa(idTarefa){
  var csrf = $('meta[name=csrf-token]').attr("content");
  $.ajax({
      method: 'POST',
        url: '/administracao/ajax/dadosTarefa',
        dataType: 'json',
        data: {
            'id': idTarefa,
            'csrfmiddlewaretoken': csrf,
        },
        success: function (data) {
            $('#corpoModal').html(data['html']);
            $('#tituloModal').html(data['titulo']);
        },
        error: function(jqXHR,error, errorThrown) {
          $('#resposta').html(jqXHR);
          console.log('===========ERRO============');
          console.log(jqXHR);
        }
    });
}