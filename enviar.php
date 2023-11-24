<?php

// Obtenemos los datos del formulario
$name = $_POST["name"];
$email = $_POST["email"];
$info = $_POST["info"];
// Creamos un mensaje de correo electrónico
$mensaje = "
to: $name <$email>
Subject: Form sent

This is an email sent from a web form.

Name: $name
Email: $email
";

// Enviamos el correo electrónico
mail("vburbano@live.com", "Submitted form", $mensaje);

// Retornamos un mensaje de confirmación
echo "The email has been sent successfully.";

?>
