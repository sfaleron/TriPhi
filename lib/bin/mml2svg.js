
// MathML to SVG via MathJax

'use strict';

const fs   = require('fs');
const path = require('path');

const      mj = require('mathjax-node');
const      vf = require('./validate-files');

const thisDir = path.dirname(process.argv[1]);


const  preProcess = (fileName) => {
  let    inputRaw = fs.readFileSync(fileName);
  return inputRaw.slice(inputRaw.indexOf('<math '));
};

// okay, first pass is a dud. but works as before.
// the id="MathJax-SVG-1-Title" is a big clue that MathJax will do this for us!

const postProcess = (fileName, svgStr, title) => {
  if (title !== null) {
    const start = svgStr.indexOf('>', svgStr.indexOf('<title') + 1) + 1;
    const   end = svgStr.indexOf('<', start);

    svgStr = `${svgStr.slice(0, start)}${title}${svgStr.slice(end)}`;
  }

  fs.writeFileSync(fileName, svgStr);
};


const mml2svg = (fileIn, fileOut, title) => {

  mj.typeset({
    math: preProcess(fileIn),
    format: 'MathML',
    svg: true,
  })
  .then ((result) => {
    postProcess(fileOut, result.svg, title);
  })
  .catch ((err) => {
    // MathJax-node already sent the error to console,
    // unless its an exception, oh my!
    if (err instanceof Error) throw err;
    else usage();
  });
};

const usage = (msg) => {
  let arg0  = path.basename(process.argv[0]);
  let arg1  = path.basename(process.argv[1]);

  if (msg) console.error(msg);

  console.error(`Usage:

    ${arg0} ${arg1} <target>
    ${arg0} ${arg1} <input MathML file> <output SVG file>


    If one argument is passed, it is the root part of the input and output
    filenames, without extensions ".mml" and ".svg", respectively, in the
    directory "../intermediates/" with respect to the location of this
    executable. Additionally, it is used to look up the title given to the
    output in the configuration file "../parameters".

    If two arguments are passed, they are interpreted directly as input and
    output files, with respect to the current directory. The title of the
    output file is left as set by MathJax, currently "Equation".

    If the output exists, it is overwritten.` + '\n');

  process.exit(1);
};

const main = () => {

  let inputFile, outputFile, title;

  const args = process.argv.slice(2);

  if (args.length == 1) {
    const target = args[0];
    const    ini = require('ini');

    const config = ini.parse(fs.readFileSync(
      path.join( thisDir, '..', 'parameters' ), 'utf-8') );

    const section = config.titles;

    if (!(target in section)) usage('Target not found');

    title = section[target];

    const stem = path.join(thisDir, '..', 'intermediates', target);

    inputFile  = stem + '.mml';
    outputFile = stem + '.svg';

  } else if (args.length == 2) {
    title      = null;
    inputFile  = args[0];
    outputFile = args[1];

  } else usage('Invalid number of arguments');

  console.log(' in: ' +  inputFile); console.log('out: ' + outputFile);

  vf.validateFile( inputFile,  'input file', fs.constants.R_OK, usage);
  vf.validateFile(outputFile, 'output file', fs.constants.W_OK, usage);

  mml2svg(inputFile, outputFile, title);
};

main();
