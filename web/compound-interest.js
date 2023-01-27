function setResult(number) {
  if (!isNaN(number)) {
    document.getElementById("result").textContent = number;
  }
}

function onInput () {
  var goal = Number(document.getElementById("goal").value);
  var nMonth = (Number(document.getElementById("nMonth").value))/12;
  var startCapital = Number(document.getElementById("startCapital").value);
  var annualInterest = (Number(document.getElementById("annualInterest").value))/100;
  var inflation = (Number(document.getElementById("inflation").value))/100+0.00000001;

  setResult( Math.ceil(( (goal - startCapital) * ((annualInterest-inflation)/12) * (1/( (1+((annualInterest-inflation)/12))**(12*nMonth)-1 ) ))));
}

document.addEventListener("DOMContentLoaded", function () {
  var sumInputs = document.getElementsByClassName("sum-input");
  for (input of sumInputs) {
    input.addEventListener('keyup', onInput);
    input.addEventListener('click', onInput);
  }
});
