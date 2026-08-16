#!/bin/bash
# Corregir todos los textos oscuros a versiones claras
find src -name "*.tsx" -exec sed -i \
  -e 's/text-grayDark-9500/text-grayDark-950/g' \
  -e 's/text-grayDark-100/text-grayDark-900/g' \
  -e 's/text-grayDark-200/text-grayDark-800/g' \
  -e 's/text-grayDark-400/text-grayDark-600/g' \
  -e 's/text-rubyDark-900/text-rubyDark-100/g' \
  -e 's/text-rubyDark-800/text-rubyDark-200/g' \
  -e 's/text-tomatoDark-800/text-tomatoDark-200/g' \
  -e 's/text-amberDark-700/text-amberDark-300/g' \
  -e 's/text-slateDark-950/text-slateDark-50/g' \
  -e 's/text-greenDark-800/text-greenDark-200/g' \
  -e 's/text-blueDark-700/text-blueDark-300/g' \
  -e 's/bg-grayDark-100/bg-grayDark-900/g' \
  -e 's/bg-grayDark-300/bg-grayDark-700/g' \
  -e 's/bg-grayDark-200/bg-grayDark-800/g' \
  -e 's/bg-blueDark-100/bg-blueDark-900/g' {} \;
echo "Corrección final completada."
