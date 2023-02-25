const express = require('express');

const app = express();
app.use(express.json());

const isValidDiceData = (diceData) => {
  if (!diceData.includes('d')) {
    return false;
  }

  if (isNaN(diceData.replace('d', ''))) {
    return false;
  }

  if (diceData.startsWith('d')) {
    return false;
  }

  if (diceData.endsWith('d')) {
    return false;
  }

  return true;
};

app.post('/diceRoll', (req, res) => {
  if (!req.body.diceData) {
    res.status(400);
    res.send('Invalid data provided! Please provide JSON data containing the diceData key and try again!');
    return;
  }

  if (!isValidDiceData(req.body.diceData)) {
    res.status(400);
    res.send('Invalid dice data format! Proper format: [amount-of-die]d[sides-on-each-die]');
    return;
  }

  const diceData = req.body.diceData.split('d');
  const amountOfDie = diceData[0];
  const sidesOnEachDie = diceData[1];

  let resultSum = 0;

  for (let i = 0; i < amountOfDie; i++) {
    resultSum += Math.floor(Math.random() * sidesOnEachDie) + 1
  }

  res.status(200);
  res.send(JSON.stringify({ result: resultSum }));
});

app.listen(80);
console.log('Microservice listening on port 80...');