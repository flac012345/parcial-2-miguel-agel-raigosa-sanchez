function potencia() {
    realizarOperacion("potencia");
}

function realizarOperacion(operacion) {
    var num1 = parseFloat(document.getElementById("numero1").value);
    var num2 = parseFloat(document.getElementById("numero2").value);
    var resultado;

    switch (operacion) {
        case "suma":
            resultado = num1 + num2;
            break;

        case "resta":
            resultado = num1 - num2;
            break;

        case "multiplicacion":
            resultado = num1 * num2;
            break;

        case "division":
            if (num2 !== 0) {
                resultado = num1 / num2;
            } else {
                resultado = "Error: No se puede dividir por cero";
            }
            break;

        case "potencia":
            resultado = Math.pow(num1, num2);
            break;

        default:
            resultado = "Operación no válida";
    }

    document.getElementById("resultado").innerText = resultado;
}
