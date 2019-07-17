
'use strict';

const fs   = require('fs');
const path = require('path');

/* Throws an exception if the filename is invalid, at least on ext4.
 * If invalid, calls the callback and returns immediately.

 * Recognized flags are R_OK or W_OK, or a bitwise combination.
 * Any other flags will be ignored, but an exception is thrown
 * if neither are present.

 * If the file does not exist, read and write checks fail.
 * For write checks, one must additionally confirm that the
 * directory exists and is not write protected. Note that a
 * writable file in a write protected directory generally
 * remains writable, although this may be filesystem or
 * operating system dependent.

 * Insufficiently documented behavior described below; the disambiguation
 * used works on my system, and seems likely to be more or less canonical,
 * but you should check with the node.js maintainers about that!

 * Concerning fs.access() and derivitives, called with F_OK:
 *   existing directory: succeeds
 *   symbolic link: follows, does the expected thing based
 *      on the referenced entry, wrt broken links or directories
 */
const validateFile = (file, shortDesc, flags, callback) => {

  let fileDir = path.dirname(file);

  const fmtCb = (msg, err) => {
    callback(`---- ${shortDesc} ----\n${msg}${err ? ': ' + err.message : ''}`);
  }

  if (!(flags & (fs.constants.R_OK|fs.constants.W_OK))) {
    throw ((message) => {
      this.message = message;
      this.name = 'FlagException';
    })('No recognized flags present. One or ' +
       'both of R_OK and W_OK must be present.');
  }

  // read access check
  if (flags & fs.constants.R_OK) {
    // existence
    try { fs.accessSync(file, fs.constants.F_OK); }
    catch(err) {
      fmtCb('not found', err);
      return;
    }

    if (!fs.statSync(file).isFile()) {
      fmtCb('not a file');
      return;
    }

    // check for read access
    try { fs.accessSync(file, fs.constants.R_OK); }
    catch(err) {
      fmtCb('This account does not posses read permissions');
      return;
    }
  }

  // write access check
  if (flags & fs.constants.W_OK) {
    // existence
    try { fs.accessSync(file, fs.constants.F_OK); }
    catch(err) {
      // okay to write to a new file, but that requires write
      // access to the directory!

      // okay, but does it even exist?
      try { fs.accessSync(path.dirname(file), fs.constants.F_OK); }
      catch(err) {
        fmtCb('directory not found', err);
        return;
      }

      // no garbage, please
      if (!fs.statSync(fileDir).isDirectory()) {
        fmtCb('containing path is not a directory');
        return;
      }

      // write access to directory
      try { fs.accessSync(path.dirname(file), fs.constants.W_OK); }
      catch(err) {
        fmtCb('This account does not posses write permissions to the directory', err);
        return;
      }
      // need a file for the actual write access check
      fs.writeFileSync(file, '');
    }

    // check for write access
    try { fs.accessSync(file, fs.constants.W_OK); }
    catch(err) {
        fmtCb('This account does not posses write permissions', err);
      return;
    }
  }
}

exports.validateFile = validateFile;
