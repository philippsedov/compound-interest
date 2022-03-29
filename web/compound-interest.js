function setResult(number) {
  if (!isNaN(number)) {
    document.getElementById("result").textContent = number;
  }
}

function onInput () {
  var goal = Number(document.getElementById("goal").value);
  var nMonth = (Number(document.getElementById("nMonth").value))/12;
  var startCapital = Number(document.getElementById("startCapital").value);
  var annualInterest = Number(document.getElementById("annualInterest").value);
  var inflation = (Number(document.getElementById("inflation").value))+0.00000001;
  var growth = ((annualInterest - inflation )/ 12);
  //console.log(nYear);
  setResult( Math.ceil(( (goal - startCapital) * growth *  (1/( (1+growth) ** (12 * nMonth)-1)) ) * 100)/100 );
}

document.addEventListener("DOMContentLoaded", function () {
  var sumInputs = document.getElementsByClassName("sum-input");
  for (input of sumInputs) {
    input.addEventListener('keyup', onInput);
  }
});
