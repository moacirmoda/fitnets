<?php

print "<ul>";
foreach(glob('*') as $file) {
	print "<li><a href='$file'>$file</a></li>";
}
print "</ul>";


?>