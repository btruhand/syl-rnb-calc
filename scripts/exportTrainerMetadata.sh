#!/usr/bin/env bash
# Loads trainer_metadata.js via Node and writes it as clean JSON.
# should be run 
node -e "
const fs = require('fs');
eval(fs.readFileSync('./src/js/data/trainer_metadata.js', 'utf8'));
fs.writeFileSync('./scripts/data/trainerMetadata.json', JSON.stringify(TRAINER_METADATA, null, 2));
"
echo "Written scripts/data/trainerMetadata.json"
