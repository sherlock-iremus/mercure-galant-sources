format_xml_file () {
  xmllint --format --noblanks $1 | tr -d '\n\r\t' | sed 's/  */ /g' > $1.f
  mv $1.f $1
  xmllint --format $1 > $1.f
  mv $1.f $1
  
  echo $1
}

for f in $(ls tei-articles/*.xml)
do
    x=$(format_xml_file $f)
    echo $x
done