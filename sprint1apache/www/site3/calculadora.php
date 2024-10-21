<!DOCTYPE html>
<body>

<h1>Calculadora</h1>
<form action="./calculadora.php" method="post">
<label for="input1">Primer valor:</label><br>
        <input type="text" id="input1" name="cantidad1"><br>
        <label for="input2">Segundo valor:</label><br>
        <input type="text" id="input2" name="cantidad2"><br>

        <select name="operacion">
            <option value="sumar">Sumar</option>
            <option value="restar">Restar</option>
            <option value="multiplicar">Multiplicar</option>
            <option value="division">Dividir</option>
        </select>

        <input type="submit" value="Operar" name="Operar">

</form>

<p> Resultado:

        <?php
        if (isset($_POST["Operar"])) {
            $op = $_POST["operacion"];
            $op1 = $_POST["cantidad1"];
            $op2 = $_POST["cantidad2"];

            switch ($op) {
                case "sumar":
                    echo $op1 . " + " . $op2 . " = " . ($op1 + $op2);
                    break;
                case "restar":
                    echo $op1 . " - " . $op2 . " = " . ($op1 - $op2);
                    break;
                case "multiplicar":
                    echo $op1 . " * " . $op2 . " = " . ($op1 * $op2);
                    break;
                case "division":
                    echo $op1 . " / " . $op2 . " = " . ($op1 / $op2);
                    break;
            }
        }

	?>
</p>

</body>
</html>
