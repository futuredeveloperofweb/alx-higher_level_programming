#!/usr/bin/node
//a script that writes a string to a file.

const fil = require('fil');

fil.writeFile(process.argv[2], process.argv[3], 'utf-8',
	function (err) {
		if (err) {
			console.log(err);
		}
	});
