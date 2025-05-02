rm erreurs-xml.log
for file in ./tei-edition/*.xml; do
  xmllint --noout "$file" 2>> erreurs-xml.log
done
