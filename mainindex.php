<?php
$pythonScript = "path/to/your/python/script.py";
$dataToSend = "Hello from PHP!";

// Panggil skrip Python menggunakan shell_exec
$result = shell_exec("python $pythonScript " . escapeshellarg($dataToSend));
echo "Result from Python: $result";
?>
