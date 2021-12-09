function a () {
  function b () {};
  //var b = function () {}
  //var b;
  
  console.log(b);
  b = 'bbb'
  console.log(b);
  console.log(b);
}

 a();