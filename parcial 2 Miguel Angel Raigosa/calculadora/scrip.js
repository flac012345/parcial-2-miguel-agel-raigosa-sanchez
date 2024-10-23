function realizarOperacion(operacion) {
    // Obtener los valores de los inputs y convertirlos a números
    var num1 = parseFloat(document.getElementById("numero1").value);
    var num2 = parseFloat(document.getElementById("numero2").value);
    var resultado;

    // Validar que los números sean válidos
    if (isNaN(num1) || isNaN(num2)) {
        resultado = "Error: Por favor ingrese números válidos";
    } else {
        // Realizar la operación según el tipo especificado
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
            case "modulo":
                resultado = num1 % num2; // Operación de módulo
                break;
            case "division":
                if (num2 !== 0) {
                    resultado = num1 / num2;
                } else {
                    resultado = "Error: No se puede dividir por cero";
                }
                break;
            default:
                resultado = "Error: Operación no válida"; // Manejo de operaciones no válidas
        }
    }

    // Mostrar el resultado en el elemento con id "resultado"
    document.getElementById("resultado").innerText = resultado;
}