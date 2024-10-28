<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die ('Fail');
?>
<html>
<style>
	table, th, td {
		border: 1px solid black;
}

	img {
		width: 50%;
	}
</style>
	<body>
<h1>Conexion establecida</h1>
<table>
		<tr>
			<th>id</th>
			<th>nombre</th>
			<th>url_imagen</th>
			<th>director</th>
			<th>año_estreno</th>
		</tr>

<?php
$query = 'SELECT * FROM tPeliculas';
$result = mysqli_query($db,$query) or die ('Query error');
while ($row = mysqli_fetch_array($result)) {
	echo '<tr>';
	echo '<td><a href="/detail.php?pelicula_id='.$row [0].'">'.$row[0].'</a></td>';
	echo '<td>'.$row ['nombre'].'</td>';
	echo '<td><img src="'.$row ['url_imagen'].'"></img></td>';
	echo '<td>'.$row ['director'].'</td>';
	echo '<td>'.$row ['año_estreno'].'</td>';
	echo '</tr>';
}

mysqli_close($db)
?>
</table>
	</body>
</html>