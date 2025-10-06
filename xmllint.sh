rm erreurs-xml.log
for file in ./tei-articles/*.xml; do
  xmllint --noout "$file" 2>> erreurs-xml.log
done
rm erreurs-po-xml.log
for file in ./po/*.xml; do
  xmllint --noout "$file" 2>> erreurs-po-xml.log
done
