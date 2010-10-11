var app = require('express').createServer();

app.get('/', function(req, res){
    res.send('let\'s build us a web app!');
});

app.listen(3000);

