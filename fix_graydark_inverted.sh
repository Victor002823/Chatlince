#!/bin/bash
find src -name "*.tsx" -exec sed -i \
  -e 's/grayDark-50/grayDark-TEMP50/g' \
  -e 's/grayDark-100/grayDark-900/g' \
  -e 's/grayDark-200/grayDark-800/g' \
  -e 's/grayDark-300/grayDark-700/g' \
  -e 's/grayDark-400/grayDark-600/g' \
  -e 's/grayDark-600/grayDark-400/g' \
  -e 's/grayDark-700/grayDark-300/g' \
  -e 's/grayDark-800/grayDark-200/g' \
  -e 's/grayDark-900/grayDark-100/g' \
  -e 's/grayDark-950/grayDark-50/g' \
  -e 's/grayDark-TEMP50/grayDark-950/g' {} \;
echo "Corrección de grayDark completada."
