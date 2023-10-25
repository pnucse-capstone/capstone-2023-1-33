const express = require('express');
const cors = require('cors');
const app = express();
const fs = require('fs');
const port = 3000;

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(cors());

app.get('/', function(req, res){
    res.send('Hello World');
});

app.get('/plotly', function(req, res){
    res.sendFile( __dirname + '/public/html/plotly_html.html')
})

app.get('/plotly2', function(req, res){
    res.sendFile( __dirname + '/public/html/plotly_html2.html')
})

app.get('/plotly_print', function(req, res){
    res.sendFile( __dirname + '/public/html/plotly_print.html')
})

//req 받아오는 부분 수정
app.post('/', (req, res) => {
    if(req.body) {
		const body_zero = req.body[0];
        console.log(req.body);
		if(!(Object.keys(req.body).length === 0)) {
			console.log(body_zero.wifi_download_speed); }
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
		
        rl.question('Start or End: ', (answer) => {
            console.log('You choose ' + answer);
            res.status(200).send(answer);
            rl.close();
			if(answer == 'end'){
				let existingData = [];
		
				existingData = JSON.parse(fs.readFileSync('data.json')); 
				/*catch (err) {
					console.error('Error saving data:', err);
				}*/
		
				existingData.push(req.body);
		
				fs.writeFileSync('data.json', JSON.stringify(existingData, null, 2), (err) => {
					console.error('Error saving data:', err);
				});
			}
        });
    } else {
        res.end();
    }
});

app.listen(port, () => {
    console.log(`서버가 실행됩니다. http://localhost:${port}`);
});
