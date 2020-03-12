function rot13(message){
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let upperAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  let cipher = '';
  message.split('').forEach(str => {
    if (alphabet.indexOf(str) !== -1 || upperAlpha.indexOf(str) !== -1) {
      let finStr = '';
      if (str === str.toUpperCase()) {
        finStr = upperAlpha.substr(upperAlpha.indexOf(str, upperAlpha[-1])) + upperAlpha.substr(0, upperAlpha.indexOf(str))
        cipher += finStr[finStr.indexOf(str) + 13]
      } else {
        finStr = alphabet.substr(alphabet.indexOf(str, alphabet[-1])) + alphabet.substr(0, alphabet.indexOf(str))
        cipher += finStr[finStr.indexOf(str) + 13]
      }
    } else {
       cipher += str;
    }
  });
  return cipher
}
