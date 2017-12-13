var request = require('request');
var cheerio = require('cheerio');

request ('https://meuguia.tv/programacao/categoria/Filmes', function(err, res, body){
    if (err) console.log('Erro' + err);

    var $ = cheerio.load(body);

    $('ul li  ').each(function() {
        var title = $(this).find('.prog_comp_tit').text().trim();
        var canal = $(this).find('.metadados ').text().trim();

        
        console.log ('titulo: ' + title);
        console.log ('Horário: '+ canal );
    });
});