
/* MathML to SVG via MathJax */

"use strict";

const fs   = require("fs");
const path = require("path");

const mj   = require("mathjax-node");
const vf   = require("./validate-files");

/* Keeping the name general, to express an aspiration
 * (perhaps unlikely) to support other formats. The
 * Ultimate Realization of this might be a module thinly
 * wrapping MathJax-node with file handling features. */

// Presumes MathML input and SVG output.
const convert = (fileIn, fileOut) => {
  mj.typeset({
    math: fs.readFileSync(fileIn),
    format: "MathML",
    svg: true,
  })
  .then ((result) => {
    fs.writeFile(fileOut, result.svg);
  })
  .catch ((err) => {
    // MathJax-node already sent the error to console
    usage();
  });
}

const usage = (msg) => {
  let arg0 = path.basename(process.argv[0]);
  let arg1 = path.basename(process.argv[1]);

  if (msg) console.error(msg);

  console.error(`Usage:

    ${arg0} ${arg1} <path to MathML input> <path to SVG output>

    If the output exists, it is overwritten.` + "\n");

  process.exit(1);
}

const main = () => {

  const args = process.argv.slice(2);

  if (args.length !== 2) usage("Invalid number of arguments");

  console.log("foo");

  vf.validateFile(args[0], "input file, first arg",   fs.constants.R_OK, usage);
  console.log("bar");

  vf.validateFile(args[1], "output file, second arg", fs.constants.W_OK, usage);
  console.log("bip");

  //convert(args[0], args[1]);
  console.log("bop");
}

main();
