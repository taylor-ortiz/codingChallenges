function createPhoneNumber(numbers){
  let phone = '';
  let phoneSyntax = { 0: '(', 3: ') ', 6: '-' };
  numbers.forEach( (numb, i) => {
    if (phoneSyntax.hasOwnProperty(i)) {
      phone += phoneSyntax[i]
    }
    phone += numb.toString();
  })
  return phone;
}
