<h1>File Convert</h1>

<p>Three types of file can be converted. --type defines file converting type.
Types are shown below:</p>
1.Csv to Xml<br>
2.Xml to Csv<br>
3.Xml to Json<br>
4.Json to Xml<br>
5.Csv to Json<br>
6.Json to Csv<br>
<br>
Format types must be like that:<br>
<h2>XML:</h2>
<div>
<pre>
  filename
    row id="id"
         item
            item-1
            item-2
            ...
</pre>
</div>
<h2>JSON:</h2>
<div><pre>id<br>{<br>   "id-items"<br>      {<br>           item<br>            {<br>               item:item_value<br>            }<br>      }<br>}
</pre></div>
<h2>CSV</h2>
<p>Semicolon must be used to separate objects</p>
<br><br>
<h3>Other </h3>
<div>
<h3>"-key":</h3>
<p>Semicolon must be used while key attribute is being created. </p>
<h3>"-xsd":</h3>
<p>Xsd file doesn't need path but you have to move xsd file the folder which includes project files</p>
</div>

<h2>Install<h2>
<p>There are two ways to install the program.You can use git clone or use <a href="https://pypi.org/project/XmlCsvJsonConvert/">this link.</a></p>
